import time as tm
import generator as gn
import sorts as srt
import numpy as np
import matplotlib.pyplot as plt



def perform_experiments(k):
    times = []
    comps = []
    for i in range(k):
        gn.generate(10 ** 4, 10 ** 6)
        start_time = tm.time()
        data, comp = srt.binary_search("P.txt", "T.txt", 10 ** 4, 10 ** 6)
        time = tm.time() - start_time
        comps.append(comp)
        times.append(time)
    return np.mean(times), np.mean(comps)


def perform_meta_experiments(n, k):
    times = []
    times_std = []
    comps = []
    comps_std = []
    for k in range(2, k):
        print("Iniciando repeticiones hasta " + str(k))
        time_means = []
        comp_means = []
        for i in range(n):
            t, c = perform_experiments(k)
            time_means.append(t)
            comp_means.append(c)
        times.append(np.mean(time_means))
        comps.append(np.mean(comp_means))
        times_std.append(np.var(time_means))
        comps_std.append(np.var(comp_means))
    return times, times_std, comps, comps_std


if __name__ == '__main__':
    means_time, std_time, means_comp, std_comp = perform_meta_experiments(5, 26)

    print("Experimento finalizado")

    x = np.arange(2, 26)

    plot_tm = plt.subplot(1,2,1)
    plot_tm.set_xlabel("Cantidad de repeticiones")
    plot_tm.set_ylabel("Tiempo en segundos")
    plot_tm.set_title("Promedio de tiempos")

    plt.errorbar(x, means_time, yerr=std_time)

    plot_cm = plt.subplot(1,2,2)
    plot_cm.set_xlabel("Cantidad de repeticiones")
    plot_cm.set_ylabel("Numero de comparaciones")
    plot_cm.set_title("Promedio de comparaciones")
    plt.errorbar(x, means_comp, yerr=std_comp)
    plt.savefig("exp-k.png")
    plt.show()

