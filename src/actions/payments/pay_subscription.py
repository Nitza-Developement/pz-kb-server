# from src.services.bigcommerce.functions.vendor.transform_to_braintree_customer import get_braintree_customer as bc_get_braintree_customer
# from src.services.paypal.braintree.services.get_customer import get_customer_by_email as pb_get_customer_by_email
# from src.services.paypal.braintree.services.create_customer import create_customer as pb_create_customer
# from src.services.paypal.braintree.services.create_credit_cart import 


def pay_subscription_braintree(customer_data):
    """
    """
    bc_customer_id = 1
    pb_customer_id = 1
    kb_customer_id = 1
    customer_data = {
        "customer_id" :1,
        "customer_email" :"test@test.com",
    }

    # buscar el customer dentro de braintree (funciones dentro de los services)

    # obtener datos clientes ya al full (funciones dentro de los services)
    
    # proceder al pago de braintree  (funciones dentro de los services)

    # proceder a notificar a bc el pago  (funciones dentro de los services)
    
    # proceder a notificar a kb el pago  (funciones dentro de los services)