# effeef
text = "yangyanmeng"
for i in text:
    print(i + ' ')

name = ["jack","tianxia","huangzi","demaxiya"]
for it in name:
    print(it,len(it))

for i in range(5):
    print(i)

print("next line\n")
for i in range(2,8):
    print(i)

print("next line\n")
for i in range(1,10,2):
    print(i)

print("next line\n")
for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 5
    print(i)
