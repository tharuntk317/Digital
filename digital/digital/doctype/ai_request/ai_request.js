frappe.ui.form.on("AI Request", {
    refresh(frm) {
        frm.save()
        frm.disable_save()
        frm.set_df_property("response", "read_only", 1);
    },
    generate_ai_response(frm) {
        generate_ai_response_function(frm);
    }
});
async function generate_ai_response_function(frm) {
    let prompt = frm.doc.prompt;
    if (!prompt) {
        frappe.msgprint("Please type a prompt first!");
        return;
    }
    frm.set_value("prompt", "");
    frm.refresh_field("prompt");

    try {
        await frappe.call({
            method: "digital.digital.doctype.ai_request.ai_request.generate_response",
            args: {
                prompt: prompt,
                docname: frm.doc.name
            }
        });
        await frm.reload_doc();
    let r = frm.fields_dict.response.$wrapper.get(0);
        r.scrollTop = r.scrollHeight;

    } catch (err) {
        frappe.msgprint("Error calling AI.");
        console.error(err);
    }
}
