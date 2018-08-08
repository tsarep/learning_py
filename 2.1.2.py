# 0,15542352 => 15.5%
# 3542352515,156467496846546 => 3,542,352,515.15 $

x = '0,15542352'
y = '3542352515,156467496846546'

def persent(x):
    y = x.replace(',', '.')
    y = float(y)
    y = '{:.1%}'.format(y)
    print(y)

def valuta(x):
    y = x.replace(',', '.')
    y = float(y)
    y = '{:,.2f}'.format(y)
    y = y + ' $'
    print(y)

persent(x)
valuta(y)
