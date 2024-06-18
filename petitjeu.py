import random


sortir = False
print("\n\n\n\n\nBonjour ! \n\nAujourd'hui vous allez participer à un petit jeu de dés (sans dés lol)\n"
      "\nVous partez avec entre 0 et 1000€ et vous pouvez gagner de l'argent en ayant de la chance\n")
arg = random.randint(0, 1000)
print("Dans ce cas, vous avez ", arg, "€\n")
print("Chaque fois que vous gagnez un pari, vous remportez 10 fois cette somme, \n\nAtteignez 10000€ pour GAGNER!!!!\n")


def bot(somme, argent):
    impossible = False
    arg = argent
    print("Combien d'argent pariez-vous ?")
    pari = somme
    if pari > arg:
        impossible = True
    if impossible == False:    
        while arg > 0 and arg < 10000:
            coef = round(pari/arg)
            if coef > 1:
                pari = pari/coef
            arg -= pari
            print("Choisissez un nombre entre 1 et 6: ")
            nb_choisi = random.randint(1,6)
            nb_du_de = random.randint(1,6)
            if nb_choisi == nb_du_de:
                arg += pari*10
                print("Bien joué, le nombre était bien", nb_du_de, "!\nVous avez maintenant ", arg, "€.\n")
            else:
                print("Mauvais choix ! Le bot a choisi ", nb_choisi, "Mais le bon nombre était: ", nb_du_de)
                print("Vous avez maintenant ", arg, "€")

        if arg >= 10000:    
            print("\n\n\n\n\n\n\nVOUS AVEZ ATTEINT ", arg, "€!!! Vous avez donc gagné la partie :)")
        elif arg <=0:    
            print("\n\n\n\n\n\n\n\n\n\nPERDU! Vous n'avez plus d'argent...\n")
        else:
            print("Pas assez d'argent :(")
    

while True:
    if sortir == True:
        break
    print("Combien d'argent pariez-vous ?")
    pari = input()
    if pari == "bot":
        somme = int(input("Combien voulez-vous que le bot parie ?"))
        bot(somme, arg)
        sortir = True
    else:
        pari = int(pari)

    if sortir == False:    
        while pari > arg:
            print("Vous n'avez pas assez d'argent ):. Réessayez:")
            pari = int(input())
        arg -= pari
        nb_choisi = int(input("Choisissez un nombre entre 1 et 6: "))
        while nb_choisi > 6 or nb_choisi < 1:
            nb_choisi = int(input("Choisissez un nombre ENTRE 1 ET 6: "))

        nb_du_de = random.randint(1,6)
        if nb_choisi == nb_du_de:
            arg += pari*10
            print("Bien joué, le nombre était bien", nb_du_de, "!\nVous avez maintenant ", arg, "€.\n")
        else:
            print("Mauvais choix ! Le bon nombre était: ", nb_du_de)
            print("Vous avez maintenant ", arg, "€")

        if arg >= 10000:    
            print("n\n\n\n\n\n\n\nVOUS AVEZ ATTEINT ", arg, "@!!! Vous avez donc gagné la partie :)")
            break
        elif arg <= 0:    
            print("\n\n\n\n\n\n\n\n\n\nPERDU! Vous n'avez plus d'argent...\n")
            break