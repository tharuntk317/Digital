frappe.ui.form.on('Digital Product', {
    before_submit(frm) {
          let info = [
            frm.doc.creator || 'NoCreator',
            frm.doc.title || 'NoTitle',
            frm.doc.category || 'NoCat',
            frm.doc.tags || 'NoTags',
            frm.doc.price || 0,
            frm.doc.file || 'NoFile'
        ].join('|');
        frm.set_value('product_detail', info);
    },
    refresh: function(frm) {
        frm.set_df_property('product_detail', 'read_only', 1);
                frappe.ui.form.ControlLink.link_options = function(link) {
    return [
        {
            html: `<span>${__("see the example output")}</span>`,
            label: __("creator"),
            value: "creator",
            action: () => {
                window.location.href = "/products";
            }
        }
    ];
}
    },
});

frappe.ui.form.on('Digital Product', {
   on_submit(frm) {
        if (frappe.session.user === frm.doc.creator) {
            frappe.msgprint("Administrator approved your product!");
        }
    }
});



// frappe.ui.form.ControlLink.link_options = function(link) {
//     return [
//         {
//             html: `<span>${__("see the example output")}</span>`,
//             label: __("creator"),
//             value: "creator",
//             action: () => {
//                 window.location.href = "/products";
//             }
//         }
//     ];
// }






