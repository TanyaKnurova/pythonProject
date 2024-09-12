import os

def process_files(file_names):
    file_info = []
    for file_name in file_names:
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_info.append((file_name, line_count, lines))
    file_info.sort(key=lambda x: x[1])

    file = os.path.abspath('C:/Users/tatia/PycharmProjects/pythonProject/file/task.txt')

    with open(file, 'w', encoding='utf-8') as f_out:
        for file_name, line_count, lines in file_info:
            f_out.write(file_name + '\n')
            f_out.write(str(line_count) + '\n')
            f_out.writelines(lines)
            f_out.write('\n')


if __name__ == '__main__':
    files_to_process = [
        '1.txt',
        '2.txt',
        '3.txt'
    ]
    process_files(files_to_process)