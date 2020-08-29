from time import sleep 
import platform, os,random

def limpa():
    if platform=="win32":
       os.system("cls")
    else:
        os.system("clear")

def banner():
    print("\033[33m="*42)
    print("{:^40}".format("Jogo da Forca versão 1.0.1"))
    print("{:^40}".format("Codificado por Clesh"))
    print("="*42,"\033[m")
    print("\n\n")
   
            

def nivel1():
    palavras=("FRANCA","MOCAMBIQUE","BANANA","MANGA","IOGURTE")
    palavras_descobertas=[]
    p=random.choice(palavras)
    acertos=0
    tentativas=6
    limpa()
    banner()
    para=False
    
    for x in range(0,len(p)):
        palavras_descobertas.append("-")
    if p=="FRANCA":
       
        print("Você tem {} tentativas para acertar a palavra".format(tentativas))
        print("\033[34mEscolhendo uma palavra...\033[m")
        sleep(3)
        while para == False:
            print("\n")
            if acertos==len(p):
                para=True
                print("\nGanhou")
                break
              
            if tentativas==0:
               para=True
               print("\n\033[31mVocê foi Enforcado\033[m")
               print("\nA Palavra secreta foi : {}".format(p))
               break
            char=str(input("\033[37mDigite uma letra:\033[m ")).strip().upper()
            limpa()
            banner()
            for x in range(0,len(p)):
                if char==p[x]:
                    palavras_descobertas[x]=char
                    acertos+=1
            if char not in p:
                 tentativas-=1
                 print(f"\033[31mERROU\nTentativas: {tentativas}\n\033[m")
                 print("\033[37mDICA: é um País localizado na Europa\033[m")
                 print("\033[37m\nA palavra tem {} Letras\n\033[m".format(len(p)))
              
            for x in range(0,len(p)):
               print("{}".format(palavras_descobertas[x]),end=" ")
       
            
    elif p=="MOCAMBIQUE":
              
              print("Você tem {} tentativas para acertar a palavra".format(tentativas))
              print("\033[34mEscolhendo uma palavra...\033[m")
              sleep(3)
              while para == False:
                         print("\n")
                         if acertos==len(p):
                                    para=True
                                    print("\n\033[38mGanhou\033[m")
                                    break
              
                         if tentativas==0:
                                  para=True
                                  print("\n\033[31mVocê foi Enforcado\033[m")
                                  print("\nA Palavra secreta foi : {}".format(p))
                                  break
                         char=str(input("\033[37mDigite uma letra:\033[m ")).strip().upper()
                         limpa()
                         banner()
                         for x in range(0,len(p)):
                                  if char==p[x]:
                                        palavras_descobertas[x]=char
                                        acertos+=1
                         if char not in p:
                                 tentativas-=1
                                 print(f"\033[31mERROU\nTentativas: {tentativas}\n\033[m")
                                 print("\033[37mDICA: é um País localizado na África Austral \033[m")
                                 print("\033[37m\nA palavra tem {} Letras\n\033[m".format(len(p)))
                         for x in range(0,len(p)):
                                 print("{}".format(palavras_descobertas[x]),end=" ")
     
    elif p=="BANANA":
             
              print("Você tem {} tentativas para acertar a palavra".format(tentativas))
              print("\033[34mEscolhendo uma palavra...\033[m")
              sleep(3)
              while para == False:
                         print("\n")
                         if acertos==len(p):
                                    para=True
                                    print("\n\033[38mGanhou\033[m")
                                    break
              
                         if tentativas==0:
                                  para=True
                                  print("\n\033[31mVocê foi Enforcado\033[m")
                                  print("\nA Palavra secreta foi : {}".format(p))
                                  break
                         char=str(input("\033[37mDigite uma letra:\033[m ")).strip().upper()
                         limpa()
                         banner()
                         for x in range(0,len(p)):
                                  if char==p[x]:
                                        palavras_descobertas[x]=char
                                        acertos+=1
                         if char not in p:
                                 tentativas-=1
                                 print(f"\033[31mERROU\nTentativas: {tentativas}\n\033[m")
                                 print("\033[37mDICA: é uma fruta muito consumida \033[m")
                                 print("\033[37m\nA palavra tem {} Letras\n\033[m".format(len(p)))
          
                         for x in range(0,len(p)):
                                 print("{}".format(palavras_descobertas[x]),end=" ")
     
    elif p=="MANGA":
              
              print("Você tem {} tentativas para acertar a palavra".format(tentativas))
              print("\033[34mEscolhendo uma palavra...\033[m")
              sleep(3)
              while para == False:
                         print("\n")
                         if acertos==len(p):
                                    para=True
                                    print("\n\033[38mGanhou\033[m")
                                    break
              
                         if tentativas==0:
                                  para=True
                                  print("\n\033[31mVocê foi Enforcado\033[m")
                                  print("\nA Palavra secreta foi : {}".format(p))
                                  break
                         char=str(input("\033[37mDigite uma letra:\033[m ")).strip().upper()
                         limpa()
                         banner()
                         for x in range(0,len(p)):
                                  if char==p[x]:
                                        palavras_descobertas[x]=char
                                        acertos+=1
                         if char not in p:
                                 tentativas-=1
                                 print(f"\033[31mERROU\nTentativas: {tentativas}\n\033[m")
                                 print("\033[37mDICA: é uma fruta \033[m")
                                 print("\033[37m\nA palavra tem {} Letras\n\033[m".format(len(p)))
          
                         for x in range(0,len(p)):
                                 print("{}".format(palavras_descobertas[x]),end=" ")
     
    elif p=="IOGURTE":
         
              print("Você tem {} tentativas para acertar a palavra".format(tentativas))
              print("\033[34mEscolhendo uma palavra...\033[m")
              sleep(3)
              while para == False:
                         print("\n")
                         if acertos==len(p):
                                    para=True
                                    print("\n\033[38mGanhou\033[m")
                                    break
              
                         if tentativas==0:
                                  para=True
                                  print("\n\033[31mVocê foi Enforcado\033[m")
                                  print("\nA Palavra secreta foi : {}".format(p)) 
                                  break
                         char=str(input("\033[37mDigite uma letra:\033[m ")).strip().upper()
                         limpa()
                         banner()
                         for x in range(0,len(p)):
                                  if char==p[x]:
                                        palavras_descobertas[x]=char
                                        acertos+=1
                         if char not in p:
                                 tentativas-=1
                                 print(f"\033[31mERROU\nTentativas: {tentativas}\n\033[m")
                                 print("\033[37mDICA: é um Líquido \033[m")
                                 print("\033[37m\nA palavra tem {} Letras\n\033[m".format(len(p)))
                         for x in range(0,len(p)):
                                 print("{}".format(palavras_descobertas[x]),end=" ")
          
          
