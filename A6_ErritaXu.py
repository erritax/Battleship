# Errita Xu
# December 8, 2021
# A6 Functions
# To simulate battleship (computer vs. player) with strategy using functions

import random
import math

#printInstructions() - welcome player and print the instructions on how to play battleship
#@param: none
#@return: none
def printInstructions():
    
    #title
    print("Welcome to battleship!")
    print(" ")
    
    #basic rules
    print("Battleship is a game played by two players. Today, it will be I (computer) vs. you!")
    print("Each player will have separate boards with 4 ships. You get to plan your own ships.")
    print("To plan your own ships, the computer will prompt you to which ship you are to plan and the length of it.")
    print("You will need to input the direction you want the ship to face.")
    print("Player's will take turn to hit the other player's board by guessing a valid coordinate.")
    print("The objective of the game is to tank all of the opponent's ship.")
    print("If you make a hit, it is still your turn until your next miss.")
    print(" ")
    
    #show what symbols in the maps that will be printed later represent 
    print("Here are some key symbols you will be seeing:")
    print("    * represents a ship occupied in the coordinate")
    print("    o represents no status")
    print("    - represents a miss")
    print("    X represents a hit")
    print(" ")
    print("Good luck!")
    print(" ")
    print(" ")

#shipSet() - set the opponent's ship based on coordinate and direction (check for invalid input and overlaps)
#@param: usedCoordinates:str[], units:int
#@return: coordinates:str[]
def shipSet(usedCoordinates, units):
    
    valid = False
    
    while valid == False:
        
        #plot first coordinate
        first_coordinate = input("Where do you want your first coordinate?")
        
        #title the coordinate
        first_coordinate = first_coordinate.title()
    
        #make sure it is a valid coordinate and not already used
        while first_coordinate not in all_coordinates or first_coordinate in usedCoordinates:
            print("Invalid Coordinate!")
            first_coordinate = input("Where do you want your first coordinate?")
            first_coordinate = first_coordinate.title()
        
        #split the letter and number
        letter = first_coordinate[0]
        number = first_coordinate[1]
        
        #ask for direction of the ship
        direction = input("Which direction do you want the ship to face:")
        direction = direction.casefold()
        
        #manage invalid direction
        while direction not in directions:
            print("Invalid Input! Your choices are north, south, east, and west.")
            direction = input("Which direction do you want the ship to face:")
            direction = direction.casefold()
        
        #destroyer
        if units == 2:
            
            if direction == 'north':
                #invalid coordinate for direction
                if number == '6':
                    print("Invalid direction for coordinate. Try another one.")
                    continue
                
                #find column the first coordinate is in and generate second coordinate
                else:
                    if first_coordinate in columnOne:
                        index = columnOne.index(first_coordinate)
                        second_coordinate = columnOne[index+1]
                    
                    elif first_coordinate in columnTwo:
                        index = columnTwo.index(first_coordinate)
                        second_coordinate = columnTwo[index+1]
                    
                    elif first_coordinate in columnThree:
                        index = columnThree.index(first_coordinate)
                        second_coordinate = columnThree[index+1]
                    
                    elif first_coordinate in columnFour:
                        index = columnFour.index(first_coordinate)
                        second_coordinate = columnFour[index+1]
                    
                    elif first_coordinate in columnFive:
                        index = columnFive.index(first_coordinate)
                        second_coordinate = columnFive[index+1]
                    
                    elif first_coordinate in columnSix:
                        index = columnSix.index(first_coordinate)
                        second_coordinate = columnSix[index+1]
                
                #check if the second coordinate is already used
                if second_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
            
            
            elif direction == 'south':
                #invalid coordinate for direction
                if number == '1':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find column the first coordinate is in and generate second coordinate
                else:
                    if first_coordinate in columnOne:
                        index = columnOne.index(first_coordinate)
                        second_coordinate = columnOne[index-1]
                    
                    elif first_coordinate in columnTwo:
                        index = columnTwo.index(first_coordinate)
                        second_coordinate = columnTwo[index-1]
                    
                    elif first_coordinate in columnThree:
                        index = columnThree.index(first_coordinate)
                        second_coordinate = columnThree[index-1]
                    
                    elif first_coordinate in columnFour:
                        index = columnFour.index(first_coordinate)
                        second_coordinate = columnFour[index-1]
                    
                    elif first_coordinate in columnFive:
                        index = columnFive.index(first_coordinate)
                        second_coordinate = columnFive[index-1]
                    
                    elif first_coordinate in columnSix:
                        index = columnSix.index(first_coordinate)
                        second_coordinate = columnSix[index-1]
                        
                #check if the second coordinate isn't used already
                if second_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
            
            
            elif direction == 'east':    
                #invalid coordinates for direction
                if letter == 'F':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find column the first coordinate is in and generate second coordinate
                else:
                    if first_coordinate in rowOne:
                        index = rowOne.index(first_coordinate)
                        second_coordinate = rowOne[index+1]
                    
                    elif first_coordinate in rowTwo:
                        index = rowTwo.index(first_coordinate)
                        second_coordinate = rowTwo[index+1]
                    
                    elif first_coordinate in rowThree:
                        index = rowThree.index(first_coordinate)
                        second_coordinate = rowThree[index+1]
                    
                    elif first_coordinate in rowFour:
                        index = rowFour.index(first_coordinate)
                        second_coordinate = rowFour[index+1]
                    
                    elif first_coordinate in rowFive:
                        index = rowFive.index(first_coordinate)
                        second_coordinate = rowFive[index+1]
                    
                    elif first_coordinate in rowSix:
                        index = rowSix.index(first_coordinate)
                        second_coordinate = rowSix[index+1]
                
                #check if the second coordinate is already used
                if second_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
            
            
            elif direction == 'west':
                #invalid coordinates for direction
                if letter == 'A':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find row the first coordinate is in and generate second coordinate
                else:
                    if first_coordinate in rowOne:
                        index = rowOne.index(first_coordinate)
                        second_coordinate = rowOne[index-1]
                    
                    elif first_coordinate in rowTwo:
                        index = rowTwo.index(first_coordinate)
                        second_coordinate = rowTwo[index-1]
                    
                    elif first_coordinate in rowThree:
                        index = rowThree.index(first_coordinate)
                        second_coordinate = rowThree[index-1]
                    
                    elif first_coordinate in rowFour:
                        index = rowFour.index(first_coordinate)
                        second_coordinate = rowFour[index-1]
                    
                    elif first_coordinate in rowFive:
                        index = rowFive.index(first_coordinate)
                        second_coordinate = rowFive[index-1]
                    
                    elif first_coordinate in rowSix:
                        index = rowSix.index(first_coordinate)
                        second_coordinate = rowSix[index-1]
                
                #check if the second coordinate is already used
                if second_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
            
            #compile the generated coordinates into list, this will be returned
            coordinates = [first_coordinate, second_coordinate]        
        
        
        #submarine
        elif units == 3:
            
            if direction == 'north':
                #invalid coordinates for direction
                if number == '6' or number == '5':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find the column the first coordinate is on. Generate second and third coordinate based on direction
                else:
                    if first_coordinate in columnOne:
                        index = columnOne.index(first_coordinate)
                        second_coordinate = columnOne[index+1]
                        third_coordinate = columnOne[index+2]
                    
                    elif first_coordinate in columnTwo:
                        index = columnTwo.index(first_coordinate)
                        second_coordinate = columnTwo[index+1]
                        third_coordinate = columnTwo[index+2]
                    
                    elif first_coordinate in columnThree:
                        index = columnThree.index(first_coordinate)
                        second_coordinate = columnThree[index+1]
                        third_coordinate = columnThree[index+2]
                    
                    elif first_coordinate in columnFour:
                        index = columnFour.index(first_coordinate)
                        second_coordinate = columnFour[index+1]
                        third_coordinate = columnFour[index+2]
                    
                    elif first_coordinate in columnFive:
                        index = columnFive.index(first_coordinate)
                        second_coordinate = columnFive[index+1]
                        third_coordinate = columnFive[index+2]
                    
                    elif first_coordinate in columnSix:
                        index = columnSix.index(first_coordinate)
                        second_coordinate = columnSix[index+1]
                        third_coordinate = columnSix[index+2]
                
                #make sure the second and third coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
                    
                    
            elif direction == 'south':
                #invalid coordinates for direction
                if number == '1' or number == '2':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find the column the first coordinate is on. Generate second and third coordinate based on direction
                else:
                    if first_coordinate in columnOne:
                        index = columnOne.index(first_coordinate)
                        second_coordinate = columnOne[index-1]
                        third_coordinate = columnOne[index-2]
                    
                    elif first_coordinate in columnTwo:
                        index = columnTwo.index(first_coordinate)
                        second_coordinate = columnTwo[index-1]
                        third_coordinate = columnTwo[index-2]
                    
                    elif first_coordinate in columnThree:
                        index = columnThree.index(first_coordinate)
                        second_coordinate = columnThree[index-1]
                        third_coordinate = columnThree[index-2]
                    
                    elif first_coordinate in columnFour:
                        index = columnFour.index(first_coordinate)
                        second_coordinate = columnFour[index-1]
                        third_coordinate = columnFour[index-2]
                    
                    elif first_coordinate in columnFive:
                        index = columnFive.index(first_coordinate)
                        second_coordinate = columnFive[index-1]
                        third_coordinate = columnFive[index-2]
                    
                    elif first_coordinate in columnSix:
                        index = columnSix.index(first_coordinate)
                        second_coordinate = columnSix[index-1]
                        third_coordinate = columnSix[index-2]
                        
                #make sure the second and third coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
            
            
            elif direction == 'east':
                #invalid coordinates for direction
                if letter == 'F' or letter == 'E':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find the row the first coordinate is on. Generate second and third coordinate based on direction
                else:
                    if first_coordinate in rowOne:
                        index = rowOne.index(first_coordinate)
                        second_coordinate = rowOne[index+1]
                        third_coordinate = rowOne[index+2]
                    
                    elif first_coordinate in rowTwo:
                        index = rowTwo.index(first_coordinate)
                        second_coordinate = rowTwo[index+1]
                        third_coordinate = rowTwo[index+2]
                    
                    elif first_coordinate in rowThree:
                        index = rowThree.index(first_coordinate)
                        second_coordinate = rowThree[index+1]
                        third_coordinate = rowThree[index+2]
                    
                    elif first_coordinate in rowFour:
                        index = rowFour.index(first_coordinate)
                        second_coordinate = rowFour[index+1]
                        third_coordinate = rowFour[index+2]
                    
                    elif first_coordinate in rowFive:
                        index = rowFive.index(first_coordinate)
                        second_coordinate = rowFive[index+1]
                        third_coordinate = rowFive[index+2]
                    
                    elif first_coordinate in rowSix:
                        index = rowSix.index(first_coordinate)
                        second_coordinate = rowSix[index+1]
                        third_coordinate = rowSix[index+2]
                
                #make sure the second and third coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
            
            elif direction == 'west':
                #invalid coordinates for direction
                if letter == 'A' or letter == 'B':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find the row the first coordinate is on. Generate second and third coordinate based on direction
                else:
                    if first_coordinate in rowOne:
                        index = rowOne.index(first_coordinate)
                        second_coordinate = rowOne[index-1]
                        third_coordinate = rowOne[index-2]
                    
                    elif first_coordinate in rowTwo:
                        index = rowTwo.index(first_coordinate)
                        second_coordinate = rowTwo[index-1]
                        third_coordinate = rowTwo[index-2]
                    
                    elif first_coordinate in rowThree:
                        index = rowThree.index(first_coordinate)
                        second_coordinate = rowThree[index-1]
                        third_coordinate = rowThree[index-2]
                    
                    elif first_coordinate in rowFour:
                        index = rowFour.index(first_coordinate)
                        second_coordinate = rowFour[index-1]
                        third_coordinate = rowFour[index-2]
                    
                    elif first_coordinate in rowFive:
                        index = rowFive.index(first_coordinate)
                        second_coordinate = rowFive[index-1]
                        third_coordinate = rowFive[index-2]
                    
                    elif first_coordinate in rowSix:
                        index = rowSix.index(first_coordinate)
                        second_coordinate = rowSix[index-1]
                        third_coordinate = rowSix[index-2]
                
                #make sure the second and third coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
             
            #compile generated coordinates into list, this will be returned
            coordinates = [first_coordinate, second_coordinate, third_coordinate]      
        
        
        #battleship
        elif units == 4:
            
            if direction == 'north':
                #invalid coordinates for direction
                if number == '6' or number == '5' or number == '4':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find column the first coordinate is on. Generate second, third, and fourth coordinates based on inputted direction
                else:
                    if first_coordinate in columnOne:
                        index = columnOne.index(first_coordinate)
                        second_coordinate = columnOne[index+1]
                        third_coordinate = columnOne[index+2]
                        fourth_coordinate = columnOne[index + 3]
                    
                    elif first_coordinate in columnTwo:
                        index = columnTwo.index(first_coordinate)
                        second_coordinate = columnTwo[index+1]
                        third_coordinate = columnTwo[index+2]
                        fourth_coordinate = columnTwo [index+3]
                    
                    elif first_coordinate in columnThree:
                        index = columnThree.index(first_coordinate)
                        second_coordinate = columnThree[index+1]
                        third_coordinate = columnThree[index+2]
                        fourth_coordinate = columnThree[index+3]
                    
                    elif first_coordinate in columnFour:
                        index = columnFour.index(first_coordinate)
                        second_coordinate = columnFour[index+1]
                        third_coordinate = columnFour[index+2]
                        fourth_coordinate = columnFour[index+3]
                    
                    elif first_coordinate in columnFive:
                        index = columnFive.index(first_coordinate)
                        second_coordinate = columnFive[index+1]
                        third_coordinate = columnFive[index+2]
                        fourth_coordinate = columnFive[index+3]
                    
                    elif first_coordinate in columnSix:
                        index = columnSix.index(first_coordinate)
                        second_coordinate = columnSix[index+1]
                        third_coordinate = columnSix[index+2]
                        fourth_coordinate = columnSix[index+3]
                
                #make sure the second, third, and fourth coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates or fourth_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
              
                    
            elif direction == 'south':
                #invalid coordinates for direction
                if number == '1' or number == '2' or number == '3':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find column the first coordinate is on. Generate second, third, and fourth coordinates based on inputted direction
                else:
                    if first_coordinate in columnOne:
                        index = columnOne.index(first_coordinate)
                        second_coordinate = columnOne[index-1]
                        third_coordinate = columnOne[index-2]
                        fourth_coordinate = columnOne [index-3]
                    
                    elif first_coordinate in columnTwo:
                        index = columnTwo.index(first_coordinate)
                        second_coordinate = columnTwo[index-1]
                        third_coordinate = columnTwo[index-2]
                        fourth_coordinate = columnTwo [index-3]
                    
                    elif first_coordinate in columnThree:
                        index = columnThree.index(first_coordinate)
                        second_coordinate = columnThree[index-1]
                        third_coordinate = columnThree[index-2]
                        fourth_coordinate = columnThree [index-3]
                    
                    elif first_coordinate in columnFour:
                        index = columnFour.index(first_coordinate)
                        second_coordinate = columnFour[index-1]
                        third_coordinate = columnFour[index-2]
                        fourth_coordinate = columnFour [index-3]
                    
                    elif first_coordinate in columnFive:
                        index = columnFive.index(first_coordinate)
                        second_coordinate = columnFive[index-1]
                        third_coordinate = columnFive[index-2]
                        fourth_coordinate = columnFive [index-3]
                    
                    elif first_coordinate in columnSix:
                        index = columnSix.index(first_coordinate)
                        second_coordinate = columnSix[index-1]
                        third_coordinate = columnSix[index-2]
                        fourth_coordinate = columnSix [index-3]
                
                #make sure the second, third, and fourth coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates or fourth_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
                    
            
            elif direction == 'east':
                #invalid coordinates for direction
                if letter == 'F' or letter == 'E' or letter == 'D':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find row the first coordinate is on. Generate second, third, and fourth coordinates based on inputted direction
                else:
                    if first_coordinate in rowOne:
                        index = rowOne.index(first_coordinate)
                        second_coordinate = rowOne[index+1]
                        third_coordinate = rowOne[index+2]
                        fourth_coordinate = rowOne[index+3]
                    
                    elif first_coordinate in rowTwo:
                        index = rowTwo.index(first_coordinate)
                        second_coordinate = rowTwo[index+1]
                        third_coordinate = rowTwo[index+2]
                        fourth_coordinate = rowTwo[index+3]
                    
                    elif first_coordinate in rowThree:
                        index = rowThree.index(first_coordinate)
                        second_coordinate = rowThree[index+1]
                        third_coordinate = rowThree[index+2]
                        fourth_coordinate = rowThree[index+3]
                    
                    elif first_coordinate in rowFour:
                        index = rowFour.index(first_coordinate)
                        second_coordinate = rowFour[index+1]
                        third_coordinate = rowFour[index+2]
                        fourth_coordinate = rowFour[index+3]
                    
                    elif first_coordinate in rowFive:
                        index = rowFive.index(first_coordinate)
                        second_coordinate = rowFive[index+1]
                        third_coordinate = rowFive[index+2]
                        fourth_coordinate = rowFive[index+3]
                    
                    elif first_coordinate in rowSix:
                        index = rowSix.index(first_coordinate)
                        second_coordinate = rowSix[index+1]
                        third_coordinate = rowSix[index+2]
                        fourth_coordinate = rowSix[index+3]
                
                #make sure the second, third, and fourth coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates or fourth_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue #send back to top
                
                else:
                    valid = True
              
                    
            elif direction == 'west':
                #invalid coordinates for direction
                if letter == 'A' or letter == 'B' or letter == 'C':
                    print("Invalid direction for coordinate! Try another one.")
                    continue
                
                #find row the first coordinate is on. Generate second, third, and fourth coordinates based on inputted direction
                else:
                    if first_coordinate in rowOne:
                        index = rowOne.index(first_coordinate)
                        second_coordinate = rowOne[index-1]
                        third_coordinate = rowOne[index-2]
                        fourth_coordinate = rowOne[index-3]
                    
                    elif first_coordinate in rowTwo:
                        index = rowTwo.index(first_coordinate)
                        second_coordinate = rowTwo[index-1]
                        third_coordinate = rowTwo[index-2]
                        fourth_coordinate = rowTwo[index-3]
                    
                    elif first_coordinate in rowThree:
                        index = rowThree.index(first_coordinate)
                        second_coordinate = rowThree[index-1]
                        third_coordinate = rowThree[index-2]
                        fourth_coordinate = rowThree[index-3]
                    
                    elif first_coordinate in rowFour:
                        index = rowFour.index(first_coordinate)
                        second_coordinate = rowFour[index-1]
                        third_coordinate = rowFour[index-2]
                        fourth_coordinate = rowFour[index-3]
                    
                    elif first_coordinate in rowFive:
                        index = rowFive.index(first_coordinate)
                        second_coordinate = rowFive[index-1]
                        third_coordinate = rowFive[index-2]
                        fourth_coordinate = rowFive[index-3]
                    
                    elif first_coordinate in rowSix:
                        index = rowSix.index(first_coordinate)
                        second_coordinate = rowSix[index-1]
                        third_coordinate = rowSix[index-2]
                        fourth_coordinate = rowSix[index-3]
                
                #make sure the second, third, and fourth coordinates aren't already used
                if second_coordinate in usedCoordinates or third_coordinate in usedCoordinates or fourth_coordinate in usedCoordinates:
                    print("Invalid! Coordinates will overlap. Try another one.")
                    continue
                
                else:
                    valid = True
            
            #compile generated coordinates into list, this will be returned
            coordinates = [first_coordinate, second_coordinate, third_coordinate, fourth_coordinate]
    
    #return the generated coordinates
    return coordinates


