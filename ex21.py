import os

os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o777)

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valormedia: float = 0.0

dir: str = '/tmp/exercicios'
arq: str = 'ex21.txt'

def med(n1, n2, n3, n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media

def entrada():
    global nome, nota1, nota2, nota3, nota4, valormedia

    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    valormedia = med(nota1, nota2, nota3, nota4)
    print(f'Média: {valormedia:.2f}')   

    cadastro(nome, nota1, nota2, nota3, nota4, valormedia)

def cadastro(nm, n1, n2, n3, n4, media):
    global dir, arq
    linha: str = ''
    linha = nm + ';' + str(n1) + ';' + str(n2) + ';' + str(n3) + ';' + str(n4) + ';' + str(media) + '\n'

    caminho = dir
    arquivo = arq

    escreveArq(caminho, arquivo, linha)

def escreveArq(cam, arq, lin):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    caminho_comleto = os.path.join(cam, arq)

    if os.path.exists(cam) and os.path.isdir(cam):
        if os.path.exists(caminho_comleto):
            tipo = 'a'
        else:
            tipo = 'w'

        enc = 'utf-8'

        with open(caminho_comleto, tipo, encoding=enc) as file:
            file.write(lin)

def main():
    contador: int = 0
    while contador < 5:
        entrada()
        contador += 1

if __name__ == '__main__':
    main()