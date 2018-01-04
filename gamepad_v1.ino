

  int fwd_pin=2;
  int rwd_pin=3;
  int lh_pin=5;
  int rh_pin=4;
  int read_rasp=0;
  int incomingByte = 0;
  byte b0;
  byte b1;
  byte b2;
  byte b3;
  byte b4;
  byte b5;
  byte b6;
  byte b7;
  
  
// the setup function runs once when you press reset or power the board
void setup() {
  
 
Serial.begin(9600);
 

  pinMode(fwd_pin, OUTPUT);
  pinMode(rwd_pin, OUTPUT);
  pinMode(lh_pin, OUTPUT);
  pinMode(rh_pin, OUTPUT);
  pinMode(13,OUTPUT);
  digitalWrite(fwd_pin, LOW);
  digitalWrite(rwd_pin, LOW);
  digitalWrite(lh_pin, LOW);
  digitalWrite(rh_pin, LOW);
}

// the loop function runs over and over again forever
void loop() {
  while(Serial.available()>0)
  {
  incomingByte = Serial.read();
  b0=bitRead(incomingByte,0);
  b1=bitRead(incomingByte,1);
  b2=bitRead(incomingByte,2);
  b3=bitRead(incomingByte,3);
  b4=bitRead(incomingByte,4);
  b5=bitRead(incomingByte,5);
  b6=bitRead(incomingByte,6);
  b7=bitRead(incomingByte,7);
 
 digitalWrite(fwd_pin, b0);
 digitalWrite(rwd_pin, b1);
 digitalWrite(lh_pin, b2);
 digitalWrite(rh_pin, b3);
 
 
 // say what you got:
 // Serial.print("I received: ");
  //Serial.println(incomingByte, BIN);
 /* if (b0==1){
  mv_fwd();
  } 
  if (b0==0){
   stp_fwd();
  } 
  else if (read_rasp==2){
  mv_rwd();
  }   
  
  else if (read_rasp==3){
  mv_lh();
  }  
  
  else if (read_rasp==4){
  mv_rh();
  }  
  
  else if (read_rasp==5){
  mv_fwdlh();
  }  
  
   else  if (read_rasp==6){
  mv_fwdrh();
  }  
  
    else if (read_rasp==7){
  mv_rwdlh();
  }  
  
    else   if (read_rasp==8){
  mv_rwdrh();
  }  
  else   if (read_rasp==9){
  mv_stop();
  }
*/

}

}


void mv_fwd(){
  digitalWrite(fwd_pin, HIGH);
  digitalWrite(rwd_pin, LOW);
  digitalWrite(13, HIGH);

}

void mv_rwd()
{
  digitalWrite(rwd_pin, HIGH);
  digitalWrite(fwd_pin, LOW);
  digitalWrite(13, LOW);
}
void mv_lh()
{
  digitalWrite(lh_pin, HIGH);
  digitalWrite(rh_pin, LOW);
  delay(200);
}
void mv_rh()
{
  digitalWrite(rh_pin, HIGH);
  digitalWrite(lh_pin, LOW);
  delay(200);
}

void mv_fwdlh()
{
  digitalWrite(fwd_pin, HIGH);
  digitalWrite(lh_pin, HIGH);
   digitalWrite(rwd_pin, LOW);
  digitalWrite(rh_pin, LOW);
}

void mv_fwdrh()
{
  digitalWrite(fwd_pin, HIGH);
  digitalWrite(rh_pin, HIGH);
  digitalWrite(rwd_pin, LOW);
  digitalWrite(lh_pin, LOW);
}

void mv_rwdlh()
{
  digitalWrite(rwd_pin, HIGH);
  digitalWrite(lh_pin, HIGH);
   digitalWrite(fwd_pin, LOW);
  digitalWrite(rh_pin, LOW);
}

void mv_rwdrh()
{
  digitalWrite(rwd_pin, HIGH);
  digitalWrite(rh_pin, HIGH);
   digitalWrite(fwd_pin, LOW);
  digitalWrite(lh_pin, LOW);
}

void mv_stop()
{
  digitalWrite(rwd_pin, LOW);
  digitalWrite(fwd_pin, LOW);
  digitalWrite(rh_pin, LOW);
  digitalWrite(lh_pin, LOW);
}

void stp_fwd()
{
    digitalWrite(fwd_pin, LOW);
}
void stp_rwd()
{
    digitalWrite(rwd_pin, LOW);
}
void stp_lh()
{
    digitalWrite(lh_pin, LOW);
}
void stp_rh()
{
    digitalWrite(rh_pin, LOW);
}
