app_name = "digital"
app_title = "Digital"
app_publisher = "tharun"
app_description = "tharun "
app_email = "tharuntk376@gmail.com"
app_license = "mit"

jinja = {
    "methods": [
        "digital.utils"
    ]
}

app_include_js = [
    "https://checkout.razorpay.com/v1/checkout.js"
]

website_route_rules = [
    {"from_route": "/product/<name>", "to_route": "product"}
]

scheduler_events = {
    "cron": {
        "35 10 * * *": [   
            "digital.tasks.send_good"
        ]
    }
}
website_context = {
    "brand_html": "Digital Marketplace",
    "favicon": "/assets/digital/images/digital_logo.png"
}

default_mail_footer = """
 <div>
 Sent via <a href="#" target="_blank">Digital Marketplace</a>
</div>
"""