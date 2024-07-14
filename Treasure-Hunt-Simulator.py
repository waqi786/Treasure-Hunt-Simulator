row1 = ["Ali","Waqar","Rao"]
row2 = ["Ahmad","Ayan","Muzamil"]
row3 = ["Bilal","Abrar","Rashid"]
m = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
a = input("enter a number where you put the treasure: ")
horizontal = int(a[0])
vertical = int(a[1])
s = m[vertical-1]
m[horizontal-1][vertical-1] = "X"
print(f"{row1}\n{row2}\n{row3}")