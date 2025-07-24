## Course Lesson Plan: Martian Rover Mission

**Mission Briefing:** You are part of the Mars Rover Exploration Team! Your robot, the "NAME OF THE ROVER.," has landed in Gale Crater on Mars to investigate potential signs of ancient life and prepare for future human missions. Your primary mission is to collect crucial data on Martian geology, search for organic molecules, and assess environmental conditions. Every task you complete will bring us closer to understanding the Red Planet.

## Contents
- [Introduction to the Rover](#introduction-to-the-rover)
- [Navigating the Martian Terrain](#navigating-the-martian-terrain)
- [The Rover's Central Processor](#the-rovers-central-processor)
- [Signaling and Communication](#signaling-and-communication)
- [Actuating Sampling Tools](#actuating-sampling-tools)
- [Precision Locomotion with Encoders](#precision-locomotion-with-encoders)
- [Autonomous Navigation Systems](#autonomous-navigation-systems)
- [Advanced Rover Maneuvers](#advanced-rover-maneuvres)
- [Geological Analysis with Sensors](#geological-analysis-with-sensors)

### Introduction to the Rover
**Mission Objective:** Familiarize yourself with the NAME OF THE ROVER. rover's systems and basic operational controls before embarking on critical research missions.

**Story:** Your ground control team needs you to perform initial systems checks on the NAME OF THE ROVER to ensure all components are functioning after its journey through space and atmospheric entry.

0. **"Mars Sandbox"** - Introduction to the rover platform, listing all its sensors and actuators (peripherals), describing the programming environment, and outlining any restrictions on libraries and command keywords.
1. **"First Contact: Test Drive"** - Practice initiating basic forward movement of the rover using the provided library functions.
2. **"Pilot's Qualification: Maneuver Certification"** - Independently write a simple program to move the rover, similar to the "Test Drive" but with a slightly more complex path. This certifies your ability to operate the rover.

### Navigating the Martian Terrain
**Mission Objective:** Master precise movement and navigation across the varied Martian landscape to reach specific geological formations.

**Story:** The rover needs to reach designated geological survey points to collect samples. Accurate navigation is crucial to avoid hazards and conserve power.

1. **"Short Range Traverse: Sample Site Approach"** - Use library functions to move the rover a specific distance, both forward and backward, to approach a potential sample collection site.
2. **"Crater Maneuvers: Orientation Adjustment"** - Practice turning the rover right and left in place to orient it correctly for scans.

3. **"Ridge Ascent: Trajectory Programming"** - Write a sequence of commands to move the rover along a predefined trajectory to collect samples around the crater.

### The Rover's Central Processor
**Mission Objective:** Understand how the rover's main processing unit (MCU) controls its various functions, using LEDs as visual indicators.

**Story:** Communication with Earth is vital. The rover uses indicator lights to signal its status and confirm commands. You need to ensure these communication lights are working.

1. **"Status Indicators: Headlights & Warnings"** - Understand the basic operation of the rover's indicator LEDs.
    *   **Task:** Program the rover to turn on its "headlights" (specific LEDs) when it's actively scanning and another set of LEDs to indicate a "warning" state.
2. **"Emergency Beacon: Robot's Alarm"** - Learn more about using `digitalWrite()` and `pinMode()` functions.
    *   **Task:** Program the rover to make its "emergency beacon" LEDs blink in a specific pattern, simulating an alarm or distress signal.

### Actuating Sampling Tools
**Mission Objective:** Learn how to control the rover's motors to deploy and operate its scientific instruments, understanding basic kinematics.

**Story:** The rover's primary tools, like the drill and robotic arm, are powered by motors. You must control these precisely to collect valuable Martian samples.

1. **"Differential Drive: Arm Deployment"** - Introduction to the robot's kinematics (how its wheels move it).
    *   **Task:** Experiment with functions for moving the rover's "arm" (represented by forward motion) to practice precise deployment.
2. **"Movement Function: Drill Positioning"** - Practice writing functions in Arduino.
    *   **Task:** Write a function to rotate the rover to specific angles, simulating positioning the drill for core sampling.
3. **"Electric Motor: Core Sample Extraction"** - Understand the basic principles of DC motors.
    *   **Task:** Move the rover to a specific point on the map using only functions that control individual motors, simulating a precise approach for core sample extraction.

### Precision Locomotion with Encoders
**Mission Objective:** Utilize encoders to achieve highly accurate movement and positioning, critical for scientific data collection.

**Story:** For accurate mapping and sample return, the rover needs to know precisely how far it has traveled and its exact orientation. Encoders provide this crucial feedback.

1. **"Encoder Feedback: Wheel Revolution Monitoring"** - Understand what an encoder is and how it provides feedback on wheel rotation.
    *   **Task:** Add a condition to a provided code snippet for reading data from encoders so that the robot stops when it detects a certain number of wheel revolutions, indicating it has moved a set distance.
---
2. **"Odometer: Traverse Distance Calculation"** - Understand how an odometer works and its implementation.
    *   **Task:** Write an odometer function that converts encoder data into real-world units (centimeters). The rover should then stop automatically after covering a specified distance, simulating a precise traverse to a geological feature.
3. **"Mission Log: Data Storage on Mars"** - Learn about reading and writing files on ESP32.
    *   **Task:** Simulate receiving text data from a sensor log file (`sensor_raw.log`) and then writing a processed summary of this data to another file (`processed_data.log`), mirroring how rovers manage onboard data.
4. **"Speedometer: Martian Wind Analysis"** - Understand how a speedometer works using distance data.
    *   **Task:** Implement a speedometer that measures the average speed of the rover's movement. This data could be correlated with Martian wind patterns affecting mobility.
5. **"Steering Adjustment: Angular Precision"** - More information about robot kinematics and solving the problem of tracking the robot's angle of rotation.
    *   **Task:** Write code to rotate the rover precisely by 90 degrees, essential for turning corners on its survey path or aligning instruments.

### Autonomous Navigation Systems
**Mission Objective:** Introduce basic concepts of automatic control theory to enable the rover to make more intelligent, self-correcting movements.

**Story:** The rover often operates autonomously. To ensure it stays on course and reaches its targets efficiently, it needs intelligent control systems to correct deviations.

1. **"Relay Controller: Simple Course Correction"** - Understand what controllers are (open-loop and closed-loop systems) and how a simple relay controller works.
    *   **Task:** Implement a relay controller for turning the robot. For example, if the robot deviates from a straight path, the controller activates a brief turn until it's back on course.
2. **"P-Controller: Proportional Guidance"** - Understand what a P-controller is and why it's an improvement over a relay controller.
    *   **Task:** Implement turning with a P-controller. This controller applies a turning force proportional to the error, leading to smoother corrections.
3. **"PI-Controller: Eliminating Drift"** - Address the drawbacks of a P-controller and learn how the integral component helps eliminate steady-state error.
    *   **Task:** Implement turning with a PI-controller. This allows the rover to reach and maintain its target angle without persistent small errors.
4. **"PID-Controller: Optimized Trajectory"** - Understand the differential component and how it helps eliminate overshoot.
    *   **Task:** Implement turning with a PID-controller for optimal, stable, and quick angle adjustments.
5. **"Tuning PID: Martian Environment Adaptation"** - Learn about methods like the Ziegler-Nichols method for tuning coefficients. (No specific task, focus on understanding).

### Advanced Rover Maneuvers
**Mission Objective:** Develop custom programming libraries for the rover to create sophisticated motion functions and optimize its performance in complex scenarios.

**Story:** To truly explore Mars, the rover needs a robust set of custom-built functions for reliable and efficient movement across diverse terrain.

1. **"Motion Library: Rover's Movement Toolkit"** - Understand why custom libraries are useful.
    *   **Task:** Begin building your own motion library for the rover, including functions for reading data from encoders.
2. **"Straight Motion: Precision Traverse"** - Improve straight motion using a controller.
    *   **Task:** Apply a controller (P, PI, or PID) to improve the rover's ability to drive perfectly straight, critical for accurate mapping.
3. **"Automatic Transmission: Speed Optimization"** - Improve motion functions with a speed controller.
    *   **Task:** Implement a speed controller to allow the rover to maintain a constant velocity, even when encountering minor obstacles or inclines.
4. **"Turning Functions: Custom Angle Rotation"** - Create more advanced functions for turning.
    *   **Task:** Develop a function that allows you to specify any desired angle as an argument, and the rover will rotate precisely to that angle.

### Geological Analysis with Sensors
**Mission Objective:** Utilize the line and color sensors for detailed geological analysis and navigation along specific Martian features.

**Story:** Your rover needs to identify specific geological features, like mineral veins (lines) or unusual rock compositions (colors), and navigate along them for detailed study.

**For a simple Martian path (simulated line on the map):**
1.  **"Line Sensor: Following Ancient Riverbeds"** - Understand what a line sensor is and how it works.
    *   **Task:** Read data from the line sensor and add a function to read this data to your custom library. The robot should travel 50 cm along a marked "riverbed" and record sensor data, which will then be compared to expected patterns of the riverbed.
2.  **"Path Entry: Locating a Mineral Vein"** - A bit about calibration (without calibration functions, just for general understanding).
    *   **Task:** Write an algorithm for automatic entry onto a "mineral vein" (a marked line). If the robot encounters the vein, it should stop precisely on it.
3.  **"Line Following: Tracing the Vein"** - Implement a line following algorithm.
    *   **Task:** Implement line following using a simple algorithm to trace the mineral vein for detailed surveying.
4.  **"Noise Filter: Data Refinement"** - Use a moving average filter to average data obtained from sensors.
    *   **Task:** Apply a noise filter to the line sensor data to get more reliable readings, especially in dusty Martian conditions.
5.  **"Line Tracking Controller: Circular Scan"** - Apply P, PD, or PID controllers for line following.
    *   **Task:** Implement a line tracking controller that allows the rover to follow a circular path (representing a large geological feature) within a specified time, simulating a continuous scan.
6.  **"Colorful World: Identifying Rock Composition"** - Understand what a color sensor is and how it works.
    *   **Task:** Read data from the color sensor. The robot should travel a specified distance and record color data, simulating the identification of different rock compositions.

**For a more complex Martian path (simulated track on the map):**
1.  **"Night Road: Traversing Shaded Canyons"** - Implement an algorithm for track navigation if there is a section with inverted color on it (simulating a shaded area where the "line" appears reversed).
2.  **"Dust Storms: Overcoming Disrupted Paths"** - The marked "road" is interrupted by several transverse lines (simulating dust dunes or rocky patches).
    *   **Task:** Implement an algorithm: if all line sensors are activated (indicating a wide obstruction), the robot needs to slow down and drive straight until it finds the continuation of the main path.
3.  **"Regolith Erosion: Missing Path Segments"** - There is a missing piece of the marked "path" (simulating erosion).
    *   **Task:** The robot must continue along the path and find its continuation. Implement an algorithm using sweeping movements to reacquire the path.
4.  **"Hazardous Terrain: Slowing for Unstable Ground"** - There is a yellow patch on the path (simulating unstable or hazardous ground) that needs to be traversed at a reduced speed.
    *   **Task:** Program the robot to detect this color change and automatically reduce its speed while crossing this zone.

[1] https://www.youtube.com/watch?v=fTmG0ClNGjo
[2] https://www.youtube.com/watch?v=cacSDQMA29Y
[3] https://www.youtube.com/watch?v=ujh-dtEvyIw
[4] https://www.youtube.com/watch?v=FVRwP3FmUeI
[5] https://www.youtube.com/watch?v=zp6pNrrPEFc
[6] https://www.youtube.com/watch?v=cf-JUz3gqdk
[7] https://www.youtube.com/watch?v=TteyPrkP6E0
[8] https://www.youtube.com/watch?v=W0Ru6hsRZcI
[9] https://www.sciencebuddies.org/blog/mars-science-lessons
[10] https://www.jpl.nasa.gov/edu/resources/lesson-plan/mission-to-mars-unit/
[11] https://cefls.libguides.com/explore-mars
[12] https://lasp.colorado.edu/maven/files/2011/10/Lesson-5_final_access.pdf
[13] https://learnenglish.britishcouncil.org/skills/reading/c1-reading/life-mars
[14] https://www.scribd.com/document/756846062/Unit-2-A-Starry-Home
[15] https://science.nasa.gov/solar-system/resources/resource-packages/mars-resources/
[16] https://education.minecraft.net/lessonsupportfiles/Mars-Lesson.docx
[17] https://mars.nasa.gov/files/mepjpl/MSIP-MarsActivities.pdf
[18] https://www.scribd.com/document/391169223/ps-sb-ls-l1-scripts