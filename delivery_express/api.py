import frappe

@frappe.whitelist()
def get_express_deliveries(status=True):
    filters = {}
    if status:
        filters["status"] = status
    jobs = frappe.get_all(
        "Delivery Job",
        fields=["name", "sales_order_link", "driver", "vehicle", "status", "creation"],
        filters=filters,
    )
    return jobs
