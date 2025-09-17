### 2. **Proportional (P) Controller**

The P controller improves on relay by making the output proportional t### Conclusion

In this lesson, we explored three control strategies for keeping a line-following robot centered: Relay, P, and PI. The relay controller is simple but leads to unstable movement. The P controller improves this by making adjustments based on how far off the robot is, but still can't fully correct long-term drift. The PI controller solves this by remembering past errors and slowly pushing the robot back on track.

Each method builds on the last, making the robot smarter and more stable. This same evolutionary progression has driven Mars exploration success - from the basic control systems that got us to Mars, to the sophisticated algorithms that enable today's rovers to navigate autonomously across kilometers of alien terrain while conducting complex scientific operations. As we go forward, we'll explore the PID controller, which adds one final component — the derivative — to further improve control and reduce overshoot, completing the same control system architecture that guides Perseverance rover's precision movements during sample collection and Ingenuity helicopter's stable flight in the thin Martian atmosphere. far off the robot is from the center of the line. This proportional response approach revolutionized spacecraft control systems and is fundamental to Mars rover operations. When NASA's Sojourner rover landed on Mars in 1997 as part of the Pathfinder mission, it used proportional control algorithms to maintain stability while navigating the Martian surface - a major advancement over the simple on-off systems used by earlier spacecraft.

**Formula:**

```
u(t) = Kp × error
```

Where:

- `u(t)` is the control output,
- `Kp` is the proportional gain (a tuning constant),
- `error` is the difference between the current position and the desired position (usually 3.5 for 8 sensors).

The farther the robot is from the line center, the stronger the correction. This makes the movement smoother and more precise. Mars rovers use this same principle for attitude control - the farther the rover's actual heading deviates from the desired path, the stronger the steering correction applied to the wheels.

![P](https://github.com/pranavk-2003/line-robot-curriculum/blob/assignments/images/module_8/p.png?raw=True)

**Limitations:**

- Can't completely eliminate steady-state error.
- High gain may cause overshoot or oscillation.

These same limitations affected early Mars missions. The Spirit rover occasionally experienced proportional control overshoot when navigating steep terrain, causing it to make slightly larger steering corrections than optimal. This taught NASA engineers valuable lessons about gain tuning for Martian conditions, leading to more sophisticated control algorithms in later missions.

---

### 3. **Proportional-Integral (PI) Controller**

The PI controller fixes the steady-state error left behind by the P controller. It adds an integral term, which keeps track of accumulated past errors. If the robot is slightly off for a long time, the integral slowly increases to push it back to the center.

This control strategy proved essential for long-duration Mars missions. Opportunity rover's 14-year operational life demonstrated the importance of integral control - small systematic errors in wheel alignment or terrain interaction could accumulate over thousands of meters of driving. The integral term in Opportunity's navigation system helped compensate for these long-term drifts, enabling the rover to maintain accurate navigation across its epic 45-kilometer journey on Mars.

**Formula:**

```
u(t) = Kp × error + Ki × sum_of_errors
```

Where:

- `Kp` is the proportional gain,
- `Ki` is the integral gain,
- `sum_of_errors` is the running total of all previous errors.

## ![Pi](https://github.com/pranavk-2003/line-robot-curriculum/blob/assignments/images/module_8/pi.png?raw=True)

## Assignment – Implement a PI Controller

### Step 1: Calculate Weighted Sum and Total Value

```cpp
int weightedSum = 0;
int totalValue = 0;

for (int i = 0; i < 8; i++) {
    if (sensorvalues[i] > MY_BLACK_THRESHOLD) {
        weightedSum += i * sensorvalues[i];
        totalValue += sensorvalues[i];
    }
}
```

### Step 2: Calculate Position and Error

```cpp
double error = 0;
if (totalValue > 0) {
    double position = weightedSum / totalValue;
    error = position - 3.5;  // 3.5 is the center of an 8-sensor array
}
```

### Step 3: Compute Control Output (PI logic)

```cpp
integral += error;
integral = constrain(integral, -30, 30);  // limit the integral to avoid windup

double output = (Kp * error) + (Ki * integral);
```

The integral windup prevention shown here (constraining the integral term) is critical for Mars rover operations. Curiosity's drilling system uses similar integral limiting to prevent the drill from applying excessive force when it encounters hard rock formations. Without proper windup protection, the accumulated drilling errors could cause the system to apply dangerous forces that might damage the drill or the sample.

### Step 4: Set Motor Speeds

```cpp
double leftSpeed = fwdspeed - 1.5 * output;
double rightSpeed = fwdspeed + 1.5 * output;

rover.runMotorSpeedLeft(leftSpeed);
rover.runMotorSpeedRight(rightSpeed);
```

This differential steering approach, where left and right motors receive different speeds based on the control output, is exactly how Mars rovers navigate. Perseverance uses a sophisticated version of this concept with its six-wheel rocker-bogie suspension system, where individual wheel speeds are continuously adjusted based on terrain conditions, heading errors, and obstacle avoidance requirements.

---

### Summary

| Controller | Formula                             | Strength                              | Weakness                       |
| ---------- | ----------------------------------- | ------------------------------------- | ------------------------------ |
| Relay      | full left/right based on error sign | Simple and fast                       | Rough, unstable, zigzag motion |
| P          | u = Kp × error                      | Smooth control                        | Small steady-state error       |
| PI         | u = Kp × error + Ki × ∑error        | Smooth and accurate, eliminates error | Slower response, needs tuning  |

This progression from simple to sophisticated control mirrors the evolution of Mars rover technology. Early missions like Viking used relay-type systems for basic operations, Pathfinder introduced proportional control for improved rover mobility, and modern missions like Mars Science Laboratory (Curiosity) and Mars 2020 (Perseverance) employ advanced PI and PID controllers for precise scientific operations and autonomous navigation across complex Martian terrain.

---

### Conclusion

In this lesson, we explored three control strategies for keeping a line-following robot centered: Relay, P, and PI. The relay controller is simple but leads to unstable movement. The P controller improves this by making adjustments based on how far off the robot is, but still can't fully correct long-term drift. The PI controller solves this by remembering past errors and slowly pushing the robot back on track.

Each method builds on the last, making the robot smarter and more stable. As we go forward, we’ll explore the PID controller, which adds one final component — the derivative — to further improve control and reduce overshoot.
