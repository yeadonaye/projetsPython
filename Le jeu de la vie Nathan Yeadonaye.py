from tkinter import*
import copy
import tkinter as tk
import time
#
#
n=100  # nombre de cases (verticalement)
p=150  # nombre de cases (horizontalement)
e=25  # aire d'une cellule
tab=[[0 for i in range(p)]for j in range(n)] # Une liste composée de sous listes remplient de 0 si la case n'est pas en vie et 1 si elle est vivante

#
#
def afficher_ligne(tab):    # Cette fonction crée des cases rouges si la cases est vivante et une cases verte si elle n'est pas en vie
    y1=0
    y2=e
    for j in range(n):
        for i in range(p):
            x1=i*e
            x2=x1+e
            if tab[j][i]==1:
                canvas.create_rectangle(x1,y1,x2,y2,width=1,fill='red')
            else:
                canvas.create_rectangle(x1,y1,x2,y2,width=1,fill='green')
        y1+=e
        y2+=e
#
#
def nombre_voisins(i,j,tab):
    col=len(tab[i])-1
    lign=len(tab)-1
    a=0
#center
    if (i!= lign and i!=0) and (j!= col and j!=0): # cette condition calcule le nombre de voisins qui lui entoure quand elle est entourée de 8 cases ( elle au "millieu")
        for d in range(i-1,i+2):
            for f in range(j-1,j+2):
                if d!= i or f!=j:
                    if tab[d][f]==1:
                        a+=1
        return a
#corner
    elif i==0 and j==0:         # Ces 4 conditions font la meme chose mais pour les cases au coin.
        for di in range(i+2):
            for fi in range(j+2):
                if di!= i or fi!=j:
                    if tab[di][fi]==1:
                        a+=1
        return a            
    elif i==0 and j==col:
        for dd in range(i+2):
            for ff in range(j-1,j+1):
                if dd!= i or ff!=j:
                    if tab[dd][ff]==1:
                        a+=1
        return a     
    elif i==lign and j==col:
        for df in range(i-1,i+1):
            for fd in range(j-1,j+1):
                if df!= i or fd!=j:
                    if tab[df][fd]==1:
                        a+=1
        return a 
    elif i==lign and j==0:
        for dfd in range(i-1,i+1):
            for fdf in range(j+2):
                if dfd!= i or fdf!=j:
                    if tab[dfd][fdf]==1:
                        a+=1
        return a 
#les côtés        
    elif i == 0:    # Ces 4 elif font la meme chose mais pour les cases sur les côtés. 
        for fkf in range(i+2):
            for kfk in range(j-1,j+2):
                if fkf!= i or kfk!=j:
                    if tab[fkf][kfk]==1:
                        a+=1
        return a
    elif i == lign:
        for ddd in range(i-1,i+1):
            for fff in range(j-1,j+2):
                if ddd!= i or fff!=j:
                    if tab[ddd][fff]==1:
                        a+=1
        return a
    elif j == 0:
        for kkk in range(i-1,i+2):
            for eee in range(j+2):
                if kkk!= i or eee!=j:
                    if tab[kkk][eee]==1:
                        a+=1
        return a
    elif j == col:
        for zzz in range(i-1,i+2):
            for yyy in range(j-1,j+1):
                if zzz!= i or yyy!=j:
                    if tab[zzz][yyy]==1:
                        a+=1
        return a                               
#
#
def evolution(tab):           # Cette fonction change les 0 (mort) en 1 (vivant) ou le contraire en regardant le nombre de voisins ( si il y a une naissaice our si elle meurt par isolement ou surpopulation)
    tab2=copy.deepcopy(tab) #Vu qu'on ne peut pas directement changer le premier tableau, on a copier son contenue sur un autre
    for i in range(n):
        for j in range(p):
            if tab2[i][j]==0 and nombre_voisins(i,j,tab)==3: #
                tab2[i][j]=1
            elif tab2[i][j]==1:
                if nombre_voisins(i,j,tab)>3 or nombre_voisins(i,j,tab)<2:
                    tab2[i][j]=0
    canvas.delete('all') # ici on efface le tableau pour rendre l'execution plus rapide ( car sa evite les cases qui se colorient plusieurs fois)
    return tab2
#
#
def joue(): #Cette fonction affiche l'etat des cellules au jour n+1
    global tab, generation  #Global dit a python que tab et generation est le meme partout dans le code
    tab = evolution(tab) # on copie le tableau qu'on a modifier dans l'ancien tableau
    afficher_ligne(tab) # Ensuite en l'affiche
    return
    


    
#
#
def planneur():   # Cette fonction dessine un planeur
    tab[1][2]=1
    tab[2][3]=1
    tab[3][1]=1
    tab[3][2]=1
    tab[3][3]=1
    afficher_ligne(tab) # Ensuite en l'affiche 
