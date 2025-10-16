frappe.ui.form.on("Chat Page", {
    refresh(frm) {
       frm.add_custom_button("Go To Home 📦", () => {
    window.location.href = "http://localhost:8001/homepage";
});
        frm.disable_save();
        if (!frm.chat_box) {
            frm.chat_box = $(`<div id="chat-box" style="
                height: 350px; overflow-y: auto;
                background: #070808; padding: 10px;
                border-radius: 10px; font-family: Arial;
                font-size: 13px; color: white;"></div>`);
            $(frm.fields_dict.chat_room.wrapper).html(frm.chat_box);
        }
        const renderChat = () => {
    if (!frm.chat_box) return;
    const messages = (frm.doc.chat_room || "").split("\n").filter(Boolean);
    frm.chat_box.html(
        messages.map(line => {
            const match = line.match(/^(.+?) \((.+?)\): (.+)$/);
            if (!match) return `<div>${line}</div>`;
            const [_, user, time, msg] = match;
            const isMe = user === frappe.session.user_fullname;
            const bg = isMe ? "#088a3aff" : "#2e2c2cff";
            const color = "rgba(255, 253, 253, 1)"; 
            const align = isMe ? "flex-end" : "flex-start";

            return `
                <div style="
                    display:flex; justify-content:${align}; margin:5px 0;">
                    <div style="
                        background:${bg}; color:${color};
                        padding:8px 12px; border-radius:18px;
                        max-width:75%; word-wrap:break-word;
                        box-shadow: 0 1px 0.5px rgba(0,0,0,0.13);">
                        <b style="font-size:12px;">${user}</b>
                        <span style="font-size:10px; color:#555;"> (${time})</span><br>
                        ${msg}
                    </div>
                </div>
            `;
        }).join("")
    );

    frm.chat_box.scrollTop(frm.chat_box[0].scrollHeight);
};
        renderChat();
    },
    send(frm) {
        const msg = frm.doc.new_message?.trim();
        if (!msg) return frappe.msgprint("Please enter a message.");

        frappe.call({
            method: "digital.digital.doctype.chat_page.chat_page.send_chat_message",
            args: { docname: frm.doc.name, message: msg },
            callback: () => {

                frm.set_value("new_message", "");
                frm.reload_doc().then(() => frm.chat_box.scrollTop(frm.chat_box[0].scrollHeight));
            }
        });
    }
});







// frappe.ui.form.on("Chat Page", {
//     refresh(frm) {
//        frm.add_custom_button("Go To Home 📦", () => {
//     window.location.href = "http://localhost:8001/homepage";
// });
//         frm.disable_save();
//         if (!frm.chat_box) {
//             frm.chat_box = $(`<div id="chat-box" style="
//                 height: 350px; overflow-y: auto;
//                 background: #070808; padding: 10px;
//                 border-radius: 10px; font-family: Arial;
//                 font-size: 13px; color: white;"></div>`);
//             $(frm.fields_dict.chat_room.wrapper).html(frm.chat_box);
//         }
//         const renderChat = () => {
//     if (!frm.chat_box) return;
//     const messages = (frm.doc.chat_room || "").split("\n").filter(Boolean);
//     frm.chat_box.html(
//         messages.map(line => {
//             const match = line.match(/^(.+?) \((.+?)\): (.+)$/);
//             if (!match) return `<div>${line}</div>`;
//             const [_, user, time, msg] = match;
//             const isMe = user === frappe.session.user_fullname;
//             const bg = isMe ? "#088a3aff" : "#2e2c2cff";
//             const color = "rgba(255, 253, 253, 1)"; 
//             const align = isMe ? "flex-end" : "flex-start";

//             return `
//                 <div style="
//                     display:flex; justify-content:${align}; margin:5px 0;">
//                     <div style="
//                         background:${bg}; color:${color};
//                         padding:8px 12px; border-radius:18px;
//                         max-width:75%; word-wrap:break-word;
//                         box-shadow: 0 1px 0.5px rgba(0,0,0,0.13);">
//                         <b style="font-size:12px;">${user}</b>
//                         <span style="font-size:10px; color:#555;"> (${time})</span><br>
//                         ${msg}
//                     </div>
//                 </div>
//             `;
//         }).join("")
//     );

//     frm.chat_box.scrollTop(frm.chat_box[0].scrollHeight);
// };
//         renderChat();
//         if (!frm._refresh_interval) {
//             frm._refresh_interval = setInterval(() => frm.reload_doc().then(renderChat), 5000);
//         }
//     },
//     send(frm) {
//         const msg = frm.doc.new_message?.trim();
//         if (!msg) return frappe.msgprint("Please enter a message.");

//         frappe.call({
//             method: "digital.digital.doctype.chat_page.chat_page.send_chat_message",
//             args: { docname: frm.doc.name, message: msg },
//             callback: () => {

//                 frm.set_value("new_message", "");
//                 frm.reload_doc().then(() => frm.chat_box.scrollTop(frm.chat_box[0].scrollHeight));
//             }
//         });
//     }
// });


