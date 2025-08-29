### **Lesson 9: Movement Function**

## **Lesson Objective**

Learn how to write your own functions to control rover movement.

## **Introduction**

In this lesson, you will learn how to write your own functions. This skill is critical for organizing and simplifying complex code, much like how engineers at NASA break down rover control into modular, reusable functions for tasks such as driving, collecting samples, or deploying instruments.

---

## **Theory**

In a previous lesson, "License to Drive," you were introduced to the concept of pre-written functions. Now, you can write your own functions to make your code more compact, readable, and easier to maintain. This approach is key to developing reliable software for autonomous systems, which is essential for Mars missions due to the communication latency.

### **Types of Functions**

Functions can return values, such as numbers, characters, strings, etc. To specify the type of data a function returns, you need to indicate the function's type. Let's explore functions that return values and those that do not.

### **Functions Returning Values**

Functions that return a value are useful for calculations and data processing. For example, a function might calculate the distance a wheel has traveled or the battery life remaining. These functions must have a **`return`** statement, which ends the function's execution and returns the specified value.

Example of an **`int`** function:

```cpp
int sum(int num1, int num2){
    int result = num1 + num2; // calculated sum of the parameters
    return result; // returns the value of the variable result
}
```

The **`sum(a, b)`** function in this example takes two integer numbers, **`num1`** and **`num2`**, as parameters and returns their sum.

Example of using the function:

```cpp
int a = 5;
int b = 10;
int c = sum(a, b); // the value of the variable c is 15
```

In this code, variables **`a`** and **`b`** are initialized, their sum is calculated by calling the **`sum()`** function, and the result is stored in variable **`c`**.

Other examples of a **`return`** statement:

```cpp
...
return 0; // This function returns an integer with the value 0.
```

```cpp
...
return 'L'; // This function returns a char data type with the character 'L'.
```

### **Functions Not Returning Values**

In the previous section, you learned about functions that return values. However, many functions perform a task without needing to return a value. These functions use the special type **`void`**. A **`void`** function does not require a **`return`** statement because it returns nothing.

Example:

```cpp
void moveRoverForwardBackward(int secondsMove, int secondsPause){
    int milliSeconds = secondsPause * 1000; // seconds converted to milliseconds for delay
    rover.moveForwardSeconds(secondsMove);
    delay(milliSeconds);
    rover.moveBackwardSeconds(secondsMove);
}
```

The **`moveRoverForwardBackward`** function takes the parameter **`secondsMove`**, which tells the rover how long to move forward and backward, and the parameter **`secondsPause`**, which specifies the pause before the rover moves backward. This is similar to how NASA's rovers execute complex, multi-step commands (or "subroutines") from a sequence file without needing to return a value.

How to use this function:

```cpp
...
void setup(){
    moveRoverForwardBackward(3, 1);
}
...
```

In this code, we called the function **`moveRoverForwardBackward`**, so the rover will move forward for 3 seconds, then stop, and move backward for 3 seconds.

Remember: You should write **`moveRoverForwardBackward(3, 1);`** instead of \~\~`rover.moveRoverForwardBackward(3, 1);`\~\~.

---

## **Assignment**

Write a program that makes the rover turn approximately 180 degrees.

You can use the functions **`runMotorSpeedLeft`**, **`runMotorSpeedRight`**, **`stopMotorRight`**, and **`stopMotorLeft`**. The functions **`moveForwardDistance`**, **`moveBackwardDistance`**, **`turnLeft`**, **`turnRight`**, **`moveForwardSeconds`**, and **`moveBackwardSeconds`** will not work.

### **Hint**

We recommend writing your own movement function. You can design it to accept several parameters, such as separate speeds for the motors and time, or just the execution time with fixed speeds.

---

## **Conclusion**

Congratulations\! In this lesson, you learned how to write your own functions, a critical skill for any programmer. By creating a custom movement function, you’ve not only made your code more efficient but also gained insight into how complex autonomous systems, like those on Mars rovers, are controlled through well-organized, modular code.
