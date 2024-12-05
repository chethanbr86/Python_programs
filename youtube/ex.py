while True:
    try:
        user_input = int(input("Enter a number: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Error: That's not a valid number. Please enter an integer.")

print(f"You entered the number: {user_input}")


    