#computerSetup() - randomize the positions of the computer's ships (cannot overlap)
#@param: length:int, already_used:str[]
#@return: coordinates:str[]
def computerSetup(length, already_used):
        
    valid = False
    
    while valid == False:
        
        #randomize the first coordinate
        computerFirst = random.choice(all_coordinates)
        
        #split the letter and number
        letterC = computerFirst[0]
        numberC = computerFirst[1]
        
        #destroyer
        if length == 2:
            
            #randomize direction
            directionChoice = random.choice(directions)
            
            if directionChoice == 'north':
                #invalid coordinate for direction or coordinate is already used
                if numberC == '6' or computerFirst in already_used:
                    continue
                
                #find which column the first coordinate is on, and generate the second coordinate based on direction
                else:
                    if computerFirst in columnOne:
                        index = columnOne.index(computerFirst)
                        computerSecond = columnOne[index+1]
                    
                    elif computerFirst in columnTwo:
                        index = columnTwo.index(computerFirst)
                        computerSecond = columnTwo[index+1]
                    
                    elif computerFirst in columnThree:
                        index = columnThree.index(computerFirst)
                        computerSecond = columnThree[index+1]
                    
                    elif computerFirst in columnFour:
                        index = columnFour.index(computerFirst)
                        computerSecond = columnFour[index+1]
                    
                    elif computerFirst in columnFive:
                        index = columnFive.index(computerFirst)
                        computerSecond = columnFive[index+1]
                    
                    elif computerFirst in columnSix:
                        index = columnSix.index(computerFirst)
                        computerSecond = columnSix[index+1]
                
                #check if the second coordinate has already been used
                if computerSecond in already_used:
                    continue
                
                else:
                    valid = True
            
            elif directionChoice == 'south':
                ##invalid coordinate for direction or coordinate is already used
                if numberC == '1' or computerFirst in already_used:
                    continue  
                
                #find which column the first coordinate is on, and generate the second coordinate based on direction
                else:
                    if computerFirst in columnOne:
                        index = columnOne.index(computerFirst)
                        computerSecond = columnOne[index-1]
                    
                    elif computerFirst in columnTwo:
                        index = columnTwo.index(computerFirst)
                        computerSecond = columnTwo[index-1]
                    
                    elif computerFirst in columnThree:
                        index = columnThree.index(computerFirst)
                        computerSecond = columnThree[index-1]
                    
                    elif computerFirst in columnFour:
                        index = columnFour.index(computerFirst)
                        computerSecond = columnFour[index-1]
                    
                    elif computerFirst in columnFive:
                        index = columnFive.index(computerFirst)
                        computerSecond = columnFive[index-1]
                    
                    elif computerFirst in columnSix:
                        index = columnSix.index(computerFirst)
                        computerSecond = columnSix[index-1]
                
                #check if the second coordinate has already been used
                if computerSecond in already_used:
                    continue
                
                else:
                    valid = True
                
            elif directionChoice == 'east':
                #invalid coordinate for direction or coordinate is already used
                if letterC == 'F' or computerFirst in already_used:
                    continue
                
                #find which row the first coordinate is on, and generate the second coordinate based on direction
                else:
                    if computerFirst in rowOne:
                        index = rowOne.index(computerFirst)
                        computerSecond = rowOne[index+1]
                    
                    elif computerFirst in rowTwo:
                        index = rowTwo.index(computerFirst)
                        computerSecond = rowTwo[index+1]
                    
                    elif computerFirst in rowThree:
                        index = rowThree.index(computerFirst)
                        computerSecond = rowThree[index+1]
                    
                    elif computerFirst in rowFour:
                        index = rowFour.index(computerFirst)
                        computerSecond = rowFour[index+1]
                    
                    elif computerFirst in rowFive:
                        index = rowFive.index(computerFirst)
                        computerSecond = rowFive[index+1]
                    
                    elif computerFirst in rowSix:
                        index = rowSix.index(computerFirst)
                        computerSecond = rowSix[index+1]
                
                #check if the second coordinate has already been used
                if computerSecond in already_used:
                    continue
                
                else:
                    valid = True
                
            elif directionChoice == 'west':
                #invalid coordinate for direction or coordinate is already used
                if letterC == 'A' or computerFirst in already_used:
                    continue
                
                #find which row the first coordinate is on, and generate the second coordinate
                else:
                    if computerFirst in rowOne:
                        index = rowOne.index(computerFirst)
                        computerSecond = rowOne[index-1]
                    
                    elif computerFirst in rowTwo:
                        index = rowTwo.index(computerFirst)
                        computerSecond = rowTwo[index-1]
                    
                    elif computerFirst in rowThree:
                        index = rowThree.index(computerFirst)
                        computerSecond = rowThree[index-1]
                    
                    elif computerFirst in rowFour:
                        index = rowFour.index(computerFirst)
                        computerSecond = rowFour[index-1]
                    
                    elif computerFirst in rowFive:
                        index = rowFive.index(computerFirst)
                        computerSecond = rowFive[index-1]
                    
                    elif computerFirst in rowSix:
                        index = rowSix.index(computerFirst)
                        computerSecond = rowSix[index-1]
                
                #see if the second coordinate has already been used
                if computerSecond in already_used:
                    continue
                
                else:
                    valid = True
            
            #add the two generated coordinates to list, this will be returned
            coordinates = [computerFirst, computerSecond]      
        
        
        #submarine
        elif length == 3:
            
            #randomize direction
            directionChoice = random.choice(directions)
            
            if directionChoice == 'north':
                #invalid coordinate for direction or coordinate is already used
                if numberC == '6' or numberC == '5' or computerFirst in already_used:
                    continue
                
                #find which column the first coordinate is on. Generate second and third coordinate
                else:
                    if computerFirst in columnOne:
                        index = columnOne.index(computerFirst)
                        computerSecond = columnOne[index+1]
                        computerThird = columnOne[index+2]
                    
                    elif computerFirst in columnTwo:
                        index = columnTwo.index(computerFirst)
                        computerSecond = columnTwo[index+1]
                        computerThird = columnTwo[index+2]
                    
                    elif computerFirst in columnThree:
                        index = columnThree.index(computerFirst)
                        computerSecond = columnThree[index+1]
                        computerThird = columnThree[index+2]
                    
                    elif computerFirst in columnFour:
                        index = columnFour.index(computerFirst)
                        computerSecond = columnFour[index+1]
                        computerThird = columnFour[index+2]
                    
                    elif computerFirst in columnFive:
                        index = columnFive.index(computerFirst)
                        computerSecond = columnFive[index+1]
                        computerThird = columnFive[index+2]
                    
                    elif computerFirst in columnSix:
                        index = columnSix.index(computerFirst)
                        computerSecond = columnSix[index+1]
                        computerThird = columnSix[index+2]
                
                #check if the second or third coordinate has already been used
                if computerSecond in already_used or computerThird in already_used:
                    continue
                
                else:
                    valid = True
                 
            elif directionChoice == 'south':
                #invalid coordinate for direction or coordinate is already used
                if numberC == '1' or numberC == '2' or computerFirst in already_used:
                    continue
                
                #find which column the first coordinate is on. Generate second and third coordinate
                else:
                    if computerFirst in columnOne:
                        index = columnOne.index(computerFirst)
                        computerSecond = columnOne[index-1]
                        computerThird = columnOne[index-2]
                    
                    elif computerFirst in columnTwo:
                        index = columnTwo.index(computerFirst)
                        computerSecond = columnTwo[index-1]
                        computerThird = columnTwo[index-2]
                    
                    elif computerFirst in columnThree:
                        index = columnThree.index(computerFirst)
                        computerSecond = columnThree[index-1]
                        computerThird = columnThree[index-2]
                    
                    elif computerFirst in columnFour:
                        index = columnFour.index(computerFirst)
                        computerSecond = columnFour[index-1]
                        computerThird = columnFour[index-2]
                    
                    elif computerFirst in columnFive:
                        index = columnFive.index(computerFirst)
                        computerSecond = columnFive[index-1]
                        computerThird = columnFive[index-2]
                    
                    elif computerFirst in columnSix:
                        index = columnSix.index(computerFirst)
                        computerSecond = columnSix[index-1]
                        computerThird = columnSix[index-2]
                        
                #see if the second or third coordinate has already been used
                if computerSecond in already_used or computerThird in already_used:
                   continue
                
                else:
                    valid = True
                
                
            elif directionChoice == 'east':
                #invalid coordinate for direction or coordinate is already used
                if letterC == 'F' or letterC == 'E' or computerFirst in already_used:
                    continue
                
                #find which row the first coordinate is on. Generate second and third coordinate
                else:
                    if computerFirst in rowOne:
                        index = rowOne.index(computerFirst)
                        computerSecond = rowOne[index+1]
                        computerThird = rowOne[index+2]
                    
                    elif computerFirst in rowTwo:
                        index = rowTwo.index(computerFirst)
                        computerSecond = rowTwo[index+1]
                        computerThird = rowTwo[index+2]
                    
                    elif computerFirst in rowThree:
                        index = rowThree.index(computerFirst)
                        computerSecond = rowThree[index+1]
                        computerThird = rowThree[index+2]
                    
                    elif computerFirst in rowFour:
                        index = rowFour.index(computerFirst)
                        computerSecond = rowFour[index+1]
                        computerThird = rowFour[index+2]
                    
                    elif computerFirst in rowFive:
                        index = rowFive.index(computerFirst)
                        computerSecond = rowFive[index+1]
                        computerThird = rowFive[index+2]
                    
                    elif computerFirst in rowSix:
                        index = rowSix.index(computerFirst)
                        computerSecond = rowSix[index+1]
                        computerThird = rowSix[index+2]
                        
                #check if the second or third coordinate has already been used
                if computerSecond in already_used or computerThird in already_used:
                    continue
                
                else:
                    valid = True
                    
                    
            elif directionChoice == 'west':
                #invalid coordinate for direction or coordinate is already used
                if letterC == 'A' or letterC == 'B' or computerFirst in already_used:
                    continue
                
                #find which row the first coordinate is on. Generate second and third coordinate
                else:
                    if computerFirst in rowOne:
                        index = rowOne.index(computerFirst)
                        computerSecond = rowOne[index-1]
                        computerThird = rowOne[index-2]
                    
                    elif computerFirst in rowTwo:
                        index = rowTwo.index(computerFirst)
                        computerSecond = rowTwo[index-1]
                        computerThird = rowTwo[index-2]
                    
                    elif computerFirst in rowThree:
                        index = rowThree.index(computerFirst)
                        computerSecond = rowThree[index-1]
                        computerThird = rowThree[index-2]
                    
                    elif computerFirst in rowFour:
                        index = rowFour.index(computerFirst)
                        computerSecond = rowFour[index-1]
                        computerThird = rowFour[index-2]
                    
                    elif computerFirst in rowFive:
                        index = rowFive.index(computerFirst)
                        computerSecond = rowFive[index-1]
                        computerThird = rowFive[index-2]
                    
                    elif computerFirst in rowSix:
                        index = rowSix.index(computerFirst)
                        computerSecond = rowSix[index-1]
                        computerThird = rowSix[index-2]
                
                #check if the second or third coordinate has already been used
                if computerSecond in already_used or computerThird in already_used:
                    continue
                
                else:
                    valid = True
            
            #compile generateed coordinates to list, this will be returned
            coordinates = [computerFirst, computerSecond, computerThird]
        
        
        #battleship
        elif length == 4:
            
            #randomize direction
            directionChoice = random.choice(directions)
        
            if directionChoice == 'north':
                #invalid coordinate for direction or coordinate is already used
                if numberC == '6' or numberC == '5' or numberC == '4' or computerFirst in already_used:
                    continue
                
                #find which column the first coordinate is on. Generate second, third, and fourth coordinate
                else:
                    if computerFirst in columnOne:
                        index = columnOne.index(computerFirst)
                        computerSecond = columnOne[index+1]
                        computerThird = columnOne[index+2]
                        computerFourth = columnOne[index+3]
                    
                    elif computerFirst in columnTwo:
                        index = columnTwo.index(computerFirst)
                        computerSecond = columnTwo[index+1]
                        computerThird = columnTwo[index+2]
                        computerFourth = columnTwo[index+3]
                    
                    elif computerFirst in columnThree:
                        index = columnThree.index(computerFirst)
                        computerSecond = columnThree[index+1]
                        computerThird = columnThree[index+2]
                        computerFourth = columnThree[index+3]
                    
                    elif computerFirst in columnFour:
                        index = columnFour.index(computerFirst)
                        computerSecond = columnFour[index+1]
                        computerThird = columnFour[index+2]
                        computerFourth = columnFour[index+3]
                    
                    elif computerFirst in columnFive:
                        index = columnFive.index(computerFirst)
                        computerSecond = columnFive[index+1]
                        computerThird = columnFive[index+2]
                        computerFourth = columnFive[index+3]
                    
                    elif computerFirst in columnSix:
                        index = columnSix.index(computerFirst)
                        computerSecond = columnSix[index+1]
                        computerThird = columnSix[index+2]
                        computerFourth = columnSix[index+3]
                
                #see if the second, third, or fourth coordinate has already been used
                if computerSecond in already_used or computerThird in already_used or computerFourth in already_used:
                    continue
                
                else:
                    valid = True
                 
                 
            elif directionChoice == 'south':
                #invalid coordinate for direction or coordinate is already used
                if numberC == '1' or numberC == '2' or numberC == '3' or computerFirst in already_used:
                    continue
                
                #find which column the first coordinate is on. Generate second, third, and fourth coordinate
                else:
                    if computerFirst in columnOne:
                        index = columnOne.index(computerFirst)
                        computerSecond = columnOne[index-1]
                        computerThird = columnOne[index-2]
                        computerFourth = columnOne[index-3]
                    
                    elif computerFirst in columnTwo:
                        index = columnTwo.index(computerFirst)
                        computerSecond = columnTwo[index-1]
                        computerThird = columnTwo[index-2]
                        computerFourth = columnTwo[index-3]
                    
                    elif computerFirst in columnThree:
                        index = columnThree.index(computerFirst)
                        computerSecond = columnThree[index-1]
                        computerThird = columnThree[index-2]
                        computerFourth = columnThree[index-3]
                    
                    elif computerFirst in columnFour:
                        index = columnFour.index(computerFirst)
                        computerSecond = columnFour[index-1]
                        computerThird = columnFour[index-2]
                        computerFourth = columnFour[index-3]
                    
                    elif computerFirst in columnFive:
                        index = columnFive.index(computerFirst)
                        computerSecond = columnFive[index-1]
                        computerThird = columnFive[index-2]
                        computerFourth = columnFive[index-3]
                    
                    elif computerFirst in columnSix:
                        index = columnSix.index(computerFirst)
                        computerSecond = columnSix[index-1]
                        computerThird = columnSix[index-2]
                        computerFourth = columnSix[index-3]
                
                #check if the second, third, or fourth coordinate has already been used
                if computerSecond in already_used or computerThird in already_used or computerFourth in already_used:
                   continue
                
                else:
                    valid = True
                
                
            elif directionChoice == 'east':
                #invalid coordinate for direction or coordinate is already used
                if letterC == 'F' or letterC == 'E' or letterC == 'D' or computerFirst in already_used:
                    continue
                
                #find which row the first coordinate is on. Generate second, third, and fourth coordinate
                else:
                    if computerFirst in rowOne:
                        index = rowOne.index(computerFirst)
                        computerSecond = rowOne[index+1]
                        computerThird = rowOne[index+2]
                        computerFourth = rowOne[index+3]
                    
                    elif computerFirst in rowTwo:
                        index = rowTwo.index(computerFirst)
                        computerSecond = rowTwo[index+1]
                        computerThird = rowTwo[index+2]
                        computerFourth = rowTwo[index+3]
                    
                    elif computerFirst in rowThree:
                        index = rowThree.index(computerFirst)
                        computerSecond = rowThree[index+1]
                        computerThird = rowThree[index+2]
                        computerFourth = rowThree[index+3]
                    
                    elif computerFirst in rowFour:
                        index = rowFour.index(computerFirst)
                        computerSecond = rowFour[index+1]
                        computerThird = rowFour[index+2]
                        computerFourth = rowFour[index+3]
                    
                    elif computerFirst in rowFive:
                        index = rowFive.index(computerFirst)
                        computerSecond = rowFive[index+1]
                        computerThird = rowFive[index+2]
                        computerFourth = rowFive[index+3]
                    
                    elif computerFirst in rowSix:
                        index = rowSix.index(computerFirst)
                        computerSecond = rowSix[index+1]
                        computerThird = rowSix[index+2]
                        computerFourth = rowSix[index+3]
                
                #check if the second, third, or fourth coordinate has already been used
                if computerSecond in already_used or computerThird in already_used or computerFourth in already_used:
                    continue
                
                else:
                    valid = True
                  
                    
            elif directionChoice == 'west':
                #invalid coordinate for direction or coordinate is already used
                if letterC == 'A' or letterC == 'B' or letterC == 'C' or computerFirst in already_used:
                    continue
                
                #find which column the row coordinate is on. Generate second, third, and fourth coordinate
                else:
                    if computerFirst in rowOne:
                        index = rowOne.index(computerFirst)
                        computerSecond = rowOne[index-1]
                        computerThird = rowOne[index-2]
                        computerFourth = rowOne[index-3]
                    
                    elif computerFirst in rowTwo:
                        index = rowTwo.index(computerFirst)
                        computerSecond = rowTwo[index-1]
                        computerThird = rowTwo[index-2]
                        computerFourth = rowTwo[index-3]
                    
                    elif computerFirst in rowThree:
                        index = rowThree.index(computerFirst)
                        computerSecond = rowThree[index-1]
                        computerThird = rowThree[index-2]
                        computerFourth = rowThree[index-3]
                    
                    elif computerFirst in rowFour:
                        index = rowFour.index(computerFirst)
                        computerSecond = rowFour[index-1]
                        computerThird = rowFour[index-2]
                        computerFourth = rowFour[index-3]
                    
                    elif computerFirst in rowFive:
                        index = rowFive.index(computerFirst)
                        computerSecond = rowFive[index-1]
                        computerThird = rowFive[index-2]
                        computerFourth = rowFive[index-3]
                    
                    elif computerFirst in rowSix:
                        index = rowSix.index(computerFirst)
                        computerSecond = rowSix[index-1]
                        computerThird = rowSix[index-2]
                        computerFourth = rowSix[index-3]
                
                #check if the second, third, or fourth coordinate has already been used
                if computerSecond in already_used or computerThird in already_used or computerFourth in already_used:
                    continue
                
                else:
                    valid = True
            
            #compile the generated coordinates into list, this will be returned
            coordinates = [computerFirst, computerSecond, computerThird, computerFourth]
    
    #return the coordinates of the ship generated
    return coordinates


