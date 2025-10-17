frappe.ui.form.on('Digital Product', {
    before_submit: function(frm) {
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
    }
});


