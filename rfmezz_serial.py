import os
import time


# input the serial in the text from GUI to a file then use this file to grab the last inputted info
# step(s) 11 of functional test
class RfSerialFile:
    def write_to_file(serial_number):
        # file path to save rf serial numbers in
        my_path = "C:\serial_file_prac"
        file_name = my_path + "/" + "serial_file.txt"
        # open the file and write to the file the inputted rf serial number
        with open(file_name, "a+") as x:
            x.write(serial_number)
            x.write('\n')
            x.close()

    def read_file(self):
        # file path to rf serial numbers
        my_path = "C:\serial_file_prac"
        file_name = my_path + "/" + "serial_file.txt"
        # read the file and get the last inputted rf serial number
        with open(file_name, "r") as y:
            first_line = y.readline()
            for last_line in y:
                pass
        # last_line holds the last inputted rf serial number
        return last_line
        y.close()


if __name__ == "__main__":
    file = RfSerialFile()
    file.write_to_file()
    file.read_file()
