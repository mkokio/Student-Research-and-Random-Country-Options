import pycountry
from random import randint

"""
In a classroom of 30 students each student will have
3 random countries from which to choose one to research.

1. ['Canada', 'Japan', 'Turkey']

Student #1 can select one of the above countries to research.

Note: It is possible that 2 students share the same country as
a choice, thus it is possible they both research the same country.
"""

def make_simple_list():
    """Creates a simple list of all the countries of the world"""
    countries_simple_list = []
    for country in pycountry.countries:
        countries_simple_list.append(country.name)
    return countries_simple_list

def random_country():
    """Returns a random country"""
    list = make_simple_list()
    length = len(list)
    random_country = list[randint(0,length-1)]
    return random_country

def countries(number):
    """Creates a selected length list of random countries"""
    countries = []
    x = 0
    while x < number:
        country = random_country()
        if country not in countries: #avoid duplicate choices for each student
            countries.append(country)
            x += 1
    return countries

def create_dictionary(students,number_of_countries):
    """Creates and prints dictonary of students and choices"""
    student_choices = {}
    x=1
    for student in range(1,students+1):
        student_choices[x] = countries(number_of_countries)
        x +=1
    return student_choices
    
def print_dictionary(dictionary):
    """Neatly print the dictionary"""
    for key, value in dictionary.items():
        print(f"{key}: {value}")
   
prompt_1 = int(input("How many students in your class? "))
prompt_2 = int(input("How many country choices per student? "))
print_dictionary(create_dictionary(prompt_1, prompt_2))
