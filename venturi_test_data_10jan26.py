
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import the local files
suit_avg_path = "/Users/tim/Desktop/Venturi/Coding/Suit_Test_10126/Suits_avg_corrected.csv" #Change to where you have the csv file

#Only use the relevant columns, here's also temp, density etc included for further analysis
suitavg = pd.read_csv(suit_avg_path,usecols=(3,9,11,16,18,19,20,21,22)) 

#Indices to manage the rows in suitavg
indices = np.array([0,16,28,40,52]) # 0-15 is Venturi, 15-27 GB, 27-39 Nopinz, 39-51 Rapha

#list of all the yaw angles indices for each set of suit
yaws = np.array([0,5,10,15]) 

speeds_venturi = np.array([25,30,35,45]) # List of all the speeds for Venturi
speeds_rest = np.array([30,35,45]) # List of all the speeds for the rest of the suits
speeds_list_list = [speeds_venturi,speeds_rest] #List to differentiate the difference in number of speeds tested at

suits = {'suits': ['Venturi','GB','Nopinz','Rapha']} #Dictionary that could've just been a list


def makedata(df):

    indices = np.array([0,16,28,40,52]) # 0-15 is Venturi, 15-27 GB, 27-39 Nopinz, 39-51 Rapha
    suits = {'suits': ['Venturi','GB','Nopinz','Rapha']}
    data = {}

    #indices for Venturi suit
    yaw_0_V= np.array([0,4,8,12])
    yaw_5_V= np.array([0,4,8,12])+1
    yaw_10_V = np.array([0,4,8,12])+2
    yaw_15_V = np.array([0,4,8,12])+3
    yaws_index_V = [yaw_0_V,yaw_5_V,yaw_10_V,yaw_15_V]

    #Indices for Rest of the suits
    yaw_0 = np.array([0,4,8])
    yaw_5 = np.array([0,4,8])+1
    yaw_10 = np.array([0,4,8])+2
    yaw_15 = np.array([0,4,8])+3

    yaws_index = [yaw_0,yaw_5,yaw_10,yaw_15]

    kph25 = np.array([0,1,2,3])
    kph30 = np.array([0,1,2,3])
    kph35 = np.array([4,5,6,7])
    kph45 = np.array([8,9,10,11])

    kph_index_V = [kph25,kph30+4,kph35+4,kph45+4]
    kph_index = [kph30,kph35,kph45]




    for i in range(4):
            if i == 0:
                speeds = speeds_list_list[0] # For Venturi
                index_yaw = yaws_index_V
                index_speed = kph_index_V
                speed_range = 4
            else:
                speeds = speeds_list_list[1] # For the rest of the suits
                index_yaw = yaws_index
                index_speed = kph_index
                speed_range = 3
                
            for j in range(4):
                cda = np.array([suitavg['cda short'][indices[i]:indices[i+1]]]) # takes the Cda for each suit, the whole list of 16 or 12 values

                #Stores all the velocities for each yaw angle
                data['%s_CdA_yaw%s'%(suits['suits'][i],yaws[j])] = cda[0][index_yaw[j]]
                
            
                
            for n in range(speed_range):
                cda = np.array([suitavg['cda short'][indices[i]:indices[i+1]]]) # takes the Cda for each suit, the whole list of 16 or 12 values

                #Store all the yaw angles for each velocity
                data['%s_CdA_%skmh'%(suits['suits'][i],speeds[n])] = cda[0][index_speed[n]]
    return data
    



data = makedata(suitavg)

yaw_symbols = ['x','+','d','X']

plt.figure(figsize=(12,9))
for i in range(len(yaws)):
    plt.plot(speeds_venturi[1:],data['Venturi_CdA_yaw%s'%(yaws[i])][1:],'-%s'%(yaw_symbols[i]),
             markersize = 8,color=('black'),label=("Venturi Rho Suit @ %s° Yaw"%(yaws[i])))
    
    plt.plot(speeds_rest,data['GB_CdA_yaw%s'%(yaws[i])],'-.%s'%(yaw_symbols[i]),
             markersize = 8,color=('cyan'),label=("GB @ %s° Yaw"%(yaws[i])))
    
    plt.plot(speeds_rest,data['Nopinz_CdA_yaw%s'%(yaws[i])],'--%s'%(yaw_symbols[i]),
             markersize = 8,color=('orangered'),label=("Nopinz @ %s° Yaw"%(yaws[i])))
    
    plt.plot(speeds_rest,data['Rapha_CdA_yaw%s'%(yaws[i])],':%s'%(yaw_symbols[i]),
             markersize = 8,color=('lime'),label=("Rapha @ %s° Yaw"%(yaws[i])))

plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
          ncol=4, fancybox=True, shadow=True)

plt.grid()
plt.xlabel("Speed (km/h)")
plt.ylabel("CdA")
plt.show()

#Plot another one

symbols = ['o','X','^']

speed_color_rest = ['cyan','darkcyan','orangered']
suit_colour = ['black','cyan','orangered','lime']

plt.figure(figsize=(12,9))
for i in range(4):
    if i == 0:
        speeds = speeds_list_list[0][1:] # For Venturi
        speed_range = 3
        speed_color = speed_color_rest
    else:
        speeds = speeds_list_list[1] # For the rest of the suits
        speed_range = 3
        speed_color = speed_color_rest
        
    for n in range(speed_range):  #Ranging through the speeds      
        if (i in[0,1,2,3] and n==3):
            continue
        else:
            plt.plot(yaws,data['%s_CdA_%skmh'%(suits['suits'][i],speeds[n])],'-%s'%(symbols[n]),
                     markersize = 9,color=(suit_colour[i]),label=("%s @ %s Kph"%(suits['suits'][i],speeds[n])))


plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
          ncol=4, fancybox=True, shadow=True)

plt.grid()
plt.xlabel("Yaw [°]")
plt.ylabel("CdA")
plt.show()

# %%
