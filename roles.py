# roles.py

# Define roles and their associated permissions according to Finvest Holdings' policy
roles_permissions = {
    "Regular Client": {
        "permissions": [
            "view_account_balance",
            "view_investments",
            "view_contact_financial_advisor"
        ]
    },
    "Premium Client": {
        "permissions": [
            "view_account_balance",
            "view_investments",
            "modify_investments",
            "view_contact_financial_planner",
            "view_contact_investment_analyst"
        ]
    },
    "Financial Advisor": {
        "permissions": [
            "view_account_balance",
            "view_investments",
            "modify_investments",
            "view_private_consumer"
        ]
    },
    "Financial Planner": {
        "permissions": [
            "view_account_balance",
            "view_investments",
            "modify_investments",
            "view_money_market",
            "view_private_consumer"
        ]
    },
    "Investment Analyst": {
        "permissions": [
            "view_account_balance",
            "view_investments",
            "modify_investments",
            "view_money_market",
            "view_derivatives",
            "view_interest",
            "view_private_consumer"
        ]
    },
    "Technical Support": {
        "permissions": [
            "view_client_info",
            "request_account_access"
        ]
    },
    "Teller": {
    "permissions": []
},
    "Compliance Officer": {
        "permissions": [
            "validate_portfolio_modifications"
        ]
    }
}

def get_permissions(role):
    """
    Retrieve the permissions for a given role.
   
    :param role: The role to retrieve permissions for.
    :return: A list of permissions for the role. Empty list if role not found.
    """
    return roles_permissions.get(role, {}).get("permissions", [])

def check_permission(role, permission):
    """
    Check if a given role has a specific permission.
   
    :param role: The role to check the permission for.
    :param permission: The permission to check.
    :return: True if the role has the permission, False otherwise.
    """
    return permission in get_permissions(role)

def add_role(role_name, permissions_list):
    """
    Add a new role with a set of permissions.
   
    :param role_name: The name of the new role.
    :param permissions_list: A list of permissions for the new role.
    """
    roles_permissions[role_name] = {"permissions": permissions_list}

def remove_role(role_name):
    """
    Remove a role from the system.
   
    :param role_name: The name of the role to remove.
    """
    if role_name in roles_permissions:
        del roles_permissions[role_name]

def update_permissions(role_name, permissions_list):
    """
    Update the permissions for an existing role.
   
    :param role_name: The name of the role to update.
    :param permissions_list: The new list of permissions for the role.
    """
    if role_name in roles_permissions:
        roles_permissions[role_name]["permissions"] = permissions_list

def list_roles():
    """
    List all roles and their permissions.
   
    :return: A dictionary of all roles and their permissions.
    """
    return roles_permissions