
void setup() {
  Serial.begin(9600);
}


void loop() {

  int pressure1 = analogRead(A0);
  int pressure2 = analogRead(A1);
  int pressure3 = analogRead(A2);
  int pressure4 = analogRead(A3);
  int pressure5 = analogRead(A4);
  int pressure6 = analogRead(A5);
  int softpot1 = analogRead(A6);
  int softpot2 = analogRead(A7);
  
  Serial.print(pressure1);
  Serial.print(" ");
  Serial.print(pressure2);
  Serial.print(" ");
  Serial.print(pressure3);
  Serial.print(" ");
  Serial.print(pressure4);
  Serial.print(" ");
  Serial.print(pressure5);
  Serial.print(" ");
  Serial.print(pressure6);
  Serial.print(" ");
  Serial.print(softpot1);
  Serial.print(" ");
  Serial.println(softpot2);
  delay(250);
}
