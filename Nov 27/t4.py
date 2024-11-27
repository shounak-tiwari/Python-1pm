day_name_hindi = ['रविवार','सोमवार', 'मंगलवार', 'बुधवार', 'गुरुवार', 'शुक्रवार', 'शनिवार' ]

import datetime 

x = datetime.date(2024,12,1)

x = x.strftime("%w")

x = int(x)
print('आज दिन है:',day_name_hindi[x])
print(x)