# **Lesson 3: Arrays and Sensor Data History Analysis**

## **Lesson Objective**

Understand how to use arrays to store and analyze sensor data.

---

## **Introduction**

Arrays allow you to store multiple values under one name. For robotics applications, arrays are perfect for handling multiple sensor readings, storing historical data, or tracking patterns over time. Instead of creating separate variables for each measurement, arrays group them together, making it easier to loop through and analyze data.

---

## **Theory**

### **What is an Array?**

An array is a fixed-size collection of elements of the same type.  
Example:

```cpp
int sensorValues[8] = {325, 410, 102, 890, 512, 78, 210, 455};
```

### **Accessing Elements**

You can access array items using indexes (starting from 0).  
`sensorValues[0]` → 325 (first sensor)  
`sensorValues[3]` → 890 (fourth sensor)

### **Looping Through Arrays**

Use a `for` loop to process all elements.

```cpp
for (int i = 0; i < 8; i++) {
    String message = "Sensor " + String(i) + ": " + String(sensorValues[i]);
    printMQTT(message);
}
```

---

## **Example Implementation**

```cpp
#include <rover.h>

void setup() {
    printMQTT("Array Example");
}

void loop() {
    // Sample light sensor readings
    int lightLevels[6] = {855, 230, 990, 470, 600, 120};
    int brightCount = 0;

    // Process the array with a loop
    for (int i = 0; i < 6; i++) {
        if (lightLevels[i] > 500) {
            brightCount++;
            // Combine all elements into a single string
            String message = "Sensor " + String(i) + " detects bright light";
            printMQTT(message);
        }
    }

    // Print count of bright sensors
    printMQTT("Number of bright sensors: " + String(brightCount));

    delay(3000); // Wait 3 seconds before repeating
}
```

---

## **Understanding the Logic**

1. The program has an array of 6 light sensor readings.
2. A loop checks each reading using an `if` condition.
3. If the value is greater than 500, it's considered "bright" and counted.
4. Each bright sensor is reported, and the total count is displayed.
5. This same approach can be used to process any type of sensor data.

---

## **Advanced Array Techniques**

### **Storing Multiple Measurements**

```cpp
// Store three sets of sensor readings
int first_measurement[8];
int second_measurement[8];
int third_measurement[8];

// Take readings at different positions
for(int i = 0; i < 8; i++){
    first_measurement[i] = octoliner.analogRead(i);
}
// Move robot and take more readings...
```

### **Processing All Stored Data**

```cpp
// Send all measurements systematically
for(int i = 0; i < 8; i++){
    printMQTT(String(first_measurement[i]));
    delay(100);  // Prevent message loss
    printMQTT(String(second_measurement[i]));
    delay(100);
    printMQTT(String(third_measurement[i]));
    delay(100);
}
```

---

## **Assignment: Sensor Data Collection and Analysis**

For this assignment, you'll create a program that:

1. Uses arrays to store sensor readings from three different rover positions
2. Moves the robot between measurements to collect varied data
3. Systematically sends all collected data via MQTT

Complete the code below:

```cpp
#include <Octoliner.h>
#include <rover.h>

// I2C Address (default 42)
Octoliner octoliner(42);
const int MY_BLACK_THRESHOLD = 100;

void setup() {
    octoliner.begin();
    octoliner.setSensitivity(245);

    // YOUR CODE HERE:
    // 1. Create three arrays to store 8 sensor readings each
    // 2. Take first set of sensor readings
    // 3. Move robot forward for 10cm and take second set of readings
    // 4. Move robot forward again by 10cm and take third set of readings
    // 5. Use loops to send all 24 values systematically using printMQTT() with delays(100ms)

}

void loop() {
    // Empty - all work done in setup() as it shall be performed only once
}
```

### **Expected Behavior:**

- The robot should collect 24 total sensor values (8 sensors × 3 positions)
- Values should be sent systematically using printMQTT() with proper delays(100ms)
- The verification system will check whether the sensor outputs are as expected.

---

## **Conclusion**

Arrays are essential for organizing and processing multiple related values in robotics. By combining arrays with movement commands and systematic data collection, you can create programs that gather comprehensive sensor data over time and space. This approach is fundamental for advanced robotics applications like mapping, pattern recognition, and environmental analysis. The ability to store, organize, and systematically process sensor data using arrays is a crucial skill for any robotics programmer.
