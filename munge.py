# Place code below to do the munging part of this assignment.
import os

"""
Accepts a temperature anomaly in 0.01 degrees Celsius as a string.
Converts anomaly to Farenheit.
Returns the result formatted to one decimal place as a string. 
"""
def convert_temperature(temp):
    return format(float(temp) / 100 * (9/5), ".1f")

"""
Accepts the temperature data from a specific year as a list.
Checks the list for missing values ("***").
Replaces any missing values with the annual average anomaly.
Returns the handled list.
"""
def handle_missing_values(temp_data):
    for i in range(1, len(temp_data)):
        if temp_data[i][0] == "*":
            total = 0
            count = 0
            for j in range(1, 13):
                if temp_data[j][0] != "*":
                    total += float(temp_data[j])
                    count += 1
            if count > 0:
                mean = round(total / count)
                temp_data[i] = str(mean)
            else:
                # Set to zero if all monthly values are missing
                temp_data[i] = "0" 
    return temp_data

def main():
    input_filepath = os.path.join("data", "GLB.Ts+dSST.txt")
    output_filepath = os.path.join("data", "clean_data.csv")

    input_file = open(input_filepath, "r", encoding="utf_8")
    output_file = open(output_filepath, 'w', encoding="utf_8")

    all_lines = input_file.readlines()
    first_heading_found = False

    for line in all_lines:
        if line[:4] == "Year":
            # Only retain the first line of column headings
            if not first_heading_found:
                heading = line.split()[:-1]
                # Standardize comma "," as the value separator
                row = ",".join(heading)
                output_file.write(row + "\n") 
                first_heading_found = True
        elif line[:4].isdigit():
            temp_data = line.split()[:-1]
            temp_data = handle_missing_values(temp_data)
            temp_data[1:] = map(convert_temperature, temp_data[1:])
            row = ",".join(temp_data)
            output_file.write(row + "\n")

    input_file.close()
    output_file.close()

if __name__ == "__main__":
    main()
