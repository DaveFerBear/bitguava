from yahoo_finance import Share

def getData(name, start_date, end_date):
	share = Share(name)
	return share.get_historical(start_date, end_date)