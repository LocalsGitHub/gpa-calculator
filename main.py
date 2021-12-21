# Grade Point Average Calculator

class calculator():
    
    def __init__(self):
        # Initialize user inputted variables
        
        self.class1 = input('Enter Math Grade: ')
        self.class2 = input('Enter Elective Grade: ')
        self.class3 = input('Enter P.E Grade: ')
        self.class4 = input('Enter English Grade: ')
        self.class5 = input('Enter Science Grade: ')
        self.class6 = input('Enter Social Studies Grade: ')
        
        # Call calculator function
        self.result = self.calculate(self.class1, self.class2, self.class3, self.class4, self.class5, self.class6)
        
        
    def calculate(self, class1, class2, class3, class4, class5, class6):
        # Create needed variables
        
        newClasses = []
        newClasse = []
        convert = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        classes = [class1, class2, class3, class4, class5, class6]
        
        for i in classes:
            # Remove minues and pluses from classes variable
            if '-' in i:
                newClasse.append(i.strip('-'))
            elif '+' in i:
                newClasse.append(i.strip('+'))
            else:
                newClasse.append(i)
                
        # Take percentage grade and attach it to letter grade
        for class1 in newClasse:
            if class1.isdigit():
                if int(class1) == 100:
                    newClasses.append("A")
                elif int(class1) < 100 and int(class1) >= 90:
                    newClasses.append("A")
                elif int(class1) < 90 and int(class1) >= 80:
                    newClasses.append("A")
                elif int(class1) < 80 and int(class1) >= 70:
                    newClasses.append("B")
                elif int(class1) < 70 and int(class1) >= 60:
                    newClasses.append("C")
                elif int(class1) < 60 and int(class1) >= 50:
                    newClasses.append("D")
                elif int(class1) < 50 and int(class1) >= 0:
                    newClasses.append("F")
            else:
                # Incase of user inputted grade already being a letter, we simply append it to our list
                newClasses.append(class1)
        
        for i in newClasses:
            if i not in convert:
                print('Error: Invalid Grade')
                return
        try:
            # Calculate GPA
            return (convert[newClasses[0]] + convert[newClasses[1]] + convert[newClasses[2]] + convert[newClasses[3]] + convert[newClasses[4]] + convert[newClasses[5]]) / 6
        except IndexError:
            print('Error: Invalid Grade')
            exit()
        
    def print_result(self) -> str:
        try:
            print('\nYour GPA is: ' + str(round(float(self.result), 1)))
        except TypeError:
            print('\nError: Invalid Grade')

Calc = calculator()
Calc.print_result()
