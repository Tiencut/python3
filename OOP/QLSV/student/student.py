input data as d

def addStudent():
    print('*** add sv ***')

    # 
    in4 = {
        'masv' : '',
        'name' : ''
    }

    # nhập masv, check trùng masv --> nhập lại
    masv = input('nhập masv: ')

    while True:
        student = findStudent(masv)
        if student != False:
            masv = input('masv này đã tồn tại, nhập lại: ')
        else:
            break
    
    in4['masv'] = masv

    # nhập tên
    in4['masv'] = input('nhập tên sv: ')

    # lưu vào ds sv
    d.listStudents.append(in4)

def findStudent(masv):
    for i in range(0, len(d.listStudents)):
        if d.listStudents[i]['masv'] == masv:
            # return mảng 2 phần tử
            # 0: vị trí tìm thấy, 1: dữ liệu
            return [i, d.listStudents[i]]
    return False

def deleteStudent():
    masv = input('nhập masv cần xoá')

    student = findStudent(masv)

    if student != False:
        d.listStudent.remove(student[1])
        print('delete success')
    else:
        print('no find sv cần delete')

def showStudent():
    print()
    print('*** SHOW LIST SINH VIÊN ***')
    for i in range(len(d.listStudents)):
        print(f"[{d.listStudents[i]['masv']},] [{d.listStudents[i]['name']}]")

def editStudent():
    masv = input('masv cần fix?: ')
    student = findStudent(masv)

    if student == False:
        print('No find')
    else:
        name = input('tên sv?: ')
        student[1]['name'] = name
        d.listStudents[student[0]] = student[1]