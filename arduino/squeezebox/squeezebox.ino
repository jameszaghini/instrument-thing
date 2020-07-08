int LED = 13;
int buttonPinA = 8;
int buttonPinB = 10;
int buttonPinC = 12;

void setup() {

  Serial.begin(9600);
  
   pinMode(buttonPinA, INPUT_PULLUP);
   pinMode(buttonPinB, INPUT_PULLUP);
   pinMode(buttonPinC, INPUT_PULLUP);
   
   pinMode(LED, OUTPUT);
}

void loop(){

   int buttonValue = digitalRead(buttonPinA);
   
   if (buttonValue == LOW){
      digitalWrite(LED,HIGH);
      Serial.println("A_DOWN");
   } else {
      digitalWrite(LED, LOW);
      Serial.println("A_UP");
   }

   int buttonValueB = digitalRead(buttonPinB);
   
   if (buttonValueB == LOW){
      digitalWrite(LED,HIGH);
      Serial.println("B_DOWN");
   } else {
      digitalWrite(LED, LOW);
      Serial.println("B_UP");
   }

   int buttonValueC = digitalRead(buttonPinC);
   
   if (buttonValueC == LOW){
      digitalWrite(LED,HIGH);
      Serial.println("C_DOWN");
   } else {
      digitalWrite(LED, LOW);
      Serial.println("C_UP");
   }   
}
