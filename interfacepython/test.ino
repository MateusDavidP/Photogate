#include <SoftwareSerial.h>

const int pinbutton = 13;
bool inicio = false;
unsigned long tempoAnterior = 0;
SoftwareSerial BTSerial(10, 11);  // Pinos 10 (RX) e 11 (TX) para comunicação Bluetooth

void setup()
{
  pinMode(pinled, OUTPUT);
  pinMode(pinbutton, INPUT);
  BTSerial.begin(9600);  // Inicializa a comunicação Bluetooth
}

void loop()
{
  bool aperto = digitalRead(pinbutton);
  if (inicio && !aperto)
  {
    unsigned long tempoAtual = millis();
    unsigned long tempoDecorrido = tempoAtual - tempoAnterior;
    
    // Enviar os dados para o computador via Bluetooth
    BTSerial.print(tempoDecorrido);
    BTSerial.println();
    
    tempoAnterior = tempoAtual;
    digitalWrite(pinled, HIGH); // Ligar o LED
  }
  inicio = aperto;
}