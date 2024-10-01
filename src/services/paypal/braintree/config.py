import braintree
from src.config import __env


ENVIRONMENT = braintree.Environment.All[__env["PPB_ENVIRONMENT"].lower()]
MERCHANT_ID = __env["PPB_MERCHANT_ID"]
PUBLIC_KEY = __env["PPB_PUBLIC_KEY"]
PRIVATE_KEY = __env["PPB_PRIVATE_KEY"]

# Braintree's config
config = braintree.Configuration(
    environment=ENVIRONMENT,
    merchant_id=MERCHANT_ID,
    public_key=PUBLIC_KEY,
    private_key=PRIVATE_KEY,
)

# Instances of BraintreeGateway's clients for direct use
gateway = braintree.BraintreeGateway(config)
