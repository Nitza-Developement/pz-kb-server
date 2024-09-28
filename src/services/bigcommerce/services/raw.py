from src.config import __env
from ..config import BC_ENDPOINTS_FILE_PATH
from src.helpers.json_parse import loadJSON
import json
import requests

ENDPOINTS = loadJSON(file_path=BC_ENDPOINTS_FILE_PATH)
BC_ACCESS_TOKEN = __env["BC_ACCESS_TOKEN"]
BC_STORE_HASH = __env["BC_STORE_HASH"]
BC_BASE_URL_BASIC = __env["BC_BASE_URL_BASIC"]
BC_BASE_URL_PAYMENT = __env["BC_BASE_URL_PAYMENT"]


class RAWService:

    STORE_HASH = BC_STORE_HASH
    X_AUTH_TOKEN = BC_ACCESS_TOKEN
    BASE_URL_BASIC = BC_BASE_URL_BASIC
    BASE_URL_PAYMENTS = BC_BASE_URL_PAYMENT

    HEADERS = {
        "X-Auth-Token": BC_ACCESS_TOKEN,
        "Accept": "application/json",
    }

    def __request(
        self,
        api_path,
        headers=HEADERS,
        method="GET",
        data=None,
        context=None,
    ):
        if context == "payment":
            # 'https://payments.bigcommerce.com/store/{STORE_HASH}/ ...'
            cur_url = f"{self.BASE_URL_PAYMENTS}/stores/{self.STORE_HASH}" + api_path
        else:
            # 'https://api.bigcommerce.com/store/{STORE_HASH}/ ...'
            cur_url = f"{self.BASE_URL_BASIC}/stores/{self.STORE_HASH}" + api_path

        if method == "POST":
            response = requests.post(cur_url, headers=headers, data=json.dumps(data))
        elif method == "PUT":
            response = requests.put(cur_url, headers=headers, data=json.dumps(data))
        elif method == "GET":
            response = requests.get(cur_url, headers=headers)

        if response and (response.status_code == 200 or response.status_code == 201):
            try:
                return response.json()  # .get('data')
            except:
                pass

        return {}

    def create_bc_customer(self, data):
        data = [
            {
                "email": "email",
                "first_name": "first_name",
                "last_name": "last_name",
                "addresses": [
                    {
                        "address1": "street1",
                        "address2": "",
                        "address_type": "residential",
                        "city": "city",
                        "country_code": "US",
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "phone": "1111111111",
                        "postal_code": "11111",
                        "state_or_province": "Texas",
                    }
                ],
                "authentication": {
                    "force_password_reset": False,
                    "new_password": "Password",
                },
                "accepts_product_review_abandoned_cart_emails": True,
            }
        ]

        return self.__request(api_path="/v3/customers", method="POST", data=data)

    def get_bc_customer(self, email):
        return self.__request(api_path="/v3/customers?email:in=" + email, method="GET")

    def create_stored_instrument(self, data):
        data = [
            {
                "billing_address": {
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "email": "email",
                    "street_1": "street_1",
                    "city": "city",
                    "zip": "77407",
                    "country_code": "US",
                    "state_or_province": "Texas",
                    "state_or_province_code": "TX",
                },
                "trusted_shipping_addresses": [
                    {
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "email": "email",
                        "street_1": "street_1",
                        "city": "city",
                        "country_code": "US",
                        "zip": "77407",
                        "state_or_province": "Texas",
                        "state_or_province_code": "TX",
                    }
                ],
                "default_instrument": True,
                "payment_method_id": "braintree.credit_card",
                "currency_code": "USD",
                "customer_id": 2,
                "instrument": {
                    "vault_token": "0nvv56s0",
                    "provider_customer_id": "84387368966",
                    "type": "credit_card",
                    "brand": "visa",
                    "expiry_year": 2028,
                    "expiry_month": 4,
                    "last_4": "0504",
                    "iin": "426555",
                },
            }
        ]

        return self.__request(
            api_path="/v3/payments/stored-instruments", method="POST", data=data
        )

    def update_stored_instrument(self, data):
        data = {
            "token": "token",
            "billing_address": {
                "first_name": "first_name",
                "last_name": "last_name",
                "email": "email",
                "address1": "address1",
                "address2": "",
                "city": "Richmond",
                "state_or_province_code": "TX",
                "country_code": "US",
                "phone": "6469450635",
                "postal_code": "77407",
            },
        }

        return self.__request(
            api_path="/v3/payments/stored-instruments", method="PUT", data=data
        )

    def create_access_token(self, order_id):
        data = {"order": {"id": order_id, "is_recurring": False}}
        return self.__request(
            api_path="/v3/payments/access_tokens", method="POST", data=data
        )

    def get_stored_instruments(self, customer_id):
        api_path = "/v3/customers/{}/stored-instruments".format(customer_id)
        return self.__request(api_path=api_path, method="GET")

    def get_default_stored_instrument(self, customer_id):
        instruments = self.get_stored_instruments(customer_id)
        for i in instruments:
            if i.get("is_default") == True:
                return i
        return None

    def get_payment_methods(self, order_id):
        return self.__request(
            api_path="/v3/payments/methods?order_id={}".format(order_id), method="GET"
        )

    def get_order_default_payment_method(self, order_id):
        payment_methods = self.get_payment_methods(order_id)

        for i in payment_methods:
            if len(i["stored_instruments"]) > 0:
                for instrument in i["stored_instruments"]:
                    if instrument["is_default"]:
                        result = {
                            "payment": {
                                "instrument": {
                                    "type": instrument["type"],
                                    "token": instrument["token"],
                                },
                                "payment_method_id": i["id"],
                            },
                        }
                        return result

    def process_payment(self, order_id):
        payment_token = self.create_access_token(order_id)
        request_headers = self.HEADERS
        request_headers["Accept"] = "application/vnd.bc.v1+json"
        request_headers["Authorization"] = "PAT {}".format(payment_token["id"])
        data = self.get_order_default_payment_method(order_id)
        return self.__request(
            api_path="/payments",
            headers=self.HEADERS,
            method="POST",
            data=data,
            context="payment",
        )

    def create_order(self, data):
        data = {
            "status_id": 0,
            "customer_id": 3,
            "payment_method": "credit_card",
            "billing_address": {
                "first_name": "Ivan",
                "last_name": "Pinkin",
                "street_1": "6030 Texas Heritage Pkwy",
                "city": "Fulshear",
                "state": "Texas",
                "zip": "77441",
                "country": "United States",
                "country_iso2": "US",
                "email": "ivan.pinkin@pinkzebrahome.com",
            },
            "products": [
                {
                    "product_id": 1793,
                    "quantity": 1,
                    "price_inc_tax": 38,
                    "price_ex_tax": 34,
                }
            ],
            "external_source": "KillBill",
            "base_handling_cost": 34 * 0.04,
            "base_shipping_cost": 4.00,
            "shipping_cost_inc_tax": 4.00,
            "handling_cost_inc_tax": 34 * 0.04,
            "shipping_cost_ex_tax": 4.00,
            "handling_cost_ex_tax": 34 * 0.04,
        }
        request_headers = self.HEADERS
        request_headers["Accept"] = "application/json"
        return self.__request(
            api_path="/v2/orders", headers=self.HEADERS, method="POST", data=data
        )


# -- Example --
# service = RAWService()
# access_token = service.create_access_token(30000507)
# default_instrument = service.get_order_default_payment_method(30000507)
# order_payment = service.process_payment(30000506)
# order = service.create_order('1')
