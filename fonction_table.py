#def table_multiplication(): //sans paramètres
#def table_multiplication(n): //misy paramètres
def table_multiplication(n,max): #afaka asiana valeur par défaut le max, @ zay tsy voatery manoratra ny valeur ny max
    """Fonction affichant la table de multiplication par nb
de 1*nb à max*nb
(max >= 0)"""
    #n=int(input("Entrez une table: ")) //sans paramètres
    i=0
    #while i<10: //rah 10 no max (prédéfinie)
    while i<max: #max toujours positif au risque d'une bloucle infinie
        print(n,"*",i,"=",n*i)
        i+=1


#print(table_multiplication) sa? Tsy aiko ny mirunner azy @ le def