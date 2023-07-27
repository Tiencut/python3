# tủ có size 3 chiều: a*b*c
# cửa nhà size: x*y
# đem tủ vào nhà được không, khi đưa có thể xoay tủ theo các kiểu khác nhau

a,b,c,x,y = map(int,input().split())


if  (a <= x and b <= y) or (b <= x and a <= y) \
    (b <= x and c <= y) or (c <= x and b <= y) \
    (a <= x and c <= y) or (c <= x and a <= y):
    print("Yes")
else:
    print("No")