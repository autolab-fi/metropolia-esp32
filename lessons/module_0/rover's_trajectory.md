# Mars Rover Mission Simulator

**Welcome to the Mars Rover Mission Simulator, where you can program and test real Mars rover navigation sequences based on current Mars exploration missions.**

When you execute your code and click 'Verify,' a blue trail will show your rover's path across the Martian surface for 20 seconds, simulating the actual telemetry data that mission controllers receive from active Mars rovers exploring the Red Planet.

---

## Description

This simulator is used for planning rover traverses, with movements measured in centimeters across the Martian terrain. Your rover operates in **Jezero Crater**, an ancient impact crater that contains fascinating geological formations, including dried river deltas and sedimentary rock layers that tell the story of Mars' watery past.

Scientists chose Jezero Crater because it was once a lake 3.8 billion years ago, making it an ideal location to search for signs of ancient microbial life. The crater's preserved river delta contains clay minerals that could have fostered early life forms.

---

## Real Mission Insights

Your simulator is based on the **Perseverance rover mission**, which landed in Jezero Crater in February 2021. The rover's main goal is to search for signs of **ancient microbial life** and collect rock and soil samples for future return to Earth.

Perseverance is also testing new technologies, like the **Mars Oxygen In-Situ Resource Utilization Experiment (MOXIE)**, which produces oxygen from the Martian atmosphere. This technology is vital for future human missions, as oxygen can be used for breathing and rocket fuel.

The **Ingenuity Mars Helicopter**, a technology demonstration that flew with Perseverance, made the **first powered, controlled flight on another planet** in April 2021. Its success has paved the way for future aerial exploration on Mars.

Another active rover, **Curiosity**, landed in Gale Crater in 2012. It found evidence that Mars once had the necessary environmental conditions to support microbial life, including an ancient lakebed.

---

## Mission

Navigate from landing site toward ancient river delta

## Mission Code Example

```cpp

#include <rover.h>

void setup() {
    // Coordinates: 18.38°N, 77.58°W in Jezero Crater
    // Mission: Navigate from landing site toward ancient river delta
    rover.turnLeftAngle(45);
    rover.moveForwardDistance(20);      // Advance 20 meters north-northwest
    rover.turnRightAngle(45);           // Adjust heading around obstacles
    rover.moveForwardDistance(40);
    rover.turnRightAngle(45);           // Navigate around rock field
    rover.moveForwardDistance(20);
    rover.turnLeftAngle(45);            // Final approach alignment
    rover.moveForwardDistance(20);      // Reach geological survey position
}

void loop() {
    // The loop function is not used for pre-planned traverses
}

```

---

## Mission Planning Hint

Real Mars rovers operate on nuclear power systems that generate about **110 watts**—less than a household light bulb—making energy efficiency crucial for every movement. They also work on **"Mars time,"** where each **sol** (Martian day) lasts 24 hours and 37 minutes, requiring mission controllers to adjust their schedules accordingly.

Notice that the trajectory of your rover is also displayed in the Output section, just like the real telemetry data received from active Mars missions. This trajectory visualization simulates actual Mars rover path planning data, similar to the navigation plots used by mission control centers for Mars exploration operations.
