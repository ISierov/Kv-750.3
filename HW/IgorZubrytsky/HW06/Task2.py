while True :
    login = input("Input login:\n") 
    match login:
        case "First" | "first":
            print(f'Hello {login} user!')
            break
        case _:
            print('Try again!')
        

   
