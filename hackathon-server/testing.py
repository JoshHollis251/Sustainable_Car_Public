from venmo_api import Client
import secret
import time

try:
    access_token_driver = Client.get_access_token(username=secret.username_driver,
                                        password=secret.password_driver,
                                        device_id=secret.device_id_driver)

    venmo_driver = Client(access_token=access_token_driver)
    charity = venmo_driver.user.get_user_by_username(secret.username_charity).id


except Exception as e:
    print("venmo don't work XD XD XD")
    print(e)


def charge(amount, message):
    if amount < 5:
        print("YOU ARE ABOUT TO PAY SOME ONE SOME $")
        time.sleep(5)
        try:
            payment_method = venmo_driver.payment.get_payment_methods()[1].id
            venmo_driver.payment.send_money(amount, message, charity, funding_source_id=payment_method) 
        except Exception as e:
            print(e)
            print("Yep payment dont work")
    else:
        print("Oh my god you just tried to charge $" + amount)

def reimburse(amount, message):
        venmo_driver.payment.request_money(amount, message, charity)


charge(0.01, "dinner's on me")
time.sleep(5)
reimburse(0.01, "actually wait dang i want that lol")
