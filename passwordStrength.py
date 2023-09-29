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

def handleNotInt(x):
    try:
        return int(x)
    except Exception as err:
        print(f"Bad input: input only numbers.")

def product(inputlist: list):
    result = 1
    for i in range(len(inputlist)):
        result *= inputlist[i]
    return result


def calculateStrength(passRec: passwordRequirements):
    # TODO
    # num of potential chars ^ num of min chars
    # adjust for required capitals (at least 1)
    # adjust for numbers required (at least 1)
    possiblities = [0]*passRec.minPasswordLength
    for i in range(passRec.minPasswordLength):
        if passRec.requireCapitals and i > 1:
            possiblities[i] = len(capitalAlpha)
        if passRec.requireNumbers and i > 2:
            possiblities[i] = len(nums)
        if passRec.requireSpecialCharacters and i > 3:
            possiblities[i] = len(specialChars)
        else:
            # print(f"""
            #     all: {allAlpha} {len(allAlpha)}
            #     cap: {capitalAlpha} {len(capitalAlpha)}
            #     nums: {nums} {len(nums)}
            #     spec: {specialChars} {len(specialChars)}
            # """)
            possiblities[i] = len(allAlpha) + len(nums) + len(specialChars)
    
    return product(possiblities)

def calculateTime(permutations):
    # calculate rough time to guess the password based on output of {calculateStrength} 10 per second
    seconds = permutations
    minutes = 0
    hours = 0
    days = 0
    if seconds < (60**2)*24:
        if seconds < 60**2:
            if seconds < 60:
                pass
            else:
                minutes = math.floor(seconds / 60)
                seconds = seconds - (minutes * 60)
        else:
            minutes = math.floor(seconds / 60)
            hours = math.floor(minutes / 60)
            seconds = seconds - (minutes * 60)
            minutes = minutes - (hours * 60)
    else:
        minutes = math.floor(seconds / 60)
        hours = math.floor(minutes / 60)
        days = math.floor(hours / 24)
        

    return f"{days}d: {hours}h: {minutes}m: {seconds}s"        


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

        perm = calculateStrength(passwordRec)
        print("number of permuatitions: ", perm)
        print(calculateTime(perm))

        if input("Exit (Y/n) ") == "n":
            os.system('cls')
        else:
            os.system('cls')
            running = False



