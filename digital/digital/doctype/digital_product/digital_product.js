
frappe.ui.form.on("Digital Product", {
    refresh(frm) {
            //  frm.set_value("creator", frappe.session.user)
    },

    status(frm) {
        if (frm.doc.status === "Published") {
            frappe.msgprint("Status is Published. Auto saving...");
            frm.save();
        }
    }
});

