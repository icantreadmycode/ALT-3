# Special Characters
# !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from dataclasses import dataclass

@dataclass
class passwordRequirements:
    "define password requirements and store in a accessible format"
    bool: requireSpecialCharacters
    bool: requireNumbers
    bool: requireCapitals
    int: passwordLength


