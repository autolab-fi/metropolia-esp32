import cv2
import math
import time
import os
import numpy as np


target_points = {
    'mission_zero': [(80, 50), (30, 0)],
    'maneuvering': [(35, 50), (30, 0)],
    'your_first_mission': [(35, 50), (30, 0)]
}

block_library_functions = {
    'mission_zero': False,
    'maneuvering': False,
    'your_first_mission': False,
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


def your_first_mission(robot, image, td: dict):
    """Verification function: Robot must navigate around red obstacle to reach checkpoint"""

    # FIXED POSITIONS AND SIZES - Change these as needed
    RED_BOX_CENTER = (700, 400)         # Red obstacle center (x, y) in pixels
    RED_BOX_WIDTH = 400                 # Red obstacle width in pixels
    RED_BOX_HEIGHT = 250                 # Red obstacle height in pixels
    CHECKPOINT_PIXEL_POS = (1000, 300)  # Checkpoint position (x, y) in pixels
    
    # Initialize result - default to failure
    result = {
        "success": False,
        "description": "Navigate around the red obstacle to reach the checkpoint",
        "score": 0
    }
    text = "Navigate to checkpoint"
    image = robot.draw_info(image)
    
    # Initialize task data
    if not td:
        td = {
            "end_time": time.time() + 30,  # 30 seconds to complete
            "start_position": None,
            "checkpoint_position": None,
            "obstacle_position": None,
            "checkpoint_reached": False,
            "red_box_collision": False,
            "trajectory": [],
            "initialized": False,
            "failure_time": None,
            "task_should_end": False
        }

    # Get robot information
    info = robot.get_info()
    robot_position = info['position']
    robot_position_px = info['position_px']
    
    if robot_position is not None:
        # Add to trajectory for visualization
        if robot_position_px is not None:
            td['trajectory'].append(robot_position_px)
        
        # Initialize positions on first frame
        if not td["initialized"] and robot_position_px is not None:
            td["start_position"] = robot_position
            
            # Convert fixed pixel positions to world coordinates
            robot_world_x, robot_world_y = robot_position
            robot_pixel_x, robot_pixel_y = robot_position_px
            
            # Scale factor: pixels to cm (adjust this value to match your setup)
            scale = 8  # pixels per cm
            
            # Calculate world positions from fixed pixel positions
            dx_obstacle = (RED_BOX_CENTER[0] - robot_pixel_x) / scale
            dy_obstacle = (RED_BOX_CENTER[1] - robot_pixel_y) / scale
            td["obstacle_position"] = (robot_world_x + dx_obstacle, robot_world_y + dy_obstacle)
            
            dx_checkpoint = (CHECKPOINT_PIXEL_POS[0] - robot_pixel_x) / scale
            dy_checkpoint = (CHECKPOINT_PIXEL_POS[1] - robot_pixel_y) / scale
            td["checkpoint_position"] = (robot_world_x + dx_checkpoint, robot_world_y + dy_checkpoint)
            
            td["initialized"] = True
            text = "Navigate around the red obstacle to reach the green checkpoint!"
        else:
            robot_x, robot_y = robot_position
            
            # Get obstacle position from stored data
            obstacle_center_x, obstacle_center_y = td["obstacle_position"]
            
            # Red box boundaries - convert pixel size to world size
            world_width = RED_BOX_WIDTH / 8   # Convert pixels to cm (8 pixels per cm)
            world_height = RED_BOX_HEIGHT / 8 # Convert pixels to cm (8 pixels per cm)
            
            red_box_bounds = {
                "x_min": obstacle_center_x - world_width/2,
                "x_max": obstacle_center_x + world_width/2,
                "y_min": obstacle_center_y - world_height/2,
                "y_max": obstacle_center_y + world_height/2
            }
            
            # Check collision with red box
            if (red_box_bounds["x_min"] <= robot_x <= red_box_bounds["x_max"] and
                red_box_bounds["y_min"] <= robot_y <= red_box_bounds["y_max"]):
                if not td["red_box_collision"]:
                    td["red_box_collision"] = True
                    td["failure_time"] = time.time()
                    text = "COLLISION! Robot hit the red obstacle - Mission Failed!"
            
            # Check checkpoint arrival (only if no collision)
            if not td["red_box_collision"] and not td["checkpoint_reached"]:
                checkpoint_x, checkpoint_y = td["checkpoint_position"]
                distance_to_checkpoint = math.sqrt(
                    (robot_x - checkpoint_x)**2 + (robot_y - checkpoint_y)**2
                )
                
                if distance_to_checkpoint <= 10:  # 10cm tolerance
                    td["checkpoint_reached"] = True
                    td["task_should_end"] = True
                    text = "SUCCESS! Checkpoint reached - Mission Accomplished!"
                else:
                    text = f"Navigate around obstacle. Distance to checkpoint: {distance_to_checkpoint:.1f}cm"

    # Draw red obstacle box using center point and dimensions
    # Calculate rectangle corners from center and size
    rect_x = RED_BOX_CENTER[0] - RED_BOX_WIDTH // 2
    rect_y = RED_BOX_CENTER[1] - RED_BOX_HEIGHT // 2
    
    # Change appearance based on collision
    if td["red_box_collision"]:
        # Solid red rectangle with flashing border
        cv2.rectangle(image, (rect_x, rect_y), (rect_x + RED_BOX_WIDTH, rect_y + RED_BOX_HEIGHT), (0, 0, 255), -1)
        flash_color = (255, 255, 255) if int(time.time() * 4) % 2 else (0, 0, 255)
        cv2.rectangle(image, (rect_x, rect_y), (rect_x + RED_BOX_WIDTH, rect_y + RED_BOX_HEIGHT), flash_color, 4)
        cv2.putText(image, "COLLISION!", (RED_BOX_CENTER[0]-60, RED_BOX_CENTER[1]), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    else:
        # Semi-transparent red rectangle
        overlay = image.copy()
        cv2.rectangle(overlay, (rect_x, rect_y), (rect_x + RED_BOX_WIDTH, rect_y + RED_BOX_HEIGHT), (0, 0, 255), -1)
        cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)
        cv2.rectangle(image, (rect_x, rect_y), (rect_x + RED_BOX_WIDTH, rect_y + RED_BOX_HEIGHT), (0, 0, 255), 3)
        cv2.putText(image, "OBSTACLE", (RED_BOX_CENTER[0]-45, RED_BOX_CENTER[1]), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Draw checkpoint at FIXED pixel position
    if td["checkpoint_reached"]:
        # Green filled circle with white border when reached
        cv2.circle(image, CHECKPOINT_PIXEL_POS, 30, (0, 255, 0), -1)
        cv2.circle(image, CHECKPOINT_PIXEL_POS, 30, (255, 255, 255), 4)
        cv2.putText(image, "REACHED!", (CHECKPOINT_PIXEL_POS[0]-45, CHECKPOINT_PIXEL_POS[1]-40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    elif td["red_box_collision"]:
        # Gray circle when mission failed
        cv2.circle(image, CHECKPOINT_PIXEL_POS, 30, (100, 100, 100), -1)
        cv2.circle(image, CHECKPOINT_PIXEL_POS, 30, (0, 0, 255), 4)
    else:
        # Green circle with pulsing effect
        pulse = int(20 + 8 * math.sin(time.time() * 3))
        cv2.circle(image, CHECKPOINT_PIXEL_POS, pulse, (0, 255, 0), -1)
        cv2.circle(image, CHECKPOINT_PIXEL_POS, 30, (255, 255, 255), 3)
        
        # Draw tolerance circle (10cm radius)
        tolerance_pixels = int(10 * 8)  # 10cm * 8 pixels/cm
        cv2.circle(image, CHECKPOINT_PIXEL_POS, tolerance_pixels, (0, 255, 0), 2)
    
    cv2.putText(image, "GOAL", (CHECKPOINT_PIXEL_POS[0]-25, CHECKPOINT_PIXEL_POS[1]+45), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Check timing for failures
    time_remaining = td["end_time"] - time.time()
    current_time = time.time()

    # Result logic
    if td["checkpoint_reached"] and not td["red_box_collision"]:
        result["success"] = True
        result["score"] = 100
        result["description"] = "Excellent! Robot successfully navigated around obstacle and reached checkpoint."
        
    elif td["red_box_collision"]:
        result["success"] = False
        result["score"] = 0
        result["description"] = "Mission failed! Robot collided with the red obstacle."
        
        if td["failure_time"] and (current_time - td["failure_time"]) >= 3:
            td["task_should_end"] = True
            
    elif time_remaining <= 0:
        result["success"] = False
        result["score"] = 0
        result["description"] = "Mission failed! The robot did not reached the checkpoint."
        
        if td["failure_time"] is None:
            td["failure_time"] = current_time
            
        if (current_time - td["failure_time"]) >= 3:
            td["task_should_end"] = True
            
    else:
        result["success"] = True
        result["score"] = 0
        result["description"] = "Mission in progress - navigate around obstacle to checkpoint"

    if td["task_should_end"] and not td["checkpoint_reached"]:
        result["success"] = False

    return image, td, text, result