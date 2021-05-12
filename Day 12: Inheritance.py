

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName,lastName,idNumber)
        self.scores=scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sums=0
        for score in scores:
            sums+=score  
            average = sums/len(scores)
        if average<40:
            return 'T'
        elif 40<=average<55:
            return 'D'
        elif 55<=average<70:
            return 'P'
        elif 70<=average<80:
            return 'A'
        elif 80<=average<90:
            return 'E'
        else:
            return 'O'
