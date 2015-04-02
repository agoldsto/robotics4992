#define DXL_BUS_SERIAL1 1 

int index = 0;
float kp = 2;
float u = 0;

Dynamixel Dxl(DXL_BUS_SERIAL1);
int inChar; // Where to store the character read
void setup() {
  pinMode(BOARD_LED_PIN, OUTPUT);
  Dxl.begin(3);
  Dxl.wheelMode(1);
}

void loop() {
  if(SerialUSB.available() > 0){
    
    while(SerialUSB.available() > 0){
      
         inChar = SerialUSB.read();    
         
         
          float k_theta = 80 - (int)inChar;
          float e = u - k_theta;
          float theta_dot = e*kp;
          int dir = 0xFBFF;
          int input = floor(abs(theta_dot));
          
          if (input > 1023){
            input = 1023;
          }
          //'P' is int 80
          if (theta_dot <= 0){
            Dxl.goalSpeed(1, input & dir);
          }
          else{
            dir = 0x400;
            Dxl.goalSpeed(1, input | dir);
          }
    }
  }
}
