frappe.ready(() => {
    // Grab product_id from URL
    const product_id = new URLSearchParams(window.location.search).get("product_id");

    if (product_id) {
        // Set value into the Product field
        frappe.web_form.set_value("product", product_id);

        // Make readonly after value is set
        frappe.web_form.fields_dict.product.$input.prop("readonly", true);
    }
});
