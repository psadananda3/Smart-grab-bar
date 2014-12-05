
void setup() {
  Serial.begin(9600);
}


void loop() {

  
  int pot1 = analogRead(A0);
  int pot2 = analogRead(A1);
  int flex1 = analogRead(A2);
  int flex2 = analogRead(A3);


  Serial.print(pot1);
  Serial.print(" ");
  Serial.print(pot2);
  Serial.print(" ");
  Serial.print(flex1);
  Serial.print(" ");
  Serial.println(flex2);
  delay(250);
}
