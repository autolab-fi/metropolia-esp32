# **Lesson 2: Loops and Conditional Logic**

## **Lesson Objective**

Learn how to repeat actions using `for` and `while` loops.

---

## **Introduction**

Loops are essential for microcontrollers perform repeated actions. Using loops saves you from writing the same code over and over, making your programs more efficient and easier to maintain.

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

### **Combining Loops with If-Else**

You can make decisions inside a loop to respond differently to changing conditions:

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

---

## **Assignment: Reading Multiple Octoliner Sensors**

Your task is to create a program that reads values from all 8 Octoliner sensors (0-7) using a for loop and prints their values to the MQTT Console.

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

---

## **Conclusion**

In this lesson, you learned how to use loops to efficiently perform repeated tasks on the ESP32. The `for` loop is particularly useful for handling multiple sensors or outputs in sequence, while combining loops with conditional statements allows your robot to make complex decisions based on changing sensor inputs.
