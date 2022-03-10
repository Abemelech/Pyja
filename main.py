import json

def access_file_function():
    '''
    A funciton that access json file which includes the dicitonary of all the
    search results
    '''
    # Reads the json file
    with open('file.json','r') as file:
        # Creates a new dictionary
        syn_dict = json.load(file)
        
    # Return dictionary
    return syn_dict

def userInput():
    ''' A function to get user input from user 
    and return their input as a string''' 

    # Takes in the user search input
    userIn = input("Search: ")

    # returns the input
    return userIn   


def main():
    ''' The main function that will get executed'''

    # Users search
    userSearch = userInput()

    # Save dictionary
    syn_dict = access_file_function()



main()
