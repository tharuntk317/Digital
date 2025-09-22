app_name = "digital"
app_title = "Digital"
app_publisher = "tharun"
app_description = "tharun "
app_email = "tharuntk376@gmail.com"
app_license = "mit"

web_include_css = "/assets/digital/css/digital.css"

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

