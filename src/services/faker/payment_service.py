import random

def process_payment():
    # Simulación de un procesamiento de pago con un 50% de éxito o fracaso
    success = random.choice([True, False])
    return "success" if success else "failure"
