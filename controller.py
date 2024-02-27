from model import Model
from view import View

# In MVC the controller knows about the model and the view
# Now we have access to both those classes

# The model isnt aware of the controller or the view
# But the view knows about the controller

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    
    def main(self):
        self.view.main()

# The entry point to the program 
if __name__ == '__main__':
    # print("Hello World")
    
    # Created an instance of the controller
    calculator = Controller()

    # Called the main function on the controller
    calculator.main()