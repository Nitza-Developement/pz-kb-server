CARD_BRANDS = {
    "AMEX": "american_express",
    "American Express": "american_express",
    "VISA": "visa",
    "MC": "mastercard",
    "MASTERCARD": "mastercard",
    "DISC": "discover",
    "DISCOVER": "discover",
    "JCB": "jcb",
    "DINERS": "diners_club",
    "DINERS CLUB": "diners_club"
}

INVERTED_CARD_BRANDS = {v: k for k, v in CARD_BRANDS.items()}
