# Lesson 9: Movement Function

## Lesson Objective
Learn how to write your own functions.

## Introduction
In this lesson, you will learn how to write your own functions in Arduino Wiring.

## Theory

In Lesson 2, "License to Drive," you were introduced to the concept of functions. Now, you can write your own functions to make your code more compact, readable, and easier to maintain.

### Types of Functions

Functions can return values, such as numbers, characters, strings, etc. To specify the type of data a function returns, you need to indicate the function's type. Let's explore functions that return values and those that do not.

### Functions Returning Values

Example of an **int** function:

```cpp
int sum(int num1, int num2){
    int result = num1 + num2; // calculated sum of the parameters
    return result; // return value of the variable result
}
```

The **sum(a, b)** function in the example takes numbers **num1** and **num2** as parameters and returns their sum. 

Example of using the function:
```cpp
int a = 5;
int b = 10;
int c = sum(a, b); // value of the variable c is 15
```
In this code, variables **a** and **b** are initialized, their sum is calculated, and the result is stored in variable **c**.

Functions that return values must have a **return** statement, which ends the function's execution and returns the specified value.
Examples:
```cpp
...
return 0;
```
This function returns 0.
```cpp
...
return 'L';
```
This function returns a **char** data type, specifically the character **'L'**.

### Functions Not Returning Values

In the previous section, you learned about functions that return values. However, there are also functions that do not return anything. These functions use the special type **void**. A void function does not require a return statement since it returns nothing.

Example:
```cpp
void moveRobotForwardBackward(int secondsMove, int secondsPause){
    int milliSeconds = secondsPause * 1000; // seconds converted to milliseconds for delay
    robot.moveForwardSeconds(secondsMove);
    delay(milliSeconds);
    robot.moveBackwardSeconds(secondsMove);
}
```

The **moveRobotForwardBackward** function takes the parameter **secondsMove**, which tells the robot how long to move forward and backward, and the parameter **secondsPause**, which specifies the pause before the robot moves backward.

How to use this function:
```cpp
...
void setup(){
    moveRobotForwardBackward(3, 1);
}
...
```
In this code, we called the function **moveRobotForwardBackward**, so the robot will move forward for 3 seconds, then stop, and move backward for 3 seconds.

Remember: You should write **moveRobotForwardBackward(3, 1);** isntead of ~~robot.moveRobotForwardBackward(3, 1);~~.

## Assignment
Write a program that makes the robot turn approximately 180 degrees.

You can use the functions **runMotorSpeedLeft**, **runMotorSpeedRight**, **stopMotorRight**, and **stopMotorLeft**. The functions **moveForwardDistance**, **moveBackwardDistance**, **turnLeft**, **turnRight**, **moveForwardSeconds**, and **moveBackwardSeconds** will not work.

### Hint
We recommend writing your own movement function. You can design it to accept several parameters, such as separate speeds for the motors and time, or just the execution time with fixed speeds.

## Conclusion
Congratulations! In this lesson, you learned how to write your own function, allowing you to organize your code more efficiently.