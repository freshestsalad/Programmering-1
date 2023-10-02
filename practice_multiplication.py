import random

score = 0
n1 = 0
n2 = 0

def correctMsg():
    print("Perfekt! ")
def wrongMsg(n1, n2):
    print("Fel svar, ", str(n1), " * ", str(n2), " är ", str(n1*n2) + "\n")

print("*" * 30 + "\n" + "Träna multiplikationstabeller" + "\n" + "*" * 30)

while True:
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

while True:
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

if difficulty == 1:
    for i in range(1, questionLimit+1):
        n1 = random.randint(1, 11)
        n2 = random.randint(1, 11)
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
elif difficulty == 2:
    for i in range(1, questionLimit+1):
        n1 = random.randint(11, 21)
        n2 = random.randint(1, 11)
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
elif difficulty == 3:
    for i in range(1, questionLimit+1):
        n1 = random.randint(11, 21)
        n2 = random.randint(11, 21)
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

print("Du svarade rätt på " + str(score) + " av " + str(questionLimit) + " frågor")
print("Ditt vitsord är " + str((score*100)//questionLimit) + "%")
