import statistics

n = int(input())

A = []
for i in range(n):
    ni = int(input())
    A.append(ni)

# trung bình
trung_binh = sum(A)/len(A)  
trung_binh_cach_2 = statistics.mean(A)

trung_binh_rouned = round(trung_binh,6)
print("{0:.6f}".format(trung_binh_rouned))

# trung vị: số nằm giữa khi đã sort tăng dần. 
# len(list) chẵn --> ptử trung vị 
# là giá trị trung bình của hai phần tử ở giữa.
A_sorted = sorted(A)
if len(A) % 2 == 0:
    vi_tri_giua_of_list_chan = len(A)//2
    trung_vi_list_chan = (A_sorted[vi_tri_giua_of_list_chan - 1] + A_sorted[vi_tri_giua_of_list_chan])/2
    print("{0:.6f}".format(trung_vi_list_chan))
else:
    vi_tri_giua_of_list_le = len(A)//2
    trung_vi_list_le = A_sorted[vi_tri_giua_of_list_le]
    print("{0:.6f}".format(trung_vi_list_le))