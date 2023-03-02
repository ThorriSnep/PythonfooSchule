import random as rand

print("Willkommen zum Zahlenraten.\n\n")
obergrenze = int(input("Rate eine Zahl zwischen 1 und "))
versuche = 0
zufallszahl = rand.randint(1, obergrenze)
while 1:
    versuche += 1
    eingabe = input("Derin Versuch: ")
    if eingabe == "ende":
        print("Auf wiedersehen!\n")
        break
    elif int(eingabe) == zufallszahl:
        print("Woop woop, deine Zahl war: {} und du hast {} versuch(e) gebraucht.\n".format(zufallszahl, versuche))
        break
    elif int(eingabe) > zufallszahl:
        print("Dein versuch war größer\n")
    elif int(eingabe) < zufallszahl:
        print("Dein versuch war kleiner\n")
    else:
        raise Exception("unreachable") 
