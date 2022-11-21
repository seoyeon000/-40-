import qrcode

file_path ='04. QR 코드 생성기\qr코드모음.txt'

with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines =f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)
        
        qr_date = line
        qr_img = qrcode.make(qr_date)
        
        save_path = '04. QR 코드 생성기\\' + qr_date + '.png'
        qr_img.save(save_path)