#gameSetup() - plan both player's ships and output the opponent's board with ships
#@param: none
#@return: opponent_ships:str[], computer_ships:str[]
def gameSetup():
    
    #print out the coordinate map for reference
    print("Here are the board coordinates:")
    print('A6 B6 C6 D6 E6 F6')
    print('A5 B5 C5 D5 E5 F5')
    print('A4 B4 C4 D4 E4 F4')
    print('A3 B3 C3 D3 E3 F3')
    print('A2 B2 C2 D2 E2 F2')
    print('A1 B1 C1 D1 E1 F1')
    
    print(' ')
    print("Let's plan your ship coordinates!")
    print(' ')
    
    
    # OPPONENT
    
    #track opponent's ship coordinates
    opponent_ships = []
    
    #generate opponent's ships
    
    #destroyer one, 2 units, return coordinate values and add to tracking list
    print("Destroyer #1 (2 units)")
    destroyerOne_opponent = shipSet(opponent_ships, 2)
    for i in range(0, 2):
        opponent_ships.append(destroyerOne_opponent[i])
    
    
    print(' ')
    
    
    #destroyer two, 2 units, return coordinate values and add to tracking list
    print("Destroyer #2 (2 units)")
    destroyerTwo_opponent = shipSet(opponent_ships, 2)
    for i in range(0, 2):
        opponent_ships.append(destroyerTwo_opponent[i])
    
    
    print(' ')
    
    
    #submarine, 4 units, return coordinate values and add to tracking list
    print("Submarine (3 units)")
    submarine_opponent = shipSet(opponent_ships, 3)
    for i in range(0, 3):
        opponent_ships.append(submarine_opponent[i])
    
    
    print(' ')
    
    
    #battleship, 4 units, return coordinate values and add to tracking list
    print("Battleship (4 units)")
    battleship_opponent = shipSet(opponent_ships, 4)
    for i in range(0, 4):
        opponent_ships.append(battleship_opponent[i])
    
    
    print(' ')
    
        
    #print opponent's ships
    print("Here are your ship positions:")
    
    #start with empty boards. ship positions will replace specific index values in specific rows
    opponentrowSix = 'oooooo'
    opponentrowFive = 'oooooo'
    opponentrowFour = 'oooooo'
    opponentrowThree = 'oooooo'
    opponentrowTwo = 'oooooo'
    opponentrowOne = 'oooooo'
    
    #check each value of the opponet_ships list and their location on the board
    for a in range (0, 11):
        if opponent_ships[a] in rowSix:
            indexVal = rowSix.index(opponent_ships[a])
            opponentrowSix = opponentrowSix[:indexVal] + '*' + opponentrowSix[indexVal+1:]
            
        elif opponent_ships[a] in rowFive:
            indexVal = rowFive.index(opponent_ships[a]) 
            opponentrowFive = opponentrowFive[:indexVal] + '*' + opponentrowFive[indexVal+1:]
            
        elif opponent_ships[a] in rowFour:
            indexVal = rowFour.index(opponent_ships[a])
            opponentrowFour = opponentrowFour[:indexVal] + '*' + opponentrowFour[indexVal+1:]
            
        elif opponent_ships[a] in rowThree:
            indexVal = rowThree.index(opponent_ships[a])
            opponentrowThree = opponentrowThree[:indexVal] + '*' + opponentrowThree[indexVal+1:]
            
        elif opponent_ships[a] in rowTwo:
            indexVal = rowTwo.index(opponent_ships[a])
            opponentrowTwo = opponentrowTwo[:indexVal] + '*' + opponentrowTwo[indexVal+1:]
            
        elif opponent_ships[a] in rowOne:
            indexVal = rowOne.index(opponent_ships[a])
            opponentrowOne = opponentrowOne[:indexVal] + '*' + opponentrowOne[indexVal+1:]
    
    #print the final board
    print(opponentrowSix)
    print(opponentrowFive)
    print(opponentrowFour)
    print(opponentrowThree)
    print(opponentrowTwo)
    print(opponentrowOne)
    
    
    # COMPUTER
    
    #track computer's ships coordinates
    computer_ships = []
    
    #destroyer one, 2 units, return coordinates, add coordinates to tracker
    computer_destroyerOne = computerSetup(2, computer_ships)
    for i in range(0, 2):
        computer_ships.append(computer_destroyerOne[i])
    
    
    #destroyer two, 2 units, return coordinates, add coordinates to tracker
    computer_destroyerTwo = computerSetup(2, computer_ships)
    for i in range(0, 2):
        computer_ships.append(computer_destroyerTwo[i])
    
    
    #submarine, 3 units, return coordinates, add coordinates to tracker
    computer_submarine = computerSetup(3, computer_ships)
    for i in range(0, 3):
        computer_ships.append(computer_submarine[i])
    
    
    #battleship, 4 units, return coordinates, add coordinates to tracker
    computer_battleship = computerSetup(4, computer_ships)
    for i in range(0, 4):
        computer_ships.append(computer_battleship[i])
    
    
    #generate computer's map
    computerrowSix = 'oooooo'
    computerrowFive = 'oooooo'
    computerrowFour = 'oooooo'
    computerrowThree = 'oooooo'
    computerrowTwo = 'oooooo'
    computerrowOne = 'oooooo'
    
    #check each value of the computer_ships list and their location on the board
    for b in range (0, 11):
        if computer_ships[b] in rowSix:
            indexVal = rowSix.index(computer_ships[b])
            computerrowSix = computerrowSix[:indexVal] + '*' + computerrowSix[indexVal+1:]
            
        elif computer_ships[b] in rowFive:
            indexVal = rowFive.index(computer_ships[b]) 
            computerrowFive = computerrowFive[:indexVal] + '*' + computerrowFive[indexVal+1:]
            
        elif computer_ships[b] in rowFour:
            indexVal = rowFour.index(computer_ships[b])
            computerrowFour = computerrowFour[:indexVal] + '*' + computerrowFour[indexVal+1:]
            
        elif computer_ships[b] in rowThree:
            indexVal = rowThree.index(computer_ships[b])
            computerrowThree = computerrowThree[:indexVal] + '*' + computerrowThree[indexVal+1:]
            
        elif computer_ships[b] in rowTwo:
            indexVal = rowTwo.index(computer_ships[b])
            computerrowTwo = computerrowTwo[:indexVal] + '*' + computerrowTwo[indexVal+1:]
            
        elif computer_ships[b] in rowOne:
            indexVal = rowOne.index(computer_ships[b])
            computerrowOne = computerrowOne[:indexVal] + '*' + computerrowOne[indexVal+1:]

    
    print(' ')
    
    #return opponent's and computer's ship coordinates
    return opponent_ships, computer_ships


