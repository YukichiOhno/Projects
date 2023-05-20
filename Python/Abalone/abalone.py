def get_abalone_value(item):
    value = 1 + ((1 / 3) * (item[2] - 0.5)) + ((1 / 3) * (item[3] - 0.4)) + ((1 / 3) * (item[4] - 0.4))
    abaloneValue = value * item[5] * 0.5
    return abaloneValue


if __name__ == "__main__":
    import csv

    with open("CIS2334CSVdata.csv", "r") as csvfile:
        abalone_reader = csv.reader(csvfile, delimiter=",")
        next(abalone_reader)

        abalone_data = []
        for row in abalone_reader:
            abalone_data.append([int(row[0]),  # ID
                                 row[1],  # Gender
                                 float(row[2]),  # Length
                                 float(row[3]),  # Diameter
                                 float(row[4]),  # Height
                                 float(row[5]),  # Whole Weight
                                 float(row[6]),  # Shucked Weight
                                 float(row[7]),  # Viscera Weight
                                 float(row[8]),  # Shell Weight
                                 int(row[9]),  # Rings
                                 int(row[10]),  # Collector ID
                                 row[11].strip(),  # Collector First name
                                 row[12].strip(),  # Collector Last name
                                 row[13].strip(),  # Collector organization
                                 int(row[14]),  # Water ID
                                 row[15].strip(),  # Water Region
                                 float(row[16])  # Feb Temp
                                 # row[17] Category
                                 # int(row[18]) Economic Value
                                 ])

    # Placing each Abalones in their respective categories
    category1 = []
    category2 = []
    category3 = []

    for row in abalone_data:
        abalone_value = get_abalone_value(row)

        if (
                ((row[9] > 15) and (row[1] == "I")) or
                ((row[1] == "M") and (row[2] > 0.75)) or
                (((row[8] > 0.8) and (row[6] > 0.5)) or row[6] > 1.2)
        ):
            row.append("I")
            row.append(abalone_value * 1.5)
            category1.append(row)
        elif (
                ((row[8] < 0.4) and (row[6] < 0.4)) or
                (((row[9] > 15) and (row[1] == "M")) or ((row[9] > 18) and (row[1] == "F"))) or
                (row[2] < 0.36)
        ):
            row.append("II")
            row.append(abalone_value * 0.8)
            category2.append(row)
        else:
            row.append("III")
            row.append(abalone_value)
            category3.append(row)

    for row in abalone_data:
        print(row)
