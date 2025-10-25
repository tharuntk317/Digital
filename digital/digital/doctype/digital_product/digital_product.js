frappe.ui.form.on('Digital Product', {
    before_submit: function(frm) {
        let info = [
            frm.doc.creator,
            frm.doc.title ,
            frm.doc.category ,
            frm.doc.tags,
            frm.doc.price,
            frm.doc.file 
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


