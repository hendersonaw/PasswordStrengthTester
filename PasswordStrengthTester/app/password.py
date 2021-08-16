__author__ = 'Aaron Henderson'

# Password scoring algorithm based on https://www.uic.edu/apps/strong-password/ #

import os

class Password:
    """Contains a password, provides statistics on password, and calculates password strength."""

    def __init__(self, password):
        self.password = password
        self.strengthScore = 0
        self.length = len(self.password)
        self.upperCase = 0     ## Upper case letters
        self.lowerCase = 0     ## Lower case letters
        self.number = 0
        self.space = 0
        self.other = 0

    def ScoreLength(self):
        """Calculates strength score based on password length."""
        self.strengthScore += self.length * 4

    def ScoreCharTypes(self, DEBUG=False):
        """Calculates strength score based on character types."""
        for char in self.password:
            if char.isupper():
                self.upperCase += 1
            elif char.islower():
                self.lowerCase += 1
            elif char.isnumeric():
                self.number += 1
            elif char.isspace():
                self.space += 1
            else:
                self.other += 1

        if(DEBUG == True):
            self.PrintPasswordStats()

        # Score calculations (Upper case, lower case, numbers, spaces, others)
        self.strengthScore += (self.length - self.upperCase) * 2
        self.strengthScore += (self.length - self.lowerCase) * 2
        self.strengthScore += self.number * 4
        self.strengthScore += self.space * 6
        self.strengthScore += self.other * 6

    def isLettersOnly(self):
        """Determines if password is letters only, excluding spaces ( Score -= Total length of password)."""

        for char in self.password:
            if not (char.isalpha() or char.isspace()):
                return None
        self.strengthScore -= self.length

    def isNumbersOnly(self):
        """Determines if password is numbers only, excluding spaces ( Score -= Total length of password)."""

        for char in self.password:
            if not (char.isnumeric() or char.isspace()):
                return None
        self.strengthScore -= self.length

    def repeatCharacters(self):
        """Determines if password contains consecutive characters (case-insensitive) (-3 points/char)."""

        previousChar = ""
        for char in self.password:
            if char.lower() == previousChar:
                self.strengthScore -= 3
            else:
                previousChar = char.lower()

    def consecutiveCharTypes(self):
        """Determines if password contains consecutive uppercase letters, lowercase letters, or numbers (-2 points/char)."""

        previousChar = ""
        for char in self.password:
            if char.isupper() and previousChar.isupper():
                self.strengthScore -= 2
            elif char.islower() and previousChar.islower():
                self.strengthScore -= 2
            elif char.isnumeric() and previousChar.isnumeric():
                self.strengthScore -= 2
            elif char.isspace() and previousChar.isspace():
                self.strengthScore -= 2
        
            previousChar = char

    def sequentialChars(self):
        """Determine if a series of 3 or more letters or numbers in password are sequential."""
        for i in range(0, self.length - 2):
            if ord(self.password[i]) + 1 == ord(self.password[i+1]):
                if ord(self.password[i+1]) + 1 == ord(self.password[i+2]):
                    self.strengthScore -= 3

            elif ord(self.password[i]) - 1 == ord(self.password[i+1]):
                if ord(self.password[i+1]) - 1 == ord(self.password[i+2]):
                    self.strengthScore -= 3

    def minimumRequirements(self):
        """Determines if password meets minimum strength requirements.
            Passwords should be at least 10 characters in length with at least one of each 
            of the following character types: Upper case, lower case letter, number, symbol."""
        if self.length >= 10:
            if self.upperCase > 0 and self.lowerCase > 0 and self.number > 0 and self.other > 0:
                self.strengthScore += 5

    def ScoreDeductions(self):
        """Subtracts points based on poor password choices."""
        self.isLettersOnly()
        self.isNumbersOnly()
        self.repeatCharacters()
        self.consecutiveCharTypes()
        self.sequentialChars()
        self.minimumRequirements()

    def PrintPasswordStats(self):
        """Prints out a nicely formatted table of password statistics."""
        print(self.password)
        print("Upper Case Letters: " + str(self.upperCase))
        print("Lower Case Letters: " + str(self.lowerCase))
        print("           Numbers: " + str(self.number))
        print("            Spaces: " + str(self.space))
        print("             Other: " + str(self.other))

    def ScoreBoundary(self):
        """Checks to make sure strength score is between 0-100 points."""
        if self.strengthScore < 0:
            self.strengthScore = 0
        elif self.strengthScore > 100:
            self.strengthScore = 100

    def CalculateScore(self):
        """Calculates the total strength score of the given password."""
        self.ScoreLength()
        self.ScoreCharTypes()
        self.ScoreDeductions()
        self.BannedPasswords()
        self.ScoreBoundary()

    def BannedPasswords(self):
        """Determines if password contains anything related to Ballad Health is in 
           of if password is in 1MillionBannedPasswords.txt from SecList's common passwords."""
        if "ballad" in self.password.lower():
            self.FoundBannedPassword()
            return None
        elif "health" in self.password.lower():
            self.FoundBannedPassword()
            return None

        passwordFile = open(os.getcwd() + "\\1MillionBannedPasswords.txt", "r")
        word = passwordFile.readline().strip()
        while word:
            if word == self.password:
                self.FoundBannedPassword()
                break;
            else:
                word = passwordFile.readline().strip()

        passwordFile.close()

    def FoundBannedPassword(self):
        """Subtracts 50 points or halves strength score, whichever is a harsher penalty."""
        if self.strengthScore / 2 > 50:
            self.strengthScore = int(self.strengthScore / 2)
        else:
            self.strengthScore -= 50

    def RankStrengthScore(self):
        """Provides a rank based on the amount of strength points awarded."""
        if self.strengthScore < 20:
            return "Very Weak. Consider making a longer password or using different types of characters."
        elif self.strengthScore < 40: 
            return "Weak."
        elif self.strengthScore < 60: 
            return "Moderate."
        elif self.strengthScore < 80:
            return "Strong."
        else:
            return "Very Strong! Your password scored above 80 points!"