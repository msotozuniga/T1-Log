
import commons as comm


def read_line(file, pos):
    f = open(file, 'r')
    f.seek(pos * 10, 0)
    buffer = f.read(10)
    f.close()
    return buffer


def read_block(file, number):
    f = open(file, 'r')
    line = number*comm.B
    f.seek(line, 0)
    buffer = str(f.read(comm.B))
    buffer = list(filter(None, buffer.split('\n')))
    f.close()
    return buffer


def read_file(file):
    f = open(file, 'r')
    buffer = str(f.read())
    buffer = list(filter(None, buffer.split('\n')))
    f.close()
    return buffer


def dump_data(data):
    f = open("output.txt", 'a')
    number_blocks = len(data) // comm.B
    for i in range(number_blocks):
        f.write(''.join(data[i * comm.B:(i + 1) * comm.B]))
    return number_blocks



