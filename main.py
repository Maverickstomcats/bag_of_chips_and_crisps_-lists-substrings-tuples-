# remember to fork this repl into your own account
# create a new github project for this. call it week 4 review : lists, strings manipulations, tuples, substrings

##############################################################################################################
# basic review
# Find and display on the screen which character occupies the fifth position within the following word:
"computer"

# Find and display the index of the last occurrence of the word "practice" in the following sentence:
"In theory, theory and practice are the same. In practice, they are not."

###############################################Review############################################################
#####################################challenge 1################################################################
# Create a list with 5 elements, inside the variable my_list. You can include strings, booleans, numbers, etc.

# Add the element "motorcycle" to the following list of means of transportation:

transportation_means = ["plane", "car", "ship", "bicycle"]

# You must not modify the already supplied line of code, but must use the appropriate list method to add a new element.

# here are two lists:
luckyNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]
friends = ["Kevin", "Karen", "jim", "oscar", "tim", "lord tennyson"]
# instructions:
######join both lists together in a new list

###### print the new list out

###### print out the first item in the list

###### remove the last item of the new list

###### print the new list out without the last item

###### add three more items to the end of the list

###### print the last item in the new list

###### sort the list

###### find a way to insert a new item at the 3rd position of the list

###### print the new list out

##### reverse the list

###### print the new list out
###### print out the length of the new list

#####################################challenge 2#######################################################
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple", "is", "better", "than", "complex."]

# Print the following text in uppercase, using the specific string method:

text1 = "Especially in electronic communications, writing in all caps is equivalent to yelling."

#substrings
# Take every third character starting from the ninth to the end of the sentence, and print the result.

text2 = "Never trust a computer you can't throw out a window"

# Reverses the position of all the characters in the following sentence and displays the result on the screen.

text3 = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"

# Extract the first word of the following sentence using slicing, and display it on the screen:
"Controlling complexity is the essence of programming"

# create a text input that asks for choice of food
#create an empty list variable called food
# add 3 items from the user into the empty list
#print out the menu list

##############################################################################################################
# what are tuples?
# exactly the same thing as an array only it is immutable, once you define the tuple, you cannot change it or modify it
#you define a tuple with () instead of [] like you would in lists
#once you define it, you cannot change it
#example
coordinates = (4, 5)
# get the first element in the above tuple
# lets make this a multidimensional array
coordindates2 = [(4, 5), (6, 7), (80, 34)]
#get the second element of the second item in coordinates2

# we use parentheses not [] in tuples
my_tuple1 = (1, 2, 3, 4)
# get the second item in the tuple1 above
my_tuple = (1, 2, (10, 20), 4)
# get the second item in the 3rd item above
#hint multidimensional array thinking

# place these numbers in separate variables from the tuple below
t = (1, 2, 3)

#get me the length of the above tuple --- there are two ways of doing this... len(), count()...  use count if you want to get how many times an item appears in a tuple

# Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:

my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

# Convert the following tuple to a list, and store it in a variable called my_list.

my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)

#Extract the elements of the following tuple into four variables: a, b, c, d

my_tuple = (1, 2, 3, 4)

###########################################################################################################################
# booleans
# a boolean can only have 2 values -- true or False
# my_bool = 5 > 4
#print(my_bool)

# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to

# you can also construct booleans to see if values ar in a variable or not found
# my_ bool = 5 in my_list
# my_bool = 5 not in my_list

# so we can see if we can make logical decisions if something is true or not
# var1 = True
# var2 = False
# print(type(var1))
# print(var1)

# list = [1,2,3,4,5,6]
# control = 5 in list
# print(type(control))
# print(control)

# Booleans Practice

# Make a comparison that returns a boolean and store the result (True/False) in a variable called test

# Check if 17834/34 is greater than 87*56 and print the boolean result to the screen using print()

# Check if the square root of 25 is equal to 5 and display the result (boolean) on the screen using print

#################################share with instructor when finished#############################

##################################################################next week ################################################
#dictionaries and  sets

# dictionaries
# another data structure that stores data that can be unstructured
# employee = {'first_name': 'steven',
#             'last_name': 'pretti',
#              'weight': 37.2,
#               'size': 5.77}
# print(employee['weight'])

#challenge 1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist
# The names of the keys and values must be equal to the ones indicated above.

#challenge 2:
# Use print to returns the second item of the list called points2, inside the following dictionary.

# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
my_dict = {
    "values_1": {
        "v1": 3,
        "v2": 6
    },
    "points": {
        "points1": 9,
        "points2": [10, 300, 15]
    }
}
# print(my_dict[]) #Use dictionary indices to extract the second item of points2

#challenge 2
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:

# name: Karen

# surname: Jurgens

# age: 36

# occupation: Editor

# country: Colombia

# to do this, you should not change the line of code already written, but update the values using dictionary methods.

# my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}

#################################share with instructor when finished#############################
