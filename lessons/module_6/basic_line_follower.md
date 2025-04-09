# **Lesson 2: Implementing Line Following with an IR Sensor**

## **Lesson Objective**

Learn how to program an **ESP32-based robot** to follow a black line using an **Octoliner** IR sensor array.

---

## **Introduction**

In this lesson, we will use an **IR line sensor array** to detect and follow a black line. The robot will read sensor values, determine the line's position, and adjust its movement accordingly.

---

## **Theory**

A **line-following robot** uses an array of **infrared (IR) sensors** to detect the track. These sensors measure reflected IR light, distinguishing between black (low reflection) and white (high reflection).

### **How IR Sensors Work**

Infrared sensors operate by emitting infrared light and detecting the amount of reflection. When placed over a white surface, a significant amount of IR light is reflected back to the sensor. However, a black surface absorbs more infrared light, resulting in lower reflection detected by the sensor. This principle is used to differentiate between the black line and the surrounding surface.

### **IR Sensor Configuration**

The **Octoliner** sensor array consists of **8 sensors**, each providing an analog value that indicates the intensity of reflected IR light.

![IR Sensor Logic](https://github.com/pranavk-2003/metropolia-esp32/blob/main/images/module_6/IR_sensor_array.png)

In this lesson:

- **Central sensors (3 & 4)** → Move straight
- **Left sensors (0,1,2)** → Guide left turns
- **Right sensors (5,6,7)** → Guide right turns

### **Line Detection Mechanism**

- If the middle sensors detect the line, the robot moves forward.
- If the left sensors detect the line, the robot turns left by reducing the left motor speed.
- If the right sensors detect the line, the robot turns right by reducing the right motor speed.
- If no sensors detect the line, the robot stops or searches for the line.

### **Challenges in Line Following**

1. **Sensor Calibration**
   - The reflectivity of different surfaces varies, so sensor thresholds must be carefully tuned.
2. **Speed Control**
   - Sudden turns can cause instability, requiring smooth speed adjustments.
3. **Noise Filtering**
   - The sensor readings may fluctuate due to variations in ambient light or minor surface irregularities. Filtering techniques may be required to stabilize the readings.

---

## **Programming the Line Following Algorithm**

This code will:

1. **Read** sensor values from all 8 sensors.
2. **Decide** the robot's movement based on sensor readings.
3. **Move** forward, turn left, turn right, or stop.

### **Code Implementation**

```cpp
#include <Octoliner.h>
#include <lineRobot.h>

// I2C Address (default 42)
Octoliner octoliner(42);
int speed=30;

// Black threshold for detection
const int MY_BLACK_THRESHOLD = 100;

void setup() {
    octoliner.begin();
    octoliner.setSensitivity(230);  // Adjust sensitivity if needed
}

void loop() {
    // Read all sensor values
    for (uint8_t i = 0; i < 8; i++) {
       int value = octoliner.analogRead(i);
    }
    robot.runMotorSpeedRight(speed);
    robot.runMotorSpeedLeft(speed);
}
```

---

## **Understanding the Logic**

### **Sensor Detection and Movement**

The robot determines movement based on which sensors detect the black line.  
Below is a flowchart for a clear understanding:

![Flow](https://github.com/pranavk-2003/line-robot-curriculum/blob/main/images/module_6/FC.png)

1. **If middle sensors (3 OR 4) detect the line** → Move forward.
2. **If left sensors (0 OR 1 OR 2) detect the line** → Turn left.
3. **If right sensors (5 OR 6 OR 7) detect the line** → Turn right.
4. **If no sensor detects the line** → Stop.

---

## **Assignment**

Modify the program to:

1. **Write a program to make the robot line follow**.
2. **Fine-tune** motor speeds for smoother movement.
3. **Experiment with different thresholds** to improve accuracy.
4. **Ensure the robot successfully crosses both checkpoints to complete the Assignment**.

---

## **Conclusion**

In this lesson, you have learned how to implement a basic **line-following algorithm** using an **Octoliner IR sensor array**. Understanding how to read sensor values and adjust movement based on input is fundamental to developing more advanced autonomous navigation systems.
