#include "mbed.h"
#include "bbcar.h"
#include "bbcar_rpc.h"
#include <string>

DigitalOut redLED(LED1);
DigitalOut greenLED(LED2);
PwmOut pin9(D9), pin8(D8);
DigitalInOut pin10(D10);
Ticker servo_ticker;
Ticker encoder_ticker;
DigitalIn pin3(D3);
Serial pc(USBTX, USBRX);
Serial xbee(D12, D11);

BBCar car(pin8, pin9, servo_ticker);



int main() {
    parallax_ping  ping1(pin10);
    parallax_encoder encoder0(pin3, encoder_ticker);
    encoder0.reset();
    pc.printf("hello\n");
    /* 直走直到偵測到左方障礙物 */ 
    float a = 0,b = 0,c =0;
    float dist;
    float original_dist;

    float way = 0;
    float far = 0;
    car.goStraight(60);
    while(encoder0.get_cm()<27) wait_ms(30);
    car.stop();
    way = encoder0.get_cm();
    encoder0.reset();
    wait(0.01);
    // b = a;
    greenLED = 1;
    a = (float)ping1;
    while(1) {
        car.goStraight(60);
        while(encoder0.get_cm()<100) 
        {
            char buff[12];
            double num = encoder0.get_cm();
            pc.printf("%f\n", num);
            sprintf(buff, "%f", num);
            buff[8] = '0';
            buff[9] = '0';
            buff[10] = '0';
            buff[11] = '/0';


            xbee.printf("%s\n", buff);
            // xbee.printf("and: %c\n", buff[10]);

            wait(1);
            
        }
        encoder0.reset();
        car.stop();


    }
   

  

    return 0;
}

