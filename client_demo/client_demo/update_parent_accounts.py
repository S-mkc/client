import frappe

def update_parent_accounts():
    # List of accounts to update with their new parent accounts
    accounts_to_update = [
        {"account_name": "11901 AccDepAdmBuildTechInstal - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11900 - AccDepAdmBuildStructure - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11902 - AccDepAdmBuildTeleAut - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11906 - AccDepOtherOperBuildStructure - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11907 - AccDepOtherOperBuildTechInstal - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11908 - AccDepOtherOperBuildTeleAut - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11920 - AccDepDamInstal - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11921 - AccDepTunnelSystem - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11922 - AccDepRockRoom - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11923 - AccDepRoadBridgeQuay - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11930 - AccDepPipeLine - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11931 - AccDepMechEquipWaterPath - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11932 - AccDepTurbine - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11933 - AccDepOtherMachineTechPart - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11940 - AccDepGeneratorPrimaryPart - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11941 - AccDepTransformerSecondaryPart - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11942 - AccDepSwitchGearHighVolt - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11943 - AccDepControlGear - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11944 - AccDepElectroTechAuxGear - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11945 - AccDepSystemControlCentre - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "11946 - AccDepTelecommCircuit - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12900 - AccDepMachinery - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12940 - AccDepMeansTransport - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12950 - AccDepFurniture - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12960 - AccDepPermBuildFixture - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12970 - AccDepTool - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12980 - AccDepComputerHardware - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12981 - AccDepComputerSoftware - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12982 - AccDepOfficeMachine - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12983 - AccDepElectricAppliances - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12984 - AccDepPhones/PhoneSystems - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12985 - AccDepOtherOfficeEquip - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        {"account_name": "12990 - AccDepOtherFixedAsset - HPL", "new_parent_account": "1780 - Accumulated Depreciation - HPL"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
        # {"account_name": "Account 3", "new_parent_account": "New Parent 3"},
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