#findWinner() - check if there is a winner in the game
#@param: c_hits_o:str[], o_hits_c:str[]
#@return: boolean:boolean
def findWinner(c_hits_o, o_hits_c):        
    
    #one of the player's has hit 11 coordinates - which is all the ships
    if len(c_hits_o) == 11 or len(o_hits_c) == 11:
        boolean = True
    
    #no one is done tanking ships
    else:
        boolean = False
    
    return boolean


#outputWinner() - check lists to determine if computer or opponent won the game
#@param: status_destroyerOne:str, status_destroyerTwo:str, status_submarine:str, status_battleship:str, cDestroyerOne_status:str[], cDestroyerTwo_status:str[], cSubmarine_status:str[], cBattleship_status:str[]
#@return: none
def outputWinner(status_destroyerOne, status_destroyerTwo, status_submarine, status_battleship, cDestroyerOne_status, cDestroyerTwo_status, cSubmarine_status, cBattleship_status):
    
    winner = 0
    
    #check to see if the opponent was the winner - hit all ships
    if status_destroyerOne == 'hit' and status_destroyerTwo == 'hit' and status_submarine == 'hit' and status_battleship == 'hit':
        winner = "You"
    
    #check to see if computer is winner - hit all ships
    if cDestroyerOne_status == 'hit' and cDestroyerTwo_status == 'hit' and cSubmarine_status == 'hit' and cBattleship_status == 'hit':
        winner = 'I'
    
    #output winner
    print("%s win! Good game :)" %winner)


