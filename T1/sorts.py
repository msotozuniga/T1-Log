import commons as comm
import access


def binary_search(P, T, p_len, t_len):
    IO_count = 0
    result = []
    for i in range(p_len):
        top = t_len - 1
        bot = 0
        p = access.read_line(P, i)
        t = 0
        while bot < top:
            mid = int((top + bot) / 2)
            t = access.read_line(T, mid)
            IO_count += 1
            if t >= p:
                top = mid
            else:
                bot = mid + 1
        t = access.read_line(T, top)
        IO_count += 2
        if p == t:
            result.append(p)
    return result, IO_count


def linear_search(P, T, t_len):
    IO_count = 0
    result = []
    for i in range(int(t_len / comm.B)):
        block = access.read_block(T, i)
        IO_count += 1

        for j in range(len(block)):
            for k in range(len(P)):
                if block[j] == P[k]:
                    result.append(P[k])
    return result, IO_count


def index_search(P, T, t_len):
    IO_count = 0
    result = []
    S = []
    for i in range(t_len / comm.B):
        S[i] = access.read_line(T, i * comm.B)
        IO_count += 1
    for i in range(len(P)):
        top = len(S) - 1
        bot = 0
        mid = 0
        while bot < top:
            mid = (top + bot) / 2
            if S[mid] >= P[i]:
                top = mid
            else:
                bot = mid + 1
        block = access.read_block(T, mid * comm.B)
        IO_count += 1
        for j in range(len(block)):
            if block[j] == P[i]:
                result.append(P[i])
    return result, IO_count
