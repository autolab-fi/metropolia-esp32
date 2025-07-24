# Lesson 3: Short Range Traverse — Approaching the Sample Site on Mars

## Objective

Learn to use functions that control the rover's movement by specifying the distance to move forward or backward, essential for precise navigation to sample collection sites.

## Mission Briefing

Your Mars rover has successfully passed its pilot certification and is now tasked with driving to a nearby **Sample Depot** zone, simulating a Martian rock sample collection site. To safely approach this area without overshooting or collision, you will program the rover to move exact distances—backward and forward—using distance-based movement commands.

## Scientific Context

Accurate positioning is critical for the rover to collect scientific samples effectively. In real Mars missions, rovers must navigate narrow paths and stop precisely near geological features. Being able to command movement by distances rather than approximate times increases landing site safety and mission success.

## Programming Theory

Previously, you learned to move the rover using time-based commands:

```cpp
robot.moveForwardSeconds(seconds);
```

Now, you will use new functions that accept a **distance** parameter (in centimeters):

- `robot.moveForwardDistance(dist)`  
  Moves the rover forward by the distance `dist` centimeters.

- `robot.moveBackwardDistance(dist)`  
  Moves the rover backward by the distance `dist` centimeters.

These functions provide improved control for navigating complex Martian terrain.

![robot_directions](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_1/directions.png?raw=true)

Write a program that commands the rover to:

1. Move **backward 35 centimeters** to back away from the initial docking position.
2. Then move **forward 20 centimeters** advancing towards the sample collection site.

## Mission Debrief

Excellent work! You’ve now mastered movement commands based on precise distances, a valuable skill for navigating the Martian surface. These functions will be essential as you explore more challenging zones like the **Crater** or **Rock Field** in upcoming lessons.

Ready for the next challenge? Your Martian adventure continues!