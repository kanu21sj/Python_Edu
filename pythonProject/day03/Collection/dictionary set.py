# set(집합)
# 중복을 허용하지 않음.

jumsu_list = [100, 30, 50, 60, 30, 100]
jumsu_set = set(jumsu_list)
print(type(jumsu_set))
print(jumsu_set)

jumsu_list2 = [50, 60, 30]
jumsu_set2= set(jumsu_list2)
result = jumsu_set2.intersection(jumsu_set)
print(result)