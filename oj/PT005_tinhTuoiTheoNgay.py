N = int(input())
# chia lấy nguyên
years = (N//365) 
# (N - years*365) : số ngày còn lại
months = (N - years*365)//30
days = (N-years*365-months*30)
if years !=0:
    print( years, 'years')
if months !=0:
    print( months, 'months')
if days !=0:
    print( days, 'days')