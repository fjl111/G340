const int s = 3000;

int b1 = 0;
int b2 = A0;
int b3 = A1;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  analogWrite(5, 0);

  if (digitalRead(b1) > 0) //4
  {
    //10101010
    analogWrite(5, 1023); 
    delay(s);
    analogWrite(5, 0); 
    delay(s);
    analogWrite(5, 1023);
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023);
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023);
    delay(s);
  }
    
  else if (analogRead(b2) > 0) //5
  {
    //1010101010
    analogWrite(5, 1023); 
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023); 
    delay(s);
    analogWrite(5, 0); 
    delay(s);
    analogWrite(5, 1023);
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023);
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023);
    delay(s);
  }

  else if (analogRead(b3) > 0) //6
  {
    //101010101010
    analogWrite(5, 1023); 
    delay(s);
    analogWrite(5, 0); 
    delay(s);
    analogWrite(5, 1023); 
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023); 
    delay(s);
    analogWrite(5, 0); 
    delay(s);
    analogWrite(5, 1023);
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023);
    delay(s);
    analogWrite(5, 0);
    delay(s);
    analogWrite(5, 1023);
    delay(s);
  }
}
