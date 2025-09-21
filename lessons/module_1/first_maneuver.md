## Lesson 4: Maneuvering

### Objective

Learn about functions for turning the rover right and left.

### Introduction

You've successfully learned how to control the rover's forward and backward movements, but that's not enough for free movement across the Martian terrain. In this lesson, you will learn the functions for turning the rover right and left.

---

### Theory

You already know how to command the rover's straight movement; now let's delve into turning the rover right and left to facilitate movement in four directions.

The image below represents the possible directions of the rover's movement.

`rover.turnLeft()`: A function for turning the rover **left**.

`rover.turnRight()`: A function for turning the rover **right**.

`rover.turnLeftAngle()` : A function for turning the rover **left** by an angle.

`rover.turnRightAngle()` : A function for turning the rover **right** by an angle.

As you can see, these turning functions don't require any parameters. It's sufficient to call them, and the rover will turn in place in the desired direction.

---

### Real Mission Insight: A Rover's First Turn

The first-ever turn executed by a rover on Mars was by the **Sojourner rover** in 1997. After driving off its landing ramp, it performed a small turn to test its steering. This first turn was a critical moment, confirming that the rover's wheels and steering mechanisms were operating correctly after the long journey and challenging landing.

---

### Assignment

Write code for the rover to perform your the following maneuvering on the martian surface.Make the rover to rotate according to the following plan :
1.90 degrees to right
2.45 degrees to left
3.135 degrees to right
4.15 degrees to right

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

Congratulations! Now you can move the rover in four directions\! This skill will prove very useful in the next lesson as you tackle more complex navigation challenges.
