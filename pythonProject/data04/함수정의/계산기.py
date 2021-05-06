def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# 다른 곳에서 import하여 기능을 사용할 때, main 안에 넣게되면
# 해당 모듈에서만 실행되고 다른 모듈에서 실행되지 않음
if __name__ == '__main__':
    print('더한 결과>> ',add(1000, 200))