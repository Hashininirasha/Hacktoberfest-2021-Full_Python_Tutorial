# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
# 60 = 0b111100
# 30 = 0b011110
x=60 ^ 30
print(x)
# Out: 34
# 34 = 0b100010
y=bin(60 ^ 30)
print(y)
# Out: 0b100010