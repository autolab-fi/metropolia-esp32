# Mars Sandbox: Rover Path Drawing

## Mission Briefing

Welcome to the **Mars Sandbox: Draw** mode! Here, you're operating your Mars rover in a simulated Martian environment. Your mission: test movement commands, observe the rover's trajectory, and practice navigating segments of Gale Crater. When you execute "Verify", a blue trail will mark the rover's recent path—like a tire track on the Martian dust—visible for 20 seconds.

## Scientific Story Context

You are at your Mars base's **Garage**. You need to test the rover's mobility before heading out to explore craters and search for signs of water ice. Every motion you command simulates a test run across a safely marked Martian test pad. The trail helps Ground Control verify your commands result in the intended path, crucial for avoiding hazards out on the real surface.

## Zone Setting

- **Garage Pad**: The sandbox is your simulated garage test area. Develop and test custom movement commands to draw defined trajectories (shapes, angles, loops) in the Garage before missions in other zones like the Crater or Sample Depot.

## Code Example

```cpp
#include 
void setup(){
   // Simulate driving out of the Garage and forming a square route.
   robot.turnLeftAngle(45);
   robot.moveForwardDistance(20); // Move towards the Crater rim
   robot.turnRight();             // Turn to simulate scanning a rock
   robot.moveForwardDistance(20); // Continue along the pad edge
   robot.turnRight();
   robot.moveForwardDistance(20); // Traverse towards the Research Lab
   robot.turnRight();
   robot.moveForwardDistance(20); // Return to starting point
}
void loop(){
}
```

- Change angles and distances to create circles, zigzags, or exploratory patterns!
- Each maneuver you command reflects how rovers chart their course around real Martian obstacles.

## Sandbox Hints

- **Trace Visibility**: Watch the blue line to check your Martian rover's traveled route. Each time you run Verify, it marks where your rover rolled, simulating an instant replay of your drive-through Gale Crater's test garage.
- **Experiment**: Try drawing different shapes (triangle, circle, letter M) to test motors and sensors.

Enjoy exploring and practicing your navigation algorithms on Mars! Your virtual tire marks are proof of your progress in mastering robotic path planning under Martian conditions.