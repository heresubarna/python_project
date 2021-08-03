import learningPython
#from learnerPython import validation_and_execute (if need to more thing add comma and add) * for all
#if use from..import then do not need to add module name. to call the functions or variables
user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit! \n")
    print(user_input)
    days_and_unit = user_input.split(":")  #list_of_days = user_input.split(", ")
    """for num_of_days_element in set(list_of_days):
        validate_and_execute()"""
    days_and_unit_dictionary = {"days":days_and_unit[0] , "unit":days_and_unit[1] }
    learningPython.validation_and_execute(days_and_unit_dictionary) #validation_and_execute(days_and_unit_dictionary)
