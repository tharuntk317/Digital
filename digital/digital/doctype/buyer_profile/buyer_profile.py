import frappe
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue

class BuyerProfile(Document):
    def on_update(self):
        # Enqueue the search index update as a background job
        # It's important to use enqueue to prevent the UI from freezing
        enqueue(
            "digital.digital.doctype.buyer_profile.buyer_profile.update_search_index",
            queue="short",
            doctype=self.doctype,
            doc_name=self.name,
            job_name=f"update_search_index_{self.doctype}_{self.name}"
        )

@frappe.whitelist()
def update_search_index(doctype, doc_name):
    """
    Python function to update the custom full-text search index for a single document.
    This function is executed as a background job.
    """
    from digital.search import DigitalAppSearch
    
    # Run as administrator to ensure the job has sufficient permissions
    frappe.set_user("Administrator")
    try:
        search_engine = DigitalAppSearch()
        search_engine.update_index_by_name(doc_name)
        frappe.db.commit()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "FullTextSearch Error")
    finally:
        # Revert user to guest after the task is complete
        frappe.set_user("Guest")


