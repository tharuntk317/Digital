import frappe
from frappe.model.document import Document


class BuyerPayment(Document):
	pass

from frappe.utils import now

@frappe.whitelist()
def after_successful_payment(docname):
    doc = frappe.get_doc("Buyer Payment", docname)
    creator = frappe.db.get_value("Digital Product", doc.product_id, "creator")
    purchase = frappe.get_doc({
        "doctype": "Purchase History",
        "user": doc.owner,
        "product": doc.product_id,
        "creator": creator, 
        "price": doc.product_price,
        "payment_id": doc.payment_id,
        "purchase_date": now()
    })
    purchase.insert(ignore_permissions=True)
    frappe.db.commit()

    return {"status": "ok", "message": "Purchase recorded"}


