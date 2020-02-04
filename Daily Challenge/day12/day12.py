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
    def __init__(self,firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        final = sum(self.scores)/len(self.scores)
        if (final >= 90 and final <= 100):
            return 'O'
        elif(final >= 80 and final < 90):
            return 'E'
        elif(final >= 70 and final < 80):
            return 'A'
        elif(final >= 55 and final < 70):
            return 'P'
        elif(final >= 40 and final < 55):
            return 'D'
        elif(final<40):
            return 'T'
