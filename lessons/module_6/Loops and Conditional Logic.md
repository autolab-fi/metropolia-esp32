# **Lesson 2: Loops and Conditional Logic**

## **Lesson Objective**

Learn how to repeat actions using `for` and `while` loops.

---

## **Introduction**

Loops are essential for microcontrollers to perform repeated actions. Using loops saves you from writing the same code over and over, making your programs more efficient and easier to maintain. Mars rovers depend heavily on loops for their daily operations - from systematically checking hundreds of system health parameters each sol (Martian day) to repeatedly scanning terrain with their cameras during autonomous navigation. The Curiosity rover uses loops to continuously monitor its six-wheel drive system, while Perseverance employs loops to coordinate the complex sequence of movements required for sample collection and caching.

---

## **Theory**

### **For Loop**

Runs code a fixed number of times - perfect for iterating through sensors or creating patterns:

```cpp
// Blink LED 5 times
for (int i = 1; i <= 5; i++) {
    digitalWrite(ledPin, HIGH);
    delay(200);
    digitalWrite(ledPin, LOW);
    delay(200);
    printMQTT("Blink #" + String(i));
}
```

Mars rovers use for loops extensively for systematic operations. When Perseverance takes a panoramic image, it uses a for loop to capture dozens of individual photos at precise angular increments, later stitched together on Earth. The rover's PIXL (Planetary Instrument for X-ray Lithochemistry) instrument uses for loops to systematically scan rock surfaces, taking thousands of measurements in a grid pattern to create detailed elemental maps that help scientists understand Martian geology.

### **While Loop**

Runs code while a condition is true - good for reading sensors until a condition is met:

```cpp
// Wait until sensor detects object
int sensorValue = 0;
while (sensorValue < threshold) {
    sensorValue = analogRead(sensorPin);
    delay(10);
}
```

While loops are critical for Mars rover safety and navigation. When the Spirit rover became stuck in soft sand at Troy crater, it used while loops to continuously monitor wheel slip and motor currents while attempting different escape maneuvers. The rover would execute: "while wheel slip exceeds safe limits, try alternative driving strategies" until either a solution was found or safe operational limits were reached. Similarly, Ingenuity helicopter uses while loops during flight: "while altitude is below target AND battery power is sufficient, continue climbing."

### **Combining Loops with If-Else**

You can make decisions inside a loop to respond differently to changing conditions. This combination of loops and conditionals forms the foundation of intelligent autonomous behavior in Mars rovers. For example, Opportunity rover used this approach during its marathon journey to Endeavour crater: the rover would loop through hazard camera images, and for each image, use if-else statements to classify terrain as safe, caution, or hazardous, then adjust its driving speed and path accordingly.

---

## **Example Implementation**

```cpp
const int ledPin = 2;
const int potPin = 36; // Potentiometer on analog pin

void setup() {
  pinMode(ledPin, OUTPUT);

  printMQTT("Loop Example");
}

void loop() {
  // Read potentiometer to set number of blinks
  int numBlinks = map(analogRead(potPin), 0, 4095, 1, 10);

  printMQTT("Blinking LED " + String(numBlinks) + " times");

  // For loop to blink LED
  for (int i = 1; i <= numBlinks; i++) {
    if (i % 2 == 0) {
      // For even counts, blink fast
      digitalWrite(ledPin, HIGH);
      delay(100);
      digitalWrite(ledPin, LOW);
      delay(100);
      printMQTT("Fast blink (even count)");
    } else {
      // For odd counts, blink slow
      digitalWrite(ledPin, HIGH);
      delay(400);
      digitalWrite(ledPin, LOW);
      delay(100);
      printMQTT("Slow blink (odd count)");
    }
  }

  delay(1000);
}
```

---

## **Understanding the Logic**

1. The program reads an analog value from a potentiometer to determine how many times to blink.
2. The `for` loop runs the specified number of times.
3. Inside the loop, an `if-else` statement checks if the current count is even or odd.
4. For even counts, the LED blinks quickly; for odd counts, it blinks slowly.
5. After completing all blinks, the program waits 1 second and repeats.

This adaptive behavior pattern mirrors how Mars rovers adjust their operations based on environmental conditions. Curiosity's drill operation uses similar logic: the rover loops through drilling attempts, and within each iteration, if-else statements determine drilling parameters based on rock hardness. For softer rocks, it uses faster drilling speeds; for harder formations, it switches to slower, more controlled drilling to prevent bit damage. This adaptive approach has allowed Curiosity to successfully drill samples from diverse Martian geological formations throughout its extended mission.

---

## **Assignment: Reading Multiple Octoliner Sensors**

Your task is to create a program that reads values from all 8 Octoliner sensors (0-7) using a for loop and prints their values to the MQTT Console. This systematic sensor polling approach is fundamental to Mars rover operations, where rovers continuously loop through their sensor arrays to maintain situational awareness and detect changes in their environment.

Complete the code below:

```cpp
#include <Octoliner.h>

// I2C Address (default 42)
Octoliner octoliner(42);

void setup() {
    octoliner.begin();
    octoliner.setSensitivity(245);
}

void loop() {

    // YOUR CODE HERE:
    // Use a loop to read and print values from all 8 sensors (0-7)
    // For each sensor, print its number and the analog value using printMQTT

}
```

Your goal is to use a loop to iterate through each sensor (indices 0-7), read its value, and print both the sensor number and value to the MQTT Console.

Expected output should look like:

```
Sensor 0: 245
Sensor 1: 127
Sensor 2: 85
...and so on for all 8 sensors
```

This systematic data collection and reporting format is identical to how Mars rovers communicate with Earth. When Perseverance transmits daily status reports, it loops through its various subsystems - power, thermal, communications, mobility, and scientific instruments - reporting key parameters in a structured format that allows mission teams to quickly assess rover health and plan the next sol's activities. The consistent formatting ensures that both automated monitoring systems and human operators can efficiently process the information.

---

## **Conclusion**

In this lesson, you learned how to use loops to efficiently perform repeated tasks on the ESP32. The `for` loop is particularly useful for handling multiple sensors or outputs in sequence, while combining loops with conditional statements allows your robot to make complex decisions based on changing sensor inputs.

These loop programming techniques you've mastered are the operational backbone of every Mars mission since the Viking landers. From the simple timer loops that regulated Viking's daily communication schedules in 1976, to the sophisticated nested loops that coordinate Perseverance's 19 cameras and multiple scientific instruments today, loops enable the systematic, reliable operation essential for space exploration. As NASA develops increasingly autonomous rovers for future Mars missions and eventual human settlements, these fundamental loop constructs will continue to be essential for creating robotic systems that can operate reliably across the vast distances and communication delays of interplanetary exploration.
