# 끝에 요소 추가하기
a = [1,2,5,3,6,4]
b = a
a.append(7)
print(a)

# 리스트 요소를 정렬하기
a.sort()
print(a)
# 리스트 순서를 역순으로 만들기
a.reverse()
# 특정 요소의 위치를 반환하기
idx = a.index(4) #4 의 위치를 반환함
print(a)
print(a[idx]) # ==> 4

#원하는 위치에 요소 삽입
a.insert(idx,9) # 4의 위치에 9를 삽입함
print(a)

#이외에도 remove, pop, extend 등의 메소드 활용가능
