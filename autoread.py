import csv

filename_input = "dummy_data_3"

with open(filename_input+".txt",mode="r") as rawfile:
    lines = rawfile.readlines()
    lines = [line.rstrip() for line in lines]

print(len(lines))

data_out = []
timestep = 0

data_row = [timestep]

for line in lines:
    if "PRESSURE LIFT" in line:
        splitline = line.split(" ")
        data_row.append(splitline[9])
        data_row.append(splitline[16])
        
    elif "VISCOUS LIFT" in line:
        splitline = line.split(" ")
        data_row.append(splitline[10])
        data_row.append(splitline[17])
        
    elif "INLET DYNAMIC HEAD" in line:
        splitline = line.split(" ")
        data_row.append(splitline[9])
        
    elif "TOTAL LIFT COEFF." in line:
        splitline = line.split(" ")
        data_row.append(splitline[7])
        
    elif "TOTAL DRAG COEFF." in line:
        splitline = line.split(" ")
        data_row.append(splitline[8])

        data_out.append(data_row)
        timestep += 1

        data_row = [timestep]

print(len(data_out))
print(data_out[-1])

    

fieldnames = ["Timestep","Pressure lift", "Pressure drag", "Viscous lift", "Viscous drag", "Dynamic pressure", "Lift coefficient", "Drag coefficient"]

with open(filename_input+".csv" , "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    for data_row in data_out:
        writer.writerow({fieldnames[0]: data_row[0],
                         fieldnames[1]: data_row[1],
                         fieldnames[2]: data_row[2],
                         fieldnames[3]: data_row[3],
                         fieldnames[4]: data_row[4],
                         fieldnames[5]: data_row[5],
                         fieldnames[6]: data_row[6],
                         fieldnames[7]: data_row[7]})
                     
                     