def nivel2():
    p=[]
    palavras_descobertas=[]
    acertos=0
    tentativas=6
    para=False
    op=0
    limpa()
    banner()
    path ="/storage/emulated/0/qpython/Python-Projects/carros.txt"
    c=open(path,"r")
    for x in c.readlines():
           p.append(x)
    word=random.choice(p)
    c.close() 
    op=len(word)-2
    for x in range(0, op):
        palavras_descobertas.append("-")
    print("Você tem {} tentativas para acertar a palavra".format(tentativas))
    print("\033[34mEscolhendo uma palavra...\033[m")
    sleep(3)
    while para == False:
            print("\n")
            if acertos==op:
                para=True
                print("\nGanhou")
                break
              
            if tentativas==0:
               para=True
               print("\n\033[31mVocê foi Enforcado\033[m")
               print("\nA Palavra secreta foi : {}".format(word))
               break
            char=str(input("\033[37mDigite uma letra:\033[m ")).strip().upper()
            limpa()
            banner()
            for x in range(0,op):
                if char==word[x]:
                    palavras_descobertas[x]=char
                    acertos+=1
            if char not in word:
                 tentativas-=1
                 print(f"\033[31mERROU\nTentativas: {tentativas}\n\033[m")
                 print("\033[37mDICA: é nome de um Carro cuja letra inicial eh {}\033[m".format(word[0]))
                 print("\033[37m\nA palavra tem {} Letras\n\033[m".format(len(word)))
              
            for x in range(0,op):
               print("{}".format(palavras_descobertas[x]),end=" ")
limpa()

#Jogo principal 
resp="S"
while resp=="SIM" or resp=="S":
    opcao=int(input("""
[1]. Jogar
[0] Finalizar\n

opção : """))

    if opcao == 1:
          limpa()
          n=int(input("""
[1] Nível Básico 
[2] Nível Intermediário 
[3] Nível Avançado\n
Escolha uma Opção: """))

          if n == 1:
             nivel1()
          elif n==2:
              nivel2()
          elif n==3:
              print("avançado ")
          else:
              print("opção inválida ")
    elif opcao==0:
          break 
    else:
        print("FIM")
    resp=str(input("\nQuer Continuar continuar?  S/N ")).upper()
