# Move handling file for rps
# Author: Chase Quinn
# Date: 3/26/2025

# The userMoveHandler takes in r/R, p/P, s/S as moves (mv)
# then assigns it to a dictionary with the correct data and art

import random
from . import asciiArt

# Handles creating the users move
def userMoveHandler(mv):
    if mv == "r" or mv == "R":
        return {
            "move": "Rock",
            "artwork": asciiArt.rock
        }
    elif mv == "p" or mv == "P":
        return {
            "move": "Paper",
            "artwork": asciiArt.paper
        }
    elif mv == "s" or mv == "S":
        return {
            "move": "Scissors",
            "artwork": asciiArt.scissors
        }

# Handles generating an AI move
def aiMoveHandler():
    # Uses a random int between 1 and 3 to decide the hand being played
    aiMove = random.randint(1, 3)
    if aiMove == 1:
        return {
            "move": "Rock",
            "artwork": asciiArt.rockReversed
        }
    elif aiMove == 2:
        return {
            "move": "Paper",
            "artwork": asciiArt.paperReversed
        }
    elif aiMove == 3:
        return {
            "move": "Scissors",
            "artwork": asciiArt.scissorsReversed
        }
    
# Turn handler to handle how the outcome of the turn is calculated
def handleTurn(mv):
    userMove = userMoveHandler(mv)
    aiMove = aiMoveHandler()

    if userMove["move"] == "Rock":
        if aiMove["move"] == "Rock":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": False,
                "tie": True,
                "artwork": asciiArt.rockVsRock
            }
        elif aiMove["move"] == "Paper":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": False,
                "tie": False,
                "artwork": asciiArt.rockVsPaper
            }
        elif aiMove["move"] == "Scissors":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": True,
                "tie": False,
                "artwork": asciiArt.rockVsScissors
            }
        
    if userMove["move"] == "Paper":
        if aiMove["move"] == "Rock":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": True,
                "tie": False,
                "artwork": asciiArt.paperVsRock
            }
        elif aiMove["move"] == "Paper":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": False,
                "tie": True,
                "artwork": asciiArt.paperVsPaper
            }
        elif aiMove["move"] == "Scissors":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": False,
                "tie": False,
                "artwork": asciiArt.paperVsScissors
            }
    
    if userMove["move"] == "Scissors":
        if aiMove["move"] == "Rock":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": False,
                "tie": False,
                "artwork": asciiArt.scissorsVsRock
            }
        elif aiMove["move"] == "Paper":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": True,
                "tie": False,
                "artwork": asciiArt.scissorsVsPaper
            }
        elif aiMove["move"] == "Scissors":
            return {
                "playerArt": userMove["artwork"],
                "playerMove": userMove["move"],
                "aiArt": aiMove["artwork"],
                "aiMove": aiMove["move"],
                "win": False,
                "tie": True,
                "artwork": asciiArt.scissorsVsScissors
            }