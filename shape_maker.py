def main():
    choice = input("Sides or angles? ").strip().lower()
    
    if choice == "sides":
        num_sides = int(input("How many sides do you want your shape to have? "))
        print(f"You chose to have a shape with {num_sides} sides.")
    else:
        print("Invalid choice. Please choose 'sides'.")

if __name__ == "__main__":
    main()