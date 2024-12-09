from database import *
import os

def display_menu():
    print("\nWelcome to the Ice Cream Parlor Cafe!")
    print("1. View all seasonal flavors")
    print("2. View all flavors")
    print("3. View all ingredients")
    print("4. View allergens")
    print("5. Add a flavor to your cart")
    print("6. View your cart")
    print("7. Add a flavor suggestion")
    print("8. Add a new allergen")
    print("9. Exit")

def main():
    if not os.path.exists('ice_cream_shop.db'):
        init_db()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            flavors = get_seasonal_flavors()
            print(f"\nSeasonal Flavors:")
            for flavor in flavors:
                print(f"- {flavor[1]}")
        
        elif choice == '2':
            flavors = get_all_flavors()
            print(f"\nAll Flavors:")
            for flavor in flavors:
                print(f"- {flavor[1]}")

        elif choice == '3':
            ingredients = get_all_ingredients()
            print(f"\nIngredients:")
            for ingredient in ingredients:
                print(f"- {ingredient[1]}")

        elif choice == '4':
            allergens = get_allergens()
            print(f"\nAllergens:")
            for allergen in allergens:
                print(f"- {allergen[1]}")

        elif choice == '5':
            flavor_name = input("Enter the flavor name to add to cart: ")
            flavor = next((f for f in get_all_flavors() if f[1].lower() == flavor_name.lower()), None)
            if flavor:
                add_to_cart(flavor[0])
                print(f"{flavor_name} added to your cart.")
            else:
                print(f"Flavor {flavor_name} not found.")

        elif choice == '6':
            cart_items = view_cart()
            if cart_items:
                print("\nYour Cart:")
                for item in cart_items:
                    print(f"- {item[0]}")
            else:
                print("Your cart is empty.")

        elif choice == '7':
            flavor_name = input("Enter the flavor name: ")
            comment = input("Enter your comment: ")
            add_suggestion(flavor_name, comment)
            print(f"Your suggestion for {flavor_name} has been added.")

        elif choice == '8':
            allergen = input("Enter a new allergen: ")
            add_allergen(allergen)
            print(f"Allergen '{allergen}' added.")

        elif choice == '9':
            print("Thanks for visiting! Come back soon :)")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
