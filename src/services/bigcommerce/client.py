from .config import (
    api_v2 as __api_v2,
    api_v3 as __api_v3,
    api_gql as __api_gql,
)


# Client's instances of Bigcommerce for direct use
api_gql = __api_gql
api_v2 = __api_v2
api_v3 = __api_v3
