import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime

class ChatPage(Document):
    pass


@frappe.whitelist()
def send_chat_message(docname, message):
    if not docname:
        frappe.throw("Document must be saved before sending messages.")

    doc = frappe.get_doc("Chat Page", docname)
    timestamp = now_datetime().strftime("%Y-%m-%d %H:%M:%S")
    user = frappe.session.user
    fullname = frappe.get_value("User", user, "full_name") or user
    chat_line = f"{fullname} ({timestamp}): {message}\n"
    doc.chat_room = (doc.chat_room or "") + chat_line
    doc.save(ignore_permissions=True)
    doc.notify_update()

    frappe.publish_realtime(
        event='chat_message',
        message={
            'docname': docname,
            'user': fullname,
            'message': message,
            'timestamp': timestamp
        },
        doctype="Chat Page",
        after_commit=True
    )

    return "Message sent!"




# @frappe.whitelist()
# def send_chat_message(docname, message):
#     if not docname:
#         frappe.throw("Document must be saved before sending messages.")
#     doc = frappe.get_doc("Chat Page", docname)
#     timestamp = now_datetime().strftime("%Y-%m-%d %H:%M:%S")
#     chat_line = f"{frappe.session.user} ({timestamp}): {message}\n"
#     doc.chat_room = (doc.chat_room or "") + chat_line
#     doc.save(ignore_permissions=True)
#     doc.notify_update()
#     frappe.publish_realtime(
#         event='chat_message',
#         message={'docname': docname, 'user': frappe.session.user, 'message': message, 'timestamp': timestamp},
#         doctype="Chat Page",
#         after_commit=True
#     )
#     return "Message sent!"



# @frappe.whitelist()
# def send_chat_message(docname, message):
#     if not docname:
#         frappe.throw("Document must be saved before sending messages.")

#     doc = frappe.get_doc("Chat Page", docname)
#     chat_line = f"{frappe.session.user}: {message}\n"
#     doc.chat_room = (doc.chat_room or "") + chat_line
#     doc.save(ignore_permissions=True)
#     doc.notify_update() 
#     frappe.publish_realtime(
#         event='chat_message',
#         message={'docname': docname, 'user': frappe.session.user, 'message': message},
#         doctype="Chat Page",
#         after_commit=True
#     )
#     return "Message sent!"
