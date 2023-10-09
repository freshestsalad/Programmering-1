import random

#(ord('A') return 65
#(chr(90) return Z



while True:
        try:
            chooseTask = int(input("Vad vill du göra?" + "\n" + "1: Kryptera ett meddelande" + "\n" + "2: Dekryptera ett meddelande" + "\n"))
        except ValueError:
            print("Välj 1, 2" + "\n")
            continue
        if chooseTask < 1 or chooseTask > 2:
            print("Välj 1 eller 2" + "\n")
            continue
        else:
            break

def cryptMessage():
    newMessage = ""
    oldMessage = input("Meddelandet du vill kryptera: " + "\n")
    key = input("Ange nyckeln: " + "\n")

    for oldCharacter in oldMessage:
        if oldCharacter.isupper():
            newCharacter = chr((ord(oldCharacter) + ord(key) - 65) % 26 + 65)
        elif oldCharacter.islower():
            newCharacter = chr((ord(oldCharacter) + ord(key) - 97) % 26 + 97)
        newMessage += newCharacter
    print(newMessage)

def decryptMessage():
    oldMessage = ""
    newMessage = input("Meddelandet du vill dekryptera: " + "\n")
    key = input("Ange nyckeln: " + "\n")

    for newCharacter in newMessage:
        if newCharacter.isupper():
            oldCharacter = chr((ord(newCharacter) - ord(key) - 65) % 26 + 65)
        elif newCharacter.islower():
            oldCharacter = chr((ord(newCharacter) - ord(key) - 97) % 26 + 97)
        oldMessage += oldCharacter
    print(oldMessage)

cryptMessage()
decryptMessage()
