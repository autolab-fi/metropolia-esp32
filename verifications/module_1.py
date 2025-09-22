import cv2
import math
import time
import os
import numpy as np


target_points = {
    'mission_zero': [(80, 50), (30, 0)],
    'maneuvering': [(35, 50), (30, 0)],
    'long_distance_race': [(35, 50), (30, 0)]
}

block_library_functions = {
    'mission_zero': False,
    'maneuvering': False,
    'long_distance_race': False,
}

def get_block_library_functions(task):
    global block_library_functions
    return block_library_functions[task]


# function to get value from dictionary target_point
def get_target_points(task):
    global target_points
    return target_points[task]

def delta_points(point_0, point_1):
    return math.sqrt(((point_0[0] - point_1[0]) ** 2) +
                     ((point_0[1] - point_1[1]) ** 2))


def mission_zero(robot, image, td: dict):
    """Test for three key positions: Location A (30cm), Location B (50cm), then return to start"""

    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Navigate to three positions"
    image = robot.draw_info(image)
    
    # Initialize the dictionary with consistent structure
    if not td:
        td = {
            "end_time": time.time() + 60,  # Extended time for three positions
            "start_position": None,
            "prev_robot_center": None,
            "current_phase": 1,  # 1: Go to A, 2: Go to B, 3: Return to start
            "phase_completed": [False, False, False],  # Track completion of each phase
            "positions": {
                "start": None,
                "location_a": None,  # 30cm target
                "location_b": None,  # 50cm target
                "current": None
            },
            "tolerances": {
                "location_a": 5,    # 5cm tolerance for Location A
                "location_b": 5,    # 5cm tolerance for Location B  
                "return_home": 8    # 8cm tolerance for returning to start
            }
        }

    # Get the current robot position
    robot_position = robot.get_info()["position"]
    
    if robot_position is not None:
        td["positions"]["current"] = robot_position
        
        # Set start position on first measurement
        if td["start_position"] is None:
            td["start_position"] = robot_position
            td["positions"]["start"] = robot_position
            text = f"Starting position set: ({robot_position[0]:.1f}, {robot_position[1]:.1f})"
        
        # Calculate distance from start
        if td["start_position"] is not None:
            distance_from_start = math.sqrt(
                (robot_position[0] - td["start_position"][0])**2 + 
                (robot_position[1] - td["start_position"][1])**2
            )
            
            # Phase 1: Navigate to Location A (30cm from start)
            if td["current_phase"] == 1 and not td["phase_completed"][0]:
                target_distance = 30
                distance_error = abs(distance_from_start - target_distance)
                
                if distance_error <= td["tolerances"]["location_a"]:
                    td["phase_completed"][0] = True
                    td["positions"]["location_a"] = robot_position
                    td["current_phase"] = 2
                    text = f"Location A reached! Distance: {distance_from_start:.1f}cm. Now go to Location B (50cm)"
                else:
                    text = f"Phase 1: Go to Location A (30cm). Current distance: {distance_from_start:.1f}cm"
            
            # Phase 2: Navigate to Location B (50cm from start)  
            elif td["current_phase"] == 2 and not td["phase_completed"][1]:
                target_distance = 50
                distance_error = abs(distance_from_start - target_distance)
                
                if distance_error <= td["tolerances"]["location_b"]:
                    td["phase_completed"][1] = True
                    td["positions"]["location_b"] = robot_position
                    td["current_phase"] = 3
                    text = f"Location B reached! Distance: {distance_from_start:.1f}cm. Now return to start"
                else:
                    text = f"Phase 2: Go to Location B (50cm). Current distance: {distance_from_start:.1f}cm"
            
            # Phase 3: Return to starting position
            elif td["current_phase"] == 3 and not td["phase_completed"][2]:
                if distance_from_start <= td["tolerances"]["return_home"]:
                    td["phase_completed"][2] = True
                    text = f"Returned to start! All phases completed. Final distance: {distance_from_start:.1f}cm"
                    # Add extra time for completion message
                    if (td["end_time"] - time.time()) > 5:
                        td["end_time"] = time.time() + 5
                else:
                    text = f"Phase 3: Return to start. Current distance from start: {distance_from_start:.1f}cm"
            
            # All phases completed
            elif all(td["phase_completed"]):
                text = f"Mission accomplished! All three positions visited successfully."
                result["description"] = "Perfect! Robot completed all three navigation phases."

    # Progress indicator
    completed_phases = sum(td["phase_completed"])
    cv2.putText(image, f"Phase: {td['current_phase']}/3 | Completed: {completed_phases}/3", 
               (20, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Check for failure conditions
    time_remaining = td["end_time"] - time.time()
    if time_remaining <= 2:
        if not all(td["phase_completed"]):
            result["success"] = False
            result["score"] = completed_phases * 33  # Partial credit
            result["description"] = f"Time expired! Completed {completed_phases}/3 phases. Score: {result['score']}"
        
    # Check if robot went too far from reasonable range
    if robot_position is not None and td["start_position"] is not None:
        distance_from_start = math.sqrt(
            (robot_position[0] - td["start_position"][0])**2 + 
            (robot_position[1] - td["start_position"][1])**2
        )
        if distance_from_start > 80:  # Too far from start
            result["success"] = False
            result["score"] = 0
            result["description"] = f"Robot went too far from start position: {distance_from_start:.1f}cm"

    td['prev_robot_center'] = robot_position
    return image, td, text, result

def manuvering(robot, image, td: dict):
    """Test for rover rotation sequence: 90° right, 45° left, 135° right, 15° right"""
    import time
    import math
    import cv2

    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Rover rotation sequence verification"
    image = robot.draw_info(image)
    
    # Initialize the dictionary with consistent structure
    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 45,  # 45 seconds for all rotations
            "target_angle": [
                {"left": 0, "right": 15},    # Step 4: 15° right
                {"left": 0, "right": 135},   # Step 3: 135° right  
                {"left": 45, "right": 0},    # Step 2: 45° left
                {"left": 0, "right": 90}     # Step 1: 90° right (first to complete)
            ],
            "initialized": False,
            "ang_0": None
        }

    min_for_error = 15  # 15 degree tolerance
    min_for_change_point = 10  # 10 degrees to consider step completed

    if robot is not None:
        # Get current angle using the same method as reference
        ang = robot.compute_angle_x()
        
        # Initialize the starting angle
        if not td["initialized"]:
            td['ang_0'] = ang
            td["initialized"] = True
            text = f"Initialization complete. Starting angle: {ang:.0f}°. Begin rotation sequence!"
            return image, td, text, result

        # Handle angle wrap-around (same logic as reference)
        if td['ang_0'] < 90 and ang > 300:
            td['ang_0'] = 360 + td['ang_0']
        elif td['ang_0'] > 300 and ang < 90:
            td['ang_0'] -= 360

        delta_ang = ang - td['ang_0']

        # Update target angles based on rotation direction
        if delta_ang < 0:  # Robot turned right (clockwise)
            if td['target_angle'][-1]['right'] > 0:
                td['target_angle'][-1]['right'] += delta_ang  # Reduce remaining right rotation
        else:  # Robot turned left (counter-clockwise)
            if td['target_angle'][-1]['left'] > 0:
                td['target_angle'][-1]['left'] -= delta_ang  # Reduce remaining left rotation

        # Check if current step is completed
        if (
            td['target_angle'][-1]['left'] <= min_for_change_point and
            td['target_angle'][-1]['right'] <= min_for_change_point
        ):
            if len(td['target_angle']) > 1:
                completed_step = 5 - len(td['target_angle'])
                step_descriptions = ["90° right", "45° left", "135° right", "15° right"]
                text = f"Step {completed_step} completed: {step_descriptions[completed_step-1]}!"
                td['target_angle'].pop()  # Move to next step
                # Add extra time for each completed step
                td["end_time"] = time.time() + 15
            else:
                text = "All rotations completed! Mission successful!"
                if (td["end_time"] - time.time()) > 5:
                    td["end_time"] = time.time() + 5

        # Update display text
        current_step = 5 - len(td['target_angle'])  # Calculate current step (1-4)
        remaining_left = max(0, td['target_angle'][-1]['left'])
        remaining_right = max(0, td['target_angle'][-1]['right'])
        
        if current_step <= 4:
            step_descriptions = ["90° right", "45° left", "135° right", "15° right"]
            text = f"Step {current_step}: {step_descriptions[current_step-1]} | "
            text += f"Current: {ang:.0f}° | "
            if remaining_right > min_for_change_point:
                text += f"Need {remaining_right:.0f}° more right"
            elif remaining_left > min_for_change_point:
                text += f"Need {remaining_left:.0f}° more left"
            else:
                text += "Step completing..."

        # Update ang_0 for next iteration
        td['ang_0'] = ang

    # Check for failure conditions
    time_left = td["end_time"] - time.time()
    if len(td['target_angle']) > 0 and (
        td['target_angle'][-1]['left'] < -min_for_error or
        td['target_angle'][-1]['right'] < -min_for_error or
        (time_left < 2 and len(td['target_angle']) > 1)
    ):
        result["success"] = False
        completed_steps = max(0, 4 - len(td['target_angle']))
        result["score"] = completed_steps * 25  # 25 points per completed step
        result["description"] = (
            f"Robot failed the rotation sequence. "
            f"Completed {completed_steps}/4 steps. "
        )
        
        # Show what rotations were still needed
        if len(td['target_angle']) > 0:
            for i in range(len(td['target_angle']) - 1, -1, -1):
                if td['target_angle'][i]['right'] > min_for_change_point:
                    result["description"] += f"{int(td['target_angle'][i]['right'])} degrees right; "
                if td['target_angle'][i]['left'] > min_for_change_point:
                    result["description"] += f"{int(td['target_angle'][i]['left'])} degrees left; "
    
    # Success condition - all steps completed
    elif len(td['target_angle']) <= 1 and (
        len(td['target_angle']) == 0 or (
            td['target_angle'][-1]['left'] <= min_for_change_point and
            td['target_angle'][-1]['right'] <= min_for_change_point
        )
    ):
        result["success"] = True
        result["description"] = "Perfect! Robot completed all rotation steps successfully."
        result["score"] = 100

    result["description"] += f' | Score: {result["score"]}'
    return image, td, text, result


def calculate_target_point(rb, targets):
    """Calculate the target points based on the robot's current position and movement directions."""
    
    # Get the robot's position properly
    pos = rb.get_info().get("position")
    
    if pos is None:
        print("Error: Robot position is None")
        return []

    point = [pos[0], pos[1]]
    direction = rb.compute_angle_x()

    res = []
    for target in targets:
        if isinstance(target, dict):
            point[0] += target['forward'] * math.cos(math.radians(direction))
            point[0] -= target['backward'] * math.cos(math.radians(direction))
            point[1] -= target['forward'] * math.sin(math.radians(direction))
            point[1] += target['backward'] * math.sin(math.radians(direction))
            res.append((point[0], point[1]))
        else:
            # Handle reversed y-axis
            direction += target[0]['left']
            direction -= target[0]['right']

    res.reverse()
    return res

def image_to_mask(filename, percentage):
    """Load an image and create a mask with a given scaling percentage."""
    
    # Try to load the image
    temp = cv2.imread(filename)

    lower_limit = np.array([0, 0, 0])  
    upper_limit = np.array([255, 254, 255])  
    mask = cv2.inRange(temp, lower_limit, upper_limit)

    return temp, mask


def long_distance_race(robot, image, td: dict):
    """Test for lesson 5: Long distance race."""

    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Not recognized"
    image = robot.draw_info(image)

    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 24,
            "data": {},
            "delta": 4,
            "reached_point": False
        }

    if not td["data"] and robot:
        route = [
            {'forward': 30, 'backward': 0},
            [{'left': 90, 'right': 0}],
            {'forward': 20, 'backward': 0},
            [{'left': 0, 'right': 90}],
            {'forward': 30, 'backward': 0},
            [{'left': 0, 'right': 90}],
            {'forward': 20, 'backward': 0}
        ]

        td["data"]['targets'] = calculate_target_point(robot, route)
        td["data"]['delta'] = 4
        td["data"]['reached_point'] = False

        td["data"]["fruit"] = {}
        td["data"]["mask"] = {}
        td["data"]["animation"] = {}

        basepath = os.path.abspath(os.path.dirname(__file__))
        

        for i in range(4):
            td["data"]["fruit"][i] = {}
            td["data"]["mask"][i] = {}

            for j in range(1, 7):
                filepath = os.path.join(basepath,'images', f'{i}-{j}.jpg')
                td["data"]["fruit"][i][j], td["data"]["mask"][i][j] = image_to_mask(filepath, percentage=0.7)

            td["data"]["animation"][i] = 1

        td["data"]['coordinates'] = [
            (robot.cm_to_pixel(x), robot.cm_to_pixel(y)) for x, y in td["data"]['targets']
        ]

    d = None

    if robot:
        robot_position = robot.get_info().get("position")
        if robot_position is not None:
            d = delta_points(robot_position, td["data"]['targets'][-1])
            text = (
                f'The distance to the next ({td["data"]["targets"][-1][0]:0.0f}, '
                f'{td["data"]["targets"][-1][1]:0.0f}) point is {d:0.0f}'
            )

            if d < td["data"]['delta']:
                if len(td["data"]['targets']) > 1:
                    td["data"]["animation"][len(td["data"]['targets']) - 1] += 1
                    td["data"]['delta'] += 1.3
                    td["data"]['targets'].pop()
                elif not td["data"]['reached_point']:
                    td["data"]["animation"][0] += 1
                    td["data"]['reached_point'] = True
                    td["end_time"] = time.time() + 4

    if d is not None and td["end_time"] - time.time() < 2 and (
            len(td["data"]['targets']) != 1 or d > td["data"]['delta']):
        if len(td["data"]['targets']) > 1:
            text = "Robot missed several checkpoints"
        else:
            text = (
                f'It is disappointing, but robot failed the task, '
                f'because it is {d:0.0f} centimeters away from the target point'
            )
        result["description"] = text
        result["success"] = False
        result["score"] = 0

    if td["data"]:
        for i in range(len(td["data"]['coordinates'])):
            if td["data"]["animation"][i] > 6:
                td["data"]['coordinates'].pop()
                td["data"]['fruit'].pop(i)
                td["data"]["mask"].pop(i)
                td["data"]["animation"].pop(i)
            else:
                x, y = td["data"]['coordinates'][i]
                fruit = td["data"]["fruit"][i][td["data"]["animation"][i]]
                mask = td["data"]["mask"][i][td["data"]["animation"][i]]

                ymin = fruit.shape[0] // 2
                ymax = fruit.shape[0] - ymin
                xmin = fruit.shape[1] // 2
                xmax = fruit.shape[1] - xmin

                cv2.copyTo(fruit, mask, image[y - ymin:y + ymax, x - xmin:x + xmax])

                if td["data"]["animation"][i] > 1:
                    td["data"]["animation"][i] += 1

    return image, td, text, result
