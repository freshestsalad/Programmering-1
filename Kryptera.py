#(ord('A') return 65
#(chr(90) return Z

repeat = True                                                      #Booleiska variabeln repeat (True), som kör en loop tills False

def cryptMessage():                                                #Definierar funktionen cryptMessage()
    newMessage = ""                                                #Tom sträng
    oldMessage = input("Meddelandet du vill kryptera: " + "\n")    #Ber användaren mata in strängen hen vill kryptera
    while True:
        try:
            key = ord(input("Ange nyckeln: " + "\n"))              #Ber användaren mata in nyckeln och ändrar den till heltalet som representerar Unicode charactern
        except TypeError:
            print("Nyckeln bör vara 1 tecken!" + "\n")             #Ber användaren ange endast ett tecken
            continue
        else:
            break
            
    for oldCharacter in oldMessage:                                #Loop som går igenom varje tecken i meddelandet
        if oldCharacter.isupper():
            newCharacter = chr((ord(oldCharacter) + key - 65) % 26 + 65)        #Värdet på nya tecknet i meddelandet (stor bokstav)
        elif oldCharacter.islower():
            newCharacter = chr((ord(oldCharacter) + key - 97) % 26 + 97)        #Värdet på nya tecknet i meddelandet (liten bokstav)
        else:
            newCharacter = oldCharacter                                         #Tecken som inte är bokstäver hålls samma
        newMessage += newCharacter                                              #Lägger nya tecknena i en tom sträng
    print(newMessage)                                                           #Skriver ut nya meddelandet

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
        
    for newCharacter in newMessage:                                #Loop som går igenom varje tecken i meddelandet
        if newCharacter.isupper():
            oldCharacter = chr((ord(newCharacter) - key - 65) % 26 + 65)        #Värdet på nya tecknet i meddelandet (stor bokstav)
        elif newCharacter.islower():
            oldCharacter = chr((ord(newCharacter) - key - 97) % 26 + 97)        #Värdet på nya tecknet i meddelandet (liten bokstav)
        else:
            newCharacter = oldCharacter                                         #Tecken som inte är bokstäver hålls samma
        oldMessage += oldCharacter                                              #Lägger nya tecknena i en tom sträng
    print(oldMessage)                                                           #Skriver ut nya meddelandet

while repeat:                                #Loop som repeterar tills användaren vill stänga programmet
    while True:
        try:
            chooseTask = int(input("Vad vill du göra?" + "\n" + "1: Kryptera ett meddelande" + "\n" + "2: Dekryptera ett meddelande" + "\n"))        #Frågar användaren mata in vad hen vill göra
        except ValueError:
            print("Välj 1, 2" + "\n")        #Användaren måste mata in 1 eller 2, annars ValueError
            continue
        if chooseTask < 1 or chooseTask > 2:            #Tvingar användaren mata in 1 eller 2, inte högre inte lägre
            print("Välj 1 eller 2" + "\n")
            continue
        else:
            break
    
    if chooseTask == 1:                      #Kör cryptMessage() om användaren matade in 1 vid chooseTask
        cryptMessage()
    elif chooseTask == 2:
        decryptMessage()                     #Kör decryptMessage() om användaren matade in 2 vid chooseTask

    repeatEnd = input('Skriv "sluta" för att sluta' + "\n")    #Frågar användaren ifall hen vill sluta spelet
    if repeatEnd.lower() == "sluta":                     #Inputen "Sluta" (oberoende av kapitalisering) stoppar "while repeat" loopen
        repeat = False                                   #repeat intar värdet False, vilket bryter "while repeat"-loopen
