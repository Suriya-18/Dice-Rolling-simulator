import random

def roll_dice(num_dice):
    """Simulate rolling `num_dice` six-sided dice."""
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        # Ask the user for the number of dice they want to roll
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice < 1:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        # Roll the dice and display the results
        results = roll_dice(num_dice)
        print(f"You rolled: {results}")
        
        # Ask if the user wants to roll again
        again = input("Would you like to roll again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
