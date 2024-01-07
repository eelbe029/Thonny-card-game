from tkinter import *
from PIL import ImageTk
from PIL import Image
from PIL import *
from time import sleep
import random


class Carte:
    """Représente une carte à jouer standard."""
    #trèfle' : 0, 'carreau': 1, 'cœur': 2, 'pique':3, ordre de comparaison des couleurs

    def __init__(self, couleur = 0, valeur = 2):
        images_trefle = [None, None, Image.open("Images/backup/Trefle_0/02.png"),
        Image.open("Images/backup/Trefle_0/03.png"),Image.open("Images/backup/Trefle_0/04.png"),
        Image.open("Images/backup/Trefle_0/05.png"), Image.open("Images/backup/Trefle_0/06.png"),
        Image.open("Images/backup/Trefle_0/07.png"), Image.open("Images/backup/Trefle_0/08.png"),
        Image.open("Images/backup/Trefle_0/09.png"), Image.open("Images/backup/Trefle_0/010.png"),
        Image.open("Images/backup/Trefle_0/011.png"), Image.open("Images/backup/Trefle_0/012.png"),
        Image.open("Images/backup/Trefle_0/013.png"), Image.open("Images/backup/Trefle_0/014.png")]
        images_carreau = [None, None, Image.open("Images/backup/Carreau_1/12.png"),
        Image.open("Images/backup/Carreau_1/13.png"),Image.open("Images/backup/Carreau_1/14.png"),
        Image.open("Images/backup/Carreau_1/15.png"), Image.open("Images/backup/Carreau_1/16.png"),
        Image.open("Images/backup/Carreau_1/17.png"), Image.open("Images/backup/Carreau_1/18.png"),
        Image.open("Images/backup/Carreau_1/19.png"), Image.open("Images/backup/Carreau_1/110.png"),
        Image.open("Images/backup/Carreau_1/111.png"), Image.open("Images/backup/Carreau_1/112.png"),
        Image.open("Images/backup/Carreau_1/113.png"), Image.open("Images/backup/Carreau_1/114.png")]
        images_coeur = [None, None, Image.open("Images/backup/Coeur_2/22.png"),
        Image.open("Images/backup/Coeur_2/23.png"),Image.open("Images/backup/Coeur_2/24.png"),
        Image.open("Images/backup/Coeur_2/25.png"), Image.open("Images/backup/Coeur_2/26.png"),
        Image.open("Images/backup/Coeur_2/27.png"), Image.open("Images/backup/Coeur_2/28.png"),
        Image.open("Images/backup/Coeur_2/29.png"), Image.open("Images/backup/Coeur_2/210.png"),
        Image.open("Images/backup/Coeur_2/211.png"), Image.open("Images/backup/Coeur_2/212.png"),
        Image.open("Images/backup/Coeur_2/213.png"), Image.open("Images/backup/Coeur_2/214.png")]
        images_pique = [None, None, Image.open("Images/backup/Pique_3/32.png"),
        Image.open("Images/backup/Pique_3/33.png"),Image.open("Images/backup/Pique_3/34.png"),
        Image.open("Images/backup/Pique_3/35.png"), Image.open("Images/backup/Pique_3/36.png"),
        Image.open("Images/backup/Pique_3/37.png"), Image.open("Images/backup/Pique_3/38.png"),
        Image.open("Images/backup/Pique_3/39.png"), Image.open("Images/backup/Pique_3/310.png"),
        Image.open("Images/backup/Pique_3/311.png"), Image.open("Images/backup/Pique_3/312.png"),
        Image.open("Images/backup/Pique_3/313.png"), Image.open("Images/backup/Pique_3/314.png")]
        self.couleur = couleur
        self.valeur = valeur
        if couleur == 0:
            self.img = images_trefle[valeur]
        if couleur == 1:
            self.img = images_carreau[valeur]
        if couleur == 2:
            self.img = images_coeur[valeur]
        if couleur == 3:
            self.img = images_pique[valeur]

    noms_couleurs = ['trèfle', 'carreau', 'cœur', 'pique']
    noms_valeurs = [None, None, '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'valet', 'dame', 'roi','as']

    def __str__(self):
        return Carte.noms_valeurs[self.valeur]+' de '+Carte.noms_couleurs[self.couleur]

    def __lt__(self, other):
    # teste si self est strictement inférieur à other
        if self.valeur < other.valeur:
            return True
        elif self.valeur > other.valeur:
            return False
        else :
            if self.couleur < other.couleur:
                return True
            else:
                return False


class Paquet:
    """Initialise un paquet puis définit les méthodes pour le manipuler"""

    def __init__(self):
        self.cartes = []
        for couleur in range(4):
            for valeur in range(2, 15):
                carte = Carte(couleur, valeur)
                self.cartes.append(carte)

    def __str__(self):
            res = []
            for carte in self.cartes:
                res.append(str(carte))
            return ', '.join(res)

    def ajouter_carte(self, carte):
        self.cartes.append(carte)

    def battre(self):
        random.shuffle(self.cartes)

    def distribuer_cartes(self, main, nombre):
        for i in range(nombre):
            main.ajouter_carte(self.cartes.pop())



class Main(Paquet):
    """Représente une main au jeu de cartes."""

    def __init__(self, etiquette = '',changement=0):
        self.cartes = []
        self.etiquette = etiquette
        self.changement = changement

    def tri(self):
        self.cartes.sort()

    def famille(self):
        listeValeurs=[carte.valeur for carte in self.cartes]
        bilan=[]
        for i in range(2,15):
            nb=listeValeurs.count(i)
            if nb>=2:
                bilan.append(nb)
        if len(bilan)==0:
            return 0
        else:
            if max(bilan)==4:           #carré
                return 7
            elif max(bilan)==3:
                if len(bilan)==2:       #full
                    return 5
                else:
                    return 3            #brelan
            else:                       # ici le max de bilan est 2
                if len(bilan)==2:       #double paire
                    return 2
                else:
                    return 1            #paire


    def quinte(self):
        self.tri()
        listeValeurs=[carte.valeur for carte in self.cartes]
        if listeValeurs[0]==14:
            listeValeurs[0]==1
        bilan=True
        i=0
        while bilan and i<len(listeValeurs)-1:
            if listeValeurs[i+1]!=listeValeurs[i]+1:
                bilan=False
            i=i+1
        if bilan==True:
            return 4
        else:
            return 0


    def couleur(self):
        listeCouleurs=[carte.couleur for carte in self.cartes]
        if listeCouleurs.count(listeCouleurs[0])==len(listeCouleurs):
            return 5
        else:
            return 0

    def quinteFlush(self):
        if self.quinte()==4 and self.couleur()==5:
            return 8
        else:
            return 0

    def score(self):
        return max([self.famille(),self.quinte(),self.couleur(),self.quinteFlush()])

    def __lt__(self, other):
    # teste si self est strictement inférieur à other
        return self.score() < other.score()
    def change_cartes(self, carte,indice):
        if self.changement <3:
            self.cartes.insert(indice,paquet.cartes[-1])
            paquet.cartes.pop(-1)
            paquet.ajouter_carte(self.cartes[indice+1])
            self.cartes.pop(indice+1)
            self.changement += 1
            print(self.changement)
        else :
            return "Vous avez deja effectué 3 changement"






def partie(main1,main2):
    """Compare deux mains et retourne un vainqueur"""
    if main2>main1:
        return main1.etiquette+" l'emporte avec "+str(main2.score())+ " points contre "+str(main1.score())
    elif main1>main2:
        return main2.etiquette+" l'emporte avec "+str(main1.score())+ " points contre "+str(main2.score())
    else :
        return "   égalité avec un score de "+str(main1.score())+" points"


"""Initialisation du jeu"""

paquet =Paquet()
paquet.battre()

main1=Main('Joueur 1')
main2=Main('Joueur 2')

paquet.distribuer_cartes(main1, 5)
paquet.distribuer_cartes(main2, 5)

main1.tri()
main2.tri()

""" Tkinter/PIL """
# La fenetre
root = Tk()
root.geometry('1920x1080')
root.title('Projet N°1 : Jeu de Poker avec changement de carte')
root.iconbitmap("Images/icone.ico")


#Fond d'ecran
global fond_ecran
fond_ecran = Canvas(root,width=1920,height=1080)
img = ImageTk.PhotoImage(Image.open("Images/Fond_Poker4K.jpg"))
fond_ecran.create_image(0,0,image=img,anchor="nw")
fond_ecran.pack()

#Titres
fond_ecran.create_text(945,60,text="Jeu de poker :",font=("Helvetica",50),fill="white")
joueur1 = fond_ecran.create_text(120,130,text="Joueur 1:",font=("Helvetica",35),fill="White")
joueur2 = fond_ecran.create_text(120,550,text="Joueur 2:",font=("Helvetica",35),fill="White")

# Fonction changement de carte
def desactiver(n):
    if n >= 6:
        main2.change_cartes(main2.cartes[n - 6], n - 6)
    else:
        main1.change_cartes(main1.cartes[n - 1], n - 1)
    changement[n - 1] = True
    if n == 1:
        changer['state'] = DISABLED
        global nvcarte
        nvcarte = ImageTk.PhotoImage(main1.cartes[0].img)
        fond_ecran.itemconfigure(af_carte,image=nvcarte)
    elif n == 2:
        changer2['state'] = DISABLED
        global nvcarte2
        nvcarte2 = ImageTk.PhotoImage(main1.cartes[1].img)
        fond_ecran.itemconfigure(af_carte2,image=nvcarte2)
    elif n == 3:
        changer3['state'] = DISABLED
        global nvcarte3
        nvcarte3 = ImageTk.PhotoImage(main1.cartes[2].img)
        fond_ecran.itemconfigure(af_carte3,image=nvcarte3)
    elif n == 4:
        changer4['state'] = DISABLED
        global nvcarte4
        nvcarte4 = ImageTk.PhotoImage(main1.cartes[3].img)
        fond_ecran.itemconfigure(af_carte4,image=nvcarte4)
    elif n == 5:
        changer5['state'] = DISABLED
        global nvcarte5
        nvcarte5 = ImageTk.PhotoImage(main1.cartes[4].img)
        fond_ecran.itemconfigure(af_carte5,image=nvcarte5)
    elif n == 6:
        changer6['state'] = DISABLED
        global nvcarte6
        nvcarte6 = ImageTk.PhotoImage(main2.cartes[0].img)
        fond_ecran.itemconfigure(af_carte6,image=nvcarte6)
    elif n == 7:
        changer7['state'] = DISABLED
        global nvcarte7
        nvcarte7 = ImageTk.PhotoImage(main2.cartes[1].img)
        fond_ecran.itemconfigure(af_carte7,image=nvcarte7)
    elif n == 8:
        changer8['state'] = DISABLED
        global nvcarte8
        nvcarte8 = ImageTk.PhotoImage(main2.cartes[2].img)
        fond_ecran.itemconfigure(af_carte8,image=nvcarte8)
    elif n == 9:
        changer9['state'] = DISABLED
        global nvcarte9
        nvcarte9 = ImageTk.PhotoImage(main2.cartes[3].img)
        fond_ecran.itemconfigure(af_carte9,image=nvcarte9)
    elif n == 10:
        changer10['state'] = DISABLED
        global nvcarte10
        nvcarte10 = ImageTk.PhotoImage(main2.cartes[4].img)
        fond_ecran.itemconfigure(af_carte10,image=nvcarte10)
    if main2.changement>=3:
        changer6['state'] = DISABLED
        changer7['state'] = DISABLED
        changer8['state'] = DISABLED
        changer9['state'] = DISABLED
        changer10['state']= DISABLED
    elif main1.changement>=3 and n<6:
        changer['state']  = DISABLED
        changer2['state'] = DISABLED
        changer3['state'] = DISABLED
        changer4['state'] = DISABLED
        changer5['state'] = DISABLED


'''Main1 : '''
global changement
changement = [False for i in range(10)]

#Carte1
print(main1)
carte = ImageTk.PhotoImage(main1.cartes[0].img)
af_carte = fond_ecran.create_image(150,200,image=carte,anchor="nw")
global changer
changer = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(1))
changer.place(x=154,y=420)


