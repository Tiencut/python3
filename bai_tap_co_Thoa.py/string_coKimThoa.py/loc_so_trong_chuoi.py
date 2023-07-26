s = input()
max_length = 0
# tách thành từng chữ bỏ vào list, check list[i] .isalpha()?
for i in s.split():
    if i.isalpha():
        max_length = max(len(i),max_length)

        if len(i) > max_length:
            max_length = len(i)
    else:
        max_length = max(max_length, sum(1 for j in i if j.isalpha()) )

print(max_length)