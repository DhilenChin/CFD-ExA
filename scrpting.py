import pandas as pd
import os
print("inset the directory to your .csv file here:")
csv = "./testinputs.csv"

df = pd.read_csv(csv)

for i in range(1):
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
    os.rename("delta-tblock.dat", name)

    os.system('./tblock < ' + name +' > store.txt')
