import frappe
from frappe.model.document import Document
from frappe.utils import now


class ChatPage(Document):
    pass

@frappe.whitelist()
def open_chat(buyer, creator, product_id):
    
    buyer_fullname = frappe.db.get_value("User", buyer, "full_name") or buyer
    creator_fullname = frappe.db.get_value("User", creator, "full_name") or creator
    
    chat_name = f"{buyer_fullname}_to_{creator_fullname}"
    if frappe.db.exists("Chat Page", chat_name):
        frappe.local.response.update({
            "type": "redirect",
            "location": f"/app/chat-page/{chat_name}"
        })
        return
    doc = frappe.get_doc({
        "doctype": "Chat Page",
        "buyer": buyer,
        "creator": creator,
        "product": product_id,
        "creation": now()
    }).insert(ignore_permissions=True)
    frappe.rename_doc("Chat Page", doc.name, chat_name, force=True)
    frappe.db.commit()

    frappe.local.response.update({
        "type": "redirect",
        "location": f"/app/chat-page/{chat_name}"
    })

@frappe.whitelist()
def send_chat_message(docname, message):
    if not docname:
        frappe.throw("Document must be saved before sending messages.")
        
    doc = frappe.get_doc("Chat Page", docname)
    timestamp = now()
    fullname = frappe.get_value("User", frappe.session.user, "full_name") or frappe.session.user
    chat_line = f"{fullname} ({timestamp}): {message}\n"
    doc.chat_room = (doc.chat_room or "") + chat_line  
    doc.save()
    doc.notify_update()
    frappe.publish_realtime(
        event='chat_message',
        message={'user': fullname, 'message': message, 'timestamp': timestamp},
        doctype="Chat Page",
        after_commit=True
    )


# @frappe.whitelist()
# def send_chat_message(docname, message):
#     if not docname:
#         frappe.throw("Document must be saved before sending messages.")
    
#     doc = frappe.get_doc("Chat Page", docname)
#     timestamp = now()
#     fullname = frappe.get_value("User", frappe.session.user, "full_name") or frappe.session.user
    
#     chat_line = f"{fullname} ({timestamp}): {message}\n"
#     doc.chat_room = (doc.chat_room or "") + chat_line  
#     doc.save()
#     doc.notify_update()
#     frappe.publish_realtime(
#         event="ne_chat_message",
#         message={
#             "sender": fullname,
#             "message": message,
#             "timestamp": timestamp,
#             "chat_name": docname
#         },
#         room=docname,
#         after_commit=True
#     )
#     return




    
# import frappe
# from frappe.model.document import Document
# from frappe.utils import 
# from frappe.utils import now


# class ChatPage(Document):
#     pass


# @frappe.whitelist()
# def send_chat_message(docname, message):
#     if not docname:
#         frappe.throw("Document must be saved before sending messages.")

#     doc = frappe.get_doc("Chat Page", docname)
#     timestamp = now_datetime().strftime("%Y-%m-%d %H:%M:%S")
#     user = frappe.session.user
#     fullname = frappe.get_value("User", user, "full_name") or user
#     chat_line = f"{fullname} ({timestamp}): {message}\n"
#     doc.chat_room = (doc.chat_room or "") + chat_line
#     doc.save()
#     doc.notify_update()
#     frappe.publish_realtime(
#         event='chat_message',
#         message={
#             'docname': docname,
#             'user': fullname,
#             'message': message,
#             'timestamp': timestamp
#         },
#         doctype="Chat Page",
#         after_commit=True
#     )

#     return "Message sent!"



# @frappe.whitelist(allow_guest=False)
# def open_chat(buyer, creator, product_id):
#     if buyer == creator:
#         frappe.throw("You cannot start a chat with yourself.")

#     buyer_fullname = frappe.db.get_value("User", buyer, "full_name") or buyer
#     creator_fullname = frappe.db.get_value("User", creator, "full_name") or creator

#     buyer_fullname = buyer_fullname.replace(" ", "_")
#     creator_fullname = creator_fullname.replace(" ", "_")

#     chat_name = f"{buyer_fullname}_to_{creator_fullname}"

#     if frappe.db.exists("Chat Page", chat_name):
#         frappe.local.response["type"] = "redirect"
#         frappe.local.response["location"] = f"/app/chat-page/{chat_name}"
#         return

#     chat_doc = frappe.get_doc({
#         "doctype": "Chat Page",
#         "buyer": buyer,
#         "creator": creator,
#         "product": product_id,
#         "creation": now()
#     })

#     chat_doc.insert(ignore_permissions=True)
#     frappe.rename_doc("Chat Page", chat_doc.name, chat_name, force=True)
#     frappe.db.commit()

#     frappe.local.response["type"] = "redirect"
#     frappe.local.response["location"] = f"/app/chat-page/{chat_name}"




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


