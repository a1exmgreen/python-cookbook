from recipes import recipes

print("================================")
print("       ALEX'S COOKBOOK")
print("================================")

while True: 
    print("\n1. View recipes")
    print("2. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print("\nAvailable recipes:")

        for recipe_name in recipes:
            print(recipe_name.title())

        recipe_choice = input("\nWhich recipe would you like to view? ").lower()

        if recipe_choice in recipes:
            recipe = recipes[recipe_choice]

            print(f"\n--- {recipe_choice.title()} ---")

            print("\nIngredients:")
            for ingredient in recipe["ingredients"]:
                print(f"- {ingredient}")

            print("\nMethod:")
            for step in recipe["method"]:
                print(f"- {step}") 

        else:
            print("\nSorry, that recipe doesn't exist.")

    elif choice == "2":
        print("\nThanks for using Alex's Cookbook!")
        break

    else:
        print("\nInvalid option. Please choose 1 or 2.")