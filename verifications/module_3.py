import cv2
import math
import time
import os
import numpy as np

target_points = {
    'manual_control': [(30, 50), (30, 0)],
    'sequenced_commands':[(50, 50), (30, 0)],
    'electric_motor': [(50, 50), (30, 0)]
}

block_library_functions = {
    'manual_control': True,
    "sequenced_commands": True,
    'electric_motor': True
}

def get_block_library_functions(task):
    """Retrieve block library status for a given task."""
    return block_library_functions.get(task, False)


def get_target_points(task):
    """Retrieve target points for a given task."""
    return target_points.get(task, [])


def sequenced_commands(robot, image, td: dict):
    """Verification function: Robot must move straight 20cm then rotate 180 degrees"""
    # Initialize result - default to failure
    result = {
        "success": False,
        "description": "Move forward 20cm then rotate 180 degrees",
        "score": 0
    }
    text = "Move forward 20cm then rotate 180°"
    image = robot.draw_info(image)
    
    # Initialize task data
    if not td:
        td = {
            "end_time": time.time() + 30,  # 30 seconds to complete
            "start_position": None,
            "current_phase": "forward",  # "forward", "rotation", "completed"
            "forward_completed": False,
            "rotation_completed": False,
            "forward_distance": 0,
            "total_rotation": 0,
            "trajectory": [],
            "recent_positions": [],  # For calculating rotation
            "initialized": False,
            "completion_time": None,
            "last_position": None,
            "movement_threshold": 2,  # cm - minimum movement to detect rotation
            "stationary_time": 0,
            "rotation_start_time": None
        }

    # Get robot information
    info = robot.get_info()
    robot_position = info['position']
    robot_position_px = info['position_px']
    
    if robot_position is not None:
        # Add to trajectory for visualization
        if robot_position_px is not None:
            td['trajectory'].append(robot_position_px)
        
        # Initialize on first frame
        if not td["initialized"]:
            td["start_position"] = robot_position
            td["last_position"] = robot_position
            td["initialized"] = True
            text = "Phase 1: Move forward 20cm"
        else:
            robot_x, robot_y = robot_position
            start_x, start_y = td["start_position"]
            last_x, last_y = td["last_position"]
            
            # Calculate distance traveled from start
            distance_traveled = math.sqrt((robot_x - start_x)**2 + (robot_y - start_y)**2)
            td["forward_distance"] = distance_traveled
            
            # Calculate movement since last frame
            movement_since_last = math.sqrt((robot_x - last_x)**2 + (robot_y - last_y)**2)
            
            # Store recent positions for rotation calculation (keep last 10 positions)
            td["recent_positions"].append(robot_position)
            if len(td["recent_positions"]) > 10:
                td["recent_positions"].pop(0)
            
            # Phase 1: Forward movement (20cm ± 2cm tolerance)
            if td["current_phase"] == "forward":
                if distance_traveled >= 18:  # 20cm with 2cm tolerance
                    td["forward_completed"] = True
                    td["current_phase"] = "rotation"
                    td["rotation_start_time"] = time.time()
                    text = "Phase 2: Rotate 180 degrees"
                else:
                    text = f"Phase 1: Move forward - {distance_traveled:.1f}cm / 20cm"
            
            # Phase 2: Rotation detection
            elif td["current_phase"] == "rotation" and td["forward_completed"]:
                # Check if robot is moving much (if so, not rotating in place)
                if movement_since_last < td["movement_threshold"]:
                    td["stationary_time"] += 1  # Count frames robot is relatively stationary
                else:
                    td["stationary_time"] = 0
                
                # Calculate rotation using trajectory changes
                if len(td["recent_positions"]) >= 5:
                    # Calculate direction vectors from trajectory
                    old_pos = td["recent_positions"][0]
                    mid_pos = td["recent_positions"][len(td["recent_positions"])//2]
                    current_pos = td["recent_positions"][-1]
                    
                    # Calculate vectors
                    vec1_x = mid_pos[0] - old_pos[0]
                    vec1_y = mid_pos[1] - old_pos[1]
                    vec2_x = current_pos[0] - mid_pos[0]
                    vec2_y = current_pos[1] - mid_pos[1]
                    
                    # Calculate angle between vectors if both have significant length
                    len1 = math.sqrt(vec1_x**2 + vec1_y**2)
                    len2 = math.sqrt(vec2_x**2 + vec2_y**2)
                    
                    if len1 > 1 and len2 > 1:  # Only if robot has moved significantly
                        # Normalize vectors
                        vec1_x /= len1
                        vec1_y /= len1
                        vec2_x /= len2
                        vec2_y /= len2
                        
                        # Calculate angle between normalized vectors
                        dot_product = vec1_x * vec2_x + vec1_y * vec2_y
                        dot_product = max(-1, min(1, dot_product))  # Clamp to [-1, 1]
                        angle_change = math.degrees(math.acos(abs(dot_product)))
                        
                        # Accumulate rotation
                        if angle_change > 10:  # Only count significant angle changes
                            td["total_rotation"] += angle_change
                
                # Alternative method: Check if robot has completed a circular path
                if len(td["trajectory"]) > 20:
                    # Check if robot has returned close to where rotation started
                    rotation_start_idx = len(td["trajectory"]) - 20
                    rotation_start_px = td["trajectory"][rotation_start_idx]
                    current_px = td["trajectory"][-1]
                    
                    if rotation_start_px and current_px:
                        distance_from_rotation_start = math.sqrt(
                            (current_px[0] - rotation_start_px[0])**2 + 
                            (current_px[1] - rotation_start_px[1])**2
                        )
                        
                        # If robot is close to where it started rotating and has been stationary
                        if distance_from_rotation_start < 50 and td["stationary_time"] > 10:
                            td["total_rotation"] = max(td["total_rotation"], 180)
                
                # Check completion
                if td["total_rotation"] >= 160:  # 180° with some tolerance
                    td["rotation_completed"] = True
                    td["current_phase"] = "completed"
                    td["completion_time"] = time.time()
                    text = "Task completed successfully!"
                else:
                    text = f"Phase 2: Rotate - {td['total_rotation']:.1f}° / 180°"
            
            # Update last position
            td["last_position"] = robot_position

    # Check timing for failures
    time_remaining = td["end_time"] - time.time()

    # Result logic
    if td["forward_completed"] and td["rotation_completed"]:
        # SUCCESS: Both phases completed
        result["success"] = True
        result["score"] = 100
        result["description"] = "Excellent! Robot moved 20cm forward and rotated 180 degrees successfully."
        
    elif time_remaining <= 0:
        # FAILURE: Time expired
        result["success"] = False
        result["score"] = 0
        if not td["forward_completed"]:
            result["description"] = f"Time expired! Robot only moved {td['forward_distance']:.1f}cm (needed 20cm)."
        elif not td["rotation_completed"]:
            result["description"] = f"Time expired! Robot rotated {td['total_rotation']:.1f}° (needed 180°)."
        else:
            result["description"] = "Time expired before task completion."
            
    else:
        # Mission in progress
        result["success"] = True  # Keep running
        result["score"] = 0
        if td["forward_completed"]:
            progress = 50 + (td['total_rotation'] / 180) * 50  # 50% for forward + up to 50% for rotation
        else:
            progress = (td['forward_distance'] / 20) * 50  # Up to 50% for forward movement
        result["description"] = f"Mission in progress - {progress:.0f}% complete"

    return image, td, text, result



def electric_motor(robot, image, td: dict):
    """Test for lesson 8: Electric motor"""
    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Not recognized"
    
    image = robot.draw_info(image)
    
    if not td:
        td = {
            "end_time": time.time() + 7,
            "data": {}
        }
        
        try:
            basepath = os.path.abspath(os.path.dirname(__file__))
            filepath = os.path.join(basepath, 'images', 'flag_finish.jpg')
              
            flag = cv2.imread(filepath)
            
            flag = cv2.resize(flag, (int(flag.shape[1]/3), int(flag.shape[0]/3)))
            lower_green = np.array([0, 240, 0]) 
            upper_green = np.array([50, 255, 50]) 
            td["data"]["flag-mask"] = cv2.bitwise_not(cv2.inRange(flag, lower_green, upper_green))
            td["data"]["flag"] = flag
            td["data"]["reached"] = False
        except Exception as e:
            print(f"Error loading or processing image: {e}")
            td["data"]["image_error"] = True
            return image, td, f"Error processing image: {str(e)}", result

    # First, set the flag coordinates if they don't exist yet
    robot_info = robot.get_info()
    position_px = robot_info["position_px"]
    if "flag-coords" not in td["data"] and  position_px is not None:
            
        angle = robot.compute_angle_x()
        
        x = position_px[0] + 180 if 90 < angle < 270 else position_px[0] - 200
        y = position_px[1] - 220 if 90 < angle < 270 else position_px[1] + 250
        td["data"]["flag-coords"] = (x, y)
        td["data"]["flag-coords-cm"] = (robot.pixels_to_cm(x), robot.pixels_to_cm(y))
    
    # Then, in a separate condition, draw the flag using those coordinates
    if "flag-coords" in td["data"]:
        flag = td["data"]["flag"]
        x_left = int(flag.shape[0]/2)
        x_right = flag.shape[0] - x_left
        y_bottom = int(flag.shape[1]/2)
        y_up = flag.shape[1] - y_bottom
        
        # Check if coordinates are within image bounds
        coords = td["data"]["flag-coords"]
        if (0 <= coords[0] - x_left < image.shape[0] and 
            coords[0] + x_right < image.shape[0] and
            0 <= coords[1] - y_bottom < image.shape[1] and
            coords[1] + y_up < image.shape[1]):
            
            if td["data"]["reached"]:
                # Increased rotation angle from 25 to 45 degrees
                result_img = rotate_image(flag, 45)  
                mask = cv2.inRange(result_img, (0, 0, 0), (205, 205, 205))
                result_img[mask > 0] = (0, 255, 0)
                cv2.circle(image, (td['data']['flag-coords'][1],td['data']['flag-coords'][0]) , 135, (0, 255, 0),2)
                cv2.copyTo(result_img, rotate_image(td["data"]["flag-mask"], 45), 
                          image[coords[0] - x_left:x_right + coords[0], 
                                coords[1] - y_bottom:y_up + coords[1]])
            else:
                cv2.copyTo(flag, td["data"]["flag-mask"], 
                          image[coords[0] - x_left:x_right + coords[0], 
                                coords[1] - y_bottom:y_up + coords[1]])
                cv2.circle(image, (td['data']['flag-coords'][1],td['data']['flag-coords'][0]) , 135, (0, 255, 0),2)

    position = robot_info["position"]
    if position and "flag-coords-cm" in td["data"]:
        delta = robot.delta_points((position[1], position[0]), td["data"]["flag-coords-cm"])
        
        # Increased threshold from 5.1 to 7.0 cm for better detection
        if delta < 9.0:
            td["data"]["reached"] = True
            text = "The robot has reached target point!"
        else:
            text = f'Distance to target point {delta:0.1f} cm'
            
    if td["end_time"] - time.time() < 1 and td["data"].get("reached", False) == False:
        result["success"] = False
        result["score"] = 0
        result["description"] = "Robot did not reach the target point"
  
    return image, td, text, result

def closest_node(node, nodes):
    """Find the index of the closest node in a set of nodes"""
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return np.argmin(dist_2)

def rotate_image(image, angle):
    """Rotate an image by the given angle"""
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

def differential_drive(robot, image, td):
    """Verification function for driving straight assignment"""
    result = {
        "success": True,
        "description": "You are amazing! The Robot has completed the assignment",
        "score": 100
    }
    text = "Drive the robot in a straight line for 3 seconds"
    
    # Draw robot info on image
    image = robot.draw_info(image)

    # Initialize td if it's the first call
    if not td:
        td = {
            "start_time": time.time(),
            "end_time": time.time() + 10,  # Verification lasts for 10 seconds
            "data": {
                "task-failed": "",
                "failed-cone": {},
                "direction_0": None,
                "prev_robot_position": None,
                "robot_start_move_time": None,
                "robot_end_move_time": None,
                "max_angle_deviation": 0,
                "straight_driving_start": None,
                "straight_driving_duration": 0
            }
        }
        
        try:
            basepath = os.path.abspath(os.path.dirname(__file__))
            filepath = os.path.join(basepath, "images", "traffic-sign.jpg")

            if not os.path.exists(filepath):
                filepath = os.path.join(basepath, "images", "traffic-sign.jpg")
                
            if not os.path.exists(filepath):
                # Create a simple colored cone as fallback
                cone = np.zeros((100, 100, 3), dtype=np.uint8)
                cone[:, :] = (0, 0, 255)  # Red rectangle
            else:
                cone = cv2.imread(filepath)
                cone = cv2.resize(cone, (int(cone.shape[1]), int(cone.shape[0])))
                
            # Define green color range
            lower_green = np.array([0, 240, 0]) 
            upper_green = np.array([35, 255, 35])
            
            td["data"]["cone-mask"] = cv2.bitwise_not(cv2.inRange(cone, lower_green, upper_green))
            td["data"]["cone"] = cone
            td["data"]["cones-coords"] = []
        except Exception as e:
            print(f"Error initializing drive straight test: {e}")
            td["data"]["image_error"] = True

    # Set up cone coordinates if robot detected and coordinates not set
    if robot and robot.position_px and len(td["data"].get("cones-coords", [])) == 0:
        # Define cone positions to create a corridor
        y_u = robot.position_px[1] - 150  # Upper row of cones
        y_d = robot.position_px[1] + 150  # Lower row of cones
        for i in range(10):
            x = robot.position_px[0] + (i % 5) * 200
            if i < 5:
                td["data"]["cones-coords"].append((y_u, x))
            else:
                td["data"]["cones-coords"].append((y_d, x))
        
        # Save initial direction when robot is first detected
        if td["data"]["direction_0"] is None:
            td["data"]["direction_0"] = robot.compute_angle_x()
            if td["data"]["direction_0"] > 180:
                td["data"]["direction_0"] -= 360

    # Draw cones if we have coordinates and cone image
    if "cones-coords" in td["data"] and "cone" in td["data"] and len(td["data"]["cones-coords"]) > 0:
        try:
            cone = td["data"]["cone"]
            x_left = int(cone.shape[0] / 2)
            x_right = cone.shape[0] - x_left
            y_bottom = int(cone.shape[1] / 2)
            y_up = cone.shape[1] - y_bottom
            
            for i in range(min(10, len(td["data"]["cones-coords"]))):
                coords = td["data"]["cones-coords"][i]
                
                # Check if coordinates are within image bounds
                if (0 <= coords[0] - x_left < image.shape[0] and 
                    coords[0] + x_right < image.shape[0] and
                    0 <= coords[1] - y_bottom < image.shape[1] and
                    coords[1] + y_up < image.shape[1]):
                    
                    if i in td["data"]["failed-cone"]:
                        result_img = rotate_image(cone, td["data"]["failed-cone"][i])
                        cv2.copyTo(
                            result_img, 
                            rotate_image(td["data"]["cone-mask"], td["data"]["failed-cone"][i]),
                            image[coords[0] - x_left:x_right + coords[0], 
                                 coords[1] - y_bottom:y_up + coords[1]]
                        )
                        if td["data"]["failed-cone"][i] > -89:
                            td["data"]["failed-cone"][i] -= 45
                    else:
                        cv2.copyTo(
                            cone,
                            td["data"]["cone-mask"],
                            image[coords[0] - x_left:x_right + coords[0], 
                                 coords[1] - y_bottom:y_up + coords[1]]
                        )
        except Exception as e:
            print(f"Error drawing cones: {e}")

    # Process robot movement
    if robot and robot.position is not None:
        # Get current angle
        angle_x = robot.compute_angle_x()
        angle_x_disp = angle_x
        
        if angle_x > 180:
            angle_x -= 360
        
        # Calculate angle difference (account for wrap-around at 360°)
        if td["data"]["direction_0"] is not None:
            angle_diff = abs(td["data"]["direction_0"] - angle_x)
            if angle_diff > 180:
                angle_diff = 360 - angle_diff
                
            # Track maximum deviation
            td["data"]["max_angle_deviation"] = max(td["data"]["max_angle_deviation"], angle_diff)
            
            text = f'Robot angle with x: {angle_x_disp:0.0f}°, Deviation: {angle_diff:.1f}°'
            
            # Check robot movement
            if td["data"]["prev_robot_position"] is not None:
                delta_pos = robot.delta_points(robot.position, td["data"]["prev_robot_position"])
                
                # Detect when robot starts moving
                if td["data"]["robot_start_move_time"] is None and delta_pos > 1:
                    td["data"]["robot_start_move_time"] = time.time()
                    td["data"]["straight_driving_start"] = time.time()
                    text = f"Robot started moving at angle {angle_x_disp:0.0f}°"
                
                # While robot is moving, check if it's staying within deviation limits
                if td["data"]["robot_start_move_time"] is not None and delta_pos > 0.5:
                    # If deviation is within limits and we're tracking straight driving
                    if angle_diff <= 10 and td["data"]["straight_driving_start"] is not None:
                        # Calculate current straight driving duration
                        current_time = time.time()
                        td["data"]["straight_driving_duration"] = current_time - td["data"]["straight_driving_start"]
                        
                        # Update text to show progress
                        if td["data"]["straight_driving_duration"] >= 3.0:
                            text = f"Success! Robot drove straight for {td['data']['straight_driving_duration']:.1f}s"
                            td["data"]["task-failed"] = ""  # Clear any failure state
                        else:
                            text = f"Straight: {td['data']['straight_driving_duration']:.1f}/3.0s, Deviation: {angle_diff:.1f}°"
                    
                    # If deviation exceeds limits
                    elif angle_diff > 10:
                        # Reset straight driving timer
                        td["data"]["straight_driving_start"] = None
                        td["data"]["straight_driving_duration"] = 0
                        
                        # Set task as failed if not already
                        if not td["data"]["task-failed"]:
                            td["data"]["task-failed"] = f"Robot deviated {angle_diff:.1f}° (max allowed: 10°)"
                            
                            # Find closest cone to knock down
                            if robot.position_px is not None and len(td["data"]["cones-coords"]) > 0:
                                min_index = closest_node((robot.position_px[1], robot.position_px[0]), 
                                                       td["data"]["cones-coords"])
                                if min_index not in td["data"]["failed-cone"]:
                                    td["data"]["failed-cone"][min_index] = -20
                
                # Detect when robot stops moving
                if td["data"]["robot_start_move_time"] is not None and delta_pos < 0.5:
                    if td["data"]["robot_end_move_time"] is None:
                        td["data"]["robot_end_move_time"] = time.time()
                        
                        # If it didn't drive straight for 3 seconds before stopping
                        if td["data"]["straight_driving_duration"] < 3.0 and not td["data"]["task-failed"]:
                            td["data"]["task-failed"] = f"Robot only drove straight for {td['data']['straight_driving_duration']:.1f}s (need 3.0s)"
        
        # Store current position for next frame
        td["data"]["prev_robot_position"] = robot.position

    # Check for task completion or failure
    if td["end_time"] - time.time() < 1:
        if td["data"]["task-failed"]:
            result["success"] = False
            result["description"] = td["data"]["task-failed"]
            result["score"] = 0
        elif td["data"].get("robot_start_move_time") is None:
            result["success"] = False
            result["description"] = "Robot didn't start moving"
            result["score"] = 0
        elif td["data"]["straight_driving_duration"] >= 3.0:
            result["success"] = True
            result["description"] = f"Success! Robot drove straight for {td['data']['straight_driving_duration']:.1f} seconds with max deviation of {td['data']['max_angle_deviation']:.1f}°"
            result["score"] = 100
        else:
            result["success"] = False
            result["description"] = f"Robot only drove straight for {td['data']['straight_driving_duration']:.1f}s (need 3.0s)"
            result["score"] = 0
    
    return image, td, text, result