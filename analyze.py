# Place code below to do the analysis part of the assignment.
import os
import csv

def main():
    filepath = os.path.join("data", "clean_data.csv")
    file = open(filepath, "r")
    csv_reader = csv.DictReader(file)

    # Dictionary to store all monthly anomalies for each decade
    anomalies = {}
    months = list(next(csv_reader).keys())[1:13]
    last_year = 0

    for row in csv_reader:
        year = int(row["Year"])
        last_year = max(last_year, year)

        for m in months:
            temp = float(row[m])
            decade = (year // 10) * 10
            # Add temp to the corresponding decade
            if decade in anomalies:
                anomalies[decade].append(temp)
            else:
                anomalies[decade] = [temp]
    
    # Dictionary to store the average anomaly for each decade
    average_anomalies = {}
    for decade, anomaly_list in anomalies.items():
        average_anomaly = sum(anomaly_list) / len(anomaly_list)
        average_anomalies[decade] = average_anomaly
    
    print("The average temperature anomaly in degrees Farenheit for each decade since 1880 are as follows,")
    for decade, average_anomaly in average_anomalies.items():
        # For the latest decade:
        if decade == max(average_anomalies):
            print(f"{decade} to {last_year}: {format(average_anomaly, '.1f')}")
        else:
            print(f"{decade} to {decade + 9}: {format(average_anomaly, '.1f')}")

if __name__ == "__main__":
    main()
