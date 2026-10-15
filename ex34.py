import os

valor: int = 0
dir: str = '/tmp/exercicios'
arq: str = 'ex34.txt'


def mult(vlr, tab):
    res: int = 0
    res = vlr * tab
    return res

def grava(c, rslt):
    caminho = os.path.join(dir, arq)

    if os.path.exists(dir) and os.path.isdir(dir):
        tipo = 'w'

        if os.path.exists(caminho) and c > 0:
            tipo = 'a'

        with open(caminho, tipo) as file:
            file.write(str(rslt) + '\n')
            
        
def main():
    global valor

    contador: int = 0
    result: int = 0

    valor = int(input('Digite um valor entre 1 e 10: '))
    
    for contador in range(1, 11):
        result = mult(valor, contador)
        grava(contador, result)

if __name__ == '__main__':
    main()