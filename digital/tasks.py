import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def send_good():
    user = "administrator@gmail.com"
    task = "Create at least one new product today"

    if not frappe.db.exists("ToDo", {"owner": user, "date": nowdate(), "description": task}):
        frappe.get_doc({
            "doctype": "ToDo",
            "owner": user,
            "assigned_by": "Administrator",
            "description": task,
            "allocated_to": "creator@gmail.com",
            "date": nowdate(),
            "priority": "Medium"
        }).insert(ignore_permissions=True)
        frappe.msgprint(f"Task assigned to {user}: {task}")
