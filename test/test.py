def luckyNum():
    # số may mắn gồm 4 và 7
    def luckySuperNum(n):
        # check ngoài số 4 và 7 còn số khác không
        so4 = 0
        so7 = 0
        # đếm số chữ số 4, 7
        for i in n:
            if i == '4':
                so4 += 1
            elif i == '7':
                so7 += 1
            else:
                return False
        if so4 == so7:
            return True
        else:
            return False

    n = input()

    if luckySuperNum(n):
        print('True')
    else:
        print('False')


# dùng hàm có sẵn
def nhiPhan_sang_thapPhan():
    s = input()
    s = int(s,2)
    print(s)


# tự viết hàm
def nhiPhan_sang_thapPhan_1():
    nhiPhan = input()

    thapPhan= 0
    for i in range(len(nhiPhan)):
        thapPhan = thapPhan * 2 + int(nhiPhan[i])

    print(thapPhan)


def nhiPhan_sang_thapPhan_2():
    s = input()
    s_reverse = s[::-1]
    thap_phan = 0
    for i in range(len(s_reverse)):
        thap_phan += int(s_reverse[i])*(2**i)
    print(thap_phan)

# nhập 1 dãy số, tính tổng các số phân biệt chia hết cho 5
def TongDSĐK():
    list_n = list(map(int,input().split()))
    
    def cach_1():
        tongCacSoPhanBietChiaHetCho5 = []
        for i in list_n:
            if i % 5 == 0 and i not in tongCacSoPhanBietChiaHetCho5:
                tongCacSoPhanBietChiaHetCho5.append(i)
        print(sum(tongCacSoPhanBietChiaHetCho5))
        
    def cach_2():
        list_n_phan_biet = list(set(list_n))
        print(list_n_phan_biet)

    # no use hàm có sẵn
    def cach_3
TongDSĐK()

def sxMaTran():
    m,n = map(int,input().split())
    L = []
    for row in range(m):
        tmp = list(map(int,input().split()))
        L.append(tmp)
    
    # sx thường
    for i in range(m):
        for j in range(n):
            for row in range(m):
                for col in range(n):
                    if L[i][j] < L[row][col]:
                        tmp = L[i][j]
                        L[i][j] = L[row][col]
                        L[row][col] = tmp

    for row in L:
        print(' '.join([str(elem) for elem in row] ))

# hàm sxMaTran(), làm cách chuyển về ma trận chiều, 