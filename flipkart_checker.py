import requests
from win10toast import ToastNotifier

# URL to the product
flipkart_url = "<ENTER THE URL HERE>"

# Fetch the HTML content
response = requests.get(flipkart_url)
html_content = response.text

# Search for the availability status string in the HTML content
if "This item is currently out of stock" not in html_content:
    # Create a ToastNotifier object
    toaster = ToastNotifier()

    # Show toast notification
    toaster.show_toast(
        "Flipkart Product Notification",
        "The Product is back in stock at Flipkart",
        duration=10,
    )

