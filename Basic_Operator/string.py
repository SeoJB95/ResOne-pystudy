# 문자열 concatenate
A = '\nHello, World!'
B = ' Welcome to Python!!\n'
# A+B = '\nHello, World! Welcome to Python!!\n'
print(A+B)

# 문자열 슬라이싱
C = 'abcdefg'
# --'0123456'
print(C[2],'==>c')
print(C[2:4],'==>cd')
print(C[2:6],'==>cdef')
print('\n')

#문자열 split ; 특정기준으로 문자열 나누기
D = '0.125, 0.524, 0.166, 0.234, 0.747'
F = D.split(',')
print(F)

# 특정 문자를 기준으로 문자열 합하기
G = ','.join('abcde')#'a,b,c,d,e'
H = '\t'.join('abcde')#'a,b,c,d,e'
print(G)
print(H)

# 대문자로 바꾸기, 소문자로 바꾸기
A_1 = A.upper()
A_2 = A.lower()
print(A_1)
print(A_2)

#문자열 교체하기
I = 'My name is replace'
print(I.replace('replace','Seo Jeongbeom'))
print(I.replace('replace','Paul'))
#from pprint import pprint
#pprint(dir(A))
