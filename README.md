# Ice-Cream-Parlor-Cafe
Welcome to the Ice Cream Cafe project! This repository contains the code and configuration files for running the Ice Cream Cafe application using Docker.

## **Overview:**
This application simulates an ice cream parlor's operations. It is a CLI-based application containerized with Docker.

## **Features:**
1. View Seasonal Flavors: Displays a list of all seasonal flavors.
2. View All Flavors: Shows all available flavors.
3. View Ingredients: Lists all ingredients used in the ice cream parlor.
4. View Allergens: Displays allergens associated with ingredients.
5. Add to Cart: Allows users to add flavors to their cart.
6. View Cart: Displays items in the user's cart.
7. Submit Suggestions: Users can suggest new flavors with comments.
8. Add Allergens: Users can add new allergens.
9. Exit: Gracefully exits the application.

## **Setup and Installation:**

**Pre-requisites:**
- Docker installed on your machine. Download Docker from https://www.docker.com/products/docker-desktop/ and follow the installation steps.
- Basic knowledge of command-line tools.

**Steps to Run the Application:**

- **Clone this repository:**

git clone https://github.com/subha0319/Ice-Cream-Parlor-Cafe

cd IceCreamCafe

- **Build the Docker image:**

docker build -t ice-cream-cafe .

- **Run the Docker container with interactive mode:**

docker run -it -p 5000:5000 ice-cream-cafe

Interact with the application using the menu displayed.

## **Application Flow**
Menu Options

1: View seasonal flavors.

2: View all flavors.

3: View ingredients.

4: View allergens.

5: Add a flavor to your cart.

6: View your cart.

7: Add a flavor suggestion.

8: Add a new allergen.

9: Exit.

## **Testing the Application:**

**Test steps to validate each feature:**

**Test 1: View Seasonal Flavors:**

Select option 1 from the menu.

**Output:**

A list of seasonal flavors:
Seasonal Flavors:
- Strawberry Cheesecake

**Test 2: View All Flavors:**

Select option 2 from the menu.

**Output:**

A list of all flavors:
All Flavors:
- Strawberry Cheesecake
- Vanilla

**Test 3: View Ingredients:**

Select option 3 from the menu.

**Output:**

A list of all ingredients
Ingredients:
- Milk
- Sugar
- Chocolate Chips

**Test 4: View Allergens:**

Select option 4 from the menu.

**Output:**

A list of allergens:
Allergens:
- Nuts
- Dairy

**Test 5: Add to Cart:**

Select option 5 from the menu.
Enter the flavor name when prompted (e.g., Vanilla).

**Output:**

Confirmation message:
Vanilla added to your cart.

**Test 6: View Cart:**

Select option 6 from the menu.

**Output:**

A list of items in the cart:
Your Cart:
- Vanilla

**Test 7: Submit a Flavor Suggestion:**

Select option 7 from the menu.
Enter a flavor name and comment.

**Output:**

Confirmation message:
Your suggestion for Mint Chocolate Chip has been added.

**Test 8: Add a New Allergen:**

Select option 8 from the menu.
Enter an allergen name (e.g., Egg).

**Output:**

Confirmation message:
Allergen 'Egg' added.

## **Future Enhancements:**
Convert CLI-based functionality into a REST API using Flask for web-based interaction.
Implement user authentication for personalized experiences.
Add functionality to delete items from the cart.
