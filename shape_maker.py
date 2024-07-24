def main():
  choice = input("Sides or angles? ").strip().lower()

  if choice == "sides":
      num_sides = int(input("How many sides do you want your shape to have? "))
      print(f"You chose to have a shape with {num_sides} sides.")
  elif choice == "angles":
      num_angles = int(input("How many angles do you want your shape to have? "))
      print(f"You chose to have a shape with {num_angles} angles.")
  else:
      print("Invalid answer. Please pick either 'sides' or 'angles.'")

      


if __name__ == "__main__":
  main()