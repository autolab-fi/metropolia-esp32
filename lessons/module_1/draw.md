---
index: 0
module: module_1
task: draw
previous: None
next: test_drive
---
# Sandbox: Draw


## Description
Hello and welcome to sandbox-draw mode, where you can test your code. Additionally, you can execute Verify' and a blue trail will be left behind the rover for 20 seconds.


## Code example
```
#include <rover.h>
void setup(){
   rover.turnLeftAngle(45);
   rover.moveForwardDistance(20);
   rover.turnRight();
   rover.moveForwardDistance(20);
   rover.turnRight();
   rover.moveForwardDistance(20);
   rover.turnRight();
   rover.moveForwardDistance(20);
}
void loop(){
}
```

## Hint 
Notice that the trajectory of your rover is also displayed in the Output section.

![Verification_output](https://github.com/autolab-fi/line-robot-curriculum/assets/13139586/2ed60da4-7158-43a8-894d-824ec26e6eab)


