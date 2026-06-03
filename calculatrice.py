nb1=int(input("Entrez un nombre: "))
op=(input("Entrez l'opération: "))
nb2=int(input("Entrez un deuxième nombre: "))

if op=="+":
    print(nb1+nb2)
elif op=="-":
    print(nb1-nb2)
elif op=="*":
    print(nb1*nb2)
elif op=="/":
    if nb2==0:
        print("erreur")
    else:
        print(nb1/nb2)
else:
    print("opération invalide")