#
#
def oiseau():     #Cette fonction dessine un oiseau
    tab[3][3]=1
    tab[5][3]=1
    tab[2][4]=1
    tab[2][5]=1
    tab[2][6]=1
    tab[2][7]=1
    tab[2][8]=1
    tab[2][9]=1
    tab[3][9]=1
    tab[4][9]=1
    tab[5][8]=1
    tab[6][5]=1
    tab[6][6]=1
    afficher_ligne(tab) # Ensuite en l'affiche 
#
#
def canon_a_planneur(): # Cette fonction dessine le canon a planeur
    tab[15][5]=1
    tab[15][6]=1
    tab[16][5]=1
    tab[16][6]=1
    tab[15][15]=1
    tab[16][15]=1
    tab[14][15]=1
    tab[13][16]=1
    tab[17][16]=1
    tab[18][17]=1
    tab[18][18]=1
    tab[12][17]=1
    tab[12][18]=1
    tab[15][19]=1
    tab[13][20]=1
    tab[17][20]=1
    tab[14][21]=1
    tab[15][21]=1
    tab[16][21]=1
    tab[15][22]=1
    tab[16][25]=1
    tab[17][25]=1
    tab[18][25]=1
    tab[16][26]=1
    tab[17][26]=1
    tab[18][26]=1
    tab[15][27]=1
    tab[19][27]=1
    tab[15][29]=1
    tab[14][29]=1
    tab[19][29]=1
    tab[20][29]=1
    tab[17][39]=1
    tab[17][40]=1
    tab[18][39]=1
    tab[18][40]=1
    afficher_ligne(tab) # Ensuite en l'affiche 
#
#
def tab_vide():  #Cette fonction vide le tableau quand le boutton "Vider" est touché
    global tab  #Global dit a python que tab est le meme partout dans le code
    tab=[[0 for i in range(p)]for j in range(n)] # Creation d'une liste composée de 0 (cellule morte)
    afficher_ligne(tab) #L'affichage
#
#
def position(event): # Cette fonction permet de colorier les cases avec la sourie
    x=event.x//e #ici on calcule l' absisse de la case touché
    y=event.y//e # Meme chos pour les ordonnées
    if tab[y][x]==0:
        tab[y][x]=1
        canvas.create_rectangle(x*e,y*e,x*e+e,y*e+e, width=1, fill='red') # Cela colorie la cases si et seulemet si elle etait morte avant 
    elif tab[y][x]==1:
        tab[y][x]=0
        canvas.create_rectangle(x*e,y*e,x*e+e,y*e+e, width=1, fill='green') # ceci fait l'opposé
    return
#
#
def semaine():   #Cette fonction affiche l'etat des cellules une semaine plus tard (7 jours)
    global tab 
    for kkkkd in range(7):
            tab=evolution(tab)
            time.sleep(0.01)
            afficher_ligne(tab)
#
#
def bouton_zoom_in():
    global tab 
    zoom_in(tab) 
    return 
#
#
def zoom_in(tab):
    global e #Global dit a python que "e" est le meme partout dans le code
    e+=3
    canvas.delete('all')
    afficher_ligne(tab)
    canvas.bind("<Button-2>",zoom_in)
#
#
def zoom_out(tab):
    global e
    e-=3
    canvas.delete('all')
    afficher_ligne(tab)
    canvas.bind("<Button-2>",zoom_in) 
#
#
def bouton_zoom_out():
    global tab 
    zoom_out(tab) 
    return
#
#
root=Tk()
#
root.title('Nathan & Yeadonaye, le jeu de la vie')       # on donne un titre a la fenetre de tkinter
#
#
canvas=Canvas(root, width=600, height=800, background='black')
but_evoluer=Button(root, text="Jour suivant", command=joue)
but_planneur=Button(root, text="Planneur", command=planneur)
but_vider=Button(root, text='Vider', command=tab_vide)
but_oiseau=Button(root, text="Oiseau", command=oiseau)
but_canon=Button(root, text='Canon', command=canon_a_planneur)
but_semaine=Button(root, text='Semaine suivante', command=semaine)
bouton_zoom_in=Button(root, text="zoom-in", command=bouton_zoom_in)
bouton_zoom_out=Button(root, text="zoom-out", command=bouton_zoom_out)
quitter_bouton=Button(root, text="Quitter", command=root.destroy, bg='red') # le bouton quitter va apparaitre en rouge
#
#
canvas.bind("<Button-1>", position)
#
# on place tous les boutons, et on leur indique la place qu ils vont occuper
but_semaine.pack(side='right', fill='both')
bouton_zoom_out.pack(side='left', fill='both')
but_vider.pack(side='top', fill='both')
but_planneur.pack(side='bottom', fill='both')
but_evoluer.pack(side='right', fill='both')
bouton_zoom_in.pack(side='left', fill='both')
quitter_bouton.pack(side='top', fill='both')
but_oiseau.pack(side='bottom', fill='both')
but_canon.pack(side='bottom', fill='both')
#
#
canvas.pack(fill='both', expand=True)
afficher_ligne(tab)
root.mainloop()