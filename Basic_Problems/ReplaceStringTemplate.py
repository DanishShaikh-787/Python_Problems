"""
   * Author - danish
   * Date - 16/11/20
   * Time - 12:31 AM
   * Title - Replace String Template “Hello <<UserName>>, How are you?”
"""
class HelloUser:
        # Defining constructor methods
        def __init__(self, userName):
                self.userName = userName

        # Method to display hello message
        def displayMessage(self):
                if (len(self.userName) > 2):
                        print(f"Hello {self.userName}, How are you?")
                else:
                        print("Entered Name Minimum Three Character")

if __name__ == "__main__":
        username = input("Enter your name: ")
        nameObject = HelloUser(username)
        nameObject.displayMessage()
