// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.query_reports["Report View For History"] = {
// 	"filters": [

// 	]
// };

frappe.query_reports["Report View For History"] = {
    "filters": [
        {
            "fieldname": "user",
            "label": __("User"),
            "fieldtype": "Link",
            "options": "User"
        },
        {
            "fieldname": "product",
            "label": __("Product"),
            "fieldtype": "Data"
        },
        {
            "fieldname": "creator",
            "label": __("Creator"),
            "fieldtype": "Data"
        },
        {
            "fieldname": "payment_id",
            "label": __("Payment ID"),
            "fieldtype": "Data"
        },
        {
            "fieldname": "purchase_date",
            "label": __("Purchase Date"),
            "fieldtype": "Date"
        }
    ]
};
