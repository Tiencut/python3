try:
    n = int(input())
    m = list(map(int,input().split()))
    
    if n != len(m):
        print("Độ dài của dãy không khớp với số phần tử đã nhập!")
    else:
        so_lan_bien_doi = 0
        is_odd = False

        # lặp đến khi dãy xuất hiện lẻ
        while is_odd == False:
            # check cả dãy chẵn?
            # for i in m:
            #     if i % 2 != 0:
            #         is_odd = True
            #         break
            for i in range(n):
                if m[i] % 2 != 0:
                    is_odd = True
                    break

            if is_odd == True:
                break

            # //= 2
            for j in range(n):
                m[j] //= 2

            so_lan_bien_doi += 1

        print(so_lan_bien_doi)
except ValueError:
    print("Đầu vào không hợp lệ!")