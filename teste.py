from datetime import datetime
date_string = "12/11/2018"
date = datetime.strptime(date_string, "%d/%m/%Y").date()
print(date)