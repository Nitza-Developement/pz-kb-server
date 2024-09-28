import bigcommerce
from src.config import __env


# Private apps (Basic Auth)
const_BAuth = {
    "host": __env["BC_BASE_URL_BASIC"],
    "basic_auth": (
        __env["BC_USERNAME"],
        __env["BC_API_TOKEN"],
    ),
}
# Private apps (Basic Payments Auth)
const_BPAuth = {
    "host": __env["BC_BASE_URL_PAYMENT"],
    "basic_auth": (
        __env["BC_USERNAME"],
        __env["BC_API_TOKEN"],
    ),
}
# Public apps (OAuth)
const_OAuth = {
    "client_id": __env["BC_APP_CLIENT_ID"],
    "store_hash": __env["BC_STORE_HASH"],
    "access_token": __env["BC_ACCESS_TOKEN"],
}

# GraphQL API Instances
client_GQL = bigcommerce.connection.GraphQLConnection(**const_OAuth)

# REST API Instances
client_BAuth = bigcommerce.api.BigcommerceApi(**const_BAuth)
client_PAuth = bigcommerce.api.BigcommerceApi(**const_BPAuth)
client_OAuth = bigcommerce.api.BigcommerceApi(**const_OAuth)
v3client_OAuth = bigcommerce.connection.OAuthConnection(
    **const_OAuth,
    api_path="/stores/{}/v3/{}",
)

BC_ENDPOINTS_FILE_PATH = "src/services/bigcommerce/endpoints.json"

# Instances of Bigcommerce's clients for direct use
api_vraw_basic = client_BAuth
api_vraw_payment = client_PAuth
api_v2 = client_OAuth
api_v3 = v3client_OAuth
api_gql = client_GQL
