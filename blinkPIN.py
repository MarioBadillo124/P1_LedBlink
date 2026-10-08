#!/usr/bin/env python3
"""
Ejemplo de control LED usando modo BOARD (numeración física)
Pin 12 corresponde a GPIO 18 en modo BCM
"""

import RPi.GPIO as GPIO
import time

# Configuración
LED_PIN = 12  # Pin físico 12 (GPIO 18 en BCM)

try:
    # 1. Configurar modo de numeración BOARD
    GPIO.setmode(GPIO.BOARD)
   
    # 2. Desactivar advertencias
    GPIO.setwarnings(False)
   
    # 3. Configurar pin como salida con valor inicial LOW
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
   
    print("Control de LED iniciado (Modo BOARD)")
    print(f"Usando Pin físico {LED_PIN}")
    print("Presiona Ctrl+C para salir")
   
    # 4. Loop principal con diferentes patrones
    contador = 0
    while contador < 10:  # 10 ciclos
        # Parpadeo rápido (3 veces)
        for _ in range(3):
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.2)
       
        # Pausa larga
        time.sleep(1)
        contador += 1
        print(f"Ciclo {contador}/10 completado")

except KeyboardInterrupt:
    print("\nPrograma interrumpido")

finally:
    # Limpieza obligatoria
    GPIO.cleanup()
    print("Sistema apagado correctamente")