#Carte2
carte2 = ImageTk.PhotoImage(main1.cartes[1].img)
af_carte2 = fond_ecran.create_image(504,200,image=carte2,anchor="nw")
global changer2
changer2 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(2))
changer2.place(x=510,y=420)

#Carte3
carte3 = ImageTk.PhotoImage(main1.cartes[2].img)
af_carte3= fond_ecran.create_image(858,200,image=carte3,anchor="nw")
global changer3
changer3= Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(3))
changer3.place(x=866,y=420)

#Carte4
carte4 = ImageTk.PhotoImage(main1.cartes[3].img)
af_carte4 = fond_ecran.create_image(1212,200,image=carte4,anchor="nw")
global changer4
changer4 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(4))
changer4.place(x=1220,y=420)

#Carte5
carte5 = ImageTk.PhotoImage(main1.cartes[4].img)
af_carte5 = fond_ecran.create_image(1566,200,image=carte5,anchor="nw")
global changer5
changer5 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(5))
changer5.place(x=1574,y=420)

'''Main2 : '''

#Carte1
carte6 = ImageTk.PhotoImage(main2.cartes[0].img)
af_carte6 = fond_ecran.create_image(150,700,image=carte6,anchor="nw")
global changer6
changer6 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(6))
changer6.place(x=156,y=920)

