// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

frappe.ui.form.on("Creator Profile", {
	refresh(frm) {
         if(frm.doc.website) {
            frm.add_web_link(frm.doc.website, 'Own Site');
        }

	},
});
