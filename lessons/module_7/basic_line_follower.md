# **Lesson 1: Relay, P, and PI Controllers**

### Objective

Understand how different types of controllers work — Relay, Proportional (P), and Proportional-Integral (PI). Learn how each improves performance for a line-following robot. These control systems form the foundation of autonomous navigation used by Mars rovers, where precise path-following and obstacle avoidance are critical for mission success millions of miles from Earth.

### 1. **Relay Controller**

A relay controller is the simplest type of control system. It just turns motors fully left or right based on which side of the line the robot is on. It doesn't care how far the robot is from the center — it only knows left or right. While effective for basic applications, this binary approach has limitations that became apparent during early Mars missions. The Viking landers used simple on-off controllers for some systems, but the lack of proportional response meant they couldn't achieve the smooth, precise movements needed for delicate scientific operations.

**Control rule:**

```
If error > 0 → turn full right
If error < 0 → turn full left
```

**Formula:**

```
u(t) = max_speed  if error > 0
u(t) = min_speed  if error <= 0
```

This results in a zigzag movement. The rover overcorrects and keeps switching directions. This same overcorrection problem plagued early spacecraft attitude control systems until engineers developed more sophisticated control algorithms that Mars rovers use today for smooth, stable navigation.

---

## **Programming the Line Following Algorithm to use a Relay Controller**

This code will:

1. Read sensor values from all 8 sensors.
2. Decide the robot's movement based on sensor readings.
3. Move forward, turn left, turn right, or stop.

This systematic approach to sensor data processing and decision-making mirrors the control algorithms used by Mars rovers. Curiosity and Perseverance use similar logic frameworks: continuously read multiple sensor inputs, process the data through decision trees, and execute appropriate motor commands. However, Mars rovers employ much more sophisticated versions of these basic concepts, with multiple layers of safety checks and gradual response adjustments rather than the binary on-off decisions of a relay controller.

### **Code Implementation**

```cpp
#include <Octoliner.h>
#include <rover.h>

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
    rover.runMotorSpeedRight(speed);
    rover.runMotorSpeedLeft(speed);
}
```

---

## **Understanding the Logic**

### **Sensor Detection and Movement**

The robot determines movement based on which sensors detect the black line.  
Below is a flowchart for a clear understanding:

![Flow](https://github.com/pranavk-2003/line-robot-curriculum/blob/assignments/images/module_7/FC.png?raw=True)

1. **If middle sensors (3 OR 4) detect the line** → Move forward.
2. **If left sensors (0 OR 1 OR 2) detect the line** → Turn left.
3. **If right sensors (5 OR 6 OR 7) detect the line** → Turn right.
4. **If no sensor detects the line** → Stop.

This decision tree approach is fundamental to Mars rover navigation systems. Perseverance's AutoNav system uses similar multi-sensor logic but with hundreds of decision points. When the rover's hazard cameras detect terrain features, it categorizes them as safe, caution, or hazardous zones, then selects appropriate driving responses. The difference is that Mars rovers use graduated responses rather than simple binary decisions - they might slow down for caution zones rather than stopping completely, or take wider turns around obstacles rather than sharp left-right corrections.

---

## **Assignment**

Modify the program to:

1. Write a program to make the robot line follow.
2. Fine-tune motor speeds for smoother movement.
3. Experiment with different thresholds to improve accuracy.
4. Ensure the rover successfully crosses both checkpoints to complete the Assignment.

This iterative tuning process reflects how Mars mission engineers optimize rover performance. When Opportunity rover was struggling with wheel problems later in its mission, engineers spent months fine-tuning driving algorithms, adjusting motor current limits, and experimenting with different movement patterns to maximize the rover's mobility while protecting damaged wheels. Similarly, Curiosity's autonomous drilling system required extensive parameter tuning to adapt to different Martian rock types encountered during its journey through Gale Crater.

---

## **Conclusion**

In this lesson, you have learned how to implement a basic **line-following algorithm** using an **Octoliner IR sensor array**. Understanding how to read sensor values and adjust movement based on input is fundamental to developing more advanced autonomous navigation systems.

These basic control principles you've mastered represent the evolutionary foundation of Mars rover autonomy. From the simple relay-like controllers that guided the first successful Mars Pathfinder mission in 1997, to the sophisticated multi-layered control systems that enable today's Perseverance rover to navigate autonomously across kilometers of Martian terrain, the core concepts remain the same: sense the environment, process the data, and respond appropriately. As NASA develops future Mars missions including sample return vehicles and human exploration support robots, these fundamental control system principles will continue to be essential for creating reliable autonomous systems capable of operating in the challenging Martian environment.
