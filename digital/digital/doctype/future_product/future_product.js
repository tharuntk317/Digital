frappe.ui.form.on("Future Product", {
    refresh(frm){
         frm.disable_save()
    },
 status(frm) {
        if (frm.doc.status === "Published") frm.save();
    }
	});
