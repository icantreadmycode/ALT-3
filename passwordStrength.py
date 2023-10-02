# Accepted characters (ASCII)
# 0123456789
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# !"#$%&\'()*+,-./:;<=>?@[]^_`{|}~
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~

from dataclasses import dataclass
import os
import math

specialChars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
allAlpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
capitalAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"

@dataclass
class passwordRequirements:
    "define password requirements and store in a accessible format"
    requireSpecialCharacters: bool
    requireNumbers: bool
    requireCapitals: bool
    minPasswordLength: int

def handleNotInt(x, default: int):
    # handle int to str conversion
    try:
        return int(x)
    except ValueError: # catch error (Value error specifically)
        print(f"Bad input: {x} is not valid. input whole numbers only. defaulting to {default}")
        return default

def product(inputlist: list):
    # multiply list of ints together
    result = 1
    for i in range(len(inputlist)):
        result *= inputlist[i]
    return result


def calculateStrength(passRec: passwordRequirements):
    # calculate the number of possible permutations the given requirements can be arranged
    possiblities = [0]*passRec.minPasswordLength
    for i in range(passRec.minPasswordLength): # loop over the length of the minPasswordLength
        if passRec.requireCapitals and i == 1:
            possiblities[i] = len(capitalAlpha) 
        elif passRec.requireNumbers and i == 2:
            possiblities[i] = len(nums)
        elif passRec.requireSpecialCharacters and i == 3:
            possiblities[i] = len(specialChars)
        else:
            possiblities[i] = len(allAlpha) + len(nums) + len(specialChars) # calculate the total amount of characters when all can be used
    
    return product(possiblities)

def calculateTime(permutations, persec):
    # calculate rough time to guess the password based on output of {calculateStrength} 10 per second
    seconds = permutations / int(persec)
    minutes = 0
    hours = 0
    days = 0
    if seconds < (60**2)*24: # if there is less than a days worth of seconds
        if seconds < 60**2: # if there is less than an hours worth of seconds
            if seconds < 60: # if there is less than a minutes worth of seconds
                pass
            else:
                minutes = math.floor(seconds / 60) # calculate minutes and seconds
                seconds = seconds - (minutes * 60)
        else:
            minutes = math.floor(seconds / 60) # calculate hours, minutes and seconds
            hours = math.floor(minutes / 60)
            seconds = seconds - (minutes * 60)
            minutes = minutes - (hours * 60)
    else:
        minutes = math.floor(seconds / 60) # calculate days, hours, minutes and seconds
        hours = math.floor(minutes / 60)
        days = math.floor(hours / 24)
        hours = hours - days*24
        minutes = minutes - (hours*60) - (days*24*(60))
        seconds = seconds - minutes*60 - (hours*60**2) - (days*24*(60**2))


    return f"it could take up to {days:,} days, {hours} hours, {minutes} minutes and {seconds} seconds to brute force the password."        


if __name__ == "__main__":  
    os.system('cls')
    running = True
    # take in password requirements
    while running:
        passwordRec = passwordRequirements(
            True if input("Require special characters? (y/N) ") == "y" else False,
            True if input("Require numbers? (y/N) ") == "y" else False,
            True if input("Require capital letters? (y/N) ") == "y" else False,
            handleNotInt(input("Input minimum password length: "), 4)
        )
        persec = handleNotInt(input("input guesses per second: "), 1)

        perm = calculateStrength(passwordRec)
        print("\nnumber of permutations: ", perm)
        print(calculateTime(perm, persec))

        if input("\nExit (Y/n) ") == "n":
            os.system('cls')
        else:
            os.system('cls')
            running = False



