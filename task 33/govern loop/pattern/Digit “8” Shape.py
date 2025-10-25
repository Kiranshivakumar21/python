# Digit 8 Shape
height = 7
width = 5
mid = height // 2
for i in range(height):
    if i == 0 or i == mid or i == height - 1:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')
