import threading
from Bar2.bar import Bar
from Bar2.bartender import Bartender
from Bar2.garcom import Garcom
from Bar2.cliente import Cliente

if __name__ == '__main__':
    n_clientes = 10
    n_garcoms = 3
    rodadas = 5
    limite_atendimentos = 3

    bar = Bar(n_clientes, rodadas)
    bartender = Bartender(bar, [])
    garcoms = [Garcom(i, bar, limite_atendimentos, bartender) for i in range(n_garcoms)]
    clientes = [Cliente(i, bar, garcoms) for i in range(n_clientes)]

    bar.start()

    for garcom in garcoms:
        garcom.start()

    for cliente in clientes:
        cliente.start()

    bar.join()

    for garcom in garcoms:
        garcom.join()

    for cliente in clientes:
        cliente.join()


    for cliente in clientes:
        cliente.join()