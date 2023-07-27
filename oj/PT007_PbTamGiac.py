a,b,c = map(float, input().split())
if a == b == c:
    print('Tam giac deu')
elif a == b or b == c or a == c: 
    print('Tam giac can')
else:
    print('Tam giac thuong')