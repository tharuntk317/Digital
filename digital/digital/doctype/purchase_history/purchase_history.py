

import frappe

from frappe.model.document import Document

class PurchaseHistory(Document):
    pass

@frappe.whitelist()
def creator_earning(name, doctype):
    doc = frappe.get_doc(doctype, name)
    product = frappe.get_doc("Digital Product", doc.product)
    product_price = float(product.price or 0)
    gst = round(product_price * 0.10, 2)
    net_price = product_price - gst
    creator_name = product.creator
    data = frappe.get_all("Creator Profile", filters={"display_name": creator_name}, fields=["name"])
    creator_profile = frappe.get_doc("Creator Profile", data[0].name) if data else frappe.get_doc({
        "doctype": "Creator Profile",
        "display_name": creator_name
    }).insert()
    creator_profile.total_earnings = [r for r in creator_profile.total_earnings if r.product_id != "TOTAL"]
    existing = next((r for r in creator_profile.total_earnings if r.product_id == doc.product), None)
    if existing:
        existing.product_price += net_price
        existing.gst += gst
        existing.result = existing.product_price - existing.gst
    else:
        creator_profile.append("total_earnings", {
            "product_id": doc.product,
            "gst": gst,
            "product_price": net_price,
            "result": net_price - gst
        })
    total_gst = sum(r.gst for r in creator_profile.total_earnings)
    total_price = sum(r.product_price for r in creator_profile.total_earnings)
    total_result = sum(r.result for r in creator_profile.total_earnings)

    creator_profile.append("total_earnings", {
        "product_id": "TOTAL",
        "gst": total_gst,
        "product_price": total_price,
        "result": total_result
    })
    creator_profile.total_earning_amount = total_price
    creator_profile.save()
    frappe.db.commit()
    frappe.msgprint(f"Earning added for creator '{creator_name}' (Price ₹{product_price}, GST ₹{gst})")
    return "Creator earnings updated successfully."
