def feet_to_yards():
    try:
        # Prompt the user to enter a value in feet
        feet = float(input("Enter your feet: "))

        # Check if the value is negative
        if feet < 0:
              print("Error: Feet cannot be negative. Please enter a positive number.")
        else:
            # Convert feet to yards using the formula yards = feet / 3
            yards = feet / 3

            # Output the result in yards
            print(f"The equivalent value in yards is: {yards:.2f} yards.")

            # Ask for confirmation of user satisfaction
            satisfied = input("Are you satisfied with the result? (yes/no): ").strip().lower()

            if satisfied == "yes":
                print("Thank you! Have a great day.")
            else:
                print("Sorry you're not satisfied. Feel free to try again later.")

    except ValueError:
        # Handle invalid (non-numeric) input
        print("Error: Please enter a valid number.")


# Call the function to execute
(feet_to_yards())

