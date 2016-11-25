class IncreasingValue:
    def __init__(self):
        self.myValue = 0

    def increment(self):
        self.myValue += 1

    def __repr__(self):
        return "Number is " + str(self.myValue)

    def __str__(self):
        return "Number is " + str(self.myValue)
