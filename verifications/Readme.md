# Description

This folder will be fully downloaded to the device responsible for automated verification.

## Structure

The name of each verification function must match the `str_id` field specified in the `lessons_list.json` file. Additionally, each verification function must be located in a Python file whose name matches the `str_id` of the module specified in the `lessons_list.json` file.

Example:
In the `lessons_list.json` file, the first module titled "Introduction to the Robot" has a `str_id` field with the value `module_0`. Therefore, this directory contains a file named `module_0.py`. Additionally, in the `lessons_list.json` file, within the module titled "Introduction to the Robot," there is a `lessons` list containing several lessons with `str_id` fields such as: `draw`, `test_drive`, and `license_to_drive`. The `module_0.py` file contains functions with corresponding names. These functions will be used by the device responsible for automated verification.

## Description of the Verification Function

The verification function is called for each frame received from the camera.

Arguments passed to the verification function:
- `robot` - a reference to the `robot` object, which has its own methods that can be used within the verification functions. For more details about the robot object's methods, refer to [here](#robot-object).
- `image` - the image from the camera, an object of type `numpy.ndarray`. The image is in RGB format.
- `td` - a dictionary containing various parameters required for the verification function, an object of type `dict`. On the first call of the function, it is set to `None`.

The function returns:
- `image` - the modified image within the verification function, which will be displayed to the user, an object of type `numpy.ndarray`. The image is in RGB format.
- `td` - a dictionary containing various parameters required for the verification function, an object of type `dict`. This dictionary can store data that will be used in subsequent iterations of the verification function. **It is mandatory** to include a field named **`end_time`** in this dictionary, which specifies when the verification will end.
- `text` - the message text to be displayed to the user, a field of type `string`.
- `result` - a dictionary containing the results of the verification iteration. This dictionary must include the following **mandatory** fields:
    - **`success`** - a field of type `boolean`. If this field is `False`, the task is considered failed, and the verification ends immediately.
    - **`description`** - a description of the result, which will be displayed to the user after the verification ends. A field of type `string`.
    - **`score`** - the task score, ranging from 0 to 100, where 0 means the task is failed, and 100 means the task is completed perfectly.

## Additional Mandatory Data in Module Files

In each module file, besides the verification functions and their helper functions, the following must **mandatorily** be included:

1) A dictionary containing the starting positions for each task. Each starting position is described by two tuples: the first is the position in centimeters on the field; the second is the robot's direction. The guiding point is calculated as follows: the robot's x-coordinate + the first value from the direction tuple, and the robot's y-coordinate + the second value from the direction tuple. The keys of the dictionary are the `str_id` fields of the tasks from the `lessons_list.json` file.

    Example of guiding point calculation:
    Suppose for the task `test_drive`, we have a list of two points: `[(35, 50), (30, 0)]`. Here, `(35, 50)` is the starting point the robot will move to. `(30, 0)` is the robot's direction. When the robot reaches the starting point, its coordinates will roughly match `(35, 50)`. The guiding point will then be calculated as: `(35+30, 50+0)`, meaning the robot will be directed toward the point `(35+30, 50+0)`, i.e., in the positive direction of the x-axis.

    Example of a dictionary with starting points:
    ```python
    # start points for the tasks
    target_points = {
        'test_drive': [(35, 50), (30, 0)],
        'license_to_drive': [(35, 50), (30, 0)],
        'draw': [(50, 50), (30, 0)]
    }
    ```

2) A dictionary containing information about blocking library functions. This is necessary to prevent cheating. For example, a course task might require the user to write a function for robot movement, but the user might attempt to use a standard library function for movement. To address this, a blocking mechanism is introduced. If the value in this dictionary is `True`, the standard library functions will be blocked. The keys of the dictionary are the `str_id` fields of the tasks from the `lessons_list.json` file.

    Example of such a dictionary:
    ```python
    block_library_functions = {
        'test_drive': False,
        'license_to_drive': False,
        'draw': False,
    }
    ```

3) A function that returns a value from dictionary 1. The function below can simply be copied into the module file.

    ```python
    # function to get value from dictionary target_point
    def get_target_points(task):
        global target_points
        return target_points[task]
    ```

4) A function that returns a value from dictionary 2. The function below can simply be copied into the module file.

    ```python
    # function to get value from dictionary block_library_functions
    def get_block_library_functions(task):
        global block_library_functions
        return block_library_functions[task]
    ```

