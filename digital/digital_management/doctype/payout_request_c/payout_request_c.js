frappe.ui.form.on("Payout Request C", {
    current_amount: function(frm) {
        if (frm.doc.current_amount) {
            let gst = frm.doc.current_amount * 0.10;
            let app_commission = frm.doc.current_amount * 0.05;
            let total_amount = frm.doc.current_amount + gst - app_commission;
            frm.set_value("gst", gst);
            frm.set_value("app_commission", app_commission);
            frm.set_value("total_amount", total_amount);
        }
    },
    send_request(frm) {
        frm.save();
        frappe.msgprint("Your payout request is being processed in the background.");

        frappe.call({
            method: "digital.digital_management.doctype.payout_request_c.payout_request_c.process_payout",
            args: { name: frm.doc.name },
        });
    }
});
