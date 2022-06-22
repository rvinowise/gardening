out_price = 3500
out_price_wholesale = 3050

blueberry = 500
Малина_черная = 150
lingonberry = 160
blackberry = 150
arctic_raspberry = 100
honeysuckle = 100
mulberry = 160
cranberry = 160
goumi = 180

blueberryW = 450
Малина_чернаяW = 120
lingonberryW = 140
blackberryW = 120
arctic_raspberryW = 90
honeysuckleW = 80
mulberryW = 140
cranberryW = 140
goumiW = 160

total_price = \
blueberry*3 + \
lingonberry*2 + \
Малина_черная*2 +\
blackberry*2 + \
arctic_raspberry*2 + \
honeysuckle*3 +\
mulberry+\
goumi*2+\
cranberry


if (total_price > 3000):
    out_price_wholesale = \
    blueberryW*3 + \
    lingonberryW*2 + \
    Малина_чернаяW*2 +\
    blackberryW*2 + \
    arctic_raspberryW*2 + \
    honeysuckleW*3 +\
    mulberryW+\
    goumiW*2+\
    cranberryW
    




print(out_price_wholesale)

with open(__file__, 'r') as f:
    lines = f.read().split('\n')
    #val = int(lines[0].split(' = ')[-1])
    new_line_price = 'out_price = {}'.format(total_price)
    #new_file = '\n'.join([new_line_price] + lines[1:])
    new_line_wholesale_price = 'out_price_wholesale = {}'.format(out_price_wholesale)
    #new_file = '\n'.join([new_line_wholesale_price] + lines[1:])

with open(__file__, 'w') as f:
    f.write('\n'.join([new_line_price] + [new_line_wholesale_price] + lines[2:]))
    