#Carte2
carte7 = ImageTk.PhotoImage(main2.cartes[1].img)
af_carte7 = fond_ecran.create_image(504,700,image=carte7,anchor="nw")
global changer7
changer7 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(7))
changer7.place(x=510,y=920)

#Carte3
carte8 = ImageTk.PhotoImage(main2.cartes[2].img)
af_carte8 = fond_ecran.create_image(858,700,image=carte8,anchor="nw")
global changer8
changer8 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(8))
changer8.place(x=866,y=920)

#Carte4
carte9 = ImageTk.PhotoImage(main2.cartes[3].img)
af_carte9 = fond_ecran.create_image(1212,700,image=carte9,anchor="nw")
global changer9
changer9 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(9))
changer9.place(x=1220,y=920)
#Carte5
carte10 = ImageTk.PhotoImage(main2.cartes[4].img)
af_carte10 = fond_ecran.create_image(1566,700,image=carte10,anchor="nw")
global changer10
print(main2)
changer10 = Button(root,text="Changer",padx=40,pady=5,command = lambda :desactiver(10))
changer10.place(x=1574,y=920)

#Fonction qui lance la partie
def lancer_le_jeu():
    fond_ecran.delete(af_carte,af_carte2,af_carte3,af_carte4,af_carte5,af_carte6,af_carte7,af_carte8,af_carte9,af_carte10,joueur1,joueur2)
    changer.destroy()
    changer2.destroy()
    changer3.destroy()
    changer4.destroy()
    changer5.destroy()
    changer6.destroy()
    changer7.destroy()
    changer8.destroy()
    changer9.destroy()
    changer10.destroy()
    fin_jeu.destroy()
   # if artie(main1,main2)[]
    fond_ecran.create_text(900,540,text=partie(main1,main2),font=("Helvetica",50),fill="white")
#Boutton de fin de jeu

fin_jeu = Button(root,text="Lancer la partie",padx = 60,pady=10,command=lancer_le_jeu)
fin_jeu.place(x=830,y=540)



#Boucle principale qui rafraichis les images
root.mainloop()

