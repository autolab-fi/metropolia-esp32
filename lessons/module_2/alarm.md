### **Lesson 7: Rover's Alarm**

## **Lesson objective**

Strengthen your understanding of the GPIO interface by creating a visual alarm system.

## **Introduction**

In this lesson, you will write a classic programming exercise to make an LED blink. This simple program is a fundamental step in embedded systems and will help you become more confident in working with the GPIO interface. This blinking function is a miniature version of the visual alarm systems used in real space missions to indicate critical events or to signal system status, which is especially important given the long communication delays between Earth and Mars.

---

## **Theory**

### **LED**

In the previous lesson, you learned about GPIO and LEDs. Now, let's take a closer look at how LEDs are connected.

![image](https://github.com/autolab-fi/line-robot-curriculum/blob/main/images/module_2/alarm_1.png?raw=true)

An LED has two contacts: an **anode** and a **cathode**. The anode is the longer contact and is connected to pin 32, while the cathode is connected to the ground. An electric current can only flow through the LED in one direction, from the anode to the cathode. When we send a high signal to pin 32, current flows, turning the LED on. When we send a low signal, the current stops flowing, and the LED turns off. Remember, current flows through the LED only from the anode to the cathode.

### **LED Blink**

You already know how to turn on an LED using the **`digitalWrite()`** function. In this lesson, we'll write a more advanced program. We'll not only turn on the LEDs on the rover but also turn them off by sending a low logic signal to the pin. To make the LEDs blink, you need to create pauses between switching signals. Given the significant **signal delay** (5 to 24 minutes one way) between Earth and Mars, rovers must operate autonomously, relying on pre-programmed instructions and real-time decision-making algorithms. This means that the blinking "alarm" must be managed locally by the rover's computer. The easiest way to create a pause in the program is to use the **`delay()`** function.

The **`delay(milliseconds)`** function pauses the program before executing the next command. This function takes a number as an argument, which represents the duration of the pause in milliseconds.

---

## **Assignment**

Write a program for the rover to turn on the LEDs for 1 second, then turn them off for 1 second, and repeat this indefinitely. This mimics a crucial function of onboard systems: providing a visible, immediate status update without the need for constant, delayed communication from Earth.

Remember, the LEDs are connected to pins defined in the code as **`ledPin1`** and **`ledPin2`**.

### **Hint**

1.  Remember, the **`setup()`** function executes only once, so the code within this function will run only a single time. In contrast, the **`loop()`** function executes continuously, meaning the code within this function will repeat indefinitely.
2.  Be careful: the argument of the **`delay()`** function is in milliseconds.

---

## **Conclusion**

Congratulations\! Now you know how to control logical signals using the GPIO interface in a more complex manner. This skill is critical for any embedded system, whether it's blinking a simple status light or signaling a critical error on a Martian mission.
