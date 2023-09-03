#TIP CALCULATOR 

#getting input bill from user

bill = float(input("What is the Bill? \n"))

#tip you want to give and number of people to split the bill

tip_percent = float(input("What percent tip did you want to give? 12, 15 or 10"))

people = int(input("How many people the Bill is going to split ? "))


each_person_should_pay = round((bill/people)*(100+tip_percent)/100,2)

print(f"So {people} will split {each_person_should_pay} on their behalf")
