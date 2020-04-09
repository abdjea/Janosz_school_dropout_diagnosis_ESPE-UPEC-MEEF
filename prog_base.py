# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:16:52 2020

@author: abhis
"""


liste_etudiant=[]
for f in liste_etudiant:
    cnt=liste_etudiant.index(f)
    globals()["%s"%liste_etudiant[cnt]]={}

#####     ajout dynamique des étudiants #####
def ajout_etudiant():
    print("liste étudiant existante : "+str(liste_etudiant))
    tete = 0

    while str(tete) != "exit":
    
        tete = input('Entrez le nom de l étudiant : ')
        liste_etudiant.append(tete)
        globals()["%s"%liste_etudiant[len(liste_etudiant)-1]]={}
        
        if str(tete) == "exit":
            del liste_etudiant[len(liste_etudiant)-1]
        

    print("liste étudiant fianlisée : "+str(liste_etudiant))

#catégorie
discrets={"engagement":0,"reussite":1,"milieu_social":1}
inadaptés={"reussite":1,"comportement":1,"milieu_familial":1}
desengagés={"comportement":0,"reussite":0,"engagement":1}
sous_performants={"engagement":1,"comportement":0,"facilité":1}


liste_cat=["discrets","inadaptés","desengagés","sous_performants"]

#recuperer clé de tous les catégories ==> lsite_complet
total={}
total.update(discrets)
total.update(inadaptés)
total.update(desengagés)
total.update(sous_performants)

liste_complet=[k  for (k, val) in total.items()]

####### attribution dynamique  notation par éléve ###########

def notation_etudiant():


    
    
    #code d'affectation de notation pour chaque étudiant
    
    autori=[0,1,2,3]
    for k in liste_etudiant:
        print(k)
        
        count=liste_etudiant.index(k)
        globals()["%s"%liste_etudiant[count]]={}  
        
       # k={}
        for i in liste_complet:
            a = input('Entrez la donnée -'+str(i)+"- : ")
            while str(a) not in str(autori):
                print('valeur incorrect - recommencez ')
                a = input('Entrez la donnée à nouveau  -'+str(i)+"- : ")
    
            globals()["%s"%liste_etudiant[count]][str(i)]=int(a)
        print(globals()["%s"%liste_etudiant[count]])

####### Matching catégorie X eleve ###########
"""
discrets={"engagement":0,"reussite":1,"milieu_social":1}
inadaptés={"reussite":1,"comportement":1,"milieu_familial":1}
desengagés={"comportement":0,"reussite":0,"engagement":1}
sous_performants={"engagement":1,"comportement":0,"facilité":1}


liste_cat=["discrets","inadaptés","desengagés","sous_performants"]

#crtiète iolé
total={}
total.update(discrets)
total.update(inadaptés)
total.update(desengagés)
total.update(sous_performants)

liste_complet=[k  for (k, val) in total.items()]

"""
taille_stat=0
for u in liste_cat:
    taille_stat=taille_stat+len(eval(u))
"""
noah={"engagement":0,"reussite":0,"comportement":0,"milieu_familial":0,"facilité":0}
gabi={"engagement":1,"reussite":1,"comportement":1,"milieu_familial":1,"facilité":1,"milieu_social":1}

#taille_i=0
"""
def diagnostique_etudiant():

    stat=0
    for e in liste_etudiant:
        print("########## DIAGNOSTIQUE ############ - "+str(e)+"\n")
    
        for i in liste_cat:
            
            for r in eval(e):
                if r in eval(i):
        
                    if eval(i)[r] == eval(e)[r]:
                        stat+=1
    
            print("----- "+str(i)+" ----")
            print("taux de matching/correspondance à la typologie "+str(i)+" : "+str(stat/len(eval(i))))
            print("taux d'appartenance à "+str(i)+" sur l'ensemble des critères"+" : "+str(stat/len(liste_complet)))
            print("\n")
        
            stat=0
    #            print(r)
    #            print(len(i))
    #            print(i)
ajout_etudiant()
notation_etudiant()
diagnostique_etudiant()