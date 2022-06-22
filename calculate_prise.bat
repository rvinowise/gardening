out_price = 2300

blueberry = 500
lingonberry = 160
blackberry = 160
Малина_черная = 150

total_price = 
blueberry*3 + 
lingonberry*2 + 
blackberry*3 +
Малина_черная*2 +




print(total_price)

with open(__file__, 'r') as f:
    lines = f.read().split('\n')
    val = int(lines[0].split(' = ')[-1])
    new_line = 'out_price = {}'.format(total_price)
    new_file = '\n'.join([new_line] + lines[1:])

with open(__file__, 'w') as f:
    f.write('\n'.join([new_line] + lines[1:]))


input("any key to exit")