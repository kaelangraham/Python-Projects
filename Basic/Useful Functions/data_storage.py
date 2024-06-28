import os
DIR = os.path.dirname(__file__)

# finds file location
data_path = "Data Storage/data.txt"
path = os.path.join(DIR, data_path)

try:
    # read data
    data=open(path)
    data_read = data.read()
    print(data_read)
    data.close()
except FileNotFoundError:
    print('File not found')

# write data
new_data = 'new_data'
data=open(path, "w")
data.write(new_data)
data.close()
