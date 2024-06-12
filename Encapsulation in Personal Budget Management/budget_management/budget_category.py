class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__expenses = 0

    # Getter for category name
    @property
    def name(self):
        return self.__name

    # Setter for category name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Category name cannot be empty")
        self.__name = value

    # Getter for allocated budget
    @property
    def budget(self):
        return self.__budget

    # Setter for allocated budget
    @budget.setter
    def budget(self, value):
        if value <= 0:
            raise ValueError("Budget must be a positive number")
        self.__budget = value

    # Method to add an expense
    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("Expense amount must be a positive number")
        if amount > self.remaining_budget:
            raise ValueError("Expense amount exceeds remaining budget")
        self.__expenses += amount

    # Method to get the remaining budget
    @property
    def remaining_budget(self):
        return self.__budget - self.__expenses

    # Method to display category summary
    def display_category_summary(self):
        return f"Category: {self.__name}, Allocated Budget: {self.__budget}, Remaining Budget: {self.remaining_budget}"
