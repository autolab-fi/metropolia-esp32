# Lesson 5: Ridge Ascent — Programming the Rover's Trajectory Around the Crater

## Objective

Write a sequence of movement commands to guide the Mars rover along a predefined trajectory, simulating sample collection around the crater.

## Mission Briefing

Your rover has successfully navigated the **Crater** zone's perimeter and is now tasked with a more complex navigation mission: program it to follow a precise trajectory simulating the collection of geological samples from key locations around the crater rim.

This mission requires chaining multiple commands to control forward movement and turning, coordinating to mimic a real Mars rover traversing varied terrain and obstacles on its scientific route.

## Scientific Context

Rovers on Mars rely on detailed command sequences to navigate safely and efficiently. Each movement contributes to data collection for geological and environmental analysis. Programming accurate trajectories is crucial to avoid hazards and ensure scientific goals are met without manual intervention.

## Programming Theory

A **program** is an ordered list of instructions executed by the rover. You will combine previously learned functions from the **lineRobot.h** library — moving forward or backward by specified distances, and turning right or left — into a single program to follow the given path.

Functions recap:

- `robot.moveForwardDistance(dist)` — moves forward by `dist` centimeters.
- `robot.turnRight()` — turns right in place.
- `robot.turnLeft()` — turns left in place.

Your program should sequence these commands to draw the rover's path as shown in the trajectory image.

## Visual Reference

![Trajectory](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_1/trajectory)

Write a program that moves the rover along the route in the image, implementing these steps:

- Move forward and turn to navigate the route’s bends.
- Follow the pattern precisely as a sample collection route around the crater.

## Mission Debrief

Excellent work! By programming a complex sequence of movements, you’ve taken a crucial step toward full rover autonomy. This prepares you for controlling the rover over more challenging Martian terrain and enhances your understanding of how real missions script rover expeditions.

Next, you will learn about controlling the rover’s speed, vital for terrain adaptation and energy efficiency.

Good luck with your continued Mars exploration!