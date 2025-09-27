frappe.ui.form.on("Digital Product", {
    refresh(frm) {
        frm.disable_save();
        frm.add_custom_button(__('Report Page'), function() {
            frappe.set_route("query-report", "Report View For History");
        });
    },

    status(frm) {
        if (frm.doc.status === "Published") {
            frm.save();
        }
    }
});

