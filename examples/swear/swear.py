# use the http://www.purgomalum.com/ to make profanity free text
# make GET request to https://www.purgomalum.com/service/ with text parameter and get the response back and print it

import requests # import the requests' library. More info: https://requests.readthedocs.io/en/master/
# library is a collection of functions and methods that you can use in your code

# def is a keyword that is used to define a function
# functions are used to group a set of statements together to perform a specific task
# functions are reusable and take parameters and return values
def get_clean_text(text): # function which takes parameter text and returns the profanity free text
    url = 'https://www.purgomalum.com/service/plain' # url to the purgomalum service
    params = {'text': text} # parameters for the request
    response = requests.get(url, params=params) # make the request
    return response.text # return the response text

if __name__ == '__main__': # if this file is run as a script (not imported) then run the code below this line

    # ask new inputs until the user types "exit"
    while True:
        text = input("Enter some dirty text (write exit to quit): ") # ask user for input
        if text == "exit": # if user types "exit" then exit the loop
            break # break out of the loop and continue with the code below the loop
        print(get_clean_text(text)) # get_clean_text function is called with text as parameter and the return value is printed

    print("Thank you for using the program!")




