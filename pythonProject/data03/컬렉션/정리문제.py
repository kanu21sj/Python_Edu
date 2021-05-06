# for x in range(3):
#     input('*')
#
# # while True:
# #     print('나는 참이야')
#
# for x in [1, 2, 3, 4]:
#     print(x)

c1 = [22, 99, 11, 23]
c2 = [44, 99, 66, 23]
count = 0
for i in range(len(c1)):
  if c1[i] == c2[i]:
    count = count + 1
    print("index : " + str(i) + ", 값은 : " + str(c1[i]))
print(count)