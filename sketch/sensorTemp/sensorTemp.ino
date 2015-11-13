#include <LinkedList.h>
#include <Gaussian.h>
#include <GaussianAverage.h>


#define pinPoten A0

GaussianAverage movAvg(20);

void setup() {
  Serial.begin(9600);
  pinMode(pinPoten,INPUT);

}

void loop() {
 
 float value = analogRead(pinPoten);
 movAvg += value;
 movAvg.process();
 Serial.println(movAvg.mean);
 delay(100);

}
