# **Lesson 1: Line Sensor and Black Line Detection**

## **Lesson Objective**

This lesson focuses on understanding how an **Octoliner** sensor detects black lines using an **ESP32**. You will learn the working principle of **IR line sensors**, explore challenges associated with black line detection, and implement a program to process sensor readings. By the end of this lesson, you will be able to detect black lines efficiently and use this data for robotics applications.

---

## **Introduction**

Infrared (IR) line sensors play a crucial role in robotics, particularly in **line-following robots**, **automated vehicles**, and **path-tracking systems**. These sensors detect **black and white surfaces** based on how much infrared light is reflected. A robot equipped with an array of IR sensors can follow a **predefined path** by continuously scanning the surface and adjusting its movement. This capability is widely used in industrial automation, logistics, and robotic competitions. In this lesson, we will explore the working principles of IR sensors and discuss how to interpret sensor readings for black line detection.

---

## **Theory**

Line sensors rely on the principle of **infrared reflection** to differentiate between black and white surfaces. When IR light is emitted by the sensor, it either gets reflected back or absorbed, depending on the surface type. **White surfaces** reflect most of the IR light, leading to a **higher voltage output**, while **black surfaces** absorb most of the IR light, resulting in a **lower voltage output**. This difference in voltage allows the ESP32 to determine whether the sensor is over a black or white surface.

A **line-following robot** typically uses a row of **multiple IR sensors** to detect the black track. When the robot moves, the sensor readings guide it by detecting the line’s position relative to its current movement path. If the black line shifts toward the left or right, the robot can adjust its trajectory accordingly. The IR sensor array provides crucial feedback for navigation, ensuring smooth and precise movement along the path.

![IR Sensor Working](https://github.com/pranavk-2003/metropolia-esp32/blob/main/images/module_6/IR's.png)

However, using IR sensors effectively requires overcoming several real-world challenges. **Surface texture variations** can affect reflection, meaning not all black surfaces absorb IR light in the same way. **Ambient light interference** from external sources like the sun or bright LEDs may cause fluctuations in sensor readings, leading to false detections. Another issue is **sensor calibration**, as different sensors may produce slightly different readings, requiring **threshold adjustments** to ensure accurate detection. **Noise in sensor data** is another challenge that must be managed using filtering techniques. To achieve optimal performance, the system needs to be tested in various conditions, and sensor thresholds should be fine-tuned.

---

## **Programming the Line Sensor**

The **Octoliner** sensor consists of **7 independent IR sensors**, each capable of detecting IR reflection. In this section, we will read values from the sensor and determine whether a black line is detected. The process involves initializing the sensor, reading data from all **7 sensors**, comparing these readings to a predefined threshold, and finally displaying the results. The program will run continuously in a loop, checking the sensor values and determining whether a black line is present.

The following example code initializes the Octoliner sensor, sets its sensitivity, and reads values from a single sensor. The data obtained can then be used to decide whether the sensor detects a black or white surface.

```cpp
#include <Octoliner.h>

// I2C Address (default 42)
Octoliner octoliner(42);

// Black threshold for detection
const int MY_BLACK_THRESHOLD = 100;

void setup() {
    octoliner.begin();
    octoliner.setSensitivity(230);  // Adjust sensitivity if needed
}

void loop() {
    int value1 = octoliner.analogRead(1);
}
```

This code is a starting point and can be expanded to process all sensor readings effectively. The **black threshold** value may need adjustment based on the environment and surface properties.

---

## **Assignment**

Now that you understand how the IR sensor detects black and white surfaces, try modifying the code to enhance its functionality. Your task is to:

1. Detect whether the **entire sensor array** identifies a black line.
2. Display meaningful messages in the **Serial Monitor** indicating whether a black line has been detected or not.
3. Experiment with different **sensitivity levels** to understand how they affect detection accuracy.

For better visualization of the logic flow, refer to the flowchart below:

![Flowchart](https://github.com/pranavk-2003/metropolia-esp32/blob/main/images/module_6/FC_module_6.png)

By modifying the `blackDetected` flag, you can fine-tune the detection mechanism and improve sensor response.

---

## **Conclusion**

Congratulations! You have successfully explored how IR sensors work and how they can be used for **black line detection**. This foundational knowledge is essential for building **autonomous robots** capable of following a predefined path. In the next lesson, we will learn how to use **sensor data** to control a robot’s movement, allowing it to follow a line autonomously.

By continuing to experiment with sensor readings and adjusting threshold values, you will gain a deeper understanding of **sensor-based navigation**. These skills will be useful in advanced robotics applications, including **PID-controlled line followers**, **maze-solving robots**, and **autonomous navigation systems**. Keep refining your code, and happy coding!
