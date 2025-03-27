# Main entry point for rps (Console-Based Rock Paper Scissors)
# Author: Chase Quinn
# Date: 3/26/2025

import sys, time
from rps import moves, asciiArt

# Function to get the input from the user,
# verify it is correct and not allow continuation of 
# the application until the criteria is met
def getUserInput():
    mv = input("What is your move? (r/p/s)")
    if mv != "r" and mv != "R" and mv != "p" and mv != "P" and mv != "s" and mv != "S" and mv != "q" and mv != "Q":
        print("Your selection was incorrect... Please use r, p, s, or q as a selection.")
        return getUserInput()
    else:
        return mv

def checkQuit(mv):
    if mv == "q" or mv == "Q":
        print("Exiting RPS...")
        time.sleep(2)
        sys.exit()


# Get information on the round outcome
def handleRound(mv):
    outcome = moves.handleTurn(mv)
    return outcome

# Game loop variable
RUNNING = True

print("You can exit the program by entering 'q' for quit.")
time.sleep(2)

while RUNNING == True:
    mv = getUserInput()
    checkQuit(mv)
    roundInfo = handleRound(mv)
    print(roundInfo["artwork"])
    if roundInfo["win"] != True and roundInfo["tie"] != True:
        print(f"\nYou lose! Your opponent won with: {roundInfo["aiMove"]}\n")
        time.sleep(1)
        print(f"{roundInfo["aiArt"]}\n\n")
        time.sleep(2)
    if roundInfo["win"] != True and roundInfo["tie"] == True:
        print(f"It's a tie! You both chose {roundInfo["playerMove"]}\n")
        time.sleep(1)
        print(f"{asciiArt.tie}\n\n")
        time.sleep(2)
    if roundInfo["win"] == True and roundInfo["tie"] != True:
        print(f"\nYou win! You won with: {roundInfo["playerMove"]}\n")
        time.sleep(1)
        print(f"{roundInfo["playerArt"]}\n\n")
        time.sleep(2)