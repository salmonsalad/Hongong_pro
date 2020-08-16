# 파이썬에서 리스트는 루프에서 사용할 때 유용함

sum = 0

# 리스트 만들기
list = range(1, 11)
# print(list)

for i in list:
  sum = sum + i

print('합계: ', sum)