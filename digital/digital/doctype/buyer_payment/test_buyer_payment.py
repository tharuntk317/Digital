# Copyright (c) 2025, tharun and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestBuyerPayment(FrappeTestCase):

    def setUp(self):
        """Set up mandatory test data"""

        # Create a test Creator Profile
        self.creator = frappe.get_doc({
            "doctype": "Creator Profile",
            "creator_name": "Test Creator",
            "display_name": "Test Creator",
            "wallet": 0
        }).insert(ignore_permissions=True)

        # Create a test Digital Product
        self.product = frappe.get_doc({
            "doctype": "Digital Product",
            "product_name": "Test Product",
            "item_code": "TEST_PRODUCT_001",
            "creator": self.creator.creator_name,
            "category": "Ebook",
            "tags": "Free",                # Must match allowed select options
            "file": "/files/test_file.pdf",
            "preview_image": "/files/test_image.png",
            "status": "Active"
        }).insert(ignore_permissions=True)

        self.user_name = "test_user@example.com"

    def tearDown(self):
        """Clean up test data"""
        frappe.delete_doc("Digital Product", self.product.name, force=True)
        frappe.delete_doc("Creator Profile", self.creator.name, force=True)
        frappe.db.commit()

    def test_after_insert_creates_records_and_updates_wallet(self):
        """Test BuyerPayment after_insert logic"""

        payment_doc = frappe.get_doc({
            "doctype": "Buyer Payment",
            "user_name": self.user_name,
            "product_id": self.product.name,
            "product_price": 150.0,
            "payment_id": "TESTPAY123"
        }).insert(ignore_permissions=True)

        # Assert payment_status
        self.assertEqual(
            frappe.get_value("Buyer Payment", payment_doc.name, "payment_status"),
            "Success"
        )

        # Assert Purchase History
        purchase_history = frappe.get_all(
            "Purchase History",
            filters={"payment_id": "TESTPAY123"}
        )
        self.assertTrue(len(purchase_history) == 1)

        # Assert Download Page
        download_page = frappe.get_all(
            "Download Page",
            filters={"user_name": self.user_name, "product_id": self.product.name}
        )
        self.assertTrue(len(download_page) == 1)

        # Assert Creator Wallet updated
        updated_wallet = frappe.get_value("Creator Profile", self.creator.name, "wallet")
        self.assertEqual(updated_wallet, 150.0)

        # Cleanup
        frappe.delete_doc("Buyer Payment", payment_doc.name, force=True)
        frappe.delete_doc("Purchase History", purchase_history[0].name, force=True)
        frappe.delete_doc("Download Page", download_page[0].name, force=True)
        frappe.db.commit()
