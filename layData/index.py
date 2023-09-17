import requests
import bs4

def get_link(link_nhap):
    links = []
    for i in range(25):
        if i<10:
            links.append(link_nhap + str(0) + str(i) + '/')
        else:
            links.append(link_nhap + str(i) + '/')
    return links

def find_match(link, masv):
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # Tìm thẻ table có class là table-striped table-hover
    table = soup.find(class_="table table-striped table-hover")

    # Tìm thẻ tr có thẻ td thứ hai có text là mã sinh viên
    student = table.find_all("tr")[0]

    if student is not None:
        student_id = student.find_all("td")[1].text

        if student_id == masv:
            return True
    return False



def main():
    masv      = input("mã sinh viên? ")
    link_nhap = input("link? ")
    link_nhap = link_nhap[:-3]

    # Lấy list link
    links = get_link(link_nhap)

    # find masv trong các link
    for link in links:
        if find_match(link, masv):
            print(link)
            return
    print("không tìm thấy")

if __name__ == "__main__":
    main()
