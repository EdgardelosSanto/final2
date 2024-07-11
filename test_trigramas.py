import sys
import os
import pytest

# Asegura que la ruta al directorio 'src' esté en sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Ahora puedes importar el módulo desde src.domain
from domain import generar_trigramas

def test_generar_trigramas():
    parrafo = "I wish I may I wish I might"
    esperado = {
        ('I', 'wish'): ['I', 'I'],
        ('wish', 'I'): ['may', 'might'],
        ('I', 'may'): ['I'],
    }
    resultado = generar_trigramas(parrafo)
    
    for key in resultado:
        resultado[key].sort()
    for key in esperado:
        esperado[key].sort()
    
    assert resultado == esperado

if __name__ == "__main__":
    pytest.main()
