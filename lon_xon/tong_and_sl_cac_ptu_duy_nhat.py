my_set = list(map(int,input("nhap cac ptu: ").split()))

total_sum = sum(map(int,my_set))

my_1_set = set(my_set)
num_uniqua_elements = len(my_1_set)

print("tong cac ptu",total_sum)
print("sl cac ptu duy nhat: ", num_uniqua_elements)