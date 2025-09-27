// frappe.ui.form.on('Buyer Payment', {
//     after_save: function(frm) {
//         frappe.call({
//             method: 'digital.digital.doctype.buyer_payment.buyer_payment.create_download_page',
//             args: { 
//                 docname: frm.doc.name,
//                 doctype: frm.doc.doctype
//              },
//             callback: function(response) {
//                 if (response.message) {
//                     frappe.msgprint(response.message);
//                     frm.reload_doc(); 
//                 }
//             }
//         });
//     }
// });

