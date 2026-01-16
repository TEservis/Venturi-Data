import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import the local files
suit_avg_path = "Suits_avg_corrected.csv" #Change to where you have the csv file

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

fig1,ax1 = plt.subplots(figsize=(9,7))

for i in range(len(yaws)):
    ax1.plot(speeds_venturi[1:],data['Venturi_CdA_yaw%s'%(yaws[i])][1:],'-%s'%(yaw_symbols[i]),markersize = 8,color=('black'),label=("Venturi Rho Suit @ %s° Yaw"%(yaws[i])))
    ax1.plot(speeds_rest,data['GB_CdA_yaw%s'%(yaws[i])],'-.%s'%(yaw_symbols[i]),markersize = 8,color=('cyan'),label=("GB @ %s° Yaw"%(yaws[i])))
    ax1.plot(speeds_rest,data['Nopinz_CdA_yaw%s'%(yaws[i])],'--%s'%(yaw_symbols[i]),markersize = 8,color=('orangered'),label=("Nopinz @ %s° Yaw"%(yaws[i])))
    ax1.plot(speeds_rest,data['Rapha_CdA_yaw%s'%(yaws[i])],':%s'%(yaw_symbols[i]),markersize = 8,color=('lime'),label=("Rapha @ %s° Yaw"%(yaws[i])))

ax1.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
          ncol=4, fancybox=True, shadow=True)

ax1.grid()
ax1.set_xlabel("Speed (km/h)")
ax1.set_ylabel("CdA")

#Plot another one

symbols = ['o','X','^']

speed_color_rest = ['cyan','darkcyan','orangered']
suit_colour = ['black','cyan','orangered','lime']

fig2,ax2 = plt.subplots(figsize=(9,7))
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
            ax2.plot(yaws,data['%s_CdA_%skmh'%(suits['suits'][i],speeds[n])],'-%s'%(symbols[n]),markersize = 9,color=(suit_colour[i]),
                     label=("%s @ %s Kph"%(suits['suits'][i],speeds[n])))


ax2.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
          ncol=4, fancybox=True, shadow=True)

ax2.grid()
ax2.set_xlabel("Yaw [°]")
ax2.set_ylabel("CdA")




#Plot with the four yaw angles in one plot
plt.style.use('dark_background')

suit_colour = ['cyan','yellow','orangered','lime']
fig_yaw, ax_yaw = plt.subplots(nrows=2,ncols=2,figsize=(16,12))
for rows in range(2):
    for cols in range(2):
        if rows==0 and cols==0:
            y=0
        if rows==0 and cols==1:
            y=1
        if rows==1 and cols==0:
            y=2
        if rows==1 and cols==1:
            y=3
        
        
        for i in range(4):
                
                if i ==0: #This one slices the 4 element big data array for the venturi suits compared to the 3 speeds for the rest
                    ax_yaw[rows,cols].plot(speeds_rest,data['%s_CdA_yaw%s'%(suits["suits"][i],yaws[y])][1:],'-%s'%(yaw_symbols[i]),markersize = 8,
                                color=(suit_colour[i]),label=("%s @ %s° Yaw"%(suits["suits"][i],yaws[y]))) 
                    
                else:    
                    ax_yaw[rows,cols].plot(speeds_rest,data['%s_CdA_yaw%s'%(suits["suits"][i],yaws[y])],'-%s'%(yaw_symbols[i]),markersize = 8,
                                color=(suit_colour[i]),label=("%s @ %s° Yaw"%(suits["suits"][i],yaws[y])))
                    
                    
                ax_yaw[rows,cols].legend()
                ax_yaw[rows,cols].set_xlabel('Velocity [km/h]')
                ax_yaw[rows,cols].set_ylabel('CdA')
                ax_yaw[rows,cols].grid('True',color=('gray'))
                ax_yaw[rows,cols].set_title('%s° yaw'%(yaws[y]))
                
                
                
### BAR CHART

suits_list = np.array(['Venturi','GB','Nopinz','Rapha'])
colors = np.array(['turquoise','yellow','tomato'])

plt.style.use('fivethirtyeight')

x = np.arange(len(suits_list[1:]))          # one base x position per suit
nspeeds = 3
width = 0.25
offsets = np.linspace(-width, width, nspeeds)

figg, axx = plt.subplots(nrows = 2, ncols = 2,layout="constrained",figsize = (12,8))

rows = np.array([0,0,1,1]) # to index the plots
cols = np.array([0,1,0,1]) # to index the plots

for y in range(len(yaws)):
    
    for i in range(len(suits_list[1:])): #Excluding venturi suit
        for s in range(len(speeds_rest)):
        
            
            cda_other = data['%s_CdA_yaw%s' %(suits_list[i+1],yaws[y])][s]
            
            cda_venturi = data['Venturi_CdA_yaw%s' %(yaws[y])][1:][s]
            
            cda_diff = cda_other - cda_venturi
            
            watt_diff = round(0.5*1.225*cda_diff*(speeds_rest[s]/3.6)**3,2)
            
            if i==2:
                rect = axx[rows[y],cols[y]].bar(x[i]+offsets[s],watt_diff,width=width,color=colors[s],label='%s kp/h'%(speeds_rest[s]),zorder=3)
            else:
                rect = axx[rows[y],cols[y]].bar(x[i]+offsets[s],watt_diff,width=width,color=colors[s],zorder=3)
            
            
            axx[rows[y],cols[y]].bar_label(rect, padding=0,color='black')
            
            
            #print(watt_diff)
    axx[rows[y],cols[y]].set_ylabel('Watts difference from RHO suit',color='black',fontsize=10)
    axx[rows[y],cols[y]].grid(zorder=0)
    axx[rows[y], cols[y]].tick_params(colors='black',which='both')
    axx[rows[y], cols[y]].set_xticks(x) and axx[rows[y], cols[y]].set_xticklabels(suits_list[1:],color='black', rotation=0, fontsize=10)
    #axx[rows[y], cols[y]].legend(loc='upper left', ncols=3,labelcolor='black')
    axx[rows[y], cols[y]].set_ylim(-10,18)
    axx[rows[y], cols[y]].set_title('%s° Yaw'%(yaws[y]),color='black', fontsize=12)
figg.legend(['30 kp/h','35 kp/h','45 kp/h'],ncols=3,labelcolor='black',bbox_to_anchor=(0., 1.02, 1., .102),loc=3)
    
            
