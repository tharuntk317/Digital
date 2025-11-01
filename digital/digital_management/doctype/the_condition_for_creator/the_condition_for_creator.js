frappe.ui.form.on("The Condition For Creator", {
    refresh(frm) {
        frm.add_custom_button("Go Home", () => {
            frappe.set_route("/app/private/creator-workspace");
        });
    },
});
