#name = input('이름을 입력해 주세요 : ')
string = 'Hi my name is {:10s}, nice to meet you'.format('Seo JB')
print(string)
# format method
result_0 = "resistance dynamometer value : {:.2f}N".format(55.623)
result_1 = "resistance dynamometer value : {:.3f}N".format(55.623)
result_2 = "resistance dynamometer value : {:.4f}N".format(55.623)
print(result_0)
print(result_1)
print(result_2)
result_3 = \
"resistance dynamometer value : {:.4f}N , {:.4f}N, {:.4f}N"\
.format(55.623,2.3456,62.123)
print(result_3)

Measured = 52.1634
# f formatting
tmp = f'resistance dynamometer value : {Measured:.3f}N'
tmp_1 = f'resistance dynamometer value : {Measured:.4f}N'
tmp_2 = f'resistance dynamometer value : {Measured:.5f}N'
print(tmp)
print(tmp_1)
print(tmp_2)
