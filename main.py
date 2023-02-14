#!/usr/bin/env python3

import csv
import re

#Demande les lettres à l'utilisateur, vérifie que les données sont bonnes

correct = 0 
while True :
    lettres = input("Quels sont vos 7 lettres ? (Veuillez séparer chaque lettre par un espace)\nSi vous voulez sortir du programme, entrez «Q»\n")
    if lettres == 'q' or lettres == 'Q':
        exit()
    lettres = lettres.strip()
    if all(x.isalpha() or x.isspace() for x in lettres) == False:
        print("Erreur : vous devez entrer des lettres\n")
        continue
    liste = lettres.split()
    if len(liste) != 7 :
        print("Erreur : veuillez entrer 7 lettres, séparés par un espace chacun\n")
        continue
    for a in liste:
        if len(a) == 1 :
            correct = 1 
        else : 
            print("Erreur : veuillez n'entrer qu'une lettre à la fois, et séparez chaque lettre par un espace")
            break 
    if correct == 1 :
        break
    else :
        continue

#Demande les lettres déjà sur le jeu, qui peuvent servir

correct = 0
while True :
    débutfin = input("Repérez, sur le jeu, des lettres déjà posés qui peuvent être utlisés pour former un mot \n(Veuillez séparer chaque lettre par un espace)\n")
    débutfin = débutfin.strip()
    if all(x.isalpha() or x.isspace() for x in débutfin) == False:
        print("Erreur : vous devez entrer des lettres\n")
        continue
    liste2 = débutfin.split()
    for a in liste2:
        if len(a) == 1 :
            correct = 1 
        else : 
            print("Erreur : veuillez n'entrer qu'une lettre à la fois, et séparez chaque lettre par un espace")
            break
    if len(liste2) > 7 :
        liste2 = liste2[0:6]
    if correct == 1 :
        break
    else :
        continue
        
#Crée la re

reg = "[" + liste[0] + liste [1] + liste[2] + liste [3] + liste[4] + liste [5] + liste[6] + "]"

#Parcours toutes les options possibles

with open("dbpurifié.txt", "r", encoding="utf-8") as file :

    lecture = csv.reader(file, delimiter="\t", quotechar='"')
    
