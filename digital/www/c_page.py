import frappe

def get_context(context):
    context.profile = frappe.get_doc("Buyer Profile","Kven")
    return context
