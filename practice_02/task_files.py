f1 = open('file_1.txt', 'r')
data1 = f1.readlines()
f1.close()

print(data1)

f2 = open('file_2.txt', 'r')
data2 = f2.readlines()
f2.close()

print(data2)

try:
    line2_f1 = data1[1]
    data2[1] = line2_f1
except IndexError:
    pass

f2 = open('file_2.txt', 'w')

try:
    f2.write(''.join(data2))
except Exception as e:
    print(e)
finally:
    f2.close()
