from machine import Pin
from time import sleep

botao = Pin(4, Pin.IN)
led_amarelo = Pin(25, Pin.OUT)
led_verde = Pin(26, Pin.OUT)
led_vermelho = Pin(27, Pin.OUT)

contador_produtos = 0
contador_caixas = 0
estado_anterior = 0

def piscar_leds():
    for _ in range(2):
        led_amarelo.on()
        led_verde.on()
        led_vermelho.on()
        sleep(0.3)
        led_amarelo.off()
        led_verde.off()
        led_vermelho.off()
        sleep(0.3)

# loop 
while contador_caixas < 5:
    scanner_produtos = botao.value()

    # detecta a mudança de estado do botão
    if scanner_produtos and not estado_anterior:
        contador_produtos += 1
        print(f"Produto detectado: {contador_produtos}")

        # a cada 10 produtos, uma caixa é completada
        if contador_produtos % 10 == 0:
            contador_caixas += 1
            print(f" Caixa completa! Total de caixas: {contador_caixas}")
            piscar_leds()

    estado_anterior = scanner_produtos
    sleep(0.05)