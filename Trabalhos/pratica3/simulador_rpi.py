# simulador_rpi.py

def simular_raspberry_pi():
    """
    Ativa o modo de simulação para a biblioteca gpiozero.

    Esta função substitui a fábrica de pinos padrão, que interage com
    o hardware do Raspberry Pi, por uma fábrica de simulação (MockFactory).
    Isso permite que o código que utiliza a gpiozero seja executado em
    qualquer computador, mesmo sem uma placa Raspberry Pi conectada.

    As ações que seriam realizadas nos pinos (ex: ligar/desligar um LED)
    serão impressas no console, permitindo a depuração da lógica do programa.
    """
    try:
        # Importa as classes necessárias da biblioteca gpiozero
        from gpiozero.pins.mock import MockFactory
        from gpiozero import Device

        # Define a fábrica de pinos do dispositivo para ser a MockFactory
        Device.pin_factory = MockFactory()

        print("**************************************************")
        print("*** MODO DE SIMULAÇÃO RASPBERRY PI ATIVADO     ***")
        print("*** As interações com GPIO serão simuladas.    ***")
        print("**************************************************")
        print() # Adiciona uma linha em branco para melhor visualização

    except ImportError:
        print("A biblioteca gpiozero não foi encontrada.")
        print("Por favor, instale-a com: pip install gpiozero")
        # Encerra o programa se a biblioteca não estiver instalada
        exit()