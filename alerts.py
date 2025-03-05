import pywhatkit as kit
from config import RECIPIENT_PHONE, ALERT_THRESHOLD
from error_handler import log_error

def send_price_alert(product_data):
    try:
        # Create a message
        alert_list = ""

        #Define Threshold
        price_threshold = ALERT_THRESHOLD 

        number = 1

        for product in product_data:
            if product[1] and product[1].replace(",", "").replace("$", "").replace(".", "").isdigit():
                price = float(product[1].replace(",", "").replace("$", ""))
                if price < price_threshold:
                    msg = (f"{number}. The price of {product[0]} has dropped to ${price}.\n")
                    alert_list += msg
                    number += 1

        kit.sendwhatmsg_instantly(RECIPIENT_PHONE, alert_list)

    except Exception as e:
        log_error(f"Unexpected error in scrape_product_data: {type(e).__name__}")
    
    return None