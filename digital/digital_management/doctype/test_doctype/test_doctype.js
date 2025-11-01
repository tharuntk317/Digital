// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Test Doctype", {
    refresh(frm) {
        frm.set_query('status', () => {
            return {
                filters: {
                    status: ['in', ['AAA', 'BBB', 'CCC']]
                }
            }
        });
    },
});

