#(ord('A') return 65
#(chr(90) return Z

repeat = True

def cryptMessage():
    newMessage = ""
    oldMessage = input("Meddelandet du vill kryptera: " + "\n")
    while True:
        try:
            key = ord(input("Ange nyckeln: " + "\n"))
        except TypeError:
            print("Nyckeln bör vara 1 tecken!" + "\n")
            continue
        else:
            break

    for oldCharacter in oldMessage:
        if oldCharacter.isupper():
            newCharacter = chr((ord(oldCharacter) + key - 65) % 26 + 65)
        elif oldCharacter.islower():
            newCharacter = chr((ord(oldCharacter) + key - 97) % 26 + 97)
        newMessage += newCharacter
    print(newMessage)

def decryptMessage():
    oldMessage = ""
    newMessage = input("Meddelandet du vill dekryptera: " + "\n")
    while True:
        try:
            key = ord(input("Ange nyckeln: " + "\n"))
        except TypeError:
            print("Nyckeln bör vara 1 tecken!" + "\n")
            continue
        else:
            break
        
    for newCharacter in newMessage:
        if newCharacter.isupper():
            oldCharacter = chr((ord(newCharacter) - key - 65) % 26 + 65)
        elif newCharacter.islower():
            oldCharacter = chr((ord(newCharacter) - key - 97) % 26 + 97)
        oldMessage += oldCharacter
    print(oldMessage)

while repeat:
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
    
    if chooseTask == 1:
        cryptMessage()
    elif chooseTask == 2:
        decryptMessage()

    repeatEnd = input('Skriv "sluta" för att sluta' + "\n")    #Frågar användaren ifall hen vill sluta spelet
    if repeatEnd.lower() == "sluta":                     #Inputen "Sluta" (oberoende av kapitalisering) stoppar "while repeat" loopen
        repeat = False