## Robot Object

The `robot` object is an instance of the `RobotESP32_MQTT` class, which is used to control and interact with the robot on the testing ground. This class provides methods and fields for retrieving information about the robot. The source files can be viewed [here](https://github.com/autolab-fi/lineRobot-cpp-worker/blob/main/src/RobotESP32MQTT.py) (if you have an access to the repository).

### Object Fields

- **`name`** (`str`): The name of the robot.
- **`model`** (`str`): The FQBN (Fully Qualified Board Name) of the robot's board. For this robot, the value is always `esp32:esp32:nodemcu-32s`.
- **`user`** (`str`): The username of the user whose code is currently being tested.
- **`status`** (`str`): The current status of the robot. Possible values: `"Online"` (connected) and `"Offline"` (not connected).
- **`position`** (`tuple[float, float]`): The position of the robot in centimeters. The point corresponds to the center of the apriltag attached to the robot.
- **`position_px`** (`tuple[int, int]`): The position of the robot in pixels on the image. The point corresponds to the center of the apriltag.
- **`top_right`** (`tuple[float, float]`): The top-right corner of the apriltag in centimeters.
- **`top_left`** (`tuple[float, float]`): The top-left corner of the apriltag in centimeters.
- **`bottom_left`** (`tuple[float, float]`): The bottom-left corner of the apriltag in centimeters.
- **`bottom_right`** (`tuple[float, float]`): The bottom-right corner of the apriltag in centimeters.
- **`top_right_px`** (`tuple[int, int]`): The top-right corner of the apriltag in pixels.
- **`top_left_px`** (`tuple[int, int]`): The top-left corner of the apriltag in pixels.
- **`bottom_left_px`** (`tuple[int, int]`): The bottom-left corner of the apriltag in pixels.
- **`bottom_right_px`** (`tuple[int, int]`): The bottom-right corner of the apriltag in pixels.

### Object Methods

#### `get_info() -> Dict[str, Any]`
Returns a dictionary with information about the robot. All data in the dictionary corresponds to the object's fields.

**Return value:**
```json
{
    "name": name,
    "position": position,
    "position_px": position_px,
    "direction": compute_angle_x(),
    "firmware_version": firmware_version,
    "top_right": top_right,
    "top_left": top_left,
    "bottom_left": bottom_left,
    "bottom_right": bottom_right,
    "top_right_px": top_right_px,
    "top_left_px": top_left_px,
    "bottom_left_px": bottom_left_px,
    "bottom_right_px": bottom_right_px
}
```

All fields related to the robot's position may have the value **`None`** if the robot is not found in the image.

#### `get_msg() -> Optional[str]`
Retrieves a message from the user's MQTT topic. If the `printMQTT` function was used in the robot's code, the message can be read using this method. Messages are placed in a queue with a size of 10. If the queue is full, the oldest message is removed.

**Important:** Messages cannot be read faster than 10 times per second (with a more likely reading speed of 6-7 times per second). It is recommended to use delays (e.g., 200-500 ms) in the user's code.

#### `pixels_to_cm(pixels: float) -> float`
Converts a value from pixels to centimeters.

**Arguments:**
- `pixels` (`float`): The value in pixels.

**Return value:**
- `float`: The value in centimeters.

#### `cm_to_pixel(cm: float) -> int`
Converts a value from centimeters to pixels.

**Arguments:**
- `cm` (`float`): The value in centimeters.

**Return value:**
- `int`: The value in pixels.

#### `create_vector(point_0: Tuple[float, float], point_1: Tuple[float, float]) -> Tuple[float, float]`
Creates a vector on the plane from two points.

**Arguments:**
- `point_0` (`Tuple[float, float]`): The starting point.
- `point_1` (`Tuple[float, float]`): The ending point.

**Return value:**
- `Tuple[float, float]`: A vector represented as a tuple of two floating-point numbers.

#### `angle_of_vectors(vec_0: Tuple[float, float], vec_1: Tuple[float, float]) -> float`
Returns the angle between two vectors.

**Arguments:**
- `vec_0` (`Tuple[float, float]`): The first vector.
- `vec_1` (`Tuple[float, float]`): The second vector.

**Return value:**
- `float`: The angle between the vectors in degrees.

#### `mid_point(point_0: Tuple[float, float], point_1: Tuple[float, float]) -> Tuple[float, float]`
Returns the midpoint between two points.

**Arguments:**
- `point_0` (`Tuple[float, float]`): The first point.
- `point_1` (`Tuple[float, float]`): The second point.

**Return value:**
- `Tuple[float, float]`: The midpoint.

#### `compute_angle_robot_point(point: Tuple[float, float]) -> float`
Calculates the angle between the robot's current direction and the vector pointing to the specified point.

**Arguments:**
- `point` (`Tuple[float, float]`): The point to which the vector is directed.

**Return value:**
- `float`: The angle in degrees.

#### `compute_angle(vec: Tuple[float, float]) -> float`
Calculates the angle between the robot's current direction and the given vector.

**Arguments:**
- `vec` (`Tuple[float, float]`): The vector with which the angle is calculated.

**Return value:**
- `float`: The angle in degrees.

#### `compute_angle_x() -> float`
Calculates the angle between the robot's current direction and the X-axis.

**Return value:**
- `float`: The angle in degrees.

#### `draw_frame(image: numpy.ndarray) -> numpy.ndarray`
Draws a frame around the apriltag and a point at the center on the image using OpenCV.

**Arguments:**
- `image` (`numpy.ndarray`): The input image.

**Return value:**
- `numpy.ndarray`: The image with the drawn frame and point.

#### `draw_info(image: numpy.ndarray) -> numpy.ndarray`
Draws graphics on top of the image, including a frame around the apriltag, the current UTC time, the robot's status, the username, and the robot's position in space.

**Arguments:**
- `image` (`numpy.ndarray`): The input image.

**Return value:**
- `numpy.ndarray`: The image with the drawn information.

#### `delta_points(point_0: Tuple[float, float], point_1: Tuple[float, float]) -> float`
Calculates the distance between two points on the plane.

**Arguments:**
- `point_0` (`Tuple[float, float]`): The first point.
- `point_1` (`Tuple[float, float]`): The second point.

**Return value:**
- `float`: The distance between the points.

## Example Implementation of a verification Function

```python
def task_test(robot, image, td: dict):
    # Initialize the result structure
    result = {"success": True, "description": "You are amazing! The Robot has completed the assignment", "score": 100}
    # Initialize text for the user
    text = "Not recognized"

    # Initialize the test data structure
    if not td:
        td = {"end_time": time.time() + 20}

    # Draw basic info about the robot, verification, and user
    image = robot.draw_info(image)

    # Get info about the robot
    info = robot.get_info()
    robot_position_px = info['position_px']
    robot_position = info['position']

    # Print the robot's position if it is found in the image
    if robot_position is not None:
        text = f'Robot position: x: {robot_position[0]:0.1f} y: {robot_position[1]:0.1f}'

    # Get a message from the robot and display it to the user if it is not None
    msg = robot.get_msg()
    if msg is not None:
        text = f"Message received: {msg}"

    # NB: Return IMAGE
    return image, td, text, result
```

- Initialization of the structure describing the verification results. As can be seen, the values in this structure are not redefined anywhere else in the code, so this verification will always succeed. For more details about the structure, see [here](#description-of-the-verification-function).

    ```python
    result = {"success": True, "description": "You are amazing! The Robot has completed the assignment", "score": 100}
    ```

- Initialization of the text for the user, which will be displayed if the robot is not found in the image and if no messages are received from MQTT.

    ```python
    text = "Not recognized"
    ```

- Initialization of the `td` structure, which can store values required for the verification. For more details about the structure, see [here](#description-of-the-verification-function).

    ```python
    if not td:
        td = {"end_time": time.time() + 20}
    ```

- Draw graphics on top of the image. For more details, see [here](#draw_infoimage-numpyndarray---numpyndarray).

    ```python
    image = robot.draw_info(image)
    ```

- Retrieve information about the robot's current position. For more details, see [here](#get_info---dictstr-any).

    ```python
    info = robot.get_info()
    robot_position_px = info['position_px']
    robot_position = info['position']
    ```

- Check if the robot was found in the image.

    ```python
    if robot_position is not None:
        text = f'Robot position: x: {robot_position[0]:0.1f} y: {robot_position[1]:0.1f}'
    ```

- Read a user message sent using `printMQTT`. For more details, see [here](#get_msg---optionalstr).

    ```python
    msg = robot.get_msg()
    if msg is not None:
        text = f"Message received: {msg}"
    ```

- The function returns **4** parameters, necessarily in this order.

    ```python
    return image, td, text, result
    ```