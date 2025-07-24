---
index: 0  
module: module_1  
task: mars_draw  
previous: None  
next: test_drive  
---

# Mission: Draw on Mars

## 🚀 Welcome to the Mars Rover Sandbox

Greetings, Cadet! Your Martian adventure begins now. In this space mission, you’ll take control of a robot rover as it navigates the *surface of Mars*! Test your code, experiment with rover movements, and visualize your rover’s path—just like leaving tracks in Martian dust. Activate **Verify** to see a glowing blue trail behind the rover for 20 Mars seconds.

## Mars Task

> **Objective:**  
> Program your rover to explore a mysterious square formation, rumored to be signals from an ancient Martian civilization!  
> Can you make your rover trace a perfect Martian square?

## Martian Rover Code Example

```cpp
#include 
void setup(){
   // Start your rover at a 45° angle—Mars style!
   robot.turnLeftAngle(45);
   robot.moveForwardDistance(20);
   robot.turnRight();
   robot.moveForwardDistance(20);
   robot.turnRight();
   robot.moveForwardDistance(20);
   robot.turnRight();
   robot.moveForwardDistance(20);
}
void loop(){
}
```

## 🌌 Mission Hints

- The red Martian sand will reveal the **path of your rover** in the Output section.
- Get creative! Try drawing new shapes the Martians may like.
- Remember: each movement leaves a mark on Mars, so plan your turns carefully.

Enjoy your journey across the *Martian sandbox*. The fate of the expedition awaits your code!

