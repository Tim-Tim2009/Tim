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
        good = False
        while not good:    
            try:
                somme = int(input("Combien voulez-vous que le bot parie ?"))
                bot(somme, arg)
                good = True
                sortir = True
            except ValueError:
                print("Entrez un nombre entier svp")
    else:
        good = False
        while not good:    
            try:
                pari = int(pari)
                good = True
            except ValueError:
                pari = input("Entrez un nombre ou faites appel au bot: ")
    if pari == 'bot': pari = 69
    if sortir == False:    
        while pari > arg:
            print("Vous n'avez pas assez d'argent ):. Réessayez:")
            good = False
            while not good:    
                try:
                    pari = int(pari)
                    good = True
                except ValueError:
                    pari = input("Entrez un nombre ou faites appel au bot: ")        
        arg -= pari
        good = False
        while not good:    
            try:
                nb_choisi = int(input("Choisissez un nombre entre 1 et 6: "))
                good = True
            except ValueError:
                print("Entrez un nombre")
        good = False
        while nb_choisi > 6 or nb_choisi < 1:
            while not good:    
                try:
                    nb_choisi = int(input("CHOISISSEZ UN NOMBRE ENTRE 1 ET 6: "))
                    good = True
                except ValueError:
                    print("J'ai dit...")

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
