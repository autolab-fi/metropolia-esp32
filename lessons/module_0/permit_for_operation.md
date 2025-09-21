## Lesson 2: Permit for Operation

### Objective

Modify a function parameter to control your rover's movement.

### Introduction

In this lesson, you will earn your official Mars rover "Permit" for operation of the rover on Mars. You'll be writing your first program from scratch, but first, let's go over a fundamental concept in programming: **functions**.

---

### Theory

In the previous lesson, we used the `rover.h` library, and we'll continue to use it. This library contains functions that allow us to easily control our rover's movements.

**Functions** are named blocks of code that perform specific tasks. When you "call" or "invoke" a function, it performs a specific action, like moving the rover or turning its wheels. Some functions have **parameters**, which allow you to pass specific data into the function to customize its behavior. For example, in the function `moveForwardDistance(distance)`, the `distance` parameter tells the rover exactly how many meters to drive.

We've already used the function `rover.moveForwardSeconds(seconds)`. This function makes the rover move forward, and the `seconds` parameter determines the duration of the movement.

---

### Real Mission Insight: Rover Autonomy

Because of the long communication delay between Earth and Mars (from a few minutes to over 20 minutes, depending on the planets' positions), mission controllers can't "joystick" the rover in real-time. Instead, they upload a complete sequence of commands for the rover to execute autonomously, typically for a full Martian day (or **sol**). **Your program simulates a small portion of this pre-planned command sequence.** The rover's on-board computer uses its navigation cameras and hazard sensors to carry out the instructions while avoiding unexpected obstacles.

---

![verfification](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_1/function.png?raw=true)

### Mission

Write a program for the rover to make it drive straight for **5 seconds**. You can refer back to the previous lesson to recall how to set the rover in motion. Good luck!

**Hint:** Remember to change the parameter inside the parentheses to control how long the rover drives.

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

Congratulations! You have written your own program for rover movement! You've taken a crucial step toward becoming a mission planner. In the next lesson, we will explore the rover's movement in different directions using the `rover.h` library.
