import frappe

def get_context(context):
    context.product = frappe.get_doc("Creator Profile","Tharun")
    return context
