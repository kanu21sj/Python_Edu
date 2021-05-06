#for문을 사용해보세요
#range
# 1. range(20) print!
for x in range(20):
    print(x)
print("=============")

# 2. 1부터 100까지 print!
for x in range(1, 100):
    print(x)
print("=============")

# 3. 0부터 200까지 print!
for x in range(0, 200):
    print(x)
print("=============")

# 4. 1부터 100까지 중 2씩 점프해서 print!
for x in range(1, 100, 2):
    print(x)
print("=============")

# 5. 100부터 500까지 중 5씩 점프해서 print!
for x in range(100, 500, 5):
    print(x)
print("=============")

# 6. 100부터 500까지 중 10씩 점프하고 모두 더해서 print!
sum2 = 0
for x in range(100, 500, 10):
    sum2 = sum2 + x
    print(sum2)
print("=============")

# 7. 3부터 200까지 중 8씩 점프한 값을 모두 곱해서 print!
sum3 = 1
for x in range(3, 200, 8):
    sum3 = sum3 * x
    print(sum3)
print("=============")

# 8. food = ['감자', '고구마', '양파']를 다음과 같이 print!
# 8-1. 감자짱!
#      고구마짱!
#      양파짱!
food = ['감자', '고구마', '양파']
for x in food:
    print(x + '짱!')
print("=============")

# 8-2. 감자짱! 고구마짱! 양파짱!
for x in food:
    print(x + '짱!', end=' ')
print("")
print("=============")

# 9. food2 = "감자 고구마 양파 스프 국수 라면"을 다음과 같이 print!
# 감자맛있어! 고구마맛있어! 스프맛있어! 라면맛있어!
food2 = "감자 고구마 양파 스프 국수 라면"
food_list = food2.split()
for x in food_list:
    if x not in ['양파', '국수']:
        print(x + '맛있어!', end=' ')
print()
for x in food_list:
    if x == '양파' or x == '국수':
        continue
    print(x + '맛있어!', end=' ')
