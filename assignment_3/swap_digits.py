#/usr/bin/python3

def swap_digits(filename):
    with open(filename, 'r+') as f:
        swapped_file = open("swapped.txt", 'w')
        for line in f:
            read_data = line
            swapped = read_data[:2] + read_data[3] + read_data[2]

            swapped_file.write(swapped + '\n')
            #rint(read_data)
            #print(swapped)

    f.close()

if __name__ == "__main__":
    # execute only if run as a script
    swap_digits("7_8_data")
