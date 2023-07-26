n = input()

def check_so_doi_xung(n):
    return n == n[::-1]

if check_so_doi_xung(n):
    print("Yes")
else:
    print("No")