import random
continuar = "s"
while (continuar=="s" or continuar=="S"):
 goleiro = random.randint(1,6)
 print("\nBem vindo ao jogo de bater penalti \n")
 print("________________________________________________")
 print("|                   ___                         |")
 print("|                  (___)                        |")
 print("|               _____!_____                     |")
 print("|                    !                          |")
 print("|                    !                          |")
 print("|                   / \                         |")
 print("|                  /   \                        |\n")
 print("Chute conforme opções abaixo !!! \n")
 print("1 - Chute na diagonal esquerda \n2 - Chute no meio e alto \n3 - Chute na diagonal direita")
 print("4 - Chute no canto esquerdo \n5 - Chute no meio e baixo \n6 - Chute no canto direito\n")
 chute = input()

#1

 if(chute=="1")and (goleiro==1):
  print("          ________________________________________________")
  print("  () - - |          __                                    |")
  print("         |  \  \   (__)                                   |")
  print("         |   \___\___|_______                             |")
  print("         |    \______________\______                      |")
  print("         |                     \______                    |")
  print("         |                                                |")
  print("         |                                                |\n")
  print(                  "TAFFAREEEEEEEEELLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="1") and (goleiro==2):
  print("          ________________________________________________")
  print("         |                     ___                       |")
  print("         |  ()             |  (___)  |                   |")
  print("         |                  |___!___|                    |")
  print("         |                      !                        |")
  print("         |                      !                        |")
  print("         |                     / \                       |")
  print("         |                    /   \                      |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="1")and (goleiro==3):
  print("          ________________________________________________")
  print("         |                             __                 |")
  print("         |  ()                        (__)   /  /         |")
  print("         |                  ____________|___/  /          |")
  print("         |           ______/______________/___/           |")
  print("         |          ______/                               |")
  print("         |                                                |")
  print("         |                                                |\n")
  print(                  "GOLAÇOOOOOO !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="1")and (goleiro==4):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |  ()                                            |")
  print("         |                                                |")
  print("         |   ________                                     |")
  print("         |         __|__________________                  |")
  print("         |        (__)_________/________                  |")
  print("         |   _______|                                     |\n")
  print(                  "GOOOOOOLLLLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="1") and (goleiro==5):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |  ()                 ___                        |")
  print("         |                    (___)                       |")
  print("         |                     _!__                       |")
  print("         |                    / ! \                       |")
  print("         |                   / _!_ \                      |")
  print("         |                    /   \                       |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="1")and (goleiro==6):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |  ()                                            |")
  print("         |                                                |")
  print("         |                                     _________  |")
  print("         |                 ___________________|__         |")
  print("         |                 _______/___________(__)        |")
  print("         |                                    |_________  |\n")
  print(                  "GOOOOOOLLLLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

#2

 elif(chute=="2")and (goleiro==1):
  print("          ________________________________________________")
  print("         |          __          ()                        |")
  print("         |  \  \   (__)                                   |")
  print("         |   \___\___|_______                             |")
  print("         |    \______________\______                      |")
  print("         |                     \______                    |")
  print("         |                                                |")
  print("         |                                                |\n")
  print(                  "GOOOOOOOOLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="2") and (goleiro==2):
  print("                                         ()                  ")
  print("                                       '                   ")
  print("          ________________________________________________")
  print("         |                     ___    '                   |")
  print("         |                 |  (___)  |                    |")
  print("         |                  |___!___|                     |")
  print("         |                      !                         |")
  print("         |                      !                         |")
  print("         |                     / \                        |")
  print("         |                    /   \                       |\n")
  print(                  "GOOOOOLEEEEEIRO !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="2")and (goleiro==3):
  print("          ________________________________________________")
  print("         |                      ()     __                 |")
  print("         |                            (__)   /  /         |")
  print("         |                  ____________|___/  /          |")
  print("         |           ______/______________/___/           |")
  print("         |          ______/                               |")
  print("         |                                                |")
  print("         |                                                |\n")
  print(                  "GOOOOOOOOOLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="2")and (goleiro==4):
  print("          ________________________________________________")
  print("         |                      ()                        |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |   ________                                     |")
  print("         |         __|__________________                  |")
  print("         |        (__)_________/________                  |")
  print("         |   _______|                                     |\n")

  print(                  "GOOOOOOLLLLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="2") and (goleiro==5):
  print("          ________________________________________________")
  print("         |                      ()                        |")
  print("         |                     ___                        |")
  print("         |                    (___)                       |")
  print("         |                     _!__                       |")
  print("         |                    / ! \                       |")
  print("         |                   / _!_ \                      |")
  print("         |                    /   \                       |\n")
  print(                  "GOOOOLLL KKKK FRANGUEIRO !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="2")and (goleiro==6):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                      ()                        |")
  print("         |                                                |")
  print("         |                                     _________  |")
  print("         |                 ___________________|__         |")
  print("         |                 _______/___________(__)        |")
  print("         |                                    |_________  |\n")

  print(                  "GOOOOOOLLLLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 #3

 elif(chute=="3")and (goleiro==1):
  print("          ________________________________________________")
  print("         |          __                                ()  |")
  print("         |  \  \   (__)                                   |")
  print("         |   \___\___|_______                             |")
  print("         |    \______________\______                      |")
  print("         |                     \______                    |")
  print("         |                                                |")
  print("         |                                                |\n")
  print(                  "GOLAÇOOOOOO, HUMILHOU !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="3") and (goleiro==2):
  print("          ________________________________________________")
  print("         |                     ___                   ()  |")
  print("         |                 |  (___)  |                   |")
  print("         |                  |___!___|                    |")
  print("         |                      !                        |")
  print("         |                      !                        |")
  print("         |                     / \                       |")
  print("         |                    /   \                      |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="3")and (goleiro==3):
  print("                                                   ´  ()     ")
  print("                                                  ´          ")
  print("          ________________________________________________ ")
  print("         |                             __                 |")
  print("         |                          __(__)   /  /         |")
  print("         |                  ____________|___/  /          |")
  print("         |           ______/______________/___/           |")
  print("         |          ______/                               |")
  print("         |                                                |")
  print("         |                                                |\n")
  print(                  "ESPAAAAALMA CÁAAÁSSSIOO !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="3")and (goleiro==4):
  print("          ________________________________________________")
  print("         |                                             () |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |   ________                                     |")
  print("         |         __|__________________                  |")
  print("         |        (__)_________/________                  |")
  print("         |   _______|                                     |\n")

  print(                  "GOOOOOOLLLLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="3") and (goleiro==5):
  print("          ________________________________________________")
  print("         |                                             () |")
  print("         |                     ___                        |")
  print("         |                    (___)                       |")
  print("         |                     _!__                       |")
  print("         |                    / ! \                       |")
  print("         |                   / _!_ \                      |")
  print("         |                    /   \                       |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="3")and (goleiro==6):
  print("          ________________________________________________")
  print("         |                                             () |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                     _________  |")
  print("         |                 ___________________|__         |")
  print("         |                 _______/___________(__)        |")
  print("         |                                    |_________  |\n")

  print(                  "GOOOOOOLLLLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

#4

 elif(chute=="4")and (goleiro==1):
  print("          ________________________________________________")
  print("         |          __                                    |")
  print("         |  \  \   (__)                                   |")
  print("         |   \___\___|_______                             |")
  print("         |    \______________\______                      |")
  print("         |                     \______                    |")
  print("         |                                                |")
  print("         |   ()                                           |\n")
  print(                  "GOOOOOOOLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="4") and (goleiro==2):
  print("          _______________________________________________")
  print("         |                     ___                       |")
  print("         |                 |  (___)  |                   |")
  print("         |                  |___!___|                    |")
  print("         |                      !                        |")
  print("         |                      !                        |")
  print("         |                     / \                       |")
  print("         |  ()                /   \                      |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="4")and (goleiro==3):
  print("          ________________________________________________ ")
  print("         |                             __                 |")
  print("         |                            (__)   /  /         |")
  print("         |                  ____________|___/  /          |")
  print("         |           ______/______________/___/           |")
  print("         |          ______/                               |")
  print("         |                                                |")
  print("         |  ()                                            |\n")
  print(                  "OLHUUUGOOOOOLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="4")and (goleiro==4):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |   ________                                     |")
  print("         |         __|__________________                  |")
  print("         |        (__)_________/________                  |")
  print("  () --- |   _______|                                     |\n")

  print(                  "DEFESAAAAÇAA !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="4") and (goleiro==5):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                     ___                        |")
  print("         |                    (___)                       |")
  print("         |                     _!__                       |")
  print("         |                    / ! \                       |")
  print("         |                   / _!_ \                      |")
  print("         |  ()                /   \                       |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="4")and (goleiro==6):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                     _________  |")
  print("         |                 ___________________|__         |")
  print("         |                 _______/___________(__)        |")
  print("         |  ()                                |_________  |\n")

  print(                  "GOOOOOOLLLLLLLLLLAÇO !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 #5

 elif(chute=="5")and (goleiro==1):
  print("          ________________________________________________")
  print("         |          __                                    |")
  print("         |  \  \   (__)                                   |")
  print("         |   \___\___|_______                             |")
  print("         |    \______________\______                      |")
  print("         |                     \______                    |")
  print("         |                                                |")
  print("         |                      ()                        |\n")
  print(                  "GOOOOOOOLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="5") and (goleiro==2):
  print("          _______________________________________________")
  print("         |                     ___                       |")
  print("         |                 |  (___)  |                   |")
  print("         |                  |___!___|                    |")
  print("         |                      !                        |")
  print("         |                      !                        |")
  print("         |                   /    \                      |")
  print("         |                  /  ()  \                     |\n")
  print(                  "GOOOLLLLL KKKKK FRANGOOO !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="5")and (goleiro==3):
  print("          ________________________________________________ ")
  print("         |                             __                 |")
  print("         |                            (__)   /  /         |")
  print("         |                  ____________|___/  /          |")
  print("         |           ______/______________/___/           |")
  print("         |          ______/                               |")
  print("         |                                                |")
  print("         |                      ()                        |\n")
  print(                  "GOOOOOLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="5")and (goleiro==4):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |   ________              ____                   |")
  print("         |         __|____________/ ___                   |")
  print("         |        (__)_________/___/                      |")
  print("         |   _______|               ()                    |\n")

  print(                  "QUAAAASE O GOLEIRO PEGA, MAS FOI GOOOOOOOOLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="5") and (goleiro==5):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                     ___                        |")
  print("         |                    (___)                       |")
  print("         |                     _!__                       |")
  print("         |                    / ! \                       |")
  print("         |                   / _!_ \()                    |")
  print("         |                    /   \                       |\n")
  print(                  "ERRRRROUUUU KK !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="5")and (goleiro==6):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                    ___             _________   |")
  print("         |                    ___\ __________|__          |")
  print("         |                        \__\_______(__)         |")
  print("         |                     ()            |________    |\n")

  print(                  "GOOOLLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 #6

 elif(chute=="6")and (goleiro==1):
  print("          ________________________________________________")
  print("         |          __                                    |")
  print("         |  \  \   (__)                                   |")
  print("         |   \___\___|_______                             |")
  print("         |    \______________\______                      |")
  print("         |                     \______                    |")
  print("         |                                                |")
  print("         |                                            ()  |\n")
  print(                  "GOOOOOOOLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="6") and (goleiro==2):
  print("          _______________________________________________")
  print("         |                     ___                       |")
  print("         |                 |  (___)  |                   |")
  print("         |                  |___!___|                    |")
  print("         |                      !                        |")
  print("         |                      !                        |")
  print("         |                     / \                       |")
  print("         |                    /   \                   () |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="6")and (goleiro==3):
  print("          ________________________________________________ ")
  print("         |                             __                 |")
  print("         |                            (__)   /  /         |")
  print("         |                  ____________|___/  /          |")
  print("         |           ______/______________/___/           |")
  print("         |          ______/                               |")
  print("         |                                                |")
  print("         |                                             () |\n")
  print(                  "OLHUUUGOOOOOLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="6")and (goleiro==4):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |   ________                                     |")
  print("         |         __|__________________                  |")
  print("         |        (__)_________/________                  |")
  print("         |   _______|                                  () |\n")

  print(                  "GOOOOOOOLLL!!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="6") and (goleiro==5):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                     ___                        |")
  print("         |                    (___)                       |")
  print("         |                     _!__                       |")
  print("         |                    / ! \                       |")
  print("         |                   / _!_ \                      |")
  print("         |                    /   \                    () |\n")
  print(                  "GOOOOOOOOOOL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")

 elif(chute=="6")and (goleiro==6):
  print("          ________________________________________________")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                                |")
  print("         |                                     _________  |")
  print("         |                 ___________________|__         |")
  print("         |                 _______/___________(__)        |")
  print("         |                                    |_________  | --- ()    \n")

  print(                  "TAFFAREEEEEELLLLLLLL !!!")
  continuar=input("\nChutar novamente ? \nS - Para sim\n N - Para não\n")
 else:
  print("Digite uma opção válida !!!")
 


