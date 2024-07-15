''' design application 
resu
123*
456-
789+
0,/=
dele
(4 colonnes)
'''

from tkinter import *

expression=""

def appuyer(touche):
    if touche=="=":
        calculer()
        return
    global expression
    expression+=str(touche)
    equation.set(expression)
def calculer():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=total
    except:
        equation.set("erreur")
        expression=""
def effacer():
    global expression
    expression=""
    equation.set("")


interface = Tk()
    #couleur de fond
interface.configure(background="#1f1f1f")
    
    #titre application
interface.title("Calculatrice")
    
    #Taille de la fenêtre
interface.geometry("250x400")
    
    #variable pour stocker le contenu actuel
equation=StringVar()
    
    #Boîte de résultats
resultat=Label(interface,bg="#1f1f1f",fg="#fff", textvariable=equation, heigh="2")
resultat.grid(columnspan=4)
    
    #boutons
boutons = [7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","="]
    
ligne = 1
colonne = 0
    
for bouton in boutons:
    b = Label(interface, text=str(bouton), bg="#368f5e", fg="#fff", height=4, width=6)
        #rendre le texte cliquable
    b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))        
    b.grid(row=ligne, column=colonne)
    colonne+=1
    if colonne==4:
        colonne=0
        ligne+=1
b = Label(interface, text="c", bg="#368f5e", fg="#ff6262", height=4, width=26)
b.bind("<Button-1>", lambda e: effacer())
b.grid(columnspan=4)
interface.mainloop()