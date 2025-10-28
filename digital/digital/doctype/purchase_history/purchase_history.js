frappe.ui.form.on("Purchase History", {
    refresh(frm) {
        frm.add_custom_button(__('Go to Product'), function() {
            if (frm.doc.product) {
                frappe.set_route('Form', 'Digital Product', frm.doc.product);
            } else {
                frappe.msgprint("No product linked to this purchase.");
            }
        });

         if (frappe.session.user === "Administrator") {
        frm.add_custom_button(__('Add Earning'), function() {
            frappe.call({
                method: "digital.digital.doctype.purchase_history.purchase_history.creator_earning", 
                args: {
                    name: frm.doc.name,
                    doctype: frm.doc.doctype
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.msgprint("Creator earnings updated successfully!");
                        frm.reload_doc();
                    }
                }
            });
        });
    }
    }
});


