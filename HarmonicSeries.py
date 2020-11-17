"""
   * Author - danish
   * Date - 16/11/20
   * Time - 9:58 AM
   * Title - Find Hormonic Series Of N'th Number and addition 
"""
class HarmonicNumber:
        # Definning constructor method
        def __init__(self,number):
                self.number = number

        # Method to check number is valid or not
        def checkValidNumber(self):
                if self.number > 0:
                        print(f"Result: {HarmonicNumber.harmonicSum(self.number)}")
                else:
                        print("Not a valid number.")

        # Method to calculate harmonic sum
        def harmonicSum(number):
                if number == 1:
                        return 1
                else:
                        return (1/number + HarmonicNumber.harmonicSum(number-1))

if __name__ == "__main__":
        number  = int(input("Enter a Number: "))
        harmonicObject = HarmonicNumber(number)
        harmonicObject.checkValidNumber()
