"""Module sorting file that does not fit into memory"""
import comparators
import argparser
import os
import os.path
import shutil

COMPARATORS = {
    'lex': comparators.lexicographical_order_key,
    'length': comparators.length_order_key,
    'random': comparators.random_order_key
}


def sort_file(file_path, comparator, reverse):
    file = open(file_path, 'r')
    lines = file.read().split('\n')
    sorted_lines = sorted(lines, key=comparator, reverse=reverse)
    file.close()
    file = open(file_path, 'w')
    file.write('\n'.join(sorted_lines))
    file.close()


def sort(comparator, reverse):
    temp_files = []
    for file in sorted(os.listdir('temp'), key=lambda x: x):
        temp_files.append(open('temp/{}'.format(file)))
    with open('result.txt', 'w') as result_file:
        lines = {}
        i = 0
        for f in temp_files:
            lines[i] = f.readline()
            i += 1
        while lines != {}:
            write_item = None
            if reverse:
                write_item = max(lines.items(), key=lambda x: comparator(x[1]))
            else:
                write_item = min(lines.items(), key=lambda x: comparator(x[1]))
            if write_item[1].endswith('\n'):
                result_file.write(write_item[1])
            else:
                result_file.write(write_item[1] + '\n')
            lines[write_item[0]] = temp_files[write_item[0]].readline()
            if lines[write_item[0]] == '':
                lines.pop(write_item[0])

    for file in temp_files:
        file.close()


def make_temp_files(file_path, buffer_size, comparator, reverse):
    temp_file_counter = 0
    file_size = os.path.getsize(file_path)
    temp_file_size = file_size // (buffer_size * 4)
    with open(file_path) as file:
        temp_file_string = b''
        file_line = file.readline().encode()
        while file_line != b'':
            temp_file_string += file_line
            if len(temp_file_string) >= temp_file_size:
                with open('temp/{}'.format(temp_file_counter), 'w') as temp_file:
                    temp_file.write(temp_file_string.rstrip(b'\n').decode())
                sort_file('temp/{}'.format(temp_file_counter), comparator, reverse)
                temp_file_string = b''
                temp_file_counter += 1
            file_line = file.readline().encode()
        with open('temp/{}'.format(temp_file_counter), 'w') as temp_file:
            temp_file.write(temp_file_string.rstrip(b'\n').decode())
        sort_file('temp/{}'.format(temp_file_counter), comparator, reverse)
        temp_file_string = b''


def main():
    args = argparser.parse_args()

    file_path = args.file_path
    buffer_size = args.buffer_size
    comparator = args.comparator

    if file_path is None:
        file_path = input('Input file path: ')

    if buffer_size is None:
        buffer_size = int(input('Input buffer size: '))

    if comparator is None:
        comparator = input('Input comparator: ')

    if os.path.exists('temp'):
        shutil.rmtree('temp')
    os.mkdir('temp')

    make_temp_files(file_path, buffer_size, COMPARATORS[comparator], args.r)

    sort(COMPARATORS[comparator], args.r)


if __name__ == "__main__":
    main()
