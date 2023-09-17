import numpy as np

# m,n = map(int,input().split())
# A = np.array( [ [ int(x) for x in input().split() ] for row in range(m) ] )

# def tong_hang_va_cot():
#     # tính tổng từng hàng
#     for row in range(m):
#         print(f"tổng hàng {row} = {A[row].sum()}")
#     # tính tổng từng cột
#     for col in range(n):
#         print(f"tổng cột {col} = {A[:, col].sum()}")

# def chuyen_vi():
#     mtr_chuyen_vi = []
#     for row in range(n):
#         mtr_chuyen_vi.append( [A[col][row] for col in range(m)] )
#     return mtr_chuyen_vi
# mtr_cv = chuyen_vi()
# print(mtr_cv)
# for row in mtr_cv:
#     print(' '.join( str(x) for x in row ))

# def check_mtr_doi_xung():
#     n = int(input())
#     A = np.array([ [ int(x) for x in input().split() ] for row in range(n) ])

#     mtr_chuyen_vi = []
#     for row in range(n):
#         mtr_chuyen_vi.append( [A[col][row] for col in range(n)] )

#     return np.all( a == b for a,b in zip(A,mtr_chuyen_vi) )

# if check_mtr_doi_xung():
#     print('true')
# else:
#     print('False')

# def trung_binh_cong_duong_cheo_chinh():
#     n = int(input())
#     A = np.array([ [ int(x) for x in input().split() ] for row in range(n) ])

#     tbc_dcc = []
#     for i in range(n):
#         tbc_dcc.append( A[i][i] )

#     return sum(tbc_dcc) / len(tbc_dcc)