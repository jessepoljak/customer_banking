# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    # Prompt the user to set the CD balance, interest rate, and months for the CD.
    savings_balance = float(input('What is your initial savings account balance in USD? '))
    savings_interest = float(input('What is the percentage interest rate for your savings account? '))
    savings_maturity = int(input('What is the length of months for your savings account? '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("The updated savings balance is: $", format(updated_savings_balance, ',.2f'))
    print("The savings interest earned is: $", format(savings_interest_earned, ',.2f'))


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('What is the percentage interest rate for your CD? '))
    cd_maturity = int(input('What is the length of months for your CD? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("The updated CD balance is: $", format(updated_cd_balance, ',.2f'))
    print("The CD interest earned is: $", format(cd_interest_earned, ',.2f'))


if __name__ == "__main__":
    # Call the main function.
    main()