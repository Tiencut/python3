do_cao, leo_duoc_a, tut_b = map(int, input().split())
so_ngay_de_an_la = 0

if leo_duoc_a >= do_cao:
    so_ngay_de_an_la = 1
else:
    while do_cao > 0:
        do_cao -= (leo_duoc_a - tut_b)
        so_ngay_de_an_la += 1

    if do_cao < 0:
        so_ngay_de_an_la = -1

print(so_ngay_de_an_la)
