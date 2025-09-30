frappe.ready(() => {
    const product_id = new URLSearchParams(window.location.search).get("product_id");
    if (product_id) {
        frappe.web_form.set_value("product", product_id);
        frappe.web_form.fields_dict.product.$input.prop("readonly", true);
    }
});

frappe.ready(() => {
  
    document.body.style.backgroundColor = "#d8ddebff";  
    // document.body.style.color = "#f9fafb";           
    // const form = document.querySelector(".web-form-wrapper");
    // if (form) {
    //     form.style.backgroundColor = "#aab0b9ff";   
    //     form.style.color = "#1c1c1dff";             
    //     form.style.borderRadius = "10px";         
    //     form.style.padding = "1.5rem";          
    // }
});

