import braintree
from src.config import __env


ENVIRONMENT = braintree.Environment.All[__env["PP_BT_ENVIRONMENT"].lower()]
MERCHANT_ID = __env["PP_BT_MERCHANT_ID"]
PUBLIC_KEY = __env["PP_BT_PUBLIC_KEY"]
PRIVATE_KEY = __env["PP_BT_PRIVATE_KEY"]

# Braintree's config
config = braintree.Configuration(
    environment=ENVIRONMENT,
    merchant_id=MERCHANT_ID,
    public_key=PUBLIC_KEY,
    private_key=PRIVATE_KEY,
)

# Instances of BraintreeGateway's clients for direct use
api = braintree.BraintreeGateway(config)
