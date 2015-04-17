#define DXL_BUS_SERIAL1 1 
#include <Servo.h> 
#include <timer.h>

Servo myservo; 
timer_dev timer;
Dynamixel Dxl(DXL_BUS_SERIAL1);

char mode = 's';
int servospeed = 94;

void setup() {
  
  timer_init(&timer);
  timer_pause(&timer);
  //timer_set_reload(&timer, 1000000);
  //timer_set_mode(&timer,TIMER_CH1,TIMER_OUTPUT_COMPARE);
  timer_resume(&timer);
  Dxl.begin(3);
  Dxl.wheelMode(1);
  Dxl.wheelMode(2);
  Dxl.wheelMode(4);
  Dxl.wheelMode(5);
  Dxl.jointMode(6);
  myservo.attach(10);
}

void loop() {
        
      SerialUSB.println("In loop");
          //Servo ID 1 and 2 control trolley movement along boom
          //F moves it away from the base
          //B moves it towards base
          if (mode == 'b'){
            Dxl.goalSpeed(2, 180 | 0x400);
            Dxl.goalSpeed(1, 205 | 0x400);
          }
          else if (mode == 'f'){
            Dxl.goalSpeed(2, 215);
            Dxl.goalSpeed(1, 170);
          }
          
          //PWD Servo controls boom rotation around base
          //R moves right
          //L moves left
          else if (mode == 'r'){
                myservo.write(92);
          }
          else if (mode == 'l'){
                myservo.write(96);
          }
  
  
          //Servo ID 4 moves the claw up and down
          //U moves the claw up
          //D moves the claw down
          else if (mode == 'u'){
              Dxl.goalSpeed(4, 200);
          }
          else if (mode == 'd'){
              Dxl.goalSpeed(4, 200 | 0x400);
          }
          
          
          //Servo ID 5 rotates the claw
          //P rotates the claw to the right (positive angle)
          //N rotates the claw to the left (negative angle)
          else if (mode == 'p'){
            Dxl.goalSpeed(5, 120);
          }
          
          else if (mode == 'n'){
            Dxl.goalSpeed(5, 120 | 0x400);
          }
          
          
          //Servo ID 6 Open and Closes the claw
          //O opens the claw
          //C closes the claw 
          else if (mode == 'o'){  
              Dxl.goalPosition(6, 0);
          }
  
          else if(mode == 'c'){
              Dxl.goalPosition(6, 140);
          }
          
          if(mode == 's'){
              Dxl.goalSpeed(1, 0);
              Dxl.goalSpeed(2, 0);
              Dxl.goalSpeed(4, 0);
              Dxl.goalSpeed(5, 0);
              myservo.write(94);
          }
          
         int time_count = timer_get_count(&timer);
         SerialUSB.println(time_count);
         mode = SerialUSB.read();  
         SerialUSB.println(mode);
}
