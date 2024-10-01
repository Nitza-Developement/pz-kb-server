import killbill
from src.config import __env


TENANT = __env["KB_TENANT"]

USERNAME = __env["KB_USERNAME"]
PASSWORD = __env["KB_PASSWORD"]
API_URL = __env["KB_API_URL"]
TIMEOUT = __env["KB_TIMEOUT"]

API_KEY = __env["KB_API_KEY"]
API_SECRET = __env["KB_API_SECRET"]
CREATED_BY = USERNAME

API_URL = "http://killbill.towithouston.com"

header = killbill.Header(
    api_key=API_KEY,
    api_secret=API_SECRET,
    created_by=CREATED_BY,
)
killbill_api = killbill.KillBillClient(
    username=USERNAME,
    password=PASSWORD,
    api_url=API_URL,
    timeout=TIMEOUT,
)
