dates = []
goods_description = []
amounts =[]
total = 0 

print ('''
Welcome to Semicolon Expense Tracker App
-----------------------------------------  ''')
print('''
1.Add an expense
2.view all expenses
3.calculate total expenses
4.exit
       ''')

while True:

   enter_choice = int(input('enter your choice: '))
   if enter_choice == 1:
    date =  input('(YYYY-MM-DD)')
    description = input('Enter the description: ')
    amount = float(input('Enter the amount: '))

    dates.append(date)
    goods_description.append(description)
    amounts.append(amount)
    print ('Expense added')
  
 


   elif enter_choice == 2:
    print('Expenses: ')
    for value in range (len(dates)):
     print('Date:', dates[value],',''Description:',goods_description[value],',''Amount:$', amounts[value]  )


   elif enter_choice == 3:
    total += amounts[value]
    print('Total Expenses:',total) 


   elif enter_choice == 4:
    print('Existing the app.Goodbye!') 
    break
     
   else:
    print('Invalid choice, enter valid number')
   
 