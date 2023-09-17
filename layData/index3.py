import requests

cookies = {"username": "22T1020761", "password": "Tiencut2711"}

# Lấy mã trạng thái của trang web
status_code = requests.get("https://student.husc.edu.vn/Course/Details/2023-2024.1.TIN3042.009/", cookies=cookies).status_code

if status_code == 401:
    print("Trang web yêu cầu đăng nhập")
elif status_code == 200:
    # Lấy data
    data = requests.get("https://student.husc.edu.vn/Course/Details/2023-2024.1.TIN3042.009/", cookies=cookies).text
    print(data)
