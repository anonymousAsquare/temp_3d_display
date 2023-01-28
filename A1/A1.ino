int readV = A0;
float voltage;
int vol;
void setup() {
  // put your setup code here, to run once:
  pinMode(readV, INPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  vol = analogRead(readV);
  voltage = (5./1023.)*vol;
  Serial.print(voltage);
  Serial.println(" V ");
  delay(100);
}
