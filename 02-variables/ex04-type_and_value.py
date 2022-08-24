width = 17
height = 12.0

TYPE = "Type:"
VALUE_1 = width // 2
VALUE_2 = width / 2.0
VALUE_3 = height / 3
VALUE_4 = 1 + 2 * 5

print("width//2: Value:",VALUE_1,"|", TYPE,type(VALUE_1))     # 8 | int
print("width/2.0: Value:",VALUE_2,"|", TYPE,type(VALUE_2))   # 8.5 | float
print("height/3: Value:",VALUE_3,"|", TYPE,type(VALUE_3))    # 4.0 | float
print("1+2*5: Value:",VALUE_4,"|", TYPE,type(VALUE_4))   # 11 | int
