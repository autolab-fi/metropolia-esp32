---
index: 3
module: module_1
task: short_distance_race
previous: license_to_drive
next: maneuvering
---

# Lesson 3. Short distance race

## Objective

Explore functions for moving the robot a specific distance.

## Introduction

In the past two lessons, we've utilized only one function from the lineRobot library. It's now time to introduce additional functions for controlling the robot: moving backward and moving forward, where the parameter is not the number of seconds but the distance.

## Theory

In the previous lesson, you gained insight into **functions** and **parameters**. You used the **moveForwardSeconds(seconds)** function, with the parameter representing the duration of robot movement in seconds. However, for precise control over the robot's position on the map, we need functions that allow movement based on distance in centimeters.

**robot.moveForwardDistance(dist)** - A function for moving the robot forward by the number of centimeters specified by the parameter **dist**.
**robot.moveBackwardDistance(dist)** - A function for moving the robot backward by the number of centimeters specified by the parameter **dist**.

Robot directions
![robot_directions](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_1/directions.png?raw=true)

## Assignment

Write a program for the robot to move **backward 35** centimeters and then **forward 20** centimeters. Good luck!

```cpp
#include <rover.h>

void setup() {
    // Your code goes here!
}

void loop() {
    // The loop function is not used for this exercise
}
```

---

### Conclusion

Congratulations\! You've learned about two crucial functions that will be valuable in your future missions. Precise distance control is a key skill for a successful Mars mission. Now, you're one step closer to navigating the Red Planet\!
