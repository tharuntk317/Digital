// Copyright (c) 2025, tharun and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Buyer Profile", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on('Buyer Profile', {
//     refresh(frm) {
//         // Add a custom button to re-index the current document
//         frm.add_custom_button(__('Re-index Buyer Profile'), () => {
//             frappe.call({
//                 method: "digital.digital.doctype.buyer_profile.buyer_profile.update_search_index",
//                 args: {
//                     doctype: frm.doctype,
//                     doc_name: frm.doc.name
//                 },
//                 callback(response) {
//                     if (!response.exc) {
//                         frappe.msgprint(__('Re-indexing job has been enqueued.'));
//                     }
//                 }
//             });
//         }, __('Actions'));
//     }
// });

