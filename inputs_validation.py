def input_validation(user_input:str, messege, level=None):
    match level:
        case "str":
            if not user_input:
                raise ValueError(f"{messege} can't be empty")
        case "int":
            if not user_input:
                raise ValueError(f"{messege} can't be empty")
            elif not user_input.isdigit():
                raise ValueError(f"{messege} must be a whole number")
        case "positive":
            if not user_input:
                raise ValueError(f"{messege} can't be empty")
            elif not user_input.isdigit():
                raise ValueError(f"{messege} must be a whole number")
            elif int(user_input) <= 0:
                raise ValueError(f"{messege} must be a positive number")
            


def get_input(messege: str):
    while True:
        user_input = input(messege).strip()
        return user_input

if __name__ == "__main__":
    print("1".isdigit())