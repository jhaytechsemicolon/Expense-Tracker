	
def get_menu():
	print('''
                 welcome to semicolon expense tracker store 
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



def get_date(date:str)->str:
	      	
	if len(date)  != 10:
		return 'invalid input'
	if date[4] != '-' or date[7] != '-':
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
			enter_date = input('Enter year(YYYY-MM-DD): ')
			date = get_date(enter_date)
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
				'date': f' {enter_date}',
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





