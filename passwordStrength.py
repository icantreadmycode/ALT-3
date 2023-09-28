# Special Characters
# !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from dataclasses import dataclass

running = True

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

if __name__ == "__main__":  
    # take in password requirements
    while running:
        passwordRec = passwordRequirements(
            True if input("Require special characters? (Y/n) ") != "n" else False,
            True if input("Require numbers? (Y/n) ") != "n" else False,
            True if input("Require capital letters? (Y/n) ") != "n" else False,
            handleNotInt(input("Input minimum password length: "))
        )

        print(passwordRec)

        if input("Exit (Y/n)") == "n":
            None
        else:
            running = False



