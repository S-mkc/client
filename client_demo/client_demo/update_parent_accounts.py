import frappe

def update_parent_accounts():
    # List of accounts to update with their new parent accounts
    accounts_to_update = [
        {"account_name": "11901 AccDepAdmBuildTechInstal - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        # {"account_name": "Account 2", "new_parent_account": "New Parent 2"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # Add more accounts as needed
    ]

    # Loop through each account and update the parent account
    for account_data in accounts_to_update:
        try:
            account = frappe.get_doc("Account", account_data["account_name"])
            account.parent_account = account_data["new_parent_account"]
            account.save()
            print(f"Successfully updated parent account for {account_data['account_name']}")
        except Exception as e:
            frappe.log_error(message=str(e), title="Failed to update parent account")
            print(f"Error updating {account_data['account_name']}: {e}")

    # Commit the changes to the database
    frappe.db.commit()
