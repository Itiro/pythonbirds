class Motor:

    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = 0 if self.velocidade <= 2 else self.velocidade - 2


class Direcao:
    direcoes = ("Norte", "Leste", "Sul", "Oeste")

    def __init__(self, direcao = "Norte"):
        if direcao in self.direcoes:
            self.valor = direcao
            self.indDirecao = self.direcoes.index(direcao)
        else:
            print("Direcao: {0} inválida!".format(direcao))

    def girar_a_direita(self):
        self.indDirecao = 0 if self.indDirecao == 3 else self.indDirecao + 1
        self.valor = self.direcoes[self.indDirecao]

    def girar_a_esquerda(self):
        self.indDirecao = 3 if self.indDirecao == 0 else self.indDirecao -1
        self.valor = self.direcoes[self.indDirecao]

class Carro:

    def __init__(self, motor = Motor(), direcao = Direcao()):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        print(self.motor.velocidade)

    def calcular_direcao(self):
        print(self.direcao.valor)

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)

    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)

    carro = Carro(motor, direcao)
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.frear()
    carro.calcular_velocidade()
    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
    carro.girar_a_esquerda()
    carro.calcular_direcao()
    carro.girar_a_esquerda()
    carro.calcular_direcao()

