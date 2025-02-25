def get_date(date:str)->str:
	
	if len(date)  != 10:
		return 'invalid input'
	if date[4] != '-' or date[7] != '-':
		return 'invalid input'
	
	return 'valid input'
			
				