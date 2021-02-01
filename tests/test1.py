# 5 = A
# 3 = B

a = "011111111111122222222222222233333333333333333"
while "01" in a  or "02" in a or "03" in a:
        a = ('103'.join(a.split('01')))
        a = ('10'.join(a.split('02')))
        a = ('210'.join(a.split('03')))
print(a)