#playerMoves() - determine who plays first and manage each player's turn based on hits and misses
#@param: opponent_ships:str[], computer_ships:str[]
#@return: none
def playerMoves(opponent_ships, computer_ships):
    
    #choose who to go first
    first_player = random.choice(['You', 'I'])
    print("%s play first." %first_player)
    
    
    #computer's ships
    global computer_destroyerOne
    computer_destroyerOne = computer_ships[0:2]
    global computer_destroyerTwo
    computer_destroyerTwo = computer_ships[2:4]
    global computer_submarine
    computer_submarine = computer_ships[4:7]
    global computer_battleship
    computer_battleship = computer_ships[7:11]
    
    
    #opponent's ships
    global opponent_destroyerOne
    opponent_destroyerOne = opponent_ships[0:2]
    global opponent_destroyerTwo
    opponent_destroyerTwo = opponent_ships[2:4]
    global opponent_submarine
    opponent_submarine = opponent_ships[4:7]
    global opponent_battleship
    opponent_battleship = opponent_ships[7:11]
    
    
    #track coordinates that have hit a ship
    c_hits_o = []
    o_hits_c = []
    
    
    #track all the coordinates that have been played
    cMoves = []
    oMoves = []
    
    
    #track individual ships that each player hits
    computerHits_destroyerOne = []
    computerHits_destroyerTwo = []
    computerHits_submarine = []
    computerHits_battleship = []
    
    opponentHits_destroyerOne = []
    opponentHits_destroyerTwo = []
    opponentHits_submarine = []
    opponentHits_battleship = []
    
    
    #track the status of each ship - when it is hit, the status will turn to 'hit'
    status_destroyerOne = 0
    status_destroyerTwo = 0
    status_submarine = 0
    status_battleship = 0
    cDestroyerOne_status = 0
    cDestroyerTwo_status = 0
    cSubmarine_status = 0
    cBattleship_status = 0
    
    
    boolean = False
    
    out = False
    
    while boolean == False and out == False:
        print(' ')
        
        #when opponent is first player
        if first_player == 'You':
            
            #take to opponentPlay() for opponent's move
            status, oppPlayed = opponentPlay(oMoves, computer_ships)
            
            #add coordinate to "hit" list, all moves list, and it's the opponent's move again
            while status == 'hit':
                
                o_hits_c.append(oppPlayed)
                oMoves.append(oppPlayed)
                
                #add coordinate to specific ship's list based on what they hit
                if oppPlayed in computer_destroyerOne:
                    opponentHits_destroyerOne.append(oppPlayed)
                    
                elif oppPlayed in computer_destroyerTwo:
                    opponentHits_destroyerTwo.append(oppPlayed)
                    
                elif oppPlayed in computer_submarine:
                    opponentHits_submarine.append(oppPlayed)
                    
                elif oppPlayed in computer_battleship:
                    opponentHits_battleship.append(oppPlayed)
                
                #send message when ship is fully tanked. empty list to avoid repeating messages. change ship status
                if len(opponentHits_destroyerOne) == 2:
                    print("You tanked a destroyer!")
                    opponentHits_destroyerOne.clear()
                    status_destroyerOne = "hit"
                
                if len(opponentHits_destroyerTwo) == 2:
                    print("You tanked a destroyer!")
                    opponentHits_destroyerTwo.clear()
                    status_destroyerTwo = "hit"
                
                if len(opponentHits_submarine) == 3:
                    print("You tanked a submarine!")
                    opponentHits_submarine.clear()
                    status_submarine = "hit"
                
                if len(opponentHits_battleship) == 4:
                    print("You tanked a battleship!")
                    opponentHits_battleship.clear()
                    status_battleship = "hit"
                
                #check if opponent tanked all ships
                if status_destroyerOne == "hit" and status_destroyerTwo == "hit" and status_submarine == "hit" and status_battleship == "hit":
                    outputWinner(status_destroyerOne, status_destroyerTwo, status_submarine, status_battleship, cDestroyerOne_status, cDestroyerTwo_status, cSubmarine_status, cBattleship_status)
                    out = True
                    break
                
                #opponent's turn again
                status, oppPlayed = opponentPlay(oMoves, computer_ships)
            
            
            #missed - add coordinate to all moves list
            else:
                oMoves.append(oppPlayed)
            
            if out == False:
                
                #computer's turn
                coordinate_computerHit, coordinate_computerMissed = computerPlay(cMoves, c_hits_o, opponent_ships, opponent_destroyerOne, opponent_destroyerTwo, opponent_submarine, opponent_battleship, computerHits_destroyerOne, computerHits_destroyerTwo, computerHits_submarine, computerHits_battleship)
                
                #update list with coordinates the computer has successfully hit
                c_hits_o = coordinate_computerHit
                
                if len(coordinate_computerHit) >= 1:
                    for i in range(0, len(coordinate_computerHit)):
                        
                        #add coordinates to ship specific lists
                        if coordinate_computerHit[i] in opponent_destroyerOne and coordinate_computerHit[i] not in cMoves:
                            computerHits_destroyerOne.append(coordinate_computerHit[i])
                        
                        elif coordinate_computerHit[i] in opponent_destroyerTwo and coordinate_computerHit[i] not in cMoves:
                            computerHits_destroyerTwo.append(coordinate_computerHit[i])
                        
                        elif coordinate_computerHit[i] in opponent_submarine and coordinate_computerHit[i] not in cMoves:
                            computerHits_submarine.append(coordinate_computerHit[i])
                        
                        elif coordinate_computerHit[i] in opponent_battleship and coordinate_computerHit[i] not in cMoves:
                            computerHits_battleship.append(coordinate_computerHit[i])
                        
                        #send message when ship is fully tanked. empty list to avoid repeating messages. change ship status
                        if len(computerHits_destroyerOne) == 2:
                            print("Computer sunk your destroyer!")
                            computerHits_destroyerOne.clear()
                            cDestroyerOne_status = 'hit'
                        
                        if len(computerHits_destroyerTwo) == 2:
                            print("Computer sunk your destroyer!")
                            computerHits_destroyerTwo.clear()
                            cDestroyerTwo_status = 'hit'
                        
                        if len(computerHits_submarine) == 3:
                            print("Computer sunk your submarine!")
                            computerHits_submarine.clear()
                            cSubmarine_status = 'hit'
                        
                        if len(computerHits_battleship) == 4:
                            print("Computer sunk your battleship!")
                            computerHits_battleship.clear()
                            cBattleship_status = 'hit'
                        
                        #add all coordinates to 'all moves' list
                        if coordinate_computerHit[i] not in cMoves:
                            cMoves.append(coordinate_computerHit[i])
                        
                        #check if computer tanked all ships
                        if cDestroyerOne_status == 'hit' and cDestroyerTwo_status == 'hit' and cSubmarine_status == 'hit' and cBattleship_status == 'hit':
                            outputWinner(status_destroyerOne, status_destroyerTwo, status_submarine, status_battleship, cDestroyerOne_status, cDestroyerTwo_status, cSubmarine_status, cBattleship_status)
                            out = True
                            break
            
                #add missed coordinates to 'all moves' list
                if len(coordinate_computerMissed) >=1:
                    for p in range (0, len(coordinate_computerMissed)):
                        if coordinate_computerMissed[p] not in cMoves:
                            cMoves.append(coordinate_computerMissed[p])    
        
        
        #when computer is first player
        elif first_player == "I":
            
            #take to computerPlay() for computer's move
            coordinate_computerHit, coordinate_computerMissed = computerPlay(cMoves, c_hits_o, opponent_ships, opponent_destroyerOne, opponent_destroyerTwo, opponent_submarine, opponent_battleship, computerHits_destroyerOne, computerHits_destroyerTwo, computerHits_submarine, computerHits_battleship)
            
            #update list with computer's successful hits
            c_hits_o = coordinate_computerHit            

            if len(coordinate_computerHit) >= 1:
                for i in range(0, len(coordinate_computerHit)):
                    
                    #add coordinates to ship specific lists
                    if coordinate_computerHit[i] in opponent_destroyerOne and coordinate_computerHit[i] not in cMoves:
                        computerHits_destroyerOne.append(coordinate_computerHit[i])
                    
                    elif coordinate_computerHit[i] in opponent_destroyerTwo and coordinate_computerHit[i] not in cMoves:
                        computerHits_destroyerTwo.append(coordinate_computerHit[i])
                    
                    elif coordinate_computerHit[i] in opponent_submarine and coordinate_computerHit[i] not in cMoves:
                        computerHits_submarine.append(coordinate_computerHit[i])
                    
                    elif coordinate_computerHit[i] in opponent_battleship and coordinate_computerHit[i] not in cMoves:
                        computerHits_battleship.append(coordinate_computerHit[i])
                    
                    
                    #send message when ship is fully tanked. empty list to avoid repeating messages. change ship status
                    if len(computerHits_destroyerOne) == 2:
                        print("Computer sunk your destroyer!")
                        computerHits_destroyerOne.clear()
                        cDestroyerOne_status = 'hit'
                    
                    if len(computerHits_destroyerTwo) == 2:
                        print("Computer sunk your destroyer!")
                        computerHits_destroyerTwo.clear()
                        cDestroyerTwo_status = 'hit'
                    
                    if len(computerHits_submarine) == 3:
                        print("Computer sunk your submarine!")
                        computerHits_submarine.clear()
                        cSubmarine_status = 'hit'
                    
                    if len(computerHits_battleship) == 4:
                        print("Computer sunk your battleship!")
                        computerHits_battleship.clear()
                        cBattleship_status = 'hit'
                    
                    #add all coordinates to 'all moves' list
                    if coordinate_computerHit[i] not in cMoves:
                        cMoves.append(coordinate_computerHit[i])
                    
                    #check if computer tanked all ships
                    if cDestroyerOne_status == 'hit' and cDestroyerTwo_status == 'hit' and cSubmarine_status == 'hit' and cBattleship_status == 'hit':
                        outputWinner(status_destroyerOne, status_destroyerTwo, status_submarine, status_battleship, cDestroyerOne_status, cDestroyerTwo_status, cSubmarine_status, cBattleship_status)
                        out = True
                        break
                        
            #add missed coordinates to 'all moves' list
            if len(coordinate_computerMissed) >=1:
                for p in range (0, len(coordinate_computerMissed)):
                    if coordinate_computerMissed[p] not in cMoves:
                        cMoves.append(coordinate_computerMissed[p])
            
            
            if out == False:
                #opponent's turn
                status, oppPlayed = opponentPlay(oMoves, computer_ships)
                
                #add coordinate to "hit" list, all moves list, and it's the opponent's move again
                while status == 'hit':
                    o_hits_c.append(oppPlayed)
                    oMoves.append(oppPlayed)
                    
                    #add coordinate to specific ship's lists that was hit
                    if oppPlayed in computer_destroyerOne:
                        opponentHits_destroyerOne.append(oppPlayed)
                    
                    elif oppPlayed in computer_destroyerTwo:
                        opponentHits_destroyerTwo.append(oppPlayed)
                        
                    elif oppPlayed in computer_submarine:
                        opponentHits_submarine.append(oppPlayed)
                        
                    elif oppPlayed in computer_battleship:
                        opponentHits_battleship.append(oppPlayed)
                        
                    #send message when ship is fully tanked. empty list to avoid repeating messages. change ship status
                    if len(opponentHits_destroyerOne) == 2:
                        print("You tanked a destroyer!")
                        opponentHits_destroyerOne.clear()
                        status_destroyerOne = "hit"
                    
                    if len(opponentHits_destroyerTwo) == 2:
                        print("You tanked a destroyer!")
                        opponentHits_destroyerTwo.clear()
                        status_destroyerTwo = "hit"
                    
                    if len(opponentHits_submarine) == 3:
                        print("You tanked a submarine!")
                        opponentHits_submarine.clear()
                        status_submarine = "hit"
                    
                    if len(opponentHits_battleship) == 4:
                        print("You tanked a battleship!")
                        opponentHits_battleship.clear()
                        status_battleship = "hit"
                    
                    # check if opponent tanked all of computer's ships
                    if status_destroyerOne == "hit" and status_destroyerTwo == "hit" and status_submarine == "hit" and status_battleship == "hit":
                        outputWinner(status_destroyerOne, status_destroyerTwo, status_submarine, status_battleship, cDestroyerOne_status, cDestroyerTwo_status, cSubmarine_status, cBattleship_status)
                        out = True
                        break
                     
                    #opponent's turn
                    status, oppPlayed = opponentPlay(oMoves, computer_ships)
                
                #missed - add coordinate to all moves lists
                else:
                    oMoves.append(oppPlayed)
        
        if out ==False:
        
            print(' ')
            
            
            #print game boards
            printMap(opponent_ships, c_hits_o, cMoves, computer_ships, o_hits_c, oMoves)
            
            #check if there is a winner yet
            boolean = findWinner(c_hits_o, o_hits_c)
        
    #there is a winner - find the winner
    else:
        if boolean == True and out != True:
            outputWinner(status_destroyerOne, status_destroyerTwo, status_submarine, status_battleship, cDestroyerOne_status, cDestroyerTwo_status, cSubmarine_status, cBattleship_status)


