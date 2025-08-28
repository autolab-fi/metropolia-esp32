# Mars Rover Mission Simulator

## Lesson 3: Short Distance Traverse

### Objective

Explore functions for moving your Mars rover a specific distance.

### Introduction

In the previous lessons, we used time-based commands to move the rover. Now, it's time to introduce new functions that allow for more precise control over its position: **moving forward and backward by a specific distance**. This is a critical skill for mission planners who need to navigate around hazards and precisely approach scientific targets.

---

### Theory

You've already learned about **functions** and **parameters**. You used `robot.moveForwardSeconds(seconds)`, where the parameter represented the duration of movement. However, for navigating the varied terrain of Mars, mission planners need functions that allow movement based on distance in **meters**. For our simulation, we will use **centimeters** to represent a smaller-scale traverse.

- `robot.moveForwardDistance(dist)`: A function for moving the rover forward by the number of centimeters specified by the parameter **dist**.
- `robot.moveBackwardDistance(dist)`: A function for moving the rover backward by the number of centimeters specified by the parameter **dist**.

---

### Real Mission Insight: Odometry

Real Mars rovers use **odometry** to track their position and distance traveled. This involves using data from their wheel rotations, combined with images from their navigation cameras, to calculate how far they've moved from a known point. While not always perfectly accurate, this method is essential for keeping track of the rover's location on the vast Martian surface.

---

### Assignment

Write a program for the rover to move **backward 35** centimeters and then **forward 20** centimeters. Good luck\!

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
