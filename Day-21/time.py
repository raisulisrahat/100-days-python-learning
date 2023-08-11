# Here i am showing python built module in Datetime

# Resource https://strftime.org/

import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%A - %B%d%Y,  %I:%M:%S %p"))