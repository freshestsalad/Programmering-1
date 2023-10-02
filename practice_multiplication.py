import random

score = 0                                   #Definierar poängena för hur många rätt svar användaren gett
n1 = 0                                      #Definierar tal 1 som ska multipliceras
n2 = 0                                      #Definierar tal 2 som ska multipliceras

def correctMsg():                           #Printar vid ett rätt svar
    print("Perfekt! ")
def wrongMsg(n1, n2):                       #Printar vid ett fel svar och berättar rätt svar
    print("Fel svar, ", str(n1), " * ", str(n2), " är ", str(n1*n2) + "\n")

print("*" * 30 + "\n" + "Träna multiplikationstabeller" + "\n" + "*" * 30)

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

if difficulty == 1:                         #Om användaren valde svårighetsgrad 1
    for i in range(1, questionLimit+1):     #For-loop för mängden av frågor användaren valde
        n1 = random.randint(1, 11)          
        n2 = random.randint(1, 11)          #Talen som ska multipliceras väljs slumpmässigt mellan 1 och 10
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
            
elif difficulty == 2:                       #Om användaren valde svårighetsgrad 2 (Nästan exakt samma kod som i svårighetsgrad 1)
    for i in range(1, questionLimit+1):
        n1 = random.randint(11, 21)         
        n2 = random.randint(1, 11)          #Första talet som ska multipliceras väljs slumpmässigt mellan 11 och 20, andra numret mellan 1 och 10
        while True:
            try: 
                answer = int(input("\n" + "Vad är " + str(n1) + " * " + str(n2) + "?" + "\n"))
            except:
                print("Ange ett heltal!")
            else:
                break
        if answer == n1 * n2:
            score += 1
            correctMsg()
            print("Du har svarat rätt på " + str(score) + " fårgor!" + "\n")
        else:
            wrongMsg(n1, n2)
            
elif difficulty == 3:                       #Om användaren valde svårighetsgrad 3 (Nästan exakt samma kod som i svårighetsgrad 1)
    for i in range(1, questionLimit+1):
        n1 = random.randint(11, 21)
        n2 = random.randint(11, 21)         #Båda talen som ska multipliceras väljs slumpmässigt mellan talen 11 och 20
        while True:
            try: 
                answer = int(input("\n" + "Vad är " + str(n1) + " * " + str(n2) + "?" + "\n"))
            except:
                print("Ange ett heltal!")
            else:
                break
        if answer == n1 * n2:
            score += 1
            correctMsg()
            print("Du har svarat rätt på " + str(score) + " fårgor!" + "\n")
        else:
            wrongMsg(n1, n2)

print("Du svarade rätt på " + str(score) + " av " + str(questionLimit) + " frågor")             #Anger hur många frågor av mängden frågor användaren fått rätt
print("Ditt vitsord är " + str((score*100)//questionLimit) + "%")                               #Ger användaren ett vitsord som ett heltal i procent
