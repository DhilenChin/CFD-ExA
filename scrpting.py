import pandas as pd
import os
csv = input("inset the directory to your .csv file here:")
df = pd.read_csv(csv)

for i in df.index:
    f = open('temp.txt', 'w')
    f.write(str(df['Mach number'][i]) + '\n')
    f.write(str(df['Reynolds number'][i]) + '\n')
    f.write(str(df['Angle of Attack'][i]) + '\n')
    f.write(str(df['Sweep angle'][i]) + '\n')
    f.write(str(df['Grid scale'][i]) + '\n')
    f.write(str(df['Wing to Tunnel Fraction'][i]) + '\n')
    f.write(str(df['Tun Height to Width Ratio'][i]) + '\n')
    f.write(str(df['Step scale'][i]) + '\n')
    f.write(str(df['Smoothing'][i]) + '\n')
    f.write(str(df['Step number'][i]) + '\n')
    f.write(str(df['Flow Type'][i]))
    f.close()
    os.system("./deltagen < temp.txt")
    name = 'tblock' + '-' + str(df['Mach number'][i]) + '-' +  str(df['Sweep angle'][i]) + '-' +  str(df['Angle of Attack'][i]) + '-' + str(df['Flow Type'][i])+'.dat'
    os.rename("./delta-tblock.dat", name)

    os.system('./tblock < ' + name+ ' > ' + name + '.txt')
    os.rename('flow1-1.vtu', name + 'flow1.vtu')
    os.rename('flow1-2.vtu', name + 'flow2.vtu')
    import csv

    filename_input = name

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
                     
                     
