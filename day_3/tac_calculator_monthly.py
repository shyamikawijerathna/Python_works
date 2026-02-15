"""Tax Calculator"""

monthly_income=float(input("Please enter your monthly income :"))
annual_income = monthly_income * 12
tax_amount = 0

if (annual_income) <= 1200000 :
    print("you have no tax")

else :
    taxable_income = (annual_income)- 1200000

    if taxable_income <= 500000 :
     tax_amount = (taxable_income * 0.06) / 12
     print(f" your annual tax is {(taxable_income * 0.06)}")
     print(f" your monthly tax is {(taxable_income * 0.06) / 12}")

    elif taxable_income <= 1000000 :
     tax_amount = (500000 * 0.06 + (taxable_income - 500000) * 0.12) / 12
     print(f" your annual tax is {(500000 * 0.06 + (taxable_income - 500000) * 0.12)}")
     print(f" your monthly tax is {(500000 * 0.06 + (taxable_income - 500000) * 0.12) / 12}")

    elif taxable_income <= 150000 :
        tax_amount = ((500000 * 0.06) + (500000 * 0.12) + (taxable_income - 1000000) * 0.18) / 12
        print(f"your annual tax is {((500000 * 0.06) + (500000 * 0.12) + (taxable_income - 1000000) * 0.18)}")
        print(f"your monthly tax is {((500000 * 0.06) + (500000 * 0.12) + (taxable_income - 1000000) * 0.18) / 12}")

    elif taxable_income <= 2000000 :
        tax_amount = ((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (taxable_income - 1500000) * 0.18) / 12
        print(f"your annual tax is {((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (taxable_income - 1500000) * 0.18)}")
        print(
            f"your monthly tax is {((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (taxable_income - 1500000) * 0.18) / 12}")

    elif taxable_income <= 2500000:
        tax_amount = ((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (taxable_income - 2000000) * 0.24) / 12
        print(
            f"your annual tax is {((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (taxable_income - 2000000) * 0.24)}")
        print(
            f"your Monthly tax is {((500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + (taxable_income - 2000000) * 0.24) / 12}")


print("Monthly take home salary",monthly_income-tax_amount)
