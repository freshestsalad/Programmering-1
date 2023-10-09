import random

repeat = True

def correctMsg():                           #Printar vid ett rätt svar
    print("Perfekt! ")
def wrongMsg(n1, n2):                       #Printar vid ett fel svar och berättar rätt svar
    print("Fel svar, " + str(n1) + " * " + str(n2) + " är " + str(n1*n2) + "\n")

def practiceMult(difficulty, questionLimit):    #Definierar funktionen practiceMult
    score = 0                                   #Ger värde åt poängena för hur många rätt svar användaren gett
    for i in range(1, questionLimit + 1):
        if difficulty == 1:                     #Ger värde åt talena som ska multipliceras vid svårighetsgrad 1
            n1 = random.randint(1, 11)          
            n2 = random.randint(1, 11)
        elif difficulty == 2:                   #Ger värde åt talena som ska multipliceras vid svårighetsgrad 2
            n1 = random.randint(11, 21)          
            n2 = random.randint(1, 11)
        elif difficulty == 3:                   #Ger värde åt talena som ska multipliceras vid svårighetsgrad 3
            n1 = random.randint(11, 21)          
            n2 = random.randint(11, 21)
        while True:                         #While-loop som ber användaren ange ett heltal som multiplikationssvar och kollar om svaret är korrekt
            try: 
                answer = int(input("\n" + "Vad är " + str(n1) + " * " + str(n2) + "?" + "\n"))
            except:
                print("Ange ett heltal!")
            else:
                break
        if answer == n1 * n2:               #Om svaret var rätt
                score += 1                      #Räknar hur många rätt svar användaren gett
                correctMsg()
                print("Du har svarat rätt på " + str(score) + " fårgor!" + "\n")
        else:                               #Om svaret var fel
                wrongMsg(n1, n2)

    print("Du svarade rätt på " + str(score) + " av " + str(questionLimit) + " frågor")             #Anger hur många frågor av mängden frågor användaren fått rätt
    print("Ditt vitsord är " + str((score*100)//questionLimit) + "%" + "\n")                        #Ger användaren ett vitsord som ett heltal i procent
    
while repeat:                                                                                 #While loop som kör spelet tills man skriver "sluta"
    print("*" * 30 + "\n" + "Träna multiplikationstabeller" + "\n" + "*" * 30)                #Estetik: titel

    while True:                                 #Definierar en variabel som styr svårighetsgraden (Tvingar användaren välja ett heltal)
        try:
            difficulty = int(input("Välj svårighetsgrad" + "\n" + "1: Lätt" + "\n" + "2: Medel" + "\n" + "3: Svår" + "\n"))
        except ValueError:
            print("Välj 1, 2 eller 3" + "\n")
            continue
        if difficulty < 1 or difficulty > 3:
            print("Välj 1, 2 eller 3" + "\n")
            continue
        else:
            break
    while True:                                 #Definierar en variabel som styr mängden av frågor (Tvingar användaren välja ett heltal)
        try:
            questionLimit = int(input("\n" + "Hur många frågor?" + "\n"))
        except ValueError:
            print("Ange ett heltal!" + "\n")
            continue
        if questionLimit < 1:
            print("Välj minst 1 fråga!" + "\n")
            continue
        else:
            break
    
    practiceMult(difficulty, questionLimit)        #Anropar multiplikationsspelet
    
    repeatEnd = input('Skriv "sluta" för att sluta' + "\n")    #Frågar användaren ifall hen vill sluta spelet
    if repeatEnd.lower() == "sluta":                     #Inputen "Sluta" (oberoende av kapitalisering) stoppar "while repeat" loopen
        repeat = False
