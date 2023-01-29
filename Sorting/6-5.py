n,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

# a= list(map(int,input().split()))
# b= list(map(int,input().split()))
sort_a=sorted(a)                # 오름차순
sort_b=sorted(b,reverse=True)   # 내림차순
for i in range(k):
    # 비교해서 b가 더 클 경우
    if sort_a[i]<sort_b[i]:
        sort_a[i],sort_b[i] = sort_b[i],sort_a[i]
    else:
        break
print(sum(sort_a))
