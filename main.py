import random
import time

# Load gun, modify for amount of ammo you'd like
def get_rounds():
    """Prompts the user for the number of bullets and blanks, returns the randomized magazine."""
    while True:
        try:
            bullets = int(input("Enter the amount of bullets you want to play with: "))
            if bullets <= 0:
                print("Number of bullets must be 1 or greater.\n")
                continue
            break
        except ValueError:
            print("Invalid input, enter a number.\n")
            continue

    while True:
        try:
            blanks = int(input("Enter the amount of blanks you want to play with: "))
            if blanks < 0:
                print("Number of blanks must be 0 or greater.\n")
                continue
            break
        except ValueError:
            print("Invalid input, enter a number.\n")
            continue

    # Create list into magazine (True for bullets, False for blanks)
    magazine = [True] * bullets + [False] * blanks
    random.shuffle(magazine)
    return magazine

# Function to shoot
def shoot(magazine):
    """Shoots the next round in the magazine (removes it from the list). Returns True for a bullet, False for a blank."""
    if magazine:
        return magazine.pop(0)
    return False  # No rounds left

def player_turn(magazine):
    """Handles the player's turn to either shoot themselves or the bot."""
    while True:
        choice = input("Do you want to shoot yourself or the bot? (self/bot): ").strip().lower()
        time.sleep(1)
        if choice == "self":
            result = shoot(magazine)
            if result:
                print("BANG! You shot yourself!")
                return "game_over"
            else:
                print("Click! It was a blank. You survive!\n")
                continue
        elif choice == "bot":
            result = shoot(magazine)
            if result:
                print("BANG! You shot the bot!")
                return "bot_lost"
            else:
                print("Click! The shot was a blank. The bot survives!\n")
                return "continue"
        else:
            print("Invalid choice. Please choose 'self' or 'bot'.")

def bot_turn(magazine): 
    """Handles the bot's turn to either shoot itself or the player."""
    while True:
        print("The bot is taking its turn...")
        time.sleep(1)  # 1-second delay for the bot
        choice = random.choice(["self", "player"])
        if choice == "self":
            result = shoot(magazine)
            if result:
                print("BANG! The bot shot itself!")
                return "game_over"
            else:
                print("Click! The bot survives!\n")
                continue
        else:
            result = shoot(magazine)
            if result:
                print("BANG! The bot shot you!")
                return "player_lost"
            else:
                print("Click! The shot was a blank. You survive!\n")
                return "continue"

def main():
    """Main game loop where the player and bot take turns to play."""
    print("Welcome to my Russian Roulette Game!\n")
    print("You will play against a bot. The rules are the following: ")
    print("1. If the shooter shoots themselves, and it's a blank, the shooter gets to go again.")
    print("2. If the shooter shoots the other person, and it's a blank, it goes to the next person's turn.\n")
    
    while True:
        magazine = get_rounds()
        print(f"The game starts with {len(magazine)} rounds in the chamber.\n")
        
        # Turns for player and bot
        while magazine:
            # Player's turn
            result = player_turn(magazine)
            if result == "game_over":
                print("Game Over! You lose!")
                break
            elif result == "bot_lost":
                print("Game Over! The bot loses!")
                break
            
            # Bot's turn
            result = bot_turn(magazine)
            if result == "game_over":
                print("Game Over! The bot loses!")
                break
            elif result == "player_lost":
                print("Game Over! You lose!")
                break
        
        replay = input("Do you want to play again (y/n)? ").lower() == "n"
        print("")
        if replay:
            break

if __name__ == "__main__":
    main()
