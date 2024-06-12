from budget_management import BudgetCategory

def main():
    # Example usage
    food_category = BudgetCategory("Food", 500)
    print(food_category.display_category_summary())

    food_category.add_expense(100)
    print(food_category.display_category_summary())

    # Attempting to add an invalid expense
    try:
        food_category.add_expense(600)
    except ValueError as e:
        print(f"Error: {e}")

    # Attempting to set an invalid budget
    try:
        food_category.budget = -200
    except ValueError as e:
        print(f"Error: {e}")

    # Display final summary
    print(food_category.display_category_summary())

if __name__ == "__main__":
    main()
