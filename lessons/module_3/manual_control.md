### **Lesson 8: Manual Control**

## **Lesson objective**

Learn about the Differential Drive Control of a Rover.

## **Introduction**

In this lesson, we will study the kinematics of the rover and examine the main issues related to motor control, a crucial aspect of autonomous planetary exploration.

---

## **Theory**

### **Rover Kinematics**

Let's consider the features of the rover from a kinematics perspective. The rover in the images is equipped with a **differential drive**, a system with two primary wheels controlled independently. This setup provides high maneuverability, allowing the rover to change direction and even rotate on the spot by varying the speed and direction of each wheel. This is similar to the design of NASA's Mars Exploration Rovers, **Spirit** and **Opportunity**, which relied on a rocker-bogie suspension system combined with differential steering to navigate the challenging Martian terrain.

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_3/robot_image.png?raw=True)

### **Challenges**

While differential drive offers great capabilities for a rover, it also introduces challenges that require sophisticated software and sensor feedback. For instance, maintaining a straight path requires precise synchronization of the motors' movements. Despite applying the same power, one motor might run slower than the other due to factors like gear inaccuracies, contamination from dust, or variations in mechanical friction.

These challenges are a major consideration for planetary rovers. On Mars, where maintenance is impossible, engineers must account for these mechanical imperfections through robust control laws to manage motor movements and ensure mission success.

### **Controlling Motors**

In the **rover** library, functions for controlling the motors are already written, and they can be used to control the motors individually.

The function **`runMotorSpeedLeft(speed)`** is used to send a signal to the left motor, with the speed parameter specified as a percentage. The speed can be either negative or positive, ranging from -100 to 100. When the parameter is greater than 0, the left wheel will rotate forward, and if the parameter is less than 0, the wheel will rotate in the opposite direction. **IMPORTANT!** These functions only start the motors; they do not stop them. To stop the motors, you can use a specific function or provide 0 as the parameter for the function, like `runMotorSpeedLeft(0)`.

The function **`runMotorSpeedRight(speed)`** works similarly for the right motor.

To stop the motors, you can also use the functions **`stopMotorRight()`** and **`stopMotorLeft()`**.

---

## **Assignment**

In this lesson, we encourage you to experiment with the differential drive of the rover. Write a program that makes the rover navigate straight for 3 seconds with a deviation of no more than 10 degrees. You will not be able to use the **`moveForwardDistance`**, **`moveForwardSpeedDistance`**, or **`moveForwardSeconds`** functions from the library. You will likely have to send the program multiple times, adjusting the motor speeds to achieve the desired result.

### **Hint**

We recommend reviewing the previous lesson to remember the **`delay()`** function, which will help you run the rover's motors for exactly 3 seconds and then turn them off.

---

## **Conclusion**

Congratulations! You learned more about your rover and encountered the first challenges of working with physical systems. This hands-on experience demonstrates the complexities that engineers face when designing real-world systems like Mars rovers. In the upcoming lessons, you will learn about writing control laws to fully manage the rover's movement and ensure smooth and even motion, just as NASA's rovers do on a planetary scale.
