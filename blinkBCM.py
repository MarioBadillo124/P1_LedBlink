MODO BCM

#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
LED_PIN = 18  # GPIO 18 (pin físico 12)
try:
    # 1. Configurar modo de numeración BCM
    GPIO.setmode(GPIO.BCM)
    # 2. Desactivar advertencias (opcional)
    GPIO.setwarnings(False)
    # 3. Configurar pin como salida
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    print("Control de LED iniciado (Modo BCM)")
    print(f"Usando GPIO {LED_PIN} (Pin físico 12)")
    print("Presiona Ctrl+C para salir")
    # 4. Loop principal - Parpadeo del LED
    while True:
        # Encender LED (HIGH = 3.3V)
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ENCENDIDO")
        time.sleep(1)
        # Apagar LED (LOW = 0V)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED APAGADO")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")
finally:
    # 5. Limpieza - Restaurar pines a estado seguro
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")