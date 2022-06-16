"""
Program handles simulation of the disease spreading between the people(Patients here) over the period of specified
days. It returns the list of contagious Patients at the specific day of simulation.
Program creates class Patient inherited from class Person with additional methods and attributes
Function load_people() is responsible to read a txt file and to create new Patient objects and connections
with friends. It returns a list of Patient objects.
Function run_simulation responsible for the simulation.

Author - Pavel Zemnukhov

Date the script was created - 30/05/2020
Date the last edit was made - 08/06/2020
"""
import random       #import of random library
from a2_31069282_task1 import Person   #import of Person class from module a2_31069282_task1

initial_health = 75        # initial health of Patient
days = 30                   # days of the simulation
meeting_probability = 0.6  # meeting probability of Patients meetings
patient_zero_health = 25    # health of Patient zero

class Patient(Person):
    """
    Declaration of Patient class
    Inheritance of Person class
    """
    def __init__(self, first_name, last_name, health):  #constructor of Patient class
        self.health = health
        self.current_health = health

        Person.__init__(self,first_name, last_name)    # inheritance of Person class(parent)

    def get_health(self):               # method returns the patient’s current_health points
        return self.current_health

    def set_health(self, new_health):   # method changes the patient’s current_health points
        if new_health >= 100:
            self.current_health = 100
        elif new_health <= 0:
            self.current_health = 0
        else:
            self.current_health = new_health

    def is_contagious(self):                # method checks if Patient is contagious or not, return boolean
        if round(self.get_health()) <= 49:  # result, depends on Patient current_health points
            return True
        else:
            return False

    def infect(self, viral_load):                                      # method infects Patient object with a viral load
        if self.get_health() <= 29:                                    # depends on current_health points, formula
            self.set_health(self.get_health() - (0.1 * viral_load))    # is different. After infection, changes current
        elif 29 < self.get_health() < 50:                              # health points
            self.set_health(self.get_health() - (1.0 * viral_load))
        elif self.get_health() >= 50:
            self.set_health(self.get_health() - (2.0 * viral_load))

    def sleep(self):                                # method to recover current_health points after one night sleep
        recover = self.get_health() + 5             # adds 5 health points every night
        self.set_health(recover)

    def viral_load(self):                                       # method to calculate a viral load, return it's value
        viral_load = 5 + ((self.get_health() - 25)**2)/62
        return viral_load



def run_simulation(days, meeting_probability, patient_zero_health):
    """
        Function to run simulation of spreading disease
        It defining the rules of the simulation and meeting order of Patients and return list with number
        of contagious Patients at the end of the day.
        :param: days, meeting_probability, patient_zero_health
        :return: contageous_list list with number of contagious Patient at the end of each day
    """
    simulation = load_patients(initial_health)          # simulation starts with calling of load_patiients function
                                                        # to create list of Patients
    simulation[0].set_health(patient_zero_health)       # set health od patient zero

    def meeting_chance(meeting_probability):
        """
            Function determine the chance of the meeting depends on probability
            :param: meeting_probability
            :return: boolean
        """
        number = random.random()        # generate number number in the range [0.0, 1.0)
        if number < meeting_probability:    # compare random number with meeting_probability
            return True                 # meeting happens
        else:
            return False                # no meeting this day

    contagious_list = []                #defining a list of contagious people per day
    for i in range(days):                                       # iterate through the days of simulation
        for patient in simulation:                              # iterate through the Patients
            pat_friends = patient.get_friends()                 # assign Patient friends to a variable
            for friend in pat_friends:                          # iterate through the Patient friends
                chance = meeting_chance(meeting_probability)    # call a function meeting_chance(meeting_probability)
                                                                # to check if the meeting happens this day
                if chance==True:                                # if meeting took place
                    pat_contagious = patient.is_contagious()    # check both Patient and friend, if contagious
                    friend_contagious = friend.is_contagious()  # at the beginning of meeting
                    pat_viral = 0
                    fr_viral = 0
                    if pat_contagious==True:                    # if Patient is contagious, calculate his/her viral load
                        pat_viral = patient.viral_load()

                    if friend_contagious==True:                 # if friend is contagious, calculate his/her viral load
                        fr_viral = friend.viral_load()

                    if pat_contagious==True:                    # appliyng infect() to friend if Patient contagious
                        friend.infect(pat_viral)

                    if friend_contagious==True:                 # appliyng infect() to Patient if friend contagious
                        patient.infect(fr_viral)

        count = 0                                               # define a count varibale to count number of contagious
                                                                # Patient
        for patient_count in simulation:                        # iterate through Patient list for specific day to find
            patient_contagious = patient_count.is_contagious()  # number of contagious Patient for this day
            if patient_contagious==True:
                count += 1
            patient_count.sleep()
        contagious_list.append(count)

    return contagious_list      # list with the daily number of contagious cases through the duration of the simulation

def load_patients(initial_health):
    """
        read data from file a2_sample_set.txt
        return list of all the Patient objects that have been created
        :param initial_health argument initial Patient health
        :return: patient_list list with Patient objects
    """
    file_initial = open('a2_sample_set.txt', 'r')
    patient_list = []  # defining a Patient list
    for line in file_initial:  # check every line of the file
        patient_line = line.split(': ')  # split line to find Patient name
        patient_line = patient_line[0]
        patient_line = patient_line.split()
        new_patient = Patient(patient_line[0], patient_line[1], initial_health)  # creating new Patient object
        patient_list.append(new_patient)  # adding this Patient to the list
        friend_line = line.split(':')  # splitting line to find Patient friends
        friend_line.pop(0)
        friend_line = friend_line[0]
        friend_line = friend_line.strip().split(', ')  # split line and strip not required characters
        for i in range(len(friend_line)):  # adding friend name to the Patient friend_list_str
            new_patient.add_friend_str(friend_line[i])  # type String

    file_initial.close()  # close file a2_sample_set.txt

    for patient in patient_list:  # iterate through list of Patient objects
        for friend in patient.get_friends_str():  # iterate through list of Patient friends names
            for patient2 in patient_list:
                if friend == patient2.get_name():  # compare friend name with Patient name in the list
                    patient.add_friend(patient2)    # add social connection, reference to another Patient object

    return patient_list  # return a list of Patient objects


if __name__ == '__main__':

    # This is a sample test case. Write your own testing code here.
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.

    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]






# do not add code here (outside the main block).
