# Lesson 1: Relay Controller

## Lesson Objective

Understand relay controllers and their role in open-loop and closed-loop systems.

## Introduction

A controller is a system that manages the behavior of a device or process. Controllers are essential in automation, ensuring that a system functions as desired. There are two main types of control systems:

1. **Open-loop systems**: These operate without feedback. The controller sends commands without knowing the actual output (e.g., turning on a heater for 10 minutes without checking the temperature).
2. **Closed-loop systems**: These use feedback to adjust their behavior, ensuring more precise control (e.g., an air conditioner adjusting cooling based on room temperature).

## Theory

### What is a Relay Controller?

A relay controller is a simple type of control system that switches between two states (ON/OFF) based on a set condition. It works like a basic thermostat, where the system turns ON when the temperature is below a threshold and OFF when it exceeds a limit.

A relay controller follows this rule:

$$
 u(t) = \begin{cases}
    U_{max}, & \text{if } e(t) > 0 \\
    U_{min}, & \text{if } e(t) \leq 0
\end{cases}
$$

where:

- \( u(t) \) is the control output,
- \( e(t) \) is the error (difference between desired and actual value),
- \( U*{max} \) and \( U*{min} \) are the two possible output states.

### Limitations of Relay Controllers

- They can cause oscillations because they switch between extreme values.
- Lack of fine control, leading to inefficiencies.
- Not suitable for smooth adjustments required in robotics.

**Note:** We already implemented a relay controller in the last lesson.

---

# Lesson 2: P-Controller

## Lesson Objective

Learn about P-controllers and their advantages over relay controllers.

## Theory

### What is a P-Controller?

A Proportional (P) controller is a type of feedback control system that uses a proportional gain to adjust the control output based on the error between the desired and actual values. The control law is given by:

$$
 u(t) = K_p \cdot e(t)
$$

where:

- \( u(t) \) is the control output,
- \( K_p \) is the proportional gain,
- \( e(t) \) is the error (desired value - actual value).

### Block Diagram

![P Controller](https://github.com/pranavk-2003/metropolia-esp32/blob/main/images/module_7/p.png)

---

# Lesson 3: PI-Controller

## Lesson Objective

Understand the limitations of a P-controller and introduce the integral component to eliminate steady-state error.

## Theory

### Drawbacks of a P-Controller

- A P-controller alone cannot eliminate steady-state error, meaning the system might not reach the exact desired value.
- If the gain is too high, the system may oscillate or become unstable.

### Eliminating Steady-State Error with the Integral Component

The PI (Proportional-Integral) controller addresses the steady-state error by adding an integral term:

$$
 u(t) = K_p \cdot e(t) + K_i \cdot \int e(t) dt
$$

where:

- \( K_i \) is the integral gain,
- The integral term accumulates past errors to eliminate steady-state error.

### Block Diagram

![PI Controller](https://github.com/pranavk-2003/metropolia-esp32/blob/main/images/module_7/pi.png)

---

# Lesson 4: PID-Controller

## Lesson Objective

Introduce the derivative component to reduce overshoot and improve stability.

## Theory

### What is a Differential Component and How Does It Help Eliminate Overshoot?

- The derivative term predicts the system's future behavior and reduces overshoot.
- The control law becomes:

$$
 u(t) = K_p \cdot e(t) + K_i \cdot \int e(t) dt + K_d \cdot \frac{de(t)}{dt}
$$

where:

- \( K_d \) is the derivative gain,
- The derivative term (\( de(t)/dt \)) reduces rapid changes and dampens oscillations.

### Block Diagram

![PID Controller](https://github.com/pranavk-2003/metropolia-esp32/blob/main/images/module_7/pid_f.png)

## Assignment

Write a program that implements a PID-controller for a line-following robot.

### **Hint: Understanding Weighted Sum, Total Value, and Error Calculation**

### **1. Calculating Weighted Sum and Total Value**

To estimate the robot's position relative to the line, we use **sensor readings** and assign weights based on their positions.

- Each sensor has an index (e.g., **0 to 7** for an 8-sensor array).
- The **weighted sum** is calculated as:

$$\text{weightedSum} = \sum_{i=0}^{7} (i \times \text{sensorValue}_i)$$

This gives more weight to sensors detecting a stronger signal (higher reading).

- The **total value** is simply:

$$\text{totalValue} = \sum_{i=0}^{7} \text{sensorValue}_i$$

It ensures that only detected parts of the line contribute to the position calculation.

Code Snippet:

```cpp
 if (sensorvalues[i] > MY_BLACK_THRESHOLD) {
        weightedSum += i * sensorvalues[i];
        totalValue += sensorvalues[i];
    }
```

#### **2. Computing the Error**

Once we calculate the weighted sum and total value, we estimate the line's **position**:

$$
\text{position} = \frac{\text{weightedSum}}{\text{totalValue}}
$$

To center the robot on the line, we define an expected **midpoint** (e.g., **3.5 for an 8-sensor array**). The error is then:

$$
\text{error} = \text{position} - 3.5
$$

Code Snippet:

```cpp
double error = 0;
if (totalValue > 0) {
    error = (weightedSum / totalValue) - 3.5;
}
```

#### **3. Applying PID Control**

The PID **output** is computed as:

$$
\text{output} = K_p \times \text{error} + K_i \times \sum \text{error} + K_d \times (\text{error} - \text{prevError})
$$

To determine **motor speeds**:

$$
\text{leftSpeed} = \text{fwdspeed} - 1.5 \times \text{output}
$$

$$
\text{rightSpeed} = \text{fwdspeed} + 1.5 \times \text{output}
$$

Code Snippet:

```cpp
integral += error;
integral = constrain(integral, -30, 30);  // Prevent integral windup
double derivative = error - prevError;
double output = (Kp * error) + (Ki * integral) + (Kd * derivative);
prevError = error;
```

#### **4. Usage of Functions**

The calculated speeds of the Left and Right motor can be passed to the functions :

```cpp
robot.runMotorSpeedLeft(leftSpeed);
robot.runMotorSpeedRight(rightSpeed);
```

to move the robot.

## **Conclusion**

Congratulations! You have successfully implemented a **PID controller** for a line-following robot using an **Octoliner IR sensor array**. Through this lesson, you learned how to read and process sensor values, calculate the **weighted sum and total value**, and use them to estimate the robot's position. By applying **PID corrections**, you were able to smoothly and accurately follow the black line, even around curves and turns.

This foundational knowledge is essential for building **autonomous robots** capable of navigating predefined paths with precision. By fine-tuning the **PID constants (Kp, Ki, and Kd)**, you can further optimize the robot's stability and responsiveness. In the next lesson, you will explore more advanced control techniques to enhance the robot's navigation capabilities.

---
