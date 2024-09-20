# access_control.py

import datetime
import roles

# Updated user roles to include Finvest Holdings roles
users = {
    'misha_lowery': 'Regular Client',
    'veronica_perez': 'Regular Client',
    'winston_callahan': 'Teller',
    'kelan_gough': 'Teller',
    'nelson_wilkins': 'Financial Advisor',
    'kelsie_chang': 'Financial Advisor',
    'howard_linkler': 'Compliance Officer',
    'stefania_smart': 'Compliance Officer',
    'willow_garza': 'Premium Client',
    'nala_preston': 'Premium Client',
    'stacy_kent': 'Investment Analyst',
    'keikilana_kapahu': 'Investment Analyst',
    'kodi_matthews': 'Financial Planner',
    'malikah_wu': 'Financial Planner',
    'caroline_lopez': 'Technical Support',
    'pawel_barclay': 'Technical Support',
    
}

# resources.py

resources = {
    'account_balance': 'view_account_balance',
    'investments_portfolio': 'view_investments',
    'modify_portfolio': 'modify_investments',
    'contact_details_financial_advisor': 'view_contact_financial_advisor',
    'contact_details_financial_planner': 'view_contact_financial_planner',
    'contact_details_investment_analyst': 'view_contact_investment_analyst',
    'money_market_instruments': 'view_money_market',
    'private_consumer_instruments': 'view_private_consumer',
    'derivatives_trading': 'view_derivatives',
    'interest_instruments': 'view_interest',
    'client_information': 'view_client_info',
    'client_account_access': 'request_account_access',
    'validate_investment_portfolio': 'validate_portfolio_modifications',
    'teller_access': 'access_during_business_hours',
    # Additional resources can be added here as needed.
}


# Function to simulate user authentication (placeholder for real authentication)
def authenticate_user(username):
    # For this mock, we assume the user is already authenticated
    return users.get(username, None)

# Function to check if a user has access to a specific resource
def check_access(username, resource):
    current_time = datetime.datetime.now().time()
    business_hours_start = datetime.time(9, 0)
    business_hours_end = datetime.time(17, 0)

    user_role = authenticate_user(username)
    if user_role is None:
        return False, "User not found or not authenticated."

    # Check for business hours if the user is a Teller
    if user_role == 'Teller':
        if not (business_hours_start <= current_time <= business_hours_end):
            return False, "Teller access is restricted to business hours."
        else:
            # Assuming Tellers have no further permissions to check
            return True, "Access granted for Teller within business hours."

    # For other roles, check the permissions as usual
    required_permission = resources.get(resource, None)
    if required_permission is None:
        return False, "Resource not found."

    if roles.check_permission(user_role, required_permission):
        return True, "Access granted."
    else:
        return False, "Access denied."


# Main function to drive the access control checks
def main():
    test_cases = [
        # Test Regular Client access
        ('misha_lowery', 'account_balance', True),
        ('misha_lowery', 'investments_portfolio', True),
        ('misha_lowery', 'modify_portfolio', False),


        # Test Investment Analyst access
        ('stacy_kent' , 'modify_portfolio', True),
        
        # Test Premium Client access
        ('willow_garza', 'account_balance', True),
        ('willow_garza', 'investments_portfolio', True),
        ('willow_garza', 'modify_portfolio', True),



       
    ]

    # Iterate over the test cases and check access
    for username, resource, expected in test_cases:
        access, message = check_access(username, resource)
        assert access == expected, f"Test failed for user '{username}' accessing '{resource}'. Expected {'access granted' if expected else 'access denied'}, but got {'access granted' if access else 'access denied'}."
        print(f"Test Case - User: '{username}', Resource: '{resource}', Expected: {'Granted' if expected else 'Denied'}, Result: {message}")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()