fp_r = open("L_In.txt", 'r')
fp_w = open("L_Out.txt", 'w')

# 첫 줄을 읽어 인덱스로 사용
index_line = fp_r.readline()
index = int(index_line.strip())  # 줄 바꿈 문자 제거 후 정수 변환

print(f"index = {index}", file=fp_w)

A = []
B = []

for i, line in enumerate(fp_r):
    if i == 0: #첫번째 줄 읽어서 파일에 쓰기
        A = list(int(x) for x in line.split())
        print(f"A = {A}", file=fp_w)
    elif i == 1:  #두번째 줄 읽어서 파일에 쓰기
        B = list(int(x) for x in line.split())
        print(f"B = {B}", file=fp_w)


tmp = A[index] + B[index]
print(f"A[{index}] + B[{index}] = {tmp}", file=fp_w)

fp_r.close()
fp_w.close()