#computerPlay() - manage the computer's turn based on hits and misses
#@param: cMoves:str[], c_hits_o:str[], opponent_ships:str[], opponent_destroyerOne:str[], opponent_destroyerTwo:str[], opponent_submarine:str[], opponent_battleship:str[], computerHits_destroyerOne:str[], computerHits_destroyerTwo:str[], computerHits_submarine:str[], computerHits_battleship:str[]:
#@return: coordinate_computerHit:str[], coordinate_computerMiss:str[]
def computerPlay(cMoves, c_hits_o, opponent_ships, opponent_destroyerOne, opponent_destroyerTwo, opponent_submarine, opponent_battleship, computerHits_destroyerOne, computerHits_destroyerTwo, computerHits_submarine, computerHits_battleship):
    
    #create tracking lists
    coordinate_computerHit = c_hits_o
    coordinate_computerMissed = []
    
    
    start = True
    
    
    valid = 0
    while valid == 0:
        
        #randomize a coordinate
        coordinate = random.choice (all_coordinates)
        
        #check if coordinate is already used
        if coordinate in cMoves:
            continue
        
        else:
            valid = 1
            
    
    while start == True:
        
        #split letter and number
        letter = coordinate[0]
        number = coordinate[1]
        
        #computer made a hit - print statement and status
        if coordinate in opponent_ships:
            print("Computer guessed {} and hit!". format(coordinate))
            status = 'hit'
        
        #computer made a miss - print statement and add coordinate to 'miss' list. exit loop
        else:
            print("Computer guessed {} and missed!". format(coordinate))
            coordinate_computerMissed.append(coordinate)
            start = False
            break
        
        #when computer makes a hit
        if status == 'hit':
            
            #add successful coordinate to 'hit' list
            coordinate_computerHit.append(coordinate)
            
            
            #coordinate is in row one. generate the valid and unused coordinates of surrounding the coordinate
            if coordinate in rowOne:
                
                #find index value of coordinate
                index = rowOne.index(coordinate)
                
                if letter != 'A' and letter != 'F':
                    list_choices = []
                    
                    choiceOne = rowOne[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                        
                    choiceTwo = rowOne[index+1]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowTwo[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'A':
                    list_choices = []
                    
                    choiceOne = rowOne[index+1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowTwo[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    #when the ship is tanked (message is printed when outside the function), ranomly guess
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice (all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        else:
                            continue
                        
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                    
                elif letter == 'F':
                    list_choices = []
                    
                    choiceOne = rowOne[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowTwo[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                    
            
            #coordinate is in row two. generate the valid and unused coordinates of surrounding the coordinate
            elif coordinate in rowTwo:
                
                #find index value of coordinate
                index = rowTwo.index(coordinate)
                
                if letter != 'A' and letter != 'F':
                    list_choices = []
                    
                    choiceOne = rowTwo[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowTwo [index+1]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowOne[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    choiceFour = rowThree[index]
                    if choiceFour not in cMoves and choiceFour not in coordinate_computerHit and choiceFour not in coordinate_computerMissed:
                        list_choices.append(choiceFour)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'A':
                    list_choices = []
                    
                    choiceOne = rowTwo[index+1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowOne[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowThree[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'F':
                    list_choices = []
                    
                    choiceOne = rowTwo[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowOne[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowThree[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
            
            #coordinate is in row three. generate the valid and unused coordinates of surrounding the coordinate
            elif coordinate in rowThree:
                
                #find index value of coordinate
                index = rowThree.index(coordinate)
                
                if letter != 'A' and letter != 'F':
                    list_choices = []
                    
                    choiceOne = rowThree[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowThree [index+1]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowTwo[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    choiceFour = rowFour[index]
                    if choiceThree not in cMoves and choiceFour not in coordinate_computerHit and choiceFour not in coordinate_computerMissed:
                        list_choices.append(choiceFour)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'A':
                    list_choices = []
                    
                    choiceOne = rowThree[index+1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFour[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowTwo[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'F':
                    list_choices = []
                    
                    choiceOne = rowThree[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFour[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowTwo[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
            
            #coordinate is in row four. generate the valid and unused coordinates of surrounding the coordinate
            elif coordinate in rowFour:
                
                #find index value of coordinate
                index = rowFour.index(coordinate)
                
                if letter != 'A' and letter != 'F':
                    list_choices = []
                    
                    choiceOne = rowFour[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFour [index+1]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowThree[index]
                    if choiceThree in cMoves and choiceThree in coordinate_computerHit and choiceThree in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    choiceFour = rowFive[index]
                    if choiceFour in cMoves and choiceFour in coordinate_computerHit and choiceFour in coordinate_computerMissed:
                        list_choices.append(choiceFour)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'A':
                    list_choices = []
                    
                    choiceOne = rowFour[index+1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFive[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowThree[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'F':
                    list_choices = []
                    
                    choiceOne = rowFour[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFive[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowThree[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
            
            #coordinate is in row five. generate the valid and unused coordinates of surrounding the coordinate
            elif coordinate in rowFive:
                
                #find index value of coordinate
                index = rowFive.index(coordinate)
                
                if letter != 'A' and letter != 'F':
                    list_choices = []
                    
                    choiceOne = rowFive[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFive [index+1]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowFour[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                        
                    choiceFour = rowSix[index]
                    if choiceFour not in cMoves and choiceFour not in coordinate_computerHit and choiceFour not in coordinate_computerMissed:
                        list_choices.append(choiceFour)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'A':
                    list_choices = []
                    
                    choiceOne = rowFive[index+1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowSix[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowFour[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                   #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'F':
                    list_choices = []
                    
                    choiceOne = rowFive[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                        
                    choiceTwo = rowSix[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                        
                    choiceThree = rowFour[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
              
                
            #coordinate is in row six. generate the valid and unused coordinates of surrounding the coordinate
            elif coordinate in rowSix:
                
                #find index value of coordinate
                index = rowSix.index(coordinate)

                if letter != 'A' and letter != 'F':
                    list_choices = []
                    
                    choiceOne = rowSix[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                        
                    choiceTwo = rowSix [index+1]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    choiceThree = rowFive[index]
                    if choiceThree not in cMoves and choiceThree not in coordinate_computerHit and choiceThree not in coordinate_computerMissed:
                        list_choices.append(choiceThree)
                
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'A':
                    list_choices = []
                    
                    choiceOne = rowSix[index+1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFive[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
                
                elif letter == 'F':
                    list_choices = []
                    
                    choiceOne = rowSix[index-1]
                    if choiceOne not in cMoves and choiceOne not in coordinate_computerHit and choiceOne not in coordinate_computerMissed:
                        list_choices.append(choiceOne)
                    
                    choiceTwo = rowFive[index]
                    if choiceTwo not in cMoves and choiceTwo not in coordinate_computerHit and choiceTwo not in coordinate_computerMissed:
                        list_choices.append(choiceTwo)
                    
                    #when the ship is tanked, randomly guess a coordinate
                    while len(list_choices) == 0:
                        
                        coordinate = random.choice(all_coordinates)
                        
                        #check if coordinate is not used
                        if coordinate not in cMoves and coordinate not in coordinate_computerHit and coordinate not in coordinate_computerMissed:
                            break
                        
                        else:
                            continue
                    
                    #randomize one of the valid options generated above
                    else:
                        coordinate = random.choice(list_choices)
                    
                    continue
                
    #return hit and missed coordinates
    return coordinate_computerHit, coordinate_computerMissed


#opponentPlay() - manage the opponent's turn. Check for invalid input and whether they hit or missed
#@param: oMoves:str[], computer_ships:str[]
#@return: status:str, coordinate:str
def opponentPlay(oMoves, computer_ships):
    
    valid = False
    while valid == False:
        
        #opponent input's a coordinate
        coordinate = input("Enter a coordinate:")
        
        #title coordinate
        coordinate = coordinate.title()
        
        #see if a valid coordinate
        if coordinate not in all_coordinates:
            print("Not a possible coordinate.")
            continue
        
        #check if already used
        if coordinate in oMoves:
            print("Already hit.")
            continue
        
        #check if there is a hit or miss
        if coordinate in computer_ships:
            status = 'hit'
            print("You hit!")
            valid = True
        else:
            status = 'miss'
            print("You missed!")
            valid = True
    
    #return if the opponent hit or missed and the coordinate they played
    return status, coordinate


#printMap() - create and print out the computer's and opponent's board after each turn (embedded in playMoves function)
#@param: opponent_ships:str[], c_hits_o:str[], cMoves:str[], computer_ships:str[], o_hits_c, oMoves:str[]
#@return: none
def printMap(opponent_ships, c_hits_o, cMoves, computer_ships, o_hits_c, oMoves):
    
    
    #OPPONENT
    
    #print the opponent's board with the hits and misses the computer made
    print("Here is your board:")
    
    computer_to_opponentrowSix = 'oooooo'
    computer_to_opponentrowFive = 'oooooo'
    computer_to_opponentrowFour = 'oooooo'
    computer_to_opponentrowThree = 'oooooo'
    computer_to_opponentrowTwo = 'oooooo'
    computer_to_opponentrowOne = 'oooooo'
    
    
    #add the opponent's ships to the board: check of the ship's coordinates, index value in specific row, and replace with *
    for a in range (0, 11):
        if opponent_ships[a] in rowSix:
            indexVal = rowSix.index(opponent_ships[a])
            computer_to_opponentrowSix = computer_to_opponentrowSix[:indexVal] + '*' + computer_to_opponentrowSix[indexVal+1:]
            
        elif opponent_ships[a] in rowFive:
            indexVal = rowFive.index(opponent_ships[a]) 
            computer_to_opponentrowFive = computer_to_opponentrowFive[:indexVal] + '*' + computer_to_opponentrowFive[indexVal+1:]
            
        elif opponent_ships[a] in rowFour:
            indexVal = rowFour.index(opponent_ships[a])
            computer_to_opponentrowFour = computer_to_opponentrowFour[:indexVal] + '*' + computer_to_opponentrowFour[indexVal+1:]
            
        elif opponent_ships[a] in rowThree:
            indexVal = rowThree.index(opponent_ships[a])
            computer_to_opponentrowThree = computer_to_opponentrowThree[:indexVal] + '*' + computer_to_opponentrowThree[indexVal+1:]
            
        elif opponent_ships[a] in rowTwo:
            indexVal = rowTwo.index(opponent_ships[a])
            computer_to_opponentrowTwo = computer_to_opponentrowTwo[:indexVal] + '*' + computer_to_opponentrowTwo[indexVal+1:]
            
        elif opponent_ships[a] in rowOne:
            indexVal = rowOne.index(opponent_ships[a])
            computer_to_opponentrowOne = computer_to_opponentrowOne[:indexVal] + '*' + computer_to_opponentrowOne[indexVal+1:]
    
    
    #add the hits made by the computer by checking each value in the c_hits_o list, the index value in a specific row, and replace with X
    for c in range(0, len(c_hits_o)):
        if c_hits_o[c] in rowSix:
            indexVal = rowSix.index(c_hits_o[c])
            computer_to_opponentrowSix = computer_to_opponentrowSix[:indexVal] + 'X' + computer_to_opponentrowSix[indexVal+1:]
        
        elif c_hits_o[c] in rowFive:
            indexVal = rowFive.index(c_hits_o[c])
            computer_to_opponentrowFive = computer_to_opponentrowFive[:indexVal] + 'X' + computer_to_opponentrowFive[indexVal+1:]
        
        elif c_hits_o[c] in rowFour:
            indexVal = rowFour.index(c_hits_o[c])
            computer_to_opponentrowFour = computer_to_opponentrowFour[:indexVal] + 'X' + computer_to_opponentrowFour[indexVal+1:]
        
        elif c_hits_o[c] in rowThree:
            indexVal = rowThree.index(c_hits_o[c])
            computer_to_opponentrowThree = computer_to_opponentrowThree[:indexVal] + 'X' + computer_to_opponentrowThree[indexVal+1:]
        
        elif c_hits_o[c] in rowTwo:
            indexVal = rowTwo.index(c_hits_o[c])
            computer_to_opponentrowTwo = computer_to_opponentrowTwo[:indexVal] + 'X' + computer_to_opponentrowTwo[indexVal+1:]
        
        elif c_hits_o[c] in rowOne:
            indexVal = rowOne.index(c_hits_o[c])
            computer_to_opponentrowOne = computer_to_opponentrowOne[:indexVal] + 'X' + computer_to_opponentrowOne[indexVal+1:]
    
    
    #create a list with all the values the computer missed
    computer_missed = []
    
    #find which coordinates computer attempted by didn't hit - add to list
    for d in range(0, len(cMoves)):
        if cMoves[d] not in c_hits_o:
            computer_missed.append(cMoves[d])
    
    #add the misses made by the computer by checking the values of the computer_missed list, the index value in a specific row, and replace with -
    for e in range(0, len(computer_missed)):
        if computer_missed[e] in rowSix:
            indexVal = rowSix.index(computer_missed[e])
            computer_to_opponentrowSix = computer_to_opponentrowSix[:indexVal] + '-' + computer_to_opponentrowSix[indexVal+1:]
        
        elif computer_missed[e] in rowFive:
            indexVal = rowFive.index(computer_missed[e])
            computer_to_opponentrowFive = computer_to_opponentrowFive[:indexVal] + '-' + computer_to_opponentrowFive[indexVal+1:]
        
        elif computer_missed[e] in rowFour:
            indexVal = rowFour.index(computer_missed[e])
            computer_to_opponentrowFour = computer_to_opponentrowFour[:indexVal] + '-' + computer_to_opponentrowFour[indexVal+1:]
        
        elif computer_missed[e] in rowThree:
            indexVal = rowThree.index(computer_missed[e])
            computer_to_opponentrowThree = computer_to_opponentrowThree[:indexVal] + '-' + computer_to_opponentrowThree[indexVal+1:]
        
        elif computer_missed[e] in rowTwo:
            indexVal = rowTwo.index(computer_missed[e])
            computer_to_opponentrowTwo = computer_to_opponentrowTwo[:indexVal] + '-' + computer_to_opponentrowTwo[indexVal+1:]
        
        elif computer_missed[e] in rowOne:
            indexVal = rowOne.index(computer_missed[e])
            computer_to_opponentrowOne = computer_to_opponentrowOne[:indexVal] + '-' + computer_to_opponentrowOne[indexVal+1:]
            
    #print out the opponent's board
    print(computer_to_opponentrowSix)
    print(computer_to_opponentrowFive)
    print(computer_to_opponentrowFour)
    print(computer_to_opponentrowThree)
    print(computer_to_opponentrowTwo)
    print(computer_to_opponentrowOne)
    
    
    
    # COMPUTER
    
    print(" ")
    print("Here is the computer's board with the moves you've made:")
    
    opponent_to_computerrowSix = 'oooooo'
    opponent_to_computerrowFive = 'oooooo'
    opponent_to_computerrowFour = 'oooooo'
    opponent_to_computerrowThree = 'oooooo'
    opponent_to_computerrowTwo = 'oooooo'
    opponent_to_computerrowOne = 'oooooo'
    
    #add the hits made by the opponent by checking each value in the o_hits_c list, the index value in a specific row, and replace with X
    for c in range(0, len(o_hits_c)):
        if o_hits_c[c] in rowSix:
            indexVal = rowSix.index(o_hits_c[c])
            opponent_to_computerrowSix = opponent_to_computerrowSix[:indexVal] + 'X' + opponent_to_computerrowSix[indexVal+1:]
        
        elif o_hits_c[c] in rowFive:
            indexVal = rowFive.index(o_hits_c[c])
            opponent_to_computerrowFive = opponent_to_computerrowFive[:indexVal] + 'X' + opponent_to_computerrowFive[indexVal+1:]
        
        elif o_hits_c[c] in rowFour:
            indexVal = rowFour.index(o_hits_c[c])
            opponent_to_computerrowFour = opponent_to_computerrowFour[:indexVal] + 'X' + opponent_to_computerrowFour[indexVal+1:]
        
        elif o_hits_c[c] in rowThree:
            indexVal = rowThree.index(o_hits_c[c])
            opponent_to_computerrowThree = opponent_to_computerrowThree[:indexVal] + 'X' + opponent_to_computerrowThree[indexVal+1:]
        
        elif o_hits_c[c] in rowTwo:
            indexVal = rowTwo.index(o_hits_c[c])
            opponent_to_computerrowTwo = opponent_to_computerrowTwo[:indexVal] + 'X' + opponent_to_computerrowTwo[indexVal+1:]
        
        elif o_hits_c[c] in rowOne:
            indexVal = rowOne.index(o_hits_c[c])
            opponent_to_computerrowOne = opponent_to_computerrowOne[:indexVal] + 'X' + opponent_to_computerrowOne[indexVal+1:]
    
    #create a list with the coordinates the opponent missed
    opponent_missed = []
    
    #check which coordinates the opponent attempted but didn't successfully hit - add to list
    for d in range(0, len(oMoves)):
        if oMoves[d] in o_hits_c:
            continue
        else:
            opponent_missed.append(oMoves[d])
    
    #add the misses made by the opponent by checking the values of the opponent_missed list, the index value in a specific row, and replace with -
    for e in range(0, len(opponent_missed)):
        if opponent_missed[e] in rowSix:
            indexVal = rowSix.index(opponent_missed[e])
            opponent_to_computerrowSix = opponent_to_computerrowSix[:indexVal] + '-' + opponent_to_computerrowSix[indexVal+1:]
        
        elif opponent_missed[e] in rowFive:
            indexVal = rowFive.index(opponent_missed[e])
            opponent_to_computerrowFive = opponent_to_computerrowFive[:indexVal] + '-' + opponent_to_computerrowFive[indexVal+1:]
        
        elif opponent_missed[e] in rowFour:
            indexVal = rowFour.index(opponent_missed[e])
            opponent_to_computerrowFour = opponent_to_computerrowFour[:indexVal] + '-' + opponent_to_computerrowFour[indexVal+1:]
        
        elif opponent_missed[e] in rowThree:
            indexVal = rowThree.index(opponent_missed[e])
            opponent_to_computerrowThree = opponent_to_computerrowThree[:indexVal] + '-' + opponent_to_computerrowThree[indexVal+1:]
        
        elif opponent_missed[e] in rowTwo:
            indexVal = rowTwo.index(opponent_missed[e])
            opponent_to_computerrowTwo = opponent_to_computerrowTwo[:indexVal] + '-' + opponent_to_computerrowTwo[indexVal+1:]
        
        elif opponent_missed[e] in rowOne:
            indexVal = rowOne.index(opponent_missed[e])
            opponent_to_computerrowOne = opponent_to_computerrowOne[:indexVal] + '-' + opponent_to_computerrowOne[indexVal+1:]
        
    #print the computer's board
    print(opponent_to_computerrowSix)
    print(opponent_to_computerrowFive)
    print(opponent_to_computerrowFour)
    print(opponent_to_computerrowThree)
    print(opponent_to_computerrowTwo)
    print(opponent_to_computerrowOne)
        

#values that will be used within the program
rowSix = ["A6", "B6", "C6", "D6", "E6", "F6"]
rowFive = ["A5", "B5", "C5", "D5", "E5", "F5"]
rowFour = ["A4", "B4", "C4", "D4", "E4", "F4"]
rowThree = ["A3", "B3", "C3", "D3", "E3", "F3"]
rowTwo = ["A2", "B2", "C2", "D2", "E2", "F2"]
rowOne = ["A1", "B1", "C1", "D1", "E1", "F1"]
columnOne = ["A1", "A2", "A3", "A4", "A5", "A6"]
columnTwo = ["B1", "B2", "B3", "B4", "B5", "B6"]
columnThree = ["C1", "C2", "C3", "C4", "C5", "C6"]
columnFour = ["D1", "D2", "D3", "D4", "D5", "D6"]
columnFive = ["E1", "E2", "E3", "E4", "E5", "E6"]
columnSix = ["F1", "F2", "F3", "F4", "F5", "F6"]
all_coordinates = rowSix + rowFive + rowFour + rowThree + rowTwo + rowOne
directions = ['north', 'south', 'east', 'west']

#print out the instructions
printInstructions()


play = 'yes'

while play == 'yes':
    
    #plan the ships
    opponent_ships, computer_ships = gameSetup()
    
    #start the moves
    playerMoves(opponent_ships, computer_ships)
    
    #option to replay
    play = input("Do you want to play again? (yes or no)")
    play = play.casefold()
    
    print(" ")
    
    #manage invalid input
    while play != 'yes' and play != 'no':
        print("Not an option!")
        play = input("Do you want to play again? (yes or no)")
        play = play.casefold()
    
    print(" ")


#opponent doesn't want to play another round
print("Good game! Hope to see you soon :)")