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

    def traceable_fixed_expenses(self):
        traceable_fixed_expenses = self.advertising_traceable + \
                                   self.depreciation + \
                                   self.managers_salary
        return traceable_fixed_expenses

    def product_line_segment_margin(self):
        product_line_segment_margin = self.contribution_margin() - self.traceable_fixed_expenses()
        return product_line_segment_margin

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
    # End: total

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

    # Contribution Income Statement
    print()
    print(f"{'Contribution Income Statement':<45}", end=" ")
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
    print()

    # This section asks for user query about which segment they want to discontinue, and it'll determine if
    # the user should actually discontinue the segment or not
    segments_dict_updated = {key.lower().replace(" ", ""): value for key, value in segments_dict.items()}

    print("List of Segments:")
    for item in range(1, len(name)):
        print(f"  {name[item]}")
    print()

    while True:
        user_segment = input("Enter a segment to discontinue (press 'q' to quit): ").lower().replace(" ", "")

        if user_segment == "q":
            break

        if user_segment in segments_dict_updated:
            lost_contribution_margin = -segments_dict_updated[user_segment]["Contribution Margin"]
            avoidable_fixed_cost = segments_dict_updated[user_segment]["Advertising, traceable"] + \
                                   segments_dict_updated[user_segment]["Salaries of product-line managers"]
            financial_standing = lost_contribution_margin + avoidable_fixed_cost

            if financial_standing < 0:
                print(f"Financial DISADVANTAGE: ${abs(int(financial_standing)):,}")
                print("DO NOT DISCONTINUE")
            else:
                print(f"Financial ADVANTAGE: ${abs(int(financial_standing)):,}")
                print("DISCONTINUE SEGMENT")
        else:
            print("Segment Does not exist")
        print()

    # Addition: data for segment income statement
    traceable_fixed_expenses = list()
    traceable_fixed_expenses.append(total.traceable_fixed_expenses())
    for i in range(len(segments)):
        traceable_fixed_expenses.append(segments[i].traceable_fixed_expenses())

    product_line_segment_margin = list()
    product_line_segment_margin.append(total.product_line_segment_margin())
    for i in range(len(segments)):
        product_line_segment_margin.append(segments[i].product_line_segment_margin())

    # Segment Income Statement
    print()
    print(f"{'Segment Income Statement':<45}", end=" ")
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

    print("Traceable Fixed expenses:")

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

    print(" " * 45, end=" ")
    print("-" * (18 * (segment_amount + 1)))

    print(f"{'Total traceable fixed expenses':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(traceable_fixed_expenses[i]):^17,}", end=" ")
    print()

    print(" " * 45, end=" ")
    print("-" * (18 * (segment_amount + 1)))

    print(f"{'Product line segment margin (loss)':<45}", end=" ")
    for i in range(segment_amount + 1):
        print(f"${int(product_line_segment_margin[i]):^17,}", end=" ")
    print()

    print(f"{'Common fixed expenses':<45}", end=" ")
    print(f"${int(common_fixed_expenses[0]):^17,}", end=" ")
    print()

    print(" " * 45, end=" ")
    print("-" * 20)

    print(f"{'Net operating income (loss)':<45}", end=" ")
    print(f"${int(net_operating_income[0]):^17,}")
