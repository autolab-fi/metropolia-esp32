## Lesson 3: Mission Zero

### Objective

Explore functions for moving your Mars rover a specific distance.

### Introduction

In the previous lessons, we used time-based commands to move the rover. Now, it's time to introduce new functions that allow for more precise control over its position: **moving forward and backward by a specific distance**. This is a critical skill for mission planners who need to navigate around hazards and precisely approach scientific targets.

---

### Theory

You've already learned about **functions** and **parameters**. You used `rover.moveForwardSeconds(seconds)`, where the parameter represented the duration of movement. However, for navigating the varied terrain of Mars, mission planners need functions that allow movement based on distance in **meters**. For our simulation, we will use **centimeters** to represent a smaller-scale traverse.

- `rover.moveForwardDistance(dist)`: A function for moving the rover forward by the number of centimeters specified by the parameter **dist**.
- `rover.moveBackwardDistance(dist)`: A function for moving the rover backward by the number of centimeters specified by the parameter **dist**.

---

### Real Mission Insight: Odometry

Real Mars rovers use **odometry** to track their position and distance traveled. This involves using data from their wheel rotations, combined with images from their navigation cameras, to calculate how far they've moved from a known point. While not always perfectly accurate, this method is essential for keeping track of the rover's location on the vast Martian surface.

---

### Assignment

Create a program that guides the rover through three key positions: first navigate to Location A (30cm from the starting point), then proceed to Location B (50cm from the starting point), and finally return to the original starting position.

Below is a Reference Image provided for your reference

![Location Info](https://github.com/autolab-fi/metropolia-esp32/blob/main/images/module_1/location_traversal.png?raw=true)

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

Congratulations! You've learned about two crucial functions that will be valuable in your future missions. Precise distance control is a key skill for a successful Mars mission. Now, you're one step closer to navigating the Red Planet!
