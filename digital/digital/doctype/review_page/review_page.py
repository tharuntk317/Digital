# import frappe
# from frappe.model.document import Document
# class ReviewPage(Document):
#     pass


import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class ReviewPage(Document):
    def after_insert(self):
        if not self.product:
            frappe.throw("Product must be linked to save a review.")
        product_doc = frappe.get_doc("Digital Product", self.product)
        product_doc.append("reviews", {
            "rating": getattr(self, "make_star", 0),
            "feedback": getattr(self, "feedback", ""),
            "review_date": getattr(self, "review_date", nowdate())
        })
        product_doc.flags.ignore_validate_update_after_submit = True
        product_doc.save(ignore_permissions=True)


