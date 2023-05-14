# User Inputs (Static variables)
user_sale_amount = int(input("Enter units sold: "))
user_sales = float(input("Enter total Sales: "))
user_variable_expenses = float(input("Enter total Variable Expenses: "))
user_fixed_expenses = float(input("Enter total Fixed Expenses: "))
print()

# Dynamic variables (Total)
contribution_margin = user_sales - user_variable_expenses
net_operating_income = contribution_margin - user_fixed_expenses

# Dynamic variables (Per Unit)
sales_per_unit = user_sales / user_sale_amount
variable_expenses_per_unit = user_variable_expenses / user_sale_amount
contribution_margin_per_unit = sales_per_unit - variable_expenses_per_unit

# Contribution Income Statement
print(f"{' ':^23} {'Total':^10} {'Per Unit':^10}")
print("-"*45)
print(f"{f'Sales ({user_sale_amount:,})':<23} ${int(user_sales):^9,} ${sales_per_unit:^9,.2f}")
print(f"{'Variable Expenses':<23} ${int(user_variable_expenses):^9,} ${variable_expenses_per_unit:^9,.2f}")
print(f"{' ':^20} {'-'*24}")
print(f"{'Contribution Margin':<23} ${int(contribution_margin):^9,} ${contribution_margin_per_unit:^9,.2f}")
print(f"{'Fixed Expenses':<23} ${int(user_fixed_expenses):^9,}")
print(f"{' ':^20} {'-'*14}")
print(f"{'Net Operating Income':<23} ${int(net_operating_income):^9,}")
print()

while True:
    print("Does the sales volume increase or decrease?")
    sales_volume_determiner = input("Hit\n"
                                    "i - increase\n"
                                    "d - decrease\n"
                                    "q - quit\n")
    print()

    if sales_volume_determiner == "q":
        break
    elif (sales_volume_determiner == "i") or (sales_volume_determiner == "d"):
        print("How much, in units, will the sales volume", end=" ")

        if sales_volume_determiner == "i":
            operator = "+"
            bump = int(input("increase by? "))
        else:
            operator = "-"
            bump = int(input("decrease by? "))

        new_sales_amount = eval(f"{user_sale_amount} {operator} {bump}")
        new_contribution_margin = int(contribution_margin_per_unit * new_sales_amount)
        revised_net_operating_income = int(new_contribution_margin - user_fixed_expenses)

        print(f"Revised Net Operating Income: ${revised_net_operating_income:,}")
        print("Net Operating Income, based on original data,", end=" ")
        if sales_volume_determiner == "i":
            print("increase by", end=" ")
            difference = abs(net_operating_income - revised_net_operating_income)
        else:
            difference = net_operating_income - revised_net_operating_income
            print("decreases by", end=" ")
        print(f"${int(difference):,}\n")
    else:
        print("Invalid option")
        print()
        continue
