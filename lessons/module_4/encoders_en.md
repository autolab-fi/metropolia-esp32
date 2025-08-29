### **Lesson 1: Encoders**

## **Lesson objective**

Learn about encoders and their purpose in rover movement.

## **Introduction**

In previous lessons, we controlled the rover's movement using time and motor speed. However, this method isn't very precise because motors can behave differently depending on battery level, surface friction, and mechanical variations. To make our rover move more accurately, we need to measure how much each wheel actually turns. This is where **encoders** come in\! They are essential for a rover's autonomous navigation, providing critical feedback on distance and direction traveled on a foreign planet.

---

## **Theory**

### **What is an Encoder?**

An encoder is a sensor that measures rotation. In robotics, we commonly use **rotary encoders**—devices that track how far something has rotated. There are two main types:

1.  **Absolute Encoders:** These tell you the exact position of rotation, much like a compass shows your precise heading.
2.  **Incremental Encoders:** These count steps of rotation, similar to counting your footsteps. They are particularly useful for measuring displacement.

NASA's Mars rovers, such as **Curiosity** and **Perseverance**, use incremental encoders on their wheels to precisely track distance traveled.This data is critical for tasks like path planning and executing complex maneuvers, ensuring the rover doesn't get lost or stray from its designated route on Mars.

### **Getting Encoder Values in Our Rover**

In this lesson, we will measure the rotation of the rover's wheels in degrees, where:

- Full wheel rotation forward = +360°
- Full wheel rotation backward = -360°

Each wheel on our rover has its own encoder, allowing us to measure the rotation of each wheel separately. We'll use the left encoder for the left wheel and the right encoder for the right wheel.

You will be able to use the following functions to read and control the encoders:

```cpp
rover.encoderDegreesLeft() // Get left wheel rotation in degrees
rover.encoderDegreesRight() // Get right wheel rotation in degrees
rover.resetLeftEncoder() // Reset left encoder to 0
rover.resetRightEncoder() // Reset right encoder to 0
```

### **Distance and Rotation**

For a wheel with diameter D, one full rotation covers a distance of $\pi \times D$. Our rover's wheels have a diameter of 3.5 cm, so:

- One full rotation = $3.5 \times \pi \approx 11 \text{ cm}$

This relationship is vital because it allows us to convert the rotational data from the encoders into a real-world distance traveled. This principle is fundamental to rover navigation on Mars, where every centimeter of movement is tracked to build an accurate map of the terrain.

---

## **Assignment**

Write a program that demonstrates encoder measurements by:

1.  Moving the rover forward exactly one wheel rotation.
2.  Then moving backward one rotation.
3.  Printing encoder values at three points:
    - Start position (after reset)
    - After forward movement
    - After backward movement

Use our new functions to get the encoder values for the left and right wheels accordingly. Print the values and compare them at different rover movement stages.

```cpp
#include <rover.h>
void setup() {
    // Reset encoders values
    rover.resetLeftEncoder();
    rover.resetRightEncoder();
    // Read start position values
    printMQTT("START POSITION");
    printMQTT("LEFT:");
    // Will take encoder values in degrees
    // Assume one rotation ~360°
    // printMQTT(rover.encoderDegreesLeft()); // TODO: this line should be done by student
    printMQTT("RIGHT:");
    //printMQTT(rover.encoderDegreesRight()); // TODO: this line should be done by student

    // Move forward
    rover.moveForwardDistance(3.5 * 2 * 3.14159); // one rotation forward (wheels diameter * pi)
    printMQTT("FORWARD MOVEMENT POSITION");
    printMQTT("LEFT:");
    //printMQTT(rover.encoderDegreesLeft()); // TODO: this line should be done by student
    printMQTT("RIGHT:");
    //printMQTT(rover.encoderDegreesRight()); // TODO: this line should be done by student

    delay(500);

    // Move backward
    rover.moveBackwardDistance(3.5 * 2 * 3.14159); // one rotation backward (wheels diameter * pi)
    printMQTT("BACKWARD MOVEMENT POSITION");
    printMQTT("LEFT:");
    // printMQTT(rover.encoderDegreesLeft()); //TODO: this line should be done by student
    printMQTT("RIGHT:");
    //printMQTT(rover.encoderDegreesRight()); //TODO: this line should be done by student
}

void loop() {
    delay(1000);
}
```

---

## **Conclusion**

You've learned about encoders—sensors vital for precise rover movement. Understanding how they work and how to read their values is crucial for advanced autonomous control, just as it is for NASA's rovers navigating the Martian landscape. In the next lesson, we'll use encoders to build an odometer that tracks the rover's total distance traveled\!
