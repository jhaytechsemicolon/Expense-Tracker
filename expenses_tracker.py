	
def get_menu():
	print('''
                  
                 1.Add an expense
		 2.view all expenses
		 3.calculate total expenses
		 4.exit

                 ''')
def get_expenses():
	expenses = []
	return expenses


def is_number(input):
	if input == "":
		return False
	for char in input:
		if  (char < '0' or char > '9'):
			return False
	return True


def get_date(year:str,month:str,day:str):
	if len(year) == 4 and is_number(year): 
		pass
	else:
		return 'invalid input' 
		 
	
	if len(month) == 2 and is_number(month) and 1 <= int(month) <= 31: 
		pass
	else:
		return 'invalid input' 
        

	if len(day) == 2 and is_number(day) and 1 <= int(day) <= 12: 
 
		pass
	else:
		return 'invalid input' 

	return 'valid input'	
      
        

def get_goods_description(items:str):
	if items == "":
		return 'invalid input'
	if is_number(items):
		return 'invalid input'
	return 'valid input'






def get_amounts(amount:int)->int:
	if amount == "":
		return 'invalid input'
	if  not is_number(amount):
		return 'invalid input'
	return 'valid input'	



def main():

	expenses = get_expenses()

	while True:

		get_menu()
		enter_choice = input('enter choice between 1-4: ')

		if enter_choice == '1':
			enter_year = input('Enter year(YYYY): ')
			enter_month = input('Enter month(MM): ')
			enter_day = input('Enter day(DD): ')
			date = get_date(enter_year,enter_month,enter_day)
			if date == 'invalid input':
				print ('invalid date. please try again:')
				continue


			enter_description = input('Enter goods description: ')
			description = get_goods_description(enter_description)
			if description == 'invalid input':
				print('invalid description. please try again:')
				continue


			enter_amount = input('Enter Amount: ')
			amounts = get_amounts(enter_amount)
			if amounts == 'invalid input':
				print ('invalid input. please try again:')
				continue


			expense = {
				'date': f' {enter_year}-{enter_month}-{enter_day}',
				'description': enter_description,
				'amounts' : int(enter_amount)
			}
			expenses.append(expense)
			print('expenses added succesfully')


		elif enter_choice == '2':
			for expense in expenses:
				print(f"date:,{expense['date']}, Description:{expense['description']}, Amount: {expense['amounts']}" )
	

		elif enter_choice == '3':
			total = 0
			for expense in expenses:
				total += expense['amounts']
			print ('total expenses:', total)



		elif enter_choice == '4':
			print('exiting app. Goodbye!')
			break
		else:
			print('invalid choice. please enter a number between 1 and 4')

main()





