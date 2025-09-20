// frappe.ui.form.on('Buyer Payment', {
//     refresh: function (frm) {
//         if (!frm.doc.payment_id) {
//             frm.add_custom_button('Make Payment', () => {
//                 let amount_in_paise = frm.doc.product_price  * 100|| 10000;
 
//                 let options = {
//                     key: "rzp_test_1DP5mmOlF5G5ag",
//                     amount: amount_in_paise,
//                     currency: "INR",
//                     name: frm.doc.passenger || "Demo User",
//                     description: "Airplane Ticket Payment",
//                     handler: function (response) {
//                         frm.set_value("payment_id", response.razorpay_payment_id);
//                         frm.set_value("status", "Booked");
//                         frm.save().then(() => {
//                             frappe.msgprint("Payment Successful. Ticket Booked!");
//                             frm.reload_doc();
//                         });
//                     },
//                     prefill: {
//                         name: frm.doc.passenger || "Test User",
//                         email: frm.doc.email || "test@example.com",
//                         contact: frm.doc.mobile || "9999999999"
//                     },
//                     theme: {
//                         color: "#33cc8cff"
//                     },
//                     modal: {
//                         ondismiss: function () {
//                             frappe.msgprint("You closed the Razorpay popup.");
//                         }
//                     }
//                 };
 
//                 let rzp = new Razorpay(options);
//                 rzp.open();
//             });
//         }
//     }
// });



// frappe.ui.form.on('Buyer Payment', {
//     refresh: function (frm) {
//         if (!frm.doc.payment_id) {
//             frm.add_custom_button('Make Payment', () => {
//                 let amount_in_paise = (frm.doc.product_price || 100) * 100;

//                 let options = {
//                     key: "rzp_test_1DP5mmOlF5G5ag",   // Replace with your Razorpay test/live key
//                     amount: amount_in_paise,
//                     currency: "INR",
//                     name: frm.doc.user_name || "Demo User",
//                     description: "Digital Product Payment",
//                     handler: function (response) {
//                         // Save payment info back to Frappe
//                         frm.set_value("payment_id", response.razorpay_payment_id);
//                         frm.set_value("payment_status", "Success");

//                         frm.save().then(() => {
//                             frappe.msgprint("✅ Payment Successful. Download will be available!");
//                             frappe.new_doc("Download Page", {
//                                 product_id: frm.doc.product_id,
//                                 product_name: frm.doc.title,
//                                 product_price: frm.doc.product_price
//                             });
//                         });
//                     },
//                     prefill: {
//                         name: frm.doc.user_name || "Test User",
//                         email: frappe.session.user,
//                         contact: frm.doc.mobile || "9999999999"
//                     },
//                     theme: {
//                         color: "#1f073bff"
//                     },
//                     modal: {
//                         ondismiss: function () {
//                             frappe.msgprint("❌ You closed the Razorpay popup.");
//                         }
//                     }
//                 };

//                 let rzp = new Razorpay(options);
//                 rzp.open();
//             });
//         }
//     }
// });


frappe.ui.form.on('Buyer Payment', {
    refresh: function (frm) {
        if (!frm.doc.payment_id) {
            frm.add_custom_button('Make Payment', () => {
                let amount_in_paise = (frm.doc.product_price || 100) * 100;

                let options = {
                    key: "rzp_test_1DP5mmOlF5G5ag",   // Replace with your Razorpay test/live key
                    amount: amount_in_paise,
                    currency: "INR",
                    name: frm.doc.user_name || "Demo User",
                    description: "Digital Product Payment",
                    handler: function (response) {
                        // Save payment info back to Frappe
                        frm.set_value("payment_id", response.razorpay_payment_id);
                        frm.set_value("payment_status", "Success");

                        frm.save().then(() => {
                            // Call backend function automatically
                            frappe.call({
                                method: "digital.digital.doctype.buyer_payment.buyer_payment.after_successful_payment",
                                args: {
                                    docname: frm.doc.name
                                },
                                callback: function(r) {
                                    if (!r.exc) {
                                        frappe.msgprint("✅ Payment Successful. Download will be available!");
                                        frappe.new_doc("Download Page", {
                                            product_id: frm.doc.product_id,
                                            product_name: frm.doc.title,
                                            product_price: frm.doc.product_price
                                        });
                                    }
                                }
                            });
                        });
                    },
                    prefill: {
                        name: frm.doc.user_name || "Test User",
                        email: frappe.session.user,
                        contact: frm.doc.mobile || "9999999999"
                    },
                    theme: {
                        color: "#1f073bff"
                    },
                    modal: {
                        ondismiss: function () {
                            frappe.msgprint("❌ You closed the Razorpay popup.");
                        }
                    }
                };

                let rzp = new Razorpay(options);
                rzp.open();
            });
        }
    }
});
