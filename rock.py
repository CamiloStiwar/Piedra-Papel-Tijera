
import random

def machineSelection():
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        return "R"  
    elif randomNumber == 2:
        return "P"  
    elif randomNumber == 3:
        return "S"  

def evaluateRockPaperScissors(machine, user):
    if machine == user:
        return "Empate"
        
    if machine == "R" and user == "S":
        return "machine"
    
    elif user == "R" and machine == "S":
         return "user"
    
    if machine == "R" and user == "P":
        return "user"
    
    elif user == "R" and machine == "P":
        return "machine"
    
    if machine == "P" and user == "S":
        return "user"
    
    elif user == "P" and machine == "S":
        return "machine"

def playRockPaperScissors():
    contMachine = 0
    contUser = 0
    
    while contMachine<2 and contUser<2:

        machine = machineSelection()
        
        
        user = input("Por favor digite su selección (R,P,S): ")
        
        result = evaluateRockPaperScissors (machine, user)

        if result == "machine":
            contMachine = contMachine + 1
            print("La maquina gana")
        
        elif result == "user":
            contUser = contUser + 1
            print("El usuario gana")

        else:
            print("Empate")
        print("usr",contUser)
        print("machine",contMachine)
    
    if contMachine == 2:
        return "machine"
    elif contUser == 2:
        return "user"

winner = playRockPaperScissors()
print("El ganador definitivo es: ", winner)
