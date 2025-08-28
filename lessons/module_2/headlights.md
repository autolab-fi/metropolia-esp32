### **Lesson 6: Rover Headlights**

## **Lesson objective**

Learn about GPIO, a foundational concept for rover control.

## **Introduction**

In this lesson, you will learn about a basic yet critical concept for microcontrollers—**General Purpose Input/Output (GPIO)**. We will explore how it works by controlling the LEDs on our rover, a function analogous to the lighting systems used by rovers on Mars to aid in navigation and data collection.

---

## **Theory**

### **What is GPIO?**

**GPIO** stands for "General Purpose Input/Output.".It is the primary interface through which a microcontroller, the "brain" of our rover, interacts with external devices in its environment. GPIO pins can be configured to either **read signals** from external sensors (acting as inputs) or **send signals** to control devices like motors and lights (acting as outputs).

The signal for a GPIO pin is a voltage. A **low signal** is always **0 volts**, but the voltage for a **high signal** (**logical high**) varies. Our rover uses an **ESP32** board, where the logical high level is **3.3 volts**. In contrast, the flight computers on NASA's Mars rovers, such as the **Perseverance rover**, are custom-built to withstand the harsh Martian environment, and their logic levels are designed with extreme precision to ensure mission success. GPIO pins on a rover's flight computer can be connected to various components, including:

- **Navigation sensors:** To determine the rover's position and orientation.
- **Scientific instruments:** For tasks like analyzing rock samples.
- **Motors:** For driving the wheels and operating robotic arms.
- **Lighting systems:** For illuminating areas during nighttime operations or in low-light conditions, much like the lights on the Mars Science Laboratory (MSL) rover, **Curiosity**, which uses LEDs to light its workspace.

### **Controlling an LED**

An LED is a semiconductor device that emits light when an electric current passes through it. The LEDs on our rover act as miniature versions of the hazard avoidance lights on NASA's rovers, which are essential for navigating treacherous terrain in low light. To control an LED with a GPIO pin, you must first configure the pin's operating mode, then set its logical signal level.

### **`pinMode()`**

The **`pinMode(pin, mode)`** function sets the operating mode for a specific GPIO pin. This is a fundamental step, ensuring the microcontroller knows whether to expect a signal from the pin or to send one out.

- **`pin`**: The number of the GPIO pin.
- **`mode`**: The operational mode you want to set, either **`INPUT`** to read a signal or **`OUTPUT`** to write a signal.

For example, to control a light, the pin must be set to `OUTPUT` mode so the microcontroller can send the electrical signal to turn the light on.

### **`digitalWrite()`**

The **`digitalWrite(pin, value)`** function is used to set a high or low logical voltage level on a pin configured as an output.

- **`pin`**: The GPIO pin number to control.
- **`value`**: The logical voltage level to set. You can provide either **`HIGH`** for a high voltage level or **`LOW`** for a low voltage level.

Using `digitalWrite(pin, HIGH)` would supply power, turning on a headlight, while `digitalWrite(pin, LOW)` would cut the power, turning it off. This simple command is the basis for complex lighting sequences used to light up the Martian surface for imaging.

---

## **Assignment**

Write a program that turns on two LEDs on the rover. The LEDs are connected to pins defined in the code as **`ledPin1`** and **`ledPin2`**. Use these predefined pin names in your program.

---

## **Hint**

You need to set the correct operating mode for the pin and send a signal to it. Use the **`pinMode()`** function to set the required operating mode for each pin, and use **`digitalWrite()`** to send a signal to each pin.

---

## **Conclusion**

Congratulations! You now understand what GPIO is and how to send a logical signal to a pin. By completing this lesson, you've performed a task that is a small but critical part of real-world rover operations, connecting your learning to the incredible engineering feats of missions like Curiosity and Perseverance.
