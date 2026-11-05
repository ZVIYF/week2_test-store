import inputs_validation as Inputs

def get_menu_choice():
    while True:
        try:        
            choice = Inputs.get_input("Choose option:")
            Inputs.input_validation(choice, "choice", "int")
            return int(choice)
        except ValueError as error:
            print(f"error: {error}")