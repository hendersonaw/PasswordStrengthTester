class Password:
    """Takes a password and determines password strength."""

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

    def ScoreDeductions(self):
        """Subtracts points based on poor password choices."""

        if self.password.isalpha():         # If password is letters only ( -Total length of password)
            self.strengthScore -= self.length
        elif self.password.isnumeric():     # If password is numbers only ( -Total length of password)
            self.strengthScore -= self.length

        # Consecutive characters (case-insensitive) (-3 points/char)
        previousChar = ""
        for char in self.password:
            if char.lower() == previousChar:
                self.strengthScore -= 3
            else:
                previousChar = char.lower()

        # Consecutive uppercase letters, lowercase letters, or numbers (-2 points/char)
        previousChar = ""
        for char in self.password:
            if char.isupper() and previousChar.isupper():
                self.strengthScore -= 2
            elif char.islower() and previousChar.islower():
                self.strengthScore -= 2
            elif char.isnumeric() and previousChar.isnumeric():
                self.strengthScore -= 2
            previousChar = char

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
        self.ScoreBoundary()

    def RankStrengthScore(self):
        """Provides a rank based on the amount of strength points awarded."""
        if self.strengthScore < 20:
            return "Very Weak. Consider making a longer password or using different types of characters. "
        elif self.strengthScore < 40: 
            return "Weak."
        elif self.strengthScore < 60: 
            return "Good."
        elif self.strengthScore < 80:
            return "Strong."
        else:
            return "Very Strong! Your password scored above 80 points!"