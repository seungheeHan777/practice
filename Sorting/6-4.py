# 성적이 낮은 순서로 학생 출력하기

# n명의 학생 정보가 이다. 정보는 이름과 성적으로 구분된다.
# 각 학생의 이름과 점수가 있을때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성


n=int(input())
array=[]
for i in range(n):
    array.append(input().split())
    array[i][1]=int(array[i][1])
    # 이런 방식도 가능
#     input_data=input().split()
#     array.append(input_data[0],int(input_data[1]))
result = sorted(array,key=lambda x:x[1])
for i in result:
    print(i[0],end=' ')