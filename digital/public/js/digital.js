// frappe.ui.form.on("Download Page", {
//     refresh: function (frm) {
//         if (frm.doc.product_id) {
//             frm.add_custom_button("Download File", () => {
//                 frappe.call({
//                     method: "digital.api.download_file",
//                     args: {
//                         product_id: frm.doc.product_id
//                     },
//                     callback: function (r) {
//                         if (r.message) {
//                             // Download in same place
//                             window.location.href = r.message;
//                         } else {
//                             frappe.msgprint("No file found for this product.");
//                         }
//                     }
//                 });
//             });
//         }
//     }
// });

// frappe.ui.form.on("Download Page", {
//     refresh: function (frm) {
//         if (frm.doc.product_id) {
//             frm.add_custom_button("Download File", () => {
//                 // Create modal
//                 let d = new frappe.ui.Dialog({
//                     title: "Download Started",
//                     fields: [
//                         {
//                             fieldtype: "HTML",
//                             fieldname: "download_info",
//                             options: `
//                                 <div style="text-align:center; padding:20px;">
//                                     <img src="/assets/digital/images/download.png" width="100"><br><br>
//                                     <h3>Your download will start shortly...</h3>
//                                 </div>
//                             `
//                         }
//                     ],
//                     primary_action_label: "Close",
//                     primary_action: () => d.hide()
//                 });

//                 d.show();

//                 // Trigger backend file download (force attachment)
//                 window.location.href = `/api/method/digital.api.download_file?product_id=${frm.doc.product_id}`;
//             });
//         }
//     }
// });




