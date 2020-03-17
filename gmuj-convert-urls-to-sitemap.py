# Summary: Program to generate an XML sitemap from a list of URLs 
# Details: 
# Last Modified: 20200317
# Modified by: JM

### import libraries

import sys, os, argparse, datetime

### define classes

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def fnTimestamp():
	##
	# Summary: returns a timestamp
	# Details: format: YYYYMMDDHHMMSS
	# Last Modified: 20160926
	# Modified by: JM
	##

	# return timestamp
	return '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())

def fnIsYes(inputString):
	##
	# Summary: checks to see if the input is a 'yes' ("y" or "Y" character)
	# Details: 
	# Last Modified: 20170929
	# Modified by: JM
	##

	# check to see if input string represents a yes
	if inputString=='y' or inputString=="Y": 
		varReturn=True
	else: 
		varReturn=False
	# return value
	return varReturn

def fnIfBlankDefaultValue(input_string,default_value):
	##
	# Summary: if the input is blank, use the provided default value
	# Details: 
	# Last Modified: 20190714
	# Modified by: JM
	##

	# is the input string blank?
	if input_string == "":
		return default_value
	else:
		return input_string

def fnOutputStringToFile(inputString,outputFileName):
	##
	# Summary: outputs a string to a file
	# Details: string to output and the name of the file to output to are specified as parameters
	# Last Modified: 20161004
	# Modified by: JM
	##

	# this script had been using: open(outputFileName, "w"), but some pages had characters that failed unless in binary mode
	# therefore I am now doing: open(outputFileName, "wb"), 
	# this then requires that the string be encoded as binary, hence the: text_file.write(inputString.encode('utf-8'))
	# prior to switching the file open mode to binary, this encoding was not needed

	# open/create text file for output ("wb" indicates opening file for writing binary data)
	text_file = open(outputFileName, "wb")
	# write output string to file
	text_file.write(inputString.encode('utf-8'))
	# close text file
	text_file.close()

def main():
	##
	# Summary: 
	# Details: 
	# Last Modified: 20200228
	# Modified by: JM
	##

	# clear screen (cross platform - cls for windows, clear for linux)
	# os.system('cls' if os.name == 'nt' else 'clear')
	#os.system('clear')
	
	print()

	# get command-line arguments
	# initialize argument parser
	parser = argparse.ArgumentParser()
	# configure argument parser
	parser.add_argument('-f','--file', help='File containing list of URLs.', required=False)
	parser.add_argument('-o','--output', help='Label for output file.', required=False)

	# parse arguments
	args = parser.parse_args()

	# set environment variables
	print(bcolors.HEADER + 'Script variables:'+ bcolors.ENDC)

	# set run timestamp
	time_stamp=fnTimestamp()
	print('Timestamp: ' + time_stamp) 

	# set current directory
	current_directory=os.path.dirname(os.path.realpath(__file__))
	print("Working directory: "+current_directory)
	print()

	# get input filename
	# was the input filename specified via command-line argument?
	if args.file:
		#print("An input filename argument was specified.")
		# with the label indicated
		input_filename=args.file
		#print("The input filename was: " + args.file)
	else:
		# the input filename was not specified via command line
		#print("No input filename argument.")
		# get input filename from user
		input_filename=input('Input file? (input-urls.txt): ')
		# handle empty input filename - provide default
		if input_filename=="": input_filename="input-urls.txt"

	print('Input file: '+input_filename)
	print()

	# get output settings
	# were the output settings specified via command-line argument?
	if args.output:
		#print("An output argument was specified.")
		# with the label indicated
		output_label=args.output
		#print("The output argument was: " + args.output)
	else:
		# the output settings were not specified via command line
		#print("No output argument.")
		# get output file label from user
		output_label=input('Output file label? ('+input_filename+'): ')

	# handle empty output label - provide default
	if output_label=="": output_label=input_filename

	# set output filename
	output_filename = "_sitemap-results/sitemap-" + output_label + "-" + time_stamp + ".xml"

	print("Output file: " + output_filename)
	print()

	if not fnIsYes(fnIfBlankDefaultValue(input('Continue? (Y/N) (Y): '),"y")):
		print(bcolors.WARNING + "Quitting Process" + bcolors.ENDC)
		exit()

	print()

	# prepare output string
	output_text=""

	# Open URL list text file for reading
	input_file = open(input_filename, 'r')
	
	# Start output
	output_text+='<?xml version="1.0" encoding="UTF-8"?>'+'\n'
	output_text+='<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+'\n'

	# Loop through lines in input file
	for line in input_file:

		# Get URL from current line of text file
		strURL=line.strip()

		output_text+='\t<url>'+'\n'
		output_text+='\t\t'+'<loc>'+strURL+'</loc>'+'\n'
		output_text+='\t</url>'+'\n'


		# flush output
		sys.stdout.flush()

	# Finish output
	output_text+='</urlset>'+'\n'

	# print completed message
	print()
	print(bcolors.OKBLUE + 'Process complete!' + bcolors.ENDC)
	print()

	# save output
	fnOutputStringToFile(output_text,output_filename)
	# print message
	print(bcolors.OKGREEN + 'Sitemap output to file: ' + output_filename + bcolors.ENDC)

	# finish output
	print()

	# make alert sound
	print('\a', end='')

### run main function if this file is loaded as the main program 
if __name__ == "__main__":
	main()
