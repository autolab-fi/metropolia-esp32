# Lesson 1: Monitoring Robot Data with printMQTT

## Lesson Objective

Learn how to use the `printMQTT` function to monitor and debug robot behavior by displaying real-time data.

---

## Introduction

When working with robots, it's essential to understand what's happening internally. The `printMQTT` function allows you to send data from your robot to be displayed on your screen, making debugging easier and helping you understand your robot's behavior better.

---

## Theory

### What is printMQTT?

`printMQTT` is a special function that sends text messages from your robot to the user interface. These messages appear in a console overlay on your screen.

### When to Use printMQTT

- Display sensor readings
- Track loop iterations
- Show calculated values
- Debug conditional statements
- Monitor robot state changes

### Basic Syntax

There are three main ways to use printMQTT:

```cpp
printMQTT("Your message here");         // Text only
printMQTT(variableName);                // Variable value
printMQTT("Speed: " + String(speed));   // Text + variable
```

---

## Code Implementation

```cpp
#include <lineRobot.h>

void setup() {
  // Initialize
  printMQTT("Robot starting up...");

  // Setting up variables
  int motorSpeed = 150;
  printMQTT("Initial motor speed: " + String(motorSpeed));

  // Show robot information
  printMQTT("Battery level: " + String(robot.getBatteryPercentage()) + "%");
}

void loop() {
  // Read a sensor
  int lightValue = robot.readLightSensor();

  // Print the value
  printMQTT("Light sensor: " + String(lightValue));

  // Small delay to avoid flooding messages
  delay(1000);
}
```

---

## Understanding the Logic

1. In `setup()`, we send initial messages showing the robot is starting
2. We display the initial settings like motor speed
3. In `loop()`, we continuously read a sensor value
4. We use `printMQTT` to send the value to our console
5. A delay prevents too many messages from being sent at once

---

## Assignment

Create a program that demonstrates all three ways of using the `printMQTT` function:

1. Create and initialize the following variables:

   - An integer called `motorSpeed` with a value of 150
   - A string called `robotStatus` with the value "Ready"
   - A float called `temperature` with a value of 25.5

2. In the `setup()` function:

   - Use `printMQTT` with text only to display "Robot diagnostic starting"
   - Use `printMQTT` with a variable only to display the value of `robotStatus`
   - Use `printMQTT` with combined text and variable to display "Motor speed set to: [motorSpeed]"
   - Use `printMQTT` with combined text and variable to display "Temperature: [temperature] C"

Your code structure should look like this:

```cpp
#include <lineRobot.h>

void setup() {
  // Initialize variables
  int motorSpeed = 150;
  String robotStatus = "Ready";
  float temperature = 25.5;

  // YOUR CODE HERE
  // 1. Use printMQTT with text only
  // 2. Use printMQTT with variable only
  // 3. Use printMQTT with text + variable (motor speed)
  // 4. Use printMQTT with text + variable (temperature)
}

void loop() {

}
```

Make sure your program demonstrates all three ways of using `printMQTT` to send information.

---

## Conclusion

The `printMQTT` function is a powerful tool for monitoring your robot's behavior in real-time. By displaying key values and state information, you can better understand how your code affects the robot's actions and quickly identify issues. Mastering the different formats of `printMQTT` will help you create more informative debug outputs for your future robot projects.
