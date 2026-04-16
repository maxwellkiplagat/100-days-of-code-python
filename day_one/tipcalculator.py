bill = input('Welcome to the tip calculator!\n' 'what is the the total bill?')
tip = input('How much tip would you like to give? 10,12 or 15?')
people = input('How many people to spilt the bill?')
# basically tip is calculated by multiplying the bill by the percentage of the tip and the adding the tip to the bill and then dividing by the number of people to get the total per person   
total =  (float(bill) * ((float(tip)+100)/100))/int(people)
#here we convert the total to a two decimal place using the .2f format specifier in the f-string
print(f'Each person should pay: ${total:.2f}')