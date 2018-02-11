import csv
import numpy as np
import matplotlib.pyplot as plt

def queue_hist(filename):
    count = 0
    interarrival_sum = 0
    service1_sum = 0
    service2_sum = 0

    interarrival_list = []
    service1_list = []
    service2_list = []
    bin_count = 0

    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row != 0:
                interarrival_sum = interarrival_sum + float(row[0])
                service1_sum = service1_sum + float(row[1])
                service2_sum = service2_sum + float(row[2])
                count = count + 1
                interarrival_list.append(float(row[0]))
                service1_list.append(float(row[1]))
                service2_list.append(float(row[2]))
        csvfile.close()

        average_interarrival = interarrival_sum / count
        average_service1 = service1_sum / count
        average_service2 = service2_sum / count
        interarrival_rate = 1 / average_interarrival
        service1_rate = 1 / average_service1
        service2_rate = 1 / average_service2
    bin_count = int(np.floor(1.66*(count**(1/3))))

    inter_hist = np.histogram(interarrival_list, bins=bin_count)
    service1_hist = np.histogram(service1_list, bins=bin_count)
    service2_hist = np.histogram(service2_list, bins=bin_count)

    plt.hist(interarrival_list, bins=bin_count)
    plt.title("Interarrival Histogram")
    plt.savefig("interarrival.jpg")

    plt.hist(service1_hist, bins=bin_count)
    plt.title("Service Time 1 Histogram")
    plt.savefig("service1.jpg")

    plt.hist(service2_hist, bins=bin_count)
    plt.title("Service Time 2 Histogram")
    plt.savefig("service2.jpg")
