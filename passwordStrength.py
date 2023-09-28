# Accepted characters (ASCII)
# 0123456789
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# !"#$%&\'()*+,-./:;<=>?@[]^_`{|}~

from dataclasses import dataclass
import os

specialChars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

@dataclass
class passwordRequirements:
    "define password requirements and store in a accessible format"
    requireSpecialCharacters: bool
    requireNumbers: bool
    requireCapitals: bool
    minPasswordLength: int

def handleNotInt(x):
    try:
        return int(x)
    except Exception as err:
        print(f"Bad input: input only numbers.")

def calculateStrength():
    # TODO
    # num of potential chars ^ num of min chars
    # adjust for required capitals (at least 1)
    # adjust for numbers required (at least 1)
    return 1 # this will be the number of possible password that fit the requirements (minimum)

def calculateTime():
    # calculate rough time to guess the password based on output of {calculateStrength}
    return 1

if __name__ == "__main__":  
    running = True
    # take in password requirements
    while running:
        passwordRec = passwordRequirements(
            True if input("Require special characters? (Y/n) ") != "n" else False,
            True if input("Require numbers? (Y/n) ") != "n" else False,
            True if input("Require capital letters? (Y/n) ") != "n" else False,
            handleNotInt(input("Input minimum password length: "))
        )
        print("")

        calculateStrength()
        calculateTime()

        if input("Exit (Y/n) ") == "n":
            os.system('cls')
        else:
            os.system('cls')
            running = False



