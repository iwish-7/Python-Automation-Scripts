keyword = "ERROR"

log_file = input("Enter the path of the log file: ")

with open(log_file, 'r') as file:
    for line_no, line in enumerate(file, 1):

        if keyword in line:
            print(f"An {keyword} was encountered in line {line_no}. The error is: {line}")
