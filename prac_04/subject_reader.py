"""
CP1404/CP5632 Practical
Data file -> lists program
"""
"""
function main()
    get datas
    for data in datas:
        summarize(data)
        
function get_data()
    datas = []
    open txt for reading as input_file
    for line in input_file:
        parts = line.split(',')
        datas.append(parts)
    return datas
    
function summarize(data):
    print f-string data
"""

FILENAME = "subject_data.txt"


def main():
    datas = get_data()
    # print(data)
    for data in datas:
        summarize(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        datas.append(parts)

    input_file.close()
    return datas


def summarize(parts):
    print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")


main()
