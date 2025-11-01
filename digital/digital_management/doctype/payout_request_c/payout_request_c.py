# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PayoutRequestC(Document):
	pass


@frappe.whitelist()
def process_payout(name):
    frappe.enqueue(run_payout_job, name=name)
    return "Payout job started"

def run_payout_job(name):
    doc = frappe.get_doc("Payout Request C", name)
    frappe.logger().info(f"Payout request processed for {doc.name} by {doc.owner}")
