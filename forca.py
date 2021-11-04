from funcoes import limpa, marcaoGrande, ganhou, menuzin

limpa()
menuzin()

nome = input("Digite seu nome: ")
palavra = input("Digite a palavra secreta:").lower().strip()
dica1 = input("Digite a 1° dica: ")
dica2 = input("Digite a 2° dica: ")
dica3 = input("Digite a 3° dica: ")
for x in range(10): #mudar para 100
    print()
digitadas = []
acertos = []
erros = 0
print("Bem vindo",nome)
print("\nDigite '1' para receber a 1° Dica, ou Digite '2' para receber a 2° dica ou '3' Para receber a 3° dica\n")
print("""
X==:==
X  :
X  O
X \|/           Vc tem 5 vidas Tome Cuidado!
X / \ 
X
===========
A quantidade de letras são:
""")
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "*"
    print(senha)    
    if senha == palavra:
        ganhou()
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa == "1":
        print("\nA 1° dica é ->",dica1)
    elif tentativa == "2":
        print("\nA 2° dica é ->",dica2)
    elif tentativa == "3":
        print("\nA 3° dica é ->",dica3)    
    try:
        digitadas
    except:
        print("Caracter inválido")  #tentativa de try except,       
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ") #Desenho tosco de um cara na forca
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 5:
        print("Enforcado Amigão!")
        marcaoGrande()
        break
logs = open("Logs.txt","w")
logs.write("A Palavra: %s \n" % palavra)

if senha == palavra:
    logs.write("Vencedor: %s \n" % nome)
else:
    logs.write("Perdedor: %s \n" % nome)
    
    

