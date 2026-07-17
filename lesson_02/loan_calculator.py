def main():

    """
    This function it's a Mortgage/Loan Calculator
    This calculator determines the monthly payment
    assuming that interest is compounded monthly.

    Parameters:
        Loan amount
        Annual Percentage Rate (APR)
        Loan duration

    Returns:
        Monthly payement
    """

    # Get the required parameters.
    loan_amount = input_loan_amount()
    annual_interest = input_annual_interest()
    loan_duration_in_years = input_loan_duration()

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
    payment_correction = value_correction(total_to_repay,
                                          round(monthly_payment, 2),
                                          loan_duration_in_months
    )

    # Generate the answer to print at the end of the program.
    answer = f"\nTo repay ${loan_amount:,.2f}"
    answer += f" in {loan_duration_in_months} months "
    answer += f"at an annual interest of {annual_interest*100:,.2f}%\n"
    answer += f"You will have to repay ${monthly_payment:,.2f} per "

    if payment_correction != 0:
        last_payment = monthly_payment + payment_correction
        answer += f"{loan_duration_in_months - 1} months"
        answer += f"\nPlus a final payment of ${last_payment:,.2f}\n"

    else:
        answer += "month.\n"

    print(answer)


def input_loan_amount():

    # Ask the user for the loan amount,
    # and check it's a valid float number.
    while True:
        try:
            amount = float(input("Enter the value of the loan: $ "))
            break
        except ValueError:
            print("Incorrect value!\nPlease enter a valid number.")

    return amount


def input_annual_interest():

    # Ask the user for the Annual Percentage Rate (APR),
    # and check it's a valid number.
    while True:
        try:
            interest = (
                float(
                    input(
                        "Enter the Annual Percentage Rate (APR) [###%]: "
                    )
                )
            ) / 100
            break
        except ValueError:
            print("Incorrect value!\nPlease enter a valid number.")

    return interest


def input_loan_duration():

    # Ask the user for the loan duration,
    # and check it's a valid number.
    while True:
        try:
            duration_years = float(input("Enter the loan duration in years: "))
            if duration_years < 0:
                raise ValueError
            break
        except ValueError:
            print("Incorrect value!")
            print("Please enter a valid number greater than 0.")

    return duration_years


def value_correction(loan, payment, duration):

    # Calculate if the monthly payments cover the whole amount.
    correction = loan - (payment * duration)

    return correction


if __name__ == "__main__":
    main()