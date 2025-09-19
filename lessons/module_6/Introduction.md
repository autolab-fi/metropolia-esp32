# Lesson 1: Monitoring Robot Data with printMQTT

## Lesson Objective

Learn how to use the `printMQTT` function to monitor and debug robot behavior by displaying real-time data.

---

## Introduction

When working with robots, it's essential to understand what's happening internally. The `printMQTT` function allows you to send data from your robot to be displayed on your screen, making debugging easier and helping you understand your robot's behavior better. This same principle of telemetry and real-time monitoring is fundamental to Mars missions, where rovers continuously transmit status data across millions of miles of space. NASA's Deep Space Network receives thousands of data points daily from Mars rovers - everything from wheel temperatures and battery voltages to atmospheric pressure and scientific measurements. Just as you'll use printMQTT to debug your classroom robot, mission engineers rely on this telemetry stream to monitor rover health and troubleshoot problems on Mars.

---

## Theory

### What is printMQTT?

`printMQTT` is a special function that sends text messages from your robot to the user interface. These messages appear in a console overlay on your screen. This mirrors how Mars rovers communicate with Earth through radio signals, sending formatted telemetry data that appears on engineers' computer screens at mission control. The Perseverance rover, for example, transmits data in structured formats that allow mission teams to quickly assess rover status and make operational decisions.

### When to Use printMQTT

- Display sensor readings
- Track loop iterations
- Show calculated values
- Debug conditional statements
- Monitor robot state changes

These use cases directly parallel Mars rover operations. Curiosity rover continuously transmits sensor readings from its weather station, tracks the number of sols (Martian days) it has been operating, shows calculated distances to target destinations, debugs autonomous navigation decisions, and monitors critical state changes like transitions between driving and scientific analysis modes. The systematic approach to data monitoring you'll learn with printMQTT is identical to the telemetry practices that have kept Mars rovers operational for years beyond their planned mission durations.

### Basic Syntax

There are three main ways to use printMQTT:

```cpp
printMQTT("Your message here");         // Text only
printMQTT(variableName);                // Variable value
printMQTT("Speed: " + String(speed));   // Text + variable
```

Mars rovers use similar data formatting approaches. The Opportunity rover transmitted simple status messages like "Drive complete," numerical sensor values such as atmospheric pressure readings, and combined text-data messages like "Sol 3487: Distance driven today 45.3 meters." This structured communication format ensures that both automated monitoring systems and human operators can efficiently process the information streaming back from Mars.

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

This logical flow matches Mars rover communication protocols. When Perseverance powers up each morning, it first sends startup diagnostic messages to confirm all systems are operational. It then reports initial configuration settings like instrument temperatures and pointing angles. Throughout the sol, it continuously streams sensor data at controlled intervals to prevent overwhelming the limited bandwidth of the interplanetary communication link. The delay concept you're learning is critical for Mars missions - rovers must carefully manage their data transmission rates to ensure all important information reaches Earth within the available communication windows.

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

This assignment structure mirrors the systematic status reporting used by Mars rovers during initialization. When Curiosity begins a new sol, it follows a similar sequence: announces the start of daily diagnostics, reports its overall operational status, confirms drive system settings, and transmits environmental sensor readings. This methodical approach to status communication has been essential for maintaining situational awareness between Earth-based mission teams and rovers operating autonomously on Mars.

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

These telemetry and monitoring skills you've developed connect directly to the communication systems that enable Mars exploration. From the first successful telemetry received from Viking 1 in 1976, to the daily status reports from today's Perseverance rover, the ability to transmit, receive, and interpret robotic status data has been fundamental to every Mars mission success. As NASA prepares for increasingly autonomous Mars rovers and eventual human missions, the systematic approach to robot monitoring and debugging that you're mastering will continue to be essential for ensuring mission safety and success across the vast distances of interplanetary space.
