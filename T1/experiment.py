import time as tm
import generator as gn
import sorts as srt
import access
import numpy as np


def test_case(p, t):
    data = []
    for i in range(len(p)):
        run = perform_experiment(p[i], t, 2)
        data.append(run)
    return data


def perform_experiment(P_size, T_size, k):
    binary_time = []
    binary_comp = []
    linear_time = []
    linear_comp = []
    index_time = []
    index_comp = []
    for i in range(k):
        gn.generate(P_size, T_size)
        print("Se generaron datos")
        now = tm.time()
        result, io = srt.binary_search("P.txt", "T.txt", P_size, T_size)
        binary_time.append(tm.time() - now)
        binary_comp.append(io)
        print("Se terminó búsqueda binaria")

        P = access.read_file("P.txt")

        now = tm.time()
        result, io = srt.linear_search(P, "T.txt", T_size)
        linear_time.append(tm.time() - now)
        linear_comp.append(io)

        print("Se terminó búsqueda lineal")

        now = tm.time()
        result, io = srt.index_search(P, "T.txt", T_size)
        index_time.append(tm.time() - now)
        index_comp.append(io)
        print("Se terminó búsqueda indexada")
    return [np.mean(binary_time), np.var(binary_time), np.mean(binary_comp), np.var(binary_comp),
            np.mean(linear_time), np.var(linear_time), np.mean(linear_comp), np.var(linear_comp),
            np.mean(index_time), np.var(index_time), np.mean(index_comp), np.var(index_comp)]


if __name__ == '__main__':
    P_case = [50, 70, 10 ** 2, 250, 500, 10 ** 3, (10 ** 4) / 2, 10 ** 4, (10 ** 5) / 2, 10 ** 5]
    T_case = 10 ** 6

    results = test_case(P_case, T_case)
    case = open("data_a.txt", 'w')
    for each in results:
        data = ''
        for numbers in each:
            data = data + str(numbers) + " "
        data = data + "\n"
        case.write(data)
