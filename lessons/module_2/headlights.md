---
index: 6
module: module_2
task: headlights
previous: long_distance_race
next: alarm
---
# Lesson 6: Headlights

## Lesson objective
Learn about GPIO.

## Introduction
In this lesson, you will learn about a basic concept for microcontrollers - GPIO, and explore how it works using LEDs installed on the rover!

## Theory
### What is GPIO?
GPIO stands for "General Purpose Input/Output." It's an interface for the microcontroller to interact with external devices. GPIO pins allow us to read signals from a pin or write signals to a device. The signal for GPIO is voltage. 

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_2/headlights_2.png?raw=True)

Today, we'll only discuss signals of the logical high and logical low types: a low signal is 0 volts, while a high signal can have different values depending on the platform. For example, on Arduino Uno, Mega, Nano, this value will be 5 volts, but our robot uses an ESP32 board, where the logical high level is 3.3 volts. With GPIO pins, we can connect various devices, including:

- Buttons/switches
- Sensors
- LEDs
- Motors
- Displays
- etc.

### Controlling LED
So in this lesson, we're looking at an LED, which is a semiconductor device that emits light when an electric current passes through it. An LED is quite an interesting thing, and we can try to use GPIO on our board using it as an example. We can set the logical signal level using the **digitalWrite()** function. But before sending any signal to a GPIO pin, we need to specify in which mode our GPIO pin should work - to read or to write a signal. To specify the operating mode of a GPIO pin, we can use the **pinMode()** function.

### pinMode()
The **pinMode(pin, mode)** function sets the operating mode of the **pin** to one of the possible modes: **INPUT** to read the signal from the pin or **OUTPUT** to write the signal.

### digitalWrite()
The **digitalWrite(pin, value)** function is used to set a high or low logical voltage level. **pin**: GPIO pin number; **value**: the value you want to set on the specified pin, you can provide values **HIGH** (high voltage level) or **LOW** (low voltage level).

## Assignment
Write a program that turns on two LEDs on the robot. The LEDs are connected to pins defined in the code as **ledPin1** and **ledPin2**. Use these predefined pin names in your program.

## Hint
You need to set the correct operating mode for the pin and send a signal to it. Use the **pinMode()** function to set the required operating mode for each pin, and use **digitalWrite()** to send a signal to each pin.

## Conclusion
Congratulations! Now you know what GPIO is and how to send a logical signal to a pin!