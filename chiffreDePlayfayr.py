def remplacerW(chaine):
    chaineSansW = chaine.replace("w","v")
    return chaineSansW

def bigramme(chaineSansW):
    chaineSansW = chaineSansW.replace("ss","sxs")
    chaineSansW = chaineSansW.replace("ee","exe")
    chaineSansW = chaineSansW.replace("ll","lxl")
    chaineSansW = chaineSansW.replace("tt","txt")
    chaineSansW = chaineSansW.replace("nn","nxn")
    chaineSansW = chaineSansW.replace("mm","mxm")
    chaineSansW = chaineSansW.replace("rr","rxr")
    chaineSansW = chaineSansW.replace("pp","pxp")
    chaineSansW = chaineSansW.replace("ff","fxf")
    chaineSansW = chaineSansW.replace("cc","cxc")
    chaineSansW = chaineSansW.replace("aa","axa")
    chaineSansW = chaineSansW.replace("uu","uxu")
    chaineSansW = chaineSansW.replace("ii","ixi")
    return(chaineSansW)

def tailleChaine(chaineSansW):
    if len(chaineSansW) % 2 != 0:
        print(chaineSansW + "x")
        
    else:
        print(chaineSansW)

def AffichageTab(liste):
    for ligne in liste:
            for x in ligne:
                print(x,' ',end='')
            print('\n')

def verifListe(liste):
    liste = liste.replace("w","")
    if len(liste) == 25:
        for i in liste:
            if liste.count(i) >= 2:
                listeVerif = False
            else:
                listeVerif = True
        if listeVerif == False:
            print("La liste n'est pas bonne, elle contient des occurences !")
            liste = input("Liste : ")
            verifListe(liste)
        else:
            liste = [[liste[i + j * 5] for i in range(5)] for j in range(5)]
            AffichageTab(liste)
            
    else:
        print("La liste n'est pas bonne !")
        liste = input("Liste : ")
        verifListe(liste)

def recupCoord(lettre,liste):
    i = 0
    j = 1
    for x in range(len(liste)):
        i += 1
        if i == 6:
            i = 1
            j += 1
        for y in range(len(liste[x])):
            if liste[x][y] == lettre:
                return i,j
    
liste = input("Liste : ")
verifListe(liste)
lettre = input("Lettre : ")
print(recupCoord(lettre,liste))

#chaine = input("Chaine : ")
#tailleChaine(bigramme(remplacerW(chaine)))
