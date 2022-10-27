
from combustivel import calc_combustivel

if __name__ == '__main__':
    tempo = int(input('Qual tempo percorrido (em horas):'))
    velocidade_media = int(input('Qual velocidade média:'))
    litros = calc_combustivel.calcula_litros(tempo,velocidade_media)
    print("Será necessário {:.3f} litros".format(litros))
