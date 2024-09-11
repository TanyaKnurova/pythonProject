with open('1.txt', encoding='utf-8') as f1:
            file1 = f1.readlines()
with open('2.txt', encoding='utf-8') as f2:
            file2 = f2.readlines()
with open('3.txt', encoding='utf-8') as f3:
            file3 = f3.readlines()
with open('file.txt', 'w', encoding='utf-8') as f:
    if len(file1) < len(file2) and len(file1) < len(file3):
        f.write('1.txt' + '\n')
        f.write(str(len(file1)) + '\n')
        f.writelines(file1)
        f.write('\n')
    elif len(file2) < len(file1) and len(file2) < len(file3):
        f.write('2.txt' + '\n')
        f.write(str(len(file2)) + '\n')
        f.writelines(file2)
        f.write('\n')
    elif len(file3) < len(file1) and len(file3) < len(file2):
        f.write('3.txt' + '\n')
        f.write(str(len(file3)) + '\n')
        f.writelines(file3)
        f.write('\n')
    if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
        f.write('1.txt' + '\n')
        f.write(str(len(file1)) + '\n')
        f.writelines(file1)
        f.write('\n')
    elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) > len(file3):
        f.write('2.txt' + '\n')
        f.write(str(len(file2)) + '\n')
        f.writelines(file2)
        f.write('\n')
    elif len(file1) > len(file3) > len(file2) or \
            len(file3) > len(file1) and len(file3) < len(file2):
        f.write('3.txt' + '\n')
        f.write(str(len(file3)) + '\n')
        f.writelines(file3)
        f.write('\n')
    if len(file1) > len(file2) and len(file1) > len(file3):
        f.write('1.txt' + '\n')
        f.write(str(len(file1)) + '\n')
        f.writelines(file1)
        f.write('\n')
    elif len(file2) > len(file1) and len(file2) > len(file3):
        f.write('2.txt' + '\n')
        f.write(str(len(file2)) + '\n')
        f.writelines(file2)
        f.write('\n')
    elif len(file3) > len(file1) and len(file3) > len(file2):
        f.write('3.txt' + '\n')
        f.write(str(len(file3)) + '\n')
        f.writelines(file3)
        f.write('\n')
    else:
        print('Проверьте корректность данных')