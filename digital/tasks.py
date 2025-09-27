import frappe
def send_good():
    print("hi")
    for user in frappe.get_all("User", filters={"enabled": 1}, pluck="name"):
        frappe.publish_realtime(
            event="msgprint",
            message=f" Hi {user}, Good Morning! Scheduler is working ",
            user=user
        )


