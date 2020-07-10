const int LED = 13;
const int buttonPinA = 8;
const int buttonPinB = 10;
const int buttonPinC = 12;
const int pingPin = 3;

void setup() {

    Serial.begin(9600);

    pinMode(buttonPinA, INPUT_PULLUP);
    pinMode(buttonPinB, INPUT_PULLUP);
    pinMode(buttonPinC, INPUT_PULLUP);

    pinMode(LED, OUTPUT);
}

void loop(){
    handleReadForButton(buttonPinA, "A_DOWN", "A_UP");
    handleReadForButton(buttonPinB, "B_DOWN", "B_UP");
    handleReadForButton(buttonPinC, "C_DOWN", "C_UP");
}

void handleReadForButton(int pin, String down, String up) {
   
    const int buttonValue = digitalRead(pin);
   
    if (buttonValue == LOW){
        digitalWrite(LED, HIGH);
        Serial.println(down);
    } else {
        digitalWrite(LED, LOW);
        Serial.println(up);
    }
}
