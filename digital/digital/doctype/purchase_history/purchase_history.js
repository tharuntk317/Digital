frappe.ui.form.on("Purchase History", {
	refresh(frm) {
frm.add_custom_button(__('Go to Product'), function() {
        frappe.set_route('Form', 'Digital Product', frm.doc.product);
    });
	},
});
