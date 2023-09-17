import requests

# định dạng data nhận được
import json

def ipLookUp(public_ip):
    r = requests.get(public_ip)

    if r.status_code == 200: # if thành công
        data = r.text
        print(data)
    else:
        print("Error Occured while making request")

# if __name__ == "__main__":
#     try:
#         ip = input("enter ip:")
#         ipLookUp(ip)
#     except:
#         print("Error Occured!")

ip = input("enter ip:")
ipLookUp(ip)
