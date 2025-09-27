frappe.ready(() => {
    const button = document.querySelector(".submit-btn");
    if (!button) return;

    button.addEventListener("click", e => {
        e.preventDefault();

        const getParam = name => new URLSearchParams(window.location.search).get(name);
        const user_name = document.querySelector('[name="user"]')?.value || "Guest User";
        const product_id = document.querySelector('[name="product_id"]')?.value || getParam("product_id");
        const product_price = parseFloat(document.querySelector('[name="product_price"]')?.value || getParam("product_price")) || 100;
        const mobile = document.querySelector('[name="mobile"]')?.value || "9999999999";

        if (!product_id) {
            frappe.msgprint("Product ID missing.");
            return;
        }
        const loadRazorpay = () => {
            if (window.Razorpay) startPayment();
            else {
                const script = document.createElement("script");
                script.src = "https://checkout.razorpay.com/v1/checkout.js";
                script.onload = startPayment;
                document.body.appendChild(script);
            }
        };
        const startPayment = () => {
            const rzp = new Razorpay({
                key: "rzp_test_1DP5mmOlF5G5ag", 
                amount: product_price * 100, 
                currency: "INR",
                name: user_name,
                description: "Digital Product Payment",
                prefill: { name: user_name, contact: mobile },
                theme: { color: "#1f073b" },
                handler: function (response) {
                    frappe.msgprint(" Payment Successful! Check you are mail Box and Your  Payment ID: " + response.razorpay_payment_id);
                    if (frappe.web_form) {
                        frappe.web_form.doc.payment_id = response.razorpay_payment_id;
                        frappe.web_form.set_value("payment_id", response.razorpay_payment_id);
                        frappe.web_form.save().then(() => {
                            console.log("Web Form saved with Payment ID:", response.razorpay_payment_id);
                        });
                    }
                },
                modal: {
                    ondismiss: function () {
                        frappe.msgprint(" Payment cancelled. Record not saved.");
                    }
                }
            });
            rzp.open();
        };

        loadRazorpay();
    });
});
