frappe.ui.form.on("Download Page", {
    download: function (frm) {
        if (frm.doc.product_id) {
            let d = new frappe.ui.Dialog({
                title: "Download Started",
                fields: [
                    {
                        fieldtype: "HTML",
                        fieldname: "download_info",
                        options: `
                            <div style="text-align:center; padding:20px;">
                                <img src="/assets/digital/images/pay.png" width="100"><br><br>
                                <h3>Your download will start shortly...</h3>
                            </div>
                        `
                    }
                ],
                primary_action_label: "Close",
                primary_action: () => d.hide()
            });

            d.show();

            // Directly trigger download
            window.location.href =
                `/api/method/digital.digital.doctype.download_page.download_page.download_file?product_id=${frm.doc.product_id}`;

        } else {
            frappe.msgprint("No Product ID found for download.");
        }
    }
});
