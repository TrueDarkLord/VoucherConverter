import os
import yaml

global read_file
global write_file
global converted_list
converted_list = []
global failed_list
failed_list = []

def get_first_key(data):
    for i in data.keys():
        return i

def alter_file_2(read, write):
    global f_data

    with open(read, "r") as f1:
        try:
            f_data = list(yaml.safe_load_all(f1))
            f_data = f_data[0][get_first_key(f_data[0])][get_first_key(f_data[0][get_first_key(f_data[0])])]
        except:
            #print("Error reading ", read)
            failed_list.append(read.strip(read_file + "\\.yml"))
            return
    try:
        f2 = open(write, "w")
        yaml.dump(f_data,f2,sort_keys=False)
    except:
        #print("Error writing data to ", write)
        failed_list.append(read.strip(read_file + "\\.yml"))
        f2.close
        os.remove(write)
        return
    finally:
        f2.close()
    converted_list.append(read.strip(read_file + "\\.yml"))

def convert_all_files():
    for voucher in os.listdir(read_file):

        file1 = read_file + "\\" + voucher
        file2 = write_file + "\\" + voucher

        alter_file_2(file1, file2)

while True:
    read_file = input("Enter the file to read from: ").strip()
    if "." in read_file:
        continue
    if os.path.exists(read_file) and os.path.isdir(read_file):
        break

while True:
    write_file = input("Enter the file to write to: ").strip()
    if "." in write_file:
        continue
    if os.path.exists(write_file) and os.path.isdir(write_file):
        break
convert_all_files()
print("\n\nConverted: ", converted_list, "\n\n\nFailed loading: ", failed_list)