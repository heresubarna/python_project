import datetime

user_input = input("Enter your goal with a deadline 'date DD.MM.YYYY format'  separated by colon|\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
 #1st is module 2nd one is class

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
# calculate how many days from now till deadline
time_till = deadline_date - today_date
print( f"Dear user time remaining for your goal: {goal} in {time_till.days} days")
print("OR")
print( f"Dear user time remaining for your goal: {goal} in {int(time_till.total_seconds() /60 /60)} hours")




