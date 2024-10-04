from datetime import datetime

def expired_date(day=1, month=1, year=None):
    """
    Check if a provided date has expired based on the provided expiry month, year, and day.

    Parameters:
    month (int, optional): The expiry month of the provided date. Defaults to 1.
    year (int, optional): The expiry year of the provided date. Defaults to CurrentYear.
    day (int, optional): The expiry day of the provided date. Defaults to 1.

    Returns:
    bool: True if the provided date has expired, False otherwise.
    """
    current_date = datetime.now()
    
    if year is None:
        year = current_date.year 
    
    expiry_date = datetime(year, month, day)
    return current_date >= expiry_date
