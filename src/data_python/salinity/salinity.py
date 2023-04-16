import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

station_3 = "Core6.txt"
station_4 = "Core7.txt"
station_5 = "Core8.txt"
station_6 = "Core9.txt"


def salinity_profile(path, station_num):
    length = 10
    file = pd.read_csv(str(path), delimiter="	")
    sal = file["Salinity [g/kg]"]
    start_of_slices = file["Start depth rate from top [cm]"]
    end_of_slices = file["End depth rate from top [cm]"]

    plt.title(f"Salinity profile station {str(station_num)}")
    for i in range(len(sal)):
        frac = (end_of_slices[i] - start_of_slices[i]) * 0.03
        plt.plot(np.linspace(sal[i] - frac, sal[i] + frac, length), 10 * [start_of_slices[i]], 'k', linewidth=1)
        plt.plot(np.linspace(sal[i] - frac, sal[i] + frac, length), 10 * [end_of_slices[i]], 'k', linewidth=1)
        plt.plot(length * [sal[i]], np.linspace(end_of_slices[i], start_of_slices[i], length), 'k')

    plt.plot(length * [sal[0]], np.linspace(end_of_slices[0], start_of_slices[0], length), 'r', label="slush layer")
    #plt.plot(length * [sal[1]], np.linspace(end_of_slices[1], start_of_slices[1], length), 'r')
    if station_num == 6:
        frac_19 = (end_of_slices[19] - start_of_slices[19]) * 0.03

        plt.plot(length * [sal[19]], np.linspace(end_of_slices[19], start_of_slices[19], length), color="orange",
                 label="alge layer")
        plt.plot(np.linspace(sal[19] - frac_19, sal[19] + frac_19, length), 10 * [start_of_slices[19]], color="orange",
                 linewidth=1)
        plt.plot(np.linspace(sal[19] - frac_19, sal[19] + frac_19, length), 10 * [end_of_slices[19]], color="orange",
                 linewidth=1)
    frac_0 = (end_of_slices[0] - start_of_slices[0]) * 0.03
    frac_1 = (end_of_slices[1] - start_of_slices[1]) * 0.03
    plt.plot(np.linspace(sal[0] - frac_0, sal[0] + frac_0, length), 10 * [start_of_slices[0]], 'r', linewidth=1)
    plt.plot(np.linspace(sal[0] - frac_0, sal[0] + frac_0, length), 10 * [end_of_slices[0]], 'r', linewidth=1)
    plt.plot(np.linspace(sal[1] - frac_1, sal[1] + frac_1, length), 10 * [start_of_slices[1]], 'r', linewidth=1)
    plt.plot(np.linspace(sal[1] - frac_1, sal[1] + frac_1, length), 10 * [end_of_slices[1]], 'r', linewidth=1)

    plt.grid()
    plt.xlabel("salinity [g/kg]")
    plt.ylabel("distance from top of ice [cm]")
    plt.savefig("station" + str(station_num))
    plt.show()


#salinity_profile(station_3, 3)
#salinity_profile(station_4, 4)
#salinity_profile(station_5, 5)
salinity_profile(station_6, 6)
