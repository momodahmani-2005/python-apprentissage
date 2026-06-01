montant=float(input("Quel est prix de la facture: "))
pourcentage=int(input("Quel pourcentage souhaitez-vous mettre sur votre facture: "))
nb_personne=int(input("Combien de personne etes-vous pour diviser la facture: "))
pourboire=round(montant*pourcentage/100,2)
total=round(montant+pourboire,2)
part=round(total/nb_personne,2)


print("====Montant de la facture====")
print(f"Montant de la facture:{montant} ")
print(f"Le montant du pourboire est de: {pourboire}")
print(f"Le total est de: {total}")
print(f"Chaque personne payera: {part}")