// frappe.ui.form.on("Chat Page", {
//     refresh(frm) {
//         frm.disable_save();

//         // Create chat box once
//         if (!frm.chat_box) {
//             frm.chat_box = $(`<div id="chat-box" style="
//                 height: 350px; overflow-y: auto;
//                 background: #070808; padding: 10px;
//                 border-radius: 10px; font-family: Arial;
//                 font-size: 13px; color: white;"></div>`);
//             $(frm.fields_dict.chat_room.wrapper).html(frm.chat_box);
//         }
//         const renderChat = () => {
//     if (!frm.chat_box) return;
//     const messages = (frm.doc.chat_room || "").split("\n").filter(Boolean);

//     frm.chat_box.html(
//         messages.map(line => {
//             const match = line.match(/^(.+?) \((.+?)\): (.+)$/);
//             if (!match) return `<div>${line}</div>`;

//             const [_, user, time, msg] = match;
//             const isMe = user === frappe.session.user_fullname;

//             // WhatsApp-style colors
//             const bg = isMe ? "#088a3aff" : "#2e2c2cff"; // green for me, white for others
//             const color = "#fffdfdff"; // text color black
//             const align = isMe ? "flex-end" : "flex-start";

//             return `
//                 <div style="
//                     display:flex; justify-content:${align}; margin:5px 0;">
//                     <div style="
//                         background:${bg}; color:${color};
//                         padding:8px 12px; border-radius:18px;
//                         max-width:75%; word-wrap:break-word;
//                         box-shadow: 0 1px 0.5px rgba(0,0,0,0.13);">
//                         <b style="font-size:12px;">${user}</b>
//                         <span style="font-size:10px; color:#555;"> (${time})</span><br>
//                         ${msg}
//                     </div>
//                 </div>
//             `;
//         }).join("")
//     );

//     frm.chat_box.scrollTop(frm.chat_box[0].scrollHeight);
// };

//         renderChat();
//         if (!frm._refresh_interval) {
//             frm._refresh_interval = setInterval(() => frm.reload_doc().then(renderChat), 5000);
//         }
//     },

//     send(frm) {
//         const msg = frm.doc.new_message?.trim();
//         if (!msg) return frappe.msgprint("Please enter a message.");

//         frappe.call({
//             method: "digital.digital.doctype.chat_page.chat_page.send_chat_message",
//             args: { docname: frm.doc.name, message: msg },
//             callback: () => {
//                 frm.set_value("new_message", "");
//                 frm.reload_doc().then(() => frm.chat_box.scrollTop(frm.chat_box[0].scrollHeight));
//             }
//         });
//     }
// });


// frappe.ui.form.on("Chat Page", {
//     refresh(frm) {
//         frm.disable_save();
//         if (!frm.fields_dict.chat_display) {
//             $(frm.fields_dict.chat_room.wrapper)
//                 .html(`<div id="chat-box" style="
//                     height: 300px; 
//                     overflow-y: auto; 
//                     padding: 10px; 
//                     background: #070808ff; 
//                     border-radius: 10px;
//                     font-family: Arial;
//                     font-size: 13px;">
//                 </div>`);
//         }
//         if (frm.doc.chat_room) {
//             let chatBox = document.getElementById("chat-box");
//             chatBox.innerHTML = frm.doc.chat_room
//                 .split("\n")
//                 .filter(Boolean)
//                 .map(line => `<div style="
//                     background:#2E8B57;
//                     color: white;
//                     margin:5px 0;
//                     padding:6px 10px;
//                     border-radius:8px;
//                     display:inline-block;">
//                     ${line}
//                 </div>`)
//                 .join("<br>");
//             chatBox.scrollTop = chatBox.scrollHeight;
//         }
//         frappe.realtime.on('chat_message', (data) => {
//             if (data.docname === frm.doc.name) {
//                 let chatBox = document.getElementById("chat-box");
//                 if (chatBox) {
//                     chatBox.innerHTML += `<div style="
//                         background:#dcf8c6;
//                         margin:5px 0;
//                         padding:6px 10px;
//                         border-radius:8px;
//                         display:inline-block;">
//                         <b>${data.user}</b>: ${data.message}
//                     </div><br>`;
//                     chatBox.scrollTop = chatBox.scrollHeight;
//                 }
//             }
//         });
//     },

//     send(frm) {
//         let msg = frm.doc.new_message?.trim();
//         if (!msg) return frappe.msgprint("Please type a message before sending.");

//         frappe.call({
//             method: "digital.digital.doctype.chat_page.chat_page.send_chat_message",
//             args: { docname: frm.doc.name, message: msg },
//             callback: () => {
//                 // Clear the input
//                 frm.set_value("new_message", "");

//                 // Automatically reload the document so chat_room updates
//                 frm.reload_doc().then(() => {
//                     // Optional: scroll to the bottom after reload
//                     let chatBox = document.getElementById("chat-box");
//                     if (chatBox) chatBox.scrollTop = chatBox.scrollHeight;
//                 });
//             }
//         });
//     }

// });




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