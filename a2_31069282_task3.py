"""
Program provide graphic illustration of the disease spreading, visualising the curve.
X axis - The days of the simulation should
Y axis - contagious patient count
It import module from task2 to run the simulation.
Arguments for the simulation asked from user input.

The results of the simulation mostly match the predictions. All 3 parameters:
days, meeting probability and patient_zero_health have direct impact on total results, and due to probability results are
different each time simulation is running for the specific parameters (with low meeting chance, curve are often
flattened, but sometimes it grows slowly). Patient zero health has impact on viral load, he or she produce. Mildly
sick Patient produce a larger viral load than a person whose health has worsened. And number of days is important for
sleep, when Patient is recover HP.

Author - Pavel Zemnukhov
Date the script was created - 01/06/2020
Date the last edit was made - 08/06/2020
"""

import matplotlib.pyplot as plt   # import of matplotlib library
from a2_31069282_task2 import *   # import module from task 2



def visual_curve(days, meeting_probability, patient_zero_health):
    """
        Function to draw the curve
        It call run_simulation() function from task2 to run the simulation and based on the results, visualise the curve
        :param: days, meeting_probability, patient_zero_health
       """
    simulation = run_simulation(days, meeting_probability, patient_zero_health) # running of simulation

    y = simulation  # assign y axis
    x = []          # defining a list for x axis
    count = 0
    for i in simulation:
        count += 1
        x.append(count)     # assigning x axis

    plt.plot(x,y)           # draw a graph
    plt.xlabel("Days")      # label x axis
    plt.ylabel("Count")     # label y axis
    plt.show()              # show graph


if __name__ == '__main__':      #main function to test the program and ask user for input

    days = int(input("Please enter number of days "))                          # ask user for days of simulation
    meeting_probability = float(input("Please enter meeting probability "))    # ask user for meeting_probability
    patient_zero_health = int(input("Please enter health of Patient Zero "))   # ask user for health of patient zero

    visual_curve(days, meeting_probability, patient_zero_health)   #call visual_curve to draw a graph







# do not add code here (outside the main block).
