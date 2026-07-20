import os

def main():
    """
    This function it's a Mortgage/Loan Calculator
    """
    while True:
        os.system('clear')
        # Get the required parameters.
        loan = input_loan_amount()
        interest = input_annual_interest()
        duration_in_years = input_loan_duration()

        print(repayment_calculation(loan, interest, duration_in_years))

        new_query = input("Would you like to make another calculation? [Y/N]: ")
        
        if new_query.lower() != "y":
            break


def repayment_calculation(loan_amount, annual_interest, loan_duration_in_years):
    """
    This calculator determines the monthly payment
    assuming that interest is compounded monthly.

    Parameters:
        Loan amount
        Annual Percentage Rate (APR)
        Loan duration

    Returns:
        Monthly payement
    """

    # Calculate loan duration in months.
    loan_duration_in_months = round(loan_duration_in_years * 12)

    # Calculate monthly interest.
    # Check if it's a no-interest loan.
    if annual_interest == 0:
        monthly_payment = loan_amount / loan_duration_in_months

    else:
        monthly_interest = annual_interest / 12

        # Calculate monthly payement.
        monthly_payment = loan_amount * (
            monthly_interest / (1 - (
                1 + monthly_interest
                ) ** (-loan_duration_in_months)
            )
        )

    total_to_repay = monthly_payment * loan_duration_in_months
    last_payment_correction = final_payment_adjustment(total_to_repay,
                                          round(monthly_payment, 2),
                                          loan_duration_in_months
    )
    # Generate the answer to print at the end of the program.
    """
    answer = f"\nTo repay ${loan_amount:,.2f}"
    answer += f" in {loan_duration_in_months} months "
    answer += f"at an annual interest of {annual_interest*100:,.2f}%\n"
    answer += f"You will have to repay ${monthly_payment:,.2f} per "
    """
    answer = (
        f"\nTo repay ${loan_amount:,.2f}"
        f" in {loan_duration_in_months} months "
        f"at an annual interest of {annual_interest*100:,.2f}%\n"
        f"You will have to repay ${monthly_payment:,.2f} "
    )
    if loan_duration_in_months == 1:
        answer += "the first month.\n"
    elif last_payment_correction != 0:
        last_payment = monthly_payment + last_payment_correction
        answer += (
            f"per {loan_duration_in_months - 1} months"
            f"\nPlus a final payment of ${last_payment:,.2f}\n"
        )

    else:
        answer += "per month.\n"

    return answer


def input_loan_amount():

    # Ask the user for the loan amount,
    # and check it's a valid float number.
    while True:
        try:
            amount = float(input("Enter the value of the loan: $ "))
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Incorrect value!")
            print("Please enter a number greater than 0.")

    return amount


def input_annual_interest():

    # Ask the user for the Annual Percentage Rate (APR),
    # and check it's a valid number.
    while True:
        try:
            interest = (
                float(
                    input(
                        "Enter the Annual Percentage Rate (APR) [e.g., enter 5 for 5%]: "
                    )
                )
            ) / 100
            if interest < 0:
                raise ValueError
            break
        except ValueError:
            print("Incorrect value!")
            print("Please enter a positive number.")

    return interest


def input_loan_duration():

    # Ask the user for the loan duration,
    # and check it's a valid number.
    while True:
        try:
            duration_years = float(input("Enter the loan duration in years: "))
            if duration_years <= 0:
                raise ValueError
            break
        except ValueError:
            print("Incorrect value!")
            print("Please enter a number greater than 0.")

    return duration_years


def final_payment_adjustment(loan, payment, duration):

    # Calculate if the monthly payments cover the whole amount.
    correction = loan - (payment * duration)

    return correction


if __name__ == "__main__":
    main()