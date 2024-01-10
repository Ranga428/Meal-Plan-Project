import random
import MealSets
import Design
import os
import time

def RandomNumbers():
    MealSet = [MealSets.A, MealSets.B, MealSets.C, MealSets.D, 
           MealSets.E, MealSets.F, MealSets.G]
    print("----------------------------------------------------------------------")
    num = 1
    for i in range(4):
        RandomNum= MealSet[(random.randint(0, 6))]
        print("Week ",num + i)
        print(RandomNum)
        print("----------------------------------------------------------------------")

def SubMain1():
        Choice = input("Would you like to plan your meals?(Y/N): ")
        Choice1=Choice.lower()
        if Choice1 == 'y':
            RandomNumbers()
        elif Choice1 == 'n':
            print(Design.GB)
            time.sleep(1.5)
            os.system('cls')  
            exit()
        else:
            print("error")
            SubMain1()
            
def SubMain2():
        Choice = input("Would you like to re-plan your meals?(Y/N): ")
        Choice1=Choice.lower()
        if Choice1 == 'y':
            Main()
        elif Choice1 == 'n':
            print(Design.GB)
            time.sleep(1.5)
            os.system('cls')  
            exit()
        else:
            print("error")
            SubMain2()
            
def Main():
    SubMain1()  
    SubMain2()

Main()
