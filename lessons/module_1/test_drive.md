# Mars Rover Mission Simulator

## Lesson 1: Test Drive

### Objective

Get started with your Mars rover and set it in motion.

### Introduction

In this lesson, you will learn how to command your rover's first movement across the Martian surface. It's not a complex task; all you need is curiosity and precision, just like real mission planners.

Behold the mighty rover, your companion in exploring the Red Planet.

Now, let's test the rover by writing a program for forward movement. This simple command mimics the initial "waking up" sequence for a newly deployed rover, ensuring all systems are go.

---

### Instructions

1.  Copy the code provided below and paste it into the code editor.

<!-- end list -->

```cpp
#include <rover.h>

void setup() {
    // Command the rover to move forward for 3 seconds
    robot.moveForwardSeconds(3);
}

void loop() {
    // The loop function is not used for this simple command
}
```

2.  Upload the program to the rover simulator.
3.  Observe the program execution results in the output and on the video feed.

---

### Real Mission Insight: The First Drive

The **Curiosity rover's** first test drive on Mars occurred on August 22, 2012, just 16 days after landing. The rover moved about 4.5 meters (15 feet) and then turned. This initial movement, called a "shakeout," was crucial for checking the rover's mobility system and ensuring it was ready for its long mission.

### Conclusion

Wasn't hard, was it? A tiny code, though a giant leap toward building your robotics skillset. You have successfully acquired the skill to make the rover move. Now, you can proceed to the next lesson\!
