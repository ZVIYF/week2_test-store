import prints, menu, orders



def main_menu():
    while True:
        try:
            prints.print_main_menu()
            choice = menu.get_menu_choice()
            match choice:
                case 0:
                    break
                case 1:
                    orders.add_new_order()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case _:
                    raise ValueError("choice is not in the menu")
        except ValueError as error:
            print(f"error: {error}")

if __name__ == "__main__":
    main_menu()