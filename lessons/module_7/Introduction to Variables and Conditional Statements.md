# **Lesson 1: Introduction to Variables and Conditional Statements**

## **Lesson Objective**

Learn how to declare and use variables in programming, and apply conditional logic using `if`, `else if`, and `else` statements to make decisions.

---

## **Introduction**

Variables are essential in microcontroller programming for storing information like sensor readings, motor speeds, and system states. In robot programming, we use conditional statements to make decisions based on these variables, creating intelligent behavior. These same programming fundamentals power Mars rovers, where variables store critical mission data like battery levels, wheel currents, instrument temperatures, and atmospheric conditions. Mars rovers like Perseverance use thousands of conditional statements to make autonomous decisions - from determining safe driving paths to deciding when to take scientific measurements based on environmental conditions.

---

## **Theory**

### **What are Variables?**

Variables are named storage locations in the memory that enable intelligent robotic behavior:

- `int motorSpeed = 200;` stores a motor speed value
- `float batteryLevel = 3.7;` stores the battery voltage
- `bool isOnLine = true;` stores whether the robot detects a line

Mars rovers rely on similar variable types to monitor their health and environment. Curiosity stores variables like `float wheelCurrent[6]` to monitor the power consumption of each wheel motor, `int soilTemperature` to track ground conditions before drilling, and `bool communicationWindowActive` to manage when the rover can transmit data to Earth. The Perseverance rover uses variables to store complex atmospheric data, with `float windSpeed`, `float pressure`, and `int dustLevel` helping determine optimal conditions for helicopter flights by its companion, Ingenuity.

### **What is an If-Else Statement?**

It enables your robot to make decisions based on conditions, forming the backbone of autonomous behavior:

```cpp
if (condition1) {
    // code runs if condition1 is true
} else if (condition2) {
    // code runs if condition1 is false but condition2 is true
} else {
    // code runs if all conditions above are false
}
```

This decision-making structure is fundamental to Mars rover operations. For example, Opportunity rover's flight software used nested if-else statements to evaluate driving conditions: if solar panel power was above minimum levels AND if hazard cameras detected a clear path AND if the target was within communication range, then the rover would proceed with autonomous driving. Otherwise, it would enter safe mode and wait for instructions from Earth. The same logical framework helps current Mars missions make thousands of autonomous decisions daily.

### **Comparison Operators**

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

These operators are crucial for Mars rover safety systems. The Spirit and Opportunity rovers used comparison operators to monitor wheel slip: `if (wheelSlip > maxAllowedSlip)` would trigger alternative navigation strategies. Perseverance's autonomous helicopter companion, Ingenuity, uses temperature comparisons `if (batteryTemp >= -15°C)` to determine if it's safe to fly, since Mars temperatures can drop to -90°C at night, potentially damaging sensitive electronics.

---

## **Example Implementation**

```cpp
#include <Arduino.h>

// Define pins
const int ledPin = 2;
const int sensorPin = 36;  // Analog sensor pin

void setup() {
  pinMode(ledPin, OUTPUT);

  printMQTT("Sensor Monitoring Started");
}

void loop() {
  // Read sensor value
  int sensorValue = analogRead(sensorPin);

  // Make decision based on threshold
  if (sensorValue > 2000) {
    digitalWrite(ledPin, HIGH);
    printMQTT("Sensor value HIGH");
  } else {
    digitalWrite(ledPin, LOW);
    printMQTT("Sensor value LOW");
  }

  delay(100);  // Small delay for stability
}
```

---

## **Understanding the Logic**

1. The program reads an analog sensor value.
2. The `if` statement compares this value against a threshold (2000).
3. If the value is above the threshold, the LED turns ON and "Sensor value HIGH" is sent.
4. Otherwise (`else`), the LED turns OFF and "Sensor value LOW" is sent.

This threshold-based decision making is identical to how Mars rovers operate their scientific instruments. When Curiosity's ChemCam laser spectrometer analyzes a rock sample, it uses conditional logic to evaluate spectral data: if certain mineral signatures exceed threshold values, the rover automatically takes additional measurements. Similarly, when Perseverance's SUPERCAM detects interesting chemical compositions, threshold comparisons determine whether to recommend the site for sample collection, potentially preserving Martian material for future return to Earth.

---

## **Assignment: Line Detection**

In this assignment, you'll use two of the Octoliner sensors to detect line positions and send appropriate messages to the MQTT dashboard. This mirrors how Mars rovers use multiple sensors to understand their environment and make navigation decisions.

Your task is to:

1. Read all the sensor values (sensor 0 to sensor 7)
2. Compare all the sensor values
3. Use if-else if-else logic to determine different conditions
4. Send different messages based on which sensors detect the line

This systematic sensor evaluation approach reflects how Perseverance rover processes hazard camera data. The rover continuously reads from multiple camera sensors, compares obstacle detection values against safety thresholds, and uses conditional logic to determine the safest path forward. Just as your robot will report which sensors detect the line, Mars rovers report terrain conditions back to mission control to help plan future driving routes.

Complete the code below by adding the conditional logic:

```cpp
#include <Octoliner.h>

// I2C Address (default 42)
Octoliner octoliner(42);

void setup() {
    octoliner.begin();
    octoliner.setSensitivity(245);
}

void loop() {
    // Read values from all sensors (0 - 7)
    int value_0 = octoliner.analogRead(0);
    int value_1 = octoliner.analogRead(1);


    // YOUR CODE HERE:
    // Add if-else if-else statements to determine which sensor(s) detect the line
    // Remember: Values greater than 200 indicate the sensor is on the line
    // Send appropriate messages via printMQTT

}
```

### Expected Output

Your code should detect and report one of the following condition:

- Only return the messages for respective sensors that are ON the line
- If only sensor 5 is on the line: "SENSOR 5 ON LINE"
- If only sensor 6 is on the line: "SENSOR 6 ON LINE"
- This should be done for all the sensors.
- If none of the sensors detect the line: "NO SENSORS ARE ON THE LINE"

This systematic reporting format is similar to how Mars rovers communicate their status to Earth. When Opportunity rover encountered the "Purgatory" sand dune in 2005, it systematically reported which wheels were experiencing high current draw, which terrain sensors detected soft sand, and which navigation cameras showed concerning terrain features. This structured status reporting helped mission engineers develop the driving techniques that eventually freed the rover and extended its mission for years beyond its planned duration.

---

## **Conclusion**

In this lesson, you learned how variables store different types of data and how conditional statements make decisions based on those values. The `if-else if-else` structure lets you create more complex logic for your robot to respond to different sensor combinations, which is essential for creating responsive robot behavior.

These fundamental programming concepts you've mastered are the same ones that have enabled every successful Mars mission since the first Viking landers in 1976. From simple temperature monitoring conditionals that kept early landers operational through Martian winters, to the complex multi-sensor decision trees that guide today's rovers through autonomous navigation, variables and conditional statements remain the building blocks of space robotics. As NASA plans future Mars missions including sample return and human exploration, these same programming principles will continue to be essential for creating reliable, intelligent robotic systems capable of operating independently millions of miles from Earth.
