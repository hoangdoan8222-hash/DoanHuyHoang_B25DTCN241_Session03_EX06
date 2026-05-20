
confirm = ''
while True:
    employese_quantity = int(input('Nhập số lượng nhân viên'))
    for i in range (1,employese_quantity + 1):
        print(f'Nhân viên {i}')
        employese_name = input('Tên Nhân viên: ')
        working_days = int(input('Số ngày đi làm: '))
        print(f'Thông tin nhân viên {i}')
        print(f'Tên: {employese_name}')
        print(f'Số ngày đi làm: {working_days}')
        if working_days < 20:
            print('Cần cải thiện chuyên cần ')
        else:
            print('Nhân viên chuyên cần tốt\n')
    confirm = input('Tiếp tục truong trinh (y/n):').lower().strip()
    if confirm == 'n':
        print('Trương trình kết thúc')
        break
