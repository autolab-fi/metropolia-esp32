# **Lesson 3: Arrays and Sensor Data History Analysis**

## **Lesson Objective**

Understand how to use arrays to store and analyze sensor data.

---

## **Introduction**

Arrays allow you to store multiple values under one name. For robotics applications, arrays are perfect for handling multiple sensor readings, storing historical data, or tracking patterns over time. Instead of creating separate variables for each measurement, arrays group them together, making it easier to loop through and analyze data. This same principle is fundamental to Mars missions, where rovers like Perseverance collect thousands of measurements daily from multiple instruments. NASA's Deep Space Network receives arrays of telemetry data from Mars rovers, including temperature readings, power levels, wheel currents, and scientific measurements that must be systematically processed and analyzed by mission teams on Earth.

---

## **Theory**

### **What is an Array?**

An array is a fixed-size collection of elements of the same type. Mars rovers use similar data structures to organize information from their instrument suites. For example, the Curiosity rover's MAHLI (Mars Hand Lens Imager) camera stores arrays of pixel intensity values for each image, while the rover's environmental monitoring station collects arrays of atmospheric pressure, temperature, and humidity measurements throughout each Martian day (sol).

Example:

```cpp
int sensorValues[8] = {325, 410, 102, 890, 512, 78, 210, 455};
```

### **Accessing Elements**

You can access array items using indexes (starting from 0).  
`sensorValues[0]` → 325 (first sensor)  
`sensorValues[3]` → 890 (fourth sensor)

### **Looping Through Arrays**

Use a `for` loop to process all elements. This systematic approach to data processing is essential for Mars missions, where rovers must efficiently cycle through sensor arrays to monitor system health, analyze scientific data, and prioritize which information to transmit back to Earth during limited communication windows.

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

This logical framework mirrors how Mars rovers process environmental data. The Perseverance rover's MOXIE (Mars Oxygen In-Situ Resource Utilization Experiment) uses similar conditional logic to monitor oxygen production rates, checking if temperature and pressure conditions are within acceptable ranges before proceeding with oxygen generation attempts. The rover's autonomous systems constantly evaluate sensor arrays using threshold-based decisions to ensure safe operation.

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

This multi-measurement approach is fundamental to Mars exploration. NASA's rovers systematically collect data at multiple locations and times to build comprehensive scientific datasets. The Opportunity rover famously analyzed the same Martian rock outcrop from multiple angles and distances, storing arrays of spectroscopic data that later confirmed the historical presence of water on Mars. Similarly, Curiosity's SAM (Sample Analysis at Mars) instrument stores arrays of mass spectrometry measurements taken at different temperatures to identify organic compounds in Martian soil samples.

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

This systematic data transmission approach is critical for Mars missions due to limited bandwidth and communication windows. Mars rovers must carefully manage data transmission rates to avoid overwhelming the communication link while ensuring all critical scientific data reaches Earth. The Mars Reconnaissance Orbiter acts as a relay satellite, receiving large data arrays from surface rovers during brief overflights and then transmitting this information to Earth during optimal communication periods. The 100ms delays in our code simulate the need for controlled data flow rates that prevent buffer overflow in space communication systems.

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

This structured data collection methodology reflects the systematic approach used by Mars missions for scientific investigations. When Perseverance drills rock samples, it follows a precise sequence: approach the target, collect initial spectroscopic readings, position the drill, take measurements during drilling, and finally analyze the collected sample. Each step generates arrays of data that must be systematically processed and transmitted to mission scientists. The rover's ability to collect, organize, and transmit this data reliably has been crucial for discovering evidence of ancient river deltas and potential biosignatures on Mars.

---

## **Conclusion**

Arrays are essential for organizing and processing multiple related values in robotics. By combining arrays with movement commands and systematic data collection, you can create programs that gather comprehensive sensor data over time and space. This approach is fundamental for advanced robotics applications like mapping, pattern recognition, and environmental analysis. The ability to store, organize, and systematically process sensor data using arrays is a crucial skill for any robotics programmer.

These same array processing techniques you've mastered are the foundation of every successful Mars mission. From the Viking landers in 1976 that first used arrays to store atmospheric measurements, to today's Perseverance rover managing thousands of daily sensor readings across multiple scientific instruments, the principles of systematic data collection and processing remain unchanged. As Mars exploration advances toward human missions, the reliable data management systems demonstrated by decades of robotic missions will be essential for keeping future astronauts safe and productive on the Red Planet.
