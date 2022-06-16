"""
Program creates class Person with required attributes and methods.
Separate function load_people() is responsible to read a txt file and to create new Person objects
and connections with friends. It returns a list of Person objects.

Author - Pavel Zemnukhov
Date the script was created - 25/05/2020
Date the last edit was made - 30/05/2020
"""

class Person:
    """
    Declaration of Person class
    """

    def __init__(self, first_name, last_name): #constructor of Person class
        self.first_name = first_name
        self.last_name = last_name
        self.friend_list = []
        self.friend_list_str = []

    def add_friend(self, friend_person): # method to add social connection
        self.friend_person = friend_person
        self.friend_list.append(self.friend_person)

    def add_friend_str(self, friend_name):  # method to add friends names
        self.friend_name = friend_name
        self.friend_list_str.append(self.friend_name)

    def get_name(self): # method to return a name of the Person
        return str(self.first_name) + " " + str(self.last_name)

    def get_friends(self): # method returns list of the Person connections with other Persons
        return self.friend_list

    def get_friends_str(self): # method returns friends names
        return self.friend_list_str


def load_people():
    """
       read data from file a2_sample_set.txt
       return list of all the Person objects that have been created
       """
    file_initial = open('a2_sample_set.txt', 'r')
    person_list = []                        #defining a list
    for line in file_initial:               #check every line of the file
        person_line = line.split(': ')      #split line to find Person name
        person_line = person_line[0]
        person_line = person_line.split()
        new_person = Person(person_line[0], person_line[1])     #creating new Person object
        person_list.append(new_person)                          #adding this Person to the list
        friend_line = line.split(':' )                          #spliting line to find Person friends
        friend_line.pop(0)
        friend_line = friend_line[0]
        friend_line = friend_line.strip().split(', ')           #split line and strip not required characters
        for i in range(len(friend_line)):                       #adding friend name to the Person friend_list_str
            new_person.add_friend_str(friend_line[i])           #type String

    file_initial.close()  #close file a2_sample_set.txt

    for person in person_list:                          #iterate through list of Person objects
         for friend in person.get_friends_str():        #iterate through list of Person friends names
             for person2 in person_list:
                 if friend == person2.get_name():       #compare friend name with Person name
                     person.add_friend(person2)         #add social connection, reference to another Person object

    return person_list      #return a list of Person objects


if __name__ == '__main__':
    load_people()










