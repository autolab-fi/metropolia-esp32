# Lesson 4: Crater Maneuvers — Orientation Adjustment on Mars

## Objective

Learn how to command your Mars rover to turn right and left in place, enabling precise orientation adjustments essential for scanning and maneuvering in the Martian crater environment.

## Mission Briefing

Your rover has arrived at the edge of the **Crater** zone, a tricky terrain where accurate orientation is crucial to safely scan and navigate the area. Before conducting scientific scans, the NAME OF THE ROVER must correctly align itself by turning right and left on the spot to face target points.

Mastering these turning commands allows the rover to pivot efficiently between different directions, preparing it to explore the crater's secrets.

## Scientific Context

On Mars, rovers often need to turn precisely to aim instruments or change direction without large translations, conserving energy and avoiding hazardous terrain. Turning in place helps the rover align for imaging, sampling, and communication tasks.

## Programming Theory

Your rover can turn in place using two simple commands from the **lineRobot.h** library:

- `robot.turnRight();` — Rotates the rover about its center to the right.
- `robot.turnLeft();` — Rotates the rover about its center to the left.

These functions do not require parameters; calling them once initiates a predefined turn, often by a fixed angle (like 90 degrees), allowing precise orientation adjustments.

Here's a diagram showing possible rover orientations after turns:

![robot_directions](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_1/directions.png?raw=true)

Write a program where the rover:

1. Turns **right** once (pivot clockwise).
2. Turns **left** once (pivot counterclockwise).
3. Turns **left** again (facing the new direction after two left turns).

This sequence simulates scanning around the crater by changing orientation efficiently.


## Mission Debrief

Well done! By controlling your rover's turning maneuvers, you have given it the ability to orient itself in four directions around the crater. This control is essential for complex operations like scanning, obstacle avoidance, and maneuvering in tight Martian terrain.

Get ready for more advanced movement control in the next lesson as you continue your Mars exploration mission!