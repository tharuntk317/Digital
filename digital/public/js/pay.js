frappe.ui.form.on("Buyer Payment", {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button('Pay Now', () => {
                let options = {
                    key: "rzp_test_1DP5mmOlF5G5ag", // Replace with Razorpay Test Key
                    amount: frm.doc.payable_amount * 100, // Convert to paise
                    currency: "INR",
                    name: "Creators Hub",
                    description: frm.doc.product_name || "Product Payment",
                    handler: function (response) {
                        frappe.call({
                            method: "digital.api.mark_payment_success",
                            args: {
                                docname: frm.doc.name,
                                razorpay_payment_id: response.razorpay_payment_id
                            },
                            callback: function (r) {
                                if (r.message && r.message.status === "success") {
                                    frappe.msgprint("✅ Payment Successful!");
                                    frm.reload_doc();
                                } else {
                                    frappe.msgprint("❌ Payment Failed. Please try again.");
                                }
                            }
                        });
                    },
                    prefill: {
                        name: frappe.session.user_fullname,
                        email: frappe.session.user,
                    },
                    theme: {
                        color: "#528FF0"
                    }
                };

                let rzp = new Razorpay(options);
                rzp.open();
            });
        }
    },
});
