# 딕셔너리는 중복 데이터가 몇 개 있는지 확인하는데 유용
# 사전이라는 의미처럼 파일을 열어서 단어의 개수를 세는 데 사용한다.
# 검색 'python dictionary word count'

handle = open("list_lotto.py")

# dictionary 초기화
words_dict = dict() 

# 파일에서 한 라인을 읽어온다
for line in handle:
  # 한 라인을 빈칸으로 구분하여 단어를 가져온다
  words = line.split()

  for word in words:
    # 기존 단어사전에서 단어의 개수를 하나 증가시킨다.
    words_dict[word] = words_dict.get(word, 0) + 1

print(words_dict)
