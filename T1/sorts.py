import commons as comm
import sys
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
            mid = (top + bot) // 2
            t = access.read_line(T, mid)
            IO_count += 1
            if t >= p:
                top = mid
            else:
                bot = mid + 1
        t = access.read_line(T, top)
        IO_count += 2
        if p == t:
            if len(result) + 1 > comm.M:
                IO_count += access.dump_data(result)
                result = []
            result.append(p)
    return result, IO_count


def linear_search(P, T, t_len):
    IO_count = 0
    result = []
    for i in range(t_len // comm.B_numbers):
        block = access.read_block(T, i)
        IO_count += 1

        for num in block:
            if num in P:
                if len(result) + len(P) + comm.B + 1 > comm.M:
                    IO_count += access.dump_data(result)
                    result = []
                result.append(num)
    return result, IO_count

def linear_binary_search(P,T,t_len):
    IO_count = 0
    result = []
    for i in range(t_len // comm.B_numbers):
        block = access.read_block(T, i)
        IO_count += 1
        for num in P:
            top = len(block)
            bot = 0
            while bot < top:
                mid = (top + bot) // 2
                t = block[mid]
                if t >= num:
                    top = mid
                else:
                    bot = mid + 1
            t = block[bot]
            if num == t:
                if len(result) + len(block) +1 > comm.M:
                    IO_count += access.dump_data(result)
                    result = []
                result.append(num)
    return result, IO_count

def linear_merge_search(P,T,t_len):
    P.sort()
    IO_count = 0
    result = []
    for i in range(t_len // comm.B_numbers):
        block = access.read_block(T, i)
        IO_count += 1
        p_i=0
        b_i=0
        while p_i<len(P) or b_i<len(block):
            if P[p_i]==block[b_i]:
                if len(result) + len(block) +1 > comm.M:
                    IO_count += access.dump_data(result)
                    result = []
                result.append(P[p_i])
            elif P[p_i]<block[b_i]:
                p_i+=1
            else:
                b_i+=1
    return result, IO_count



def index_search(P, T, t_len):
    IO_count = 0
    result = []
    S = []
    rango = range(t_len // comm.B_numbers)
    for i in rango:
        S.append(access.read_line(T, i * comm.B_numbers))
        IO_count += 1
    for i in range(len(P)):
        top = len(S) - 1
        bot = 0
        mid = 0
        while bot < top:
            mid = (top + bot + 1) // 2
            if S[mid] > P[i]:
                top = mid - 1
            else:
                bot = mid
        block = access.read_block(T, bot)
        IO_count += 1
        if P[i] in block:
            if len(result) + len(P) + comm.B + 1 + len(S) > comm.M:
                IO_count += access.dump_data(result)
                result = []
            result.append(P[i])
    return result, IO_count
