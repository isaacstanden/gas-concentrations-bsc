'''

Isaac Standen
Supervisor: Dr. Rebecca Fisher

'''

import numpy as np
import matplotlib.pyplot as plt


#2009-2021 monthly averages

#adding lines to change of callibration dates
plt.axvline(x=2016.708,color="#525252",linestyle="dotted",linewidth="0.75")
plt.axvline(x=2011.042,color="#525252",linestyle="dotted",linewidth="0.75")
plt.axvline(x=2009.125,color="#525252",linestyle="dotted",linewidth="0.75")

#imports and plots monthly data from dat file
plt.plot(*np.loadtxt("monthly_MaceHead.dat",unpack=True),linewidth=1.0,
         marker=',',color='#6CBEED',label="Mace Head")
plt.plot(*np.loadtxt("monthly_Egham.dat",unpack=True),linewidth=1.0,
            marker=',',color='#A23B72',label="Egham")

#sets x axis ticks to values specified
plt.xlim(left=2008,right=2023)
#plt.ylim(top=580)
plt.xticks(ticks=(2009,2011,2013,2015,2017,2019,2021))

#creates title and axes labels for plot & the legend
plt.title("Monthly averages of atmospheric hydrogen \n in Egham, England vs in Mace Head, Ireland")
plt.xlabel("Date of measurement")
plt.ylabel("$H_2$ concentration (ppb)")
plt.legend(loc="lower right",fontsize=7)

#annotating change of callibration lines
plt.annotate("Change of callibration \n in Egham",xy=(2016.708,490),
             xycoords="data",xytext=(+10,+15), textcoords="offset points",
             fontsize="7",color="#525252")
plt.arrow(2017.2,495,-6.05,-10,color="#525252",linewidth="0.2")
plt.arrow(2017.2,495,-0.41,-5,color="#525252",linewidth="0.2")
plt.arrow(2017.2,495,-7.95,-7,color="#525252",linewidth="0.2")

#outputs graph and saves as png file
plt.savefig("H2_MHD_vs_EGH.png",dpi=300,edgecolor="#A80874")
plt.show()

