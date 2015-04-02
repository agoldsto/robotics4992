#define DXL_BUS_SERIAL1 1 

int index = 0;
int pxval = 0;
int cxval = 0;
int adjxval = 0;
float kp = 1;
float pcomp = 0;
float input = 0;

Dynamixel Dxl(DXL_BUS_SERIAL1);
int inChar; // Where to store the character read
void setup() {
  pinMode(BOARD_LED_PIN, OUTPUT);
  Dxl.begin(3);
  Dxl.wheelMode(1);
}

void loop() {
  if(SerialUSB.available() > 0){
    int inData[20];
    
    while(SerialUSB.available() > 0){
      
      if(index < 19){
         inChar = SerialUSB.read();    
         inData[index] = (int)inChar;
         
         index++;
         inData[index] = '\0'; //Null terminate the string
         
          cxval = inData[index-1];
          
          adjxval = 80 - cxval;
          pcomp = adjxval*kp;
          input = pcomp;
          
          
          SerialUSB.print("input = ");
          SerialUSB.println(input);
          
          //'P' is int 80
          if (input > 0){
            Dxl.goalSpeed(1, 75 | 0x400);
          }
          else if (input < 0){
            Dxl.goalSpeed(1, 75);
          }
          else{
            Dxl.goalSpeed(1, 0);
          }
          pxval = cxval;
      }
      index = 0;
      
    }
     
  }
  delay(20);
}

