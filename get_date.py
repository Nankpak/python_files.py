from datetime import datetime 
def get_date():
    now = datetime.now()
    get_date = now.strftime('%d-%m-%y')
    get_year = now.year
    return get_date,get_year
get_date,get_year = get_date()
print(get_date,get_year)
