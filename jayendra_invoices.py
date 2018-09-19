# This program program prints invoices as per request.
# Studant ID - 10360474,
# By Jaynedra Monpara


import string

def main():
	# get input files from user or work with default files
	print "\nThis program is to generate invoice for each invoice number."
	print "\nEnter the input file name for invoices or hit Enter for default invoice file."
	print
	invoice_infile = raw_input("Enter input file for invoice details: ") or 'InvoiceDetails.csv'
	print "\nEnter the input file name for cuatomer addresses or hit Enter for default customer file."
	print
	cust_add_infile = raw_input("Enter the input file for customer address: ") or 'CustomerAddresses.csv'
	print "\nEnter the output file name for invoices or hit Enter for default output file."
	print
	invoice_outfile = raw_input("Enter the out file name: ") or 'invoices.txt'
		
	# open Input/Output files for reading or writing as needed by assigning a file handler variable.
	
	ininvoices = open(invoice_infile, 'r')
	cust_add = open (cust_add_infile, 'r')
	outfile = open(invoice_outfile, 'w')
	
	# ask used for starting invoice number that needs to be printed and validate entry.
	
	invalid = True
	while invalid:
		while True:
			try:
				print
				starting_invoice = raw_input("Enter starting invoice number between 1 to 9999 to print : ")
				starting_invoice_no = int(starting_invoice)
				break
			except: 
				print "\nSorry, can not take non-numeric values, please enter valid invoice number"
				print
		if (starting_invoice_no < 1) or (starting_invoice_no > 9999):
			print "\nSorry, invoice number must be in between 1 and 9999"
			continue
		elif (starting_invoice_no >= 111) and (starting_invoice_no <= 116):
			print "\nStarting Invoice Number is : ", starting_invoice_no
			invalid = False
			break
		else:
			print "\nsorry, invoice doesnot exist"	
			print "\nNote: For this program, only available invoice numbers are from 111 to 116."
			continue 
	
	# asking for ending invoice number and validation of the entry
	invalid = True
	while invalid:
		while True:
			try:
				print
				ending_invoice = raw_input("Enter ending invoice number between 1 to 9999 to print : ")
				ending_invoice_no = int(ending_invoice)
				break
			except: 
				print "\nSorry, can not take non-numeric values, please enter valid invoice number"
				print
		if (ending_invoice_no >= starting_invoice_no) and (ending_invoice_no <= 9999):
			print '\n ending invoice number is: ', ending_invoice_no
		else:
			print "\nsorry, please enter the valid ending invoice number between starting invoice number and 9999"	
			continue 
		invalid = False
		
	
	# Asking for PO number and validating the entry
	# PO number is Optional
	print '\nPO_number is alphanumeric string and should not be longer than 12 characters'
	print '\n PO_number is optional, Hit Enter if you do not want to print PO number.'
	
	invalid = True
	while True:
		print
		po_number = raw_input('Enter PO_number: ')
		if len(po_number) > 12:
			print '\nSorry, PO-number can not be longer than 12 characters. Please enter valid PO_number'
			continue
		else:
			break
		invalid = False
		
	# Read customer file name and assign a variable 'customer'
	customer = cust_add.readlines()
	
	# Read invoice file name and assign a variable 'invoices_in'
	invoices_in = ininvoices.readlines()
	
	#iterate through all invoices from starting invoice number and ending invoice number
	
	for invoices in range(starting_invoice_no,(ending_invoice_no +1),1):
		# Associate customer to each invoice number for address printing purpose
		if invoices == 111 or invoices == 112:
			data = string.split(customer[1], ",")
			title = data[1]
			firstname = data[2]
			lastname = data[3]
			address1 = data[4]
			address2 = data[5]
			address3 = data[6]
			address4 = data[7]
			address5 = data[8]
			cust_num = data[0]
			
		elif invoices == 113:
			data = string.split(customer[2], ",")
			title = data[1]
			firstname = data[2]
			lastname = data[3]
			address1 = data[4]
			address2 = data[5]
			address3 = data[6]
			address4 = data[7]
			address5 = data[8]
			cust_num = data[0]
		elif invoices == 114:
			data = string.split(customer[4], ",")
			title = data[1]
			firstname = data[2]
			lastname = data[3]
			address1 = data[4]
			address2 = data[5]
			address3 = data[6]
			address4 = data[7]
			address5 = data[8]
			cust_num = data[0]
		elif invoices == 115 or invoices == 116:
			data = string.split(customer[5], ",")
			title = data[1]
			firstname = data[2]
			lastname = data[3]
			address1 = data[4]
			address2 = data[5]
			address3 = data[6]
			address4 = data[7]
			address5 = data[8]
			cust_num = data[0]
				

		# import date library to print the date of printing.
		import datetime
		date1 = datetime.datetime.now().date()
				
		# Format header of the invoice
		outstring = "%5s THE ACADAMIC SUPPLY COMPANY LTD %40s" % ("","I N V O I C E")
		outfile.write(outstring+"\n")
					
		outstring = "%5s %72s" % ("","- - - - - - -")
		outfile.write(outstring+"\n\n")
					
		outstring = "%5s %12s %61s %3d" % ("","Castle House","Invoice Number:", invoices) 
		outfile.write(outstring+"\n")
						
		outstring = "%5s %13s %50s %10s" % ("","George Street","Date:", str(date1)) 
		outfile.write(outstring+"\n")
						
		outstring = "%5s %8s" % ("","Dublin 2")
		outfile.write(outstring+"\n\n")
						
		outstring = "%5s %3s " % ("","TO:") 
		outfile.write(outstring+"\n")
					
		outstring = "%5s %-2s %-3s %-20s %40s %-12s" % ("",title,firstname,lastname,"po_number:",po_number) 
		outfile.write(outstring+"\n")
					
		outstring = "%5s %-20s %54s %-12s" % ("",address1,"Customer Number:",cust_num) 
		outfile.write(outstring+"\n")
					
		outstring = "%5s %-20s" % ("", address2) 
		outfile.write(outstring+"\n")
					
		outstring = "%5s %-20s" % ("",address3) 
		outfile.write(outstring+"\n")
					
		outstring = "%5s %-20s" % ("",address4) 
		outfile.write(outstring+"\n")
					
		outstring = "%5s %-20s" % ("",address5) 
		outfile.write(outstring+"\n")
		
		outstring = "%2s %6s %12s %39s %10s %15s" %("","Item","Description","Unit Price","Quantity","Extended Price")
		outfile.write(outstring+"\n")
								
		outstring = "%2s %6s %12s %39s %10s %15s" %("","----","-----------","----------","--------","--------------")
		outfile.write(outstring+"\n")
		
		
		# iterate through the list of 'invoice_in' file by assigning variable 'record'
		# split the record by comma,
		# assign variables for details in record by indexing
		# calculate total, VAT, Grand_Total.
		# increase the item number by 1 for each line.
		item = 1
		Total = 0
		firsttime = True
		
		for record in invoices_in:
			if firsttime:
				firsttime = False
				continue
			record = string.split(record,",")
			if str(invoices) == record[1]:	
				cust_id = record[0]
				description = record[3]
				unit_price = float(record[4])
				quantity = float(record[5])
				extended_price = (unit_price) * (quantity)
				# print the details in outfile
				outstring = " %6d    %-29s %19.2f %10.2f %15.2f" %(item,description,unit_price,quantity,extended_price) 
				outfile.write(outstring+"\n")
				item = item + 1
				Total = Total + extended_price
			else:
				continue
			
				
		VAT = 0.23 * Total
		Grand_Total = VAT + Total
				
		# print the Total, VAT and grand total.
			
		outstring = " %78s %7.2f" %("Total: ", Total)
		outfile.write("\n" + outstring+"\n")
		
		outstring = " %78s %7.2f " %("VAT (23%): ", VAT)
		outfile.write(outstring+"\n")
			
		outstring = " %77s %8.2f" %("Grand Total:", Grand_Total)
		outfile.write(outstring+"\n\n\n\n\n")
			
		# print the footer for the invoice
			
		outstring = "      Make all cheques payable to THE ACADAMIC SUPPLY COMPANY LTD\n      Total due in 15 days."
		outfile.write(outstring+"\n\n\n")
			
		s = "Thank you for you business!"
		outstring = string.center(s,100)
		outfile.write(outstring + "\n")
		
	print '\nInvoice generated'
		
	# close the input/output files	
	ininvoices.close()
	cust_add.close()
	outfile.close()
	
	
	
main()
	