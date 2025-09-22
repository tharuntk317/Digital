import frappe

def get_context(context):
    context.products = frappe.get_all(
        "Digital Product",
        fields=["name", "title", "price", "preview_image", "creator","category","download_count"]
    )
    creators = frappe.get_all("Creator Profile", fields=["name", "logo"])
    context.creator_logos = {c.name: c.logo for c in creators}

    return context
