frappe.ui.form.on("Chat Page", {
    refresh(frm) {
        frm.disable_save();
        if (!frm.fields_dict.chat_display) {
            $(frm.fields_dict.chat_room.wrapper)
                .html(`<div id="chat-box" style="
                    height: 300px; 
                    overflow-y: auto; 
                    padding: 10px; 
                    background: #070808ff; 
                    border-radius: 10px;
                    font-family: Arial;
                    font-size: 13px;">
                </div>`);
        }
        if (frm.doc.chat_room) {
            let chatBox = document.getElementById("chat-box");
            chatBox.innerHTML = frm.doc.chat_room
                .split("\n")
                .filter(Boolean)
                .map(line => `<div style="
                    background:#2E8B57;
                    color: white;
                    margin:5px 0;
                    padding:6px 10px;
                    border-radius:8px;
                    display:inline-block;">
                    ${line}
                </div>`)
                .join("<br>");
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        frappe.realtime.on('chat_message', (data) => {
            if (data.docname === frm.doc.name) {
                let chatBox = document.getElementById("chat-box");
                if (chatBox) {
                    chatBox.innerHTML += `<div style="
                        background:#dcf8c6;
                        margin:5px 0;
                        padding:6px 10px;
                        border-radius:8px;
                        display:inline-block;">
                        <b>${data.user}</b>: ${data.message}
                    </div><br>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            }
        });
    },

    // send(frm) {
    //     let msg = frm.doc.new_message?.trim();
    //     if (!msg) return frappe.msgprint("Please type a message before sending.");
    //     frappe.call({
    //         method: "digital.digital.doctype.chat_page.chat_page.send_chat_message",
    //         args: { docname: frm.doc.name, message: msg },
    //         callback: () => {
    //             frm.set_value("new_message", "");
    //             frm.refresh_field("new_message");
    //         },
    //     });
    // }

    send(frm) {
        let msg = frm.doc.new_message?.trim();
        if (!msg) return frappe.msgprint("Please type a message before sending.");

        frappe.call({
            method: "digital.digital.doctype.chat_page.chat_page.send_chat_message",
            args: { docname: frm.doc.name, message: msg },
            callback: () => {
                // Clear the input
                frm.set_value("new_message", "");

                // Automatically reload the document so chat_room updates
                frm.reload_doc().then(() => {
                    // Optional: scroll to the bottom after reload
                    let chatBox = document.getElementById("chat-box");
                    if (chatBox) chatBox.scrollTop = chatBox.scrollHeight;
                });
            }
        });
    }

});




// frappe.ui.form.on("Chat Page", {
//     refresh(frm) {
//         frm.disable_save();
//         if (frm.doc.__islocal) {
//             frappe.msgprint("Please save the document first to start chat.");
//             return;
//         }
//          frappe.realtime.on('chat_message', (data) => {
//             if (data.docname === frm.doc.name) {
//                 let current = frm.doc.chat_room || "";
//                 frm.set_value("chat_room", current + `${data.user}: ${data.message}\n`);
// (or)
//                 frm.set_value("chat_room", current + `${data.user} (${now}): ${data.message}\n`);
//                 frm.refresh_field("chat_room");
//             }
// });
//     },
//     send(frm) {
//         let msg = frm.doc.new_message?.trim();
//         if (!msg) return frappe.msgprint("Please type a message before sending.");
//         frappe.call({
//             method: "digital.digital.doctype.chat_page.chat_page.send_chat_message",
//             args: { docname: frm.doc.name, message: msg },
//             callback: () => {
//                 frm.set_value("new_message", "");
//                 frm.refresh_field("new_message");
//             }
//         });
//     }
// });