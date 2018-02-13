import csv

def arrival_times(filename):

    arrival_time_list = []
    sum = 0
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            sum = sum + float(row[0])
            arrival_time_list.append(sum)
    csvfile.close()

    return arrival_time_list

def service_times(filename, column=1):
    if column != 1 && column != 2:
        except ValueError:
            print("This assignment only has service time data in columns 1 and 2")

    service_time_list = []

    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            service_time_list.append(row[column])
    csvfile.close()

    return service_time_list
