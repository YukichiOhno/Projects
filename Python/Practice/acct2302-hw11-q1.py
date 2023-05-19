class Segments:

    def __init__(self):
        self.name = "none"
        self.sales = 0.0
        self.variable = 0.0

        # fixed expenses
        self.advertising_traceable = 0.0
        self.depreciation = 0.0
        self.managers_salary = 0.0
        self.common_fixed_expenses = 0.0

    def contribution_margin(self):
        return self.sales - self.variable

    def total_fixed_expenses(self):
        fixed_expenses = self.advertising_traceable + \
                         self.depreciation + \
                         self.managers_salary + \
                         self.common_fixed_expenses
        return fixed_expenses

    def net_operating_income(self):
        return self.contribution_margin() - self.total_fixed_expenses()


if __name__ == "__main__":
    segment_amount = int(input("Enter the amount of segments: "))
    print()

    segments = []
    for i in range(1, segment_amount+1):
        division = Segments()
        print(f"Division {i} Information")
        division.name = input("Enter name: ")
        division.sales = float(input("Enter total sales: "))
        division.variable = float(input("Enter total variable expenses: "))

        # Fixed Expenses
        division.advertising_traceable = float(input("Enter advertising traceable: "))
        division.depreciation = float(input("Enter depreciation of sales equipment: "))
        division.managers_salary = float(input("Enter salaries of product-line managers: "))
        division.common_fixed_expenses = float(input("Enter allocated common fixed expenses: "))

        segments.append(division)
        print()

    # Start: Total
    total = Segments()
    total.name = "Total"

    # Total Sales
    total.sales = 0.0
    for i in range(len(segments)):
        total.sales = total.sales + segments[i].sales

    # Total Variable Manufacturing and Selling Expenses
    total.variable = 0.0
    for i in range(len(segments)):
        total.variable = total.variable + segments[i].variable

    # Total Fixed Expenses
    total.advertising_traceable = 0.0
    for i in range(len(segments)):
        total.advertising_traceable = total.advertising_traceable + segments[i].advertising_traceable

    total.depreciation = 0.0
    for i in range(len(segments)):
        total.depreciation = total.depreciation + segments[i].depreciation

    total.managers_salary = 0.0
    for i in range(len(segments)):
        total.managers_salary = total.managers_salary + segments[i].managers_salary

    total.common_fixed_expenses = 0.0
    for i in range(len(segments)):
        total.common_fixed_expenses = total.common_fixed_expenses + segments[i].common_fixed_expenses

    # Storing all accounts from each segments + total\
    name = list()
    name.append(total.name)
    for i in range(len(segments)):
        name.append(segments[i].name)

    sales = list()
    sales.append(total.sales)
    for i in range(len(segments)):
        sales.append(segments[i].sales)

    variable = list()
    variable.append(total.variable)
    for i in range(len(segments)):
        variable.append(segments[i].variable)

    contribution_margin = list()
    contribution_margin.append(total.contribution_margin())
    for i in range(len(segments)):
        contribution_margin.append(segments[i].contribution_margin())

    advertising_traceable = list()
    advertising_traceable.append(total.advertising_traceable)
    for i in range(len(segments)):
        advertising_traceable.append(segments[i].advertising_traceable)

    depreciation = list()
    depreciation.append(total.depreciation)
    for i in range(len(segments)):
        depreciation.append(segments[i].depreciation)

    manager_salary = list()
    manager_salary.append(total.managers_salary)
    for i in range(len(segments)):
        manager_salary.append(segments[i].managers_salary)

    common_fixed_expenses = list()
    common_fixed_expenses.append(total.common_fixed_expenses)
    for i in range(len(segments)):
        common_fixed_expenses.append(segments[i].common_fixed_expenses)

    fixed_expenses = list()
    fixed_expenses.append(total.total_fixed_expenses())
    for i in range(len(segments)):
        fixed_expenses.append(segments[i].total_fixed_expenses())

    net_operating_income = list()
    net_operating_income.append(total.net_operating_income())
    for i in range(len(segments)):
        net_operating_income.append(segments[i].net_operating_income())

    # Segments dictionary
    segments_dict = {}
    for i in range(segment_amount + 1):
        segments_dict[name[i]] = {"Sales": sales[i],
                                  "Variable manufacturing and selling expenses": variable[i],
                                  "Contribution Margin": contribution_margin[i],
                                  "Advertising, traceable": advertising_traceable[i],
                                  "Depreciation of special equipment": depreciation[i],
                                  "Salaries of product-line managers": manager_salary[i],
                                  "Allocated common fixed expenses": common_fixed_expenses[i],
                                  "Total fixed expenses": fixed_expenses[i],
                                  "Net Operating Income (Loss)": net_operating_income[i]}

    # Output all Segments including total
    print()
    print(" " * 45, end=" ")
    for i in range(segment_amount + 1):
        print(f"{name[i]:-^17}", end=" ")
    print()

    print("-" * 46, end="")
    print("-" * (18 * (segment_amount + 1)))

    print(f"{'Sales':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(sales[i]):^17,}", end=" ")
    print()

    print(f"{'Variable manufacturing and selling expenses':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(variable[i]):^17,}", end=" ")
    print()

    print(" " * 45, end=" ")
    print("-" * (18 * (segment_amount + 1)))

    print(f"{'Contribution Margin (loss)':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(contribution_margin[i]):^17,}", end=" ")
    print()

    print("Fixed expenses:")

    print(f"{'  Advertising, traceable':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(advertising_traceable[i]):^17,}", end=" ")
    print()

    print(f"{'  Depreciation of special equipment':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(depreciation[i]):^17,}", end=" ")
    print()

    print(f"{'  Salaries of product-line managers':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(manager_salary[i]):^17,}", end=" ")
    print()

    print(f"{'  Allocated common fixed expenses':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(common_fixed_expenses[i]):^17,}", end=" ")
    print()

    print(" " * 45, end=" ")
    print("-" * (18 * (segment_amount + 1)))

    print(f"{'Total fixed expenses':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(fixed_expenses[i]):^17,}", end=" ")
    print()

    print(" " * 45, end=" ")
    print("-" * (18 * (segment_amount + 1)))

    print(f"{'Net operating income (loss)':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(net_operating_income[i]):^17,}", end=" ")
    print()