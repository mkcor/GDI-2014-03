
# function to create a letter with personalised parameters

def dear_friend(yourname, name,age,country,accident,reward,email): 

	letter = "Dearest %s, my name is %s. I am a %d years old Girl from %s, My father Dr. YAK Ayopak was the former minister of finance\
	and Special Adviser to the President of %s. He was killed in a %s and soon after, my uncle conspired with my step mother and sold my father's properties to a \
	Chinese Expatriate. On a faithful morning I opened my father's briefcase and found out documents which indicate another money deposit \
	in a Bank in Burkina Faso, with my name as the next of kin. I have chosen to contact you after my prayers and I believe that you can help me \
	get this deposit since I'm not of legal age. \
	I know I can trust you and in return you will receive %f in reward. \
	My email addres is:  %s \n" %(yourname, name, age, country, country, accident, reward, email)

	endofletter = "Sincerely yours\n %s" %(name)

	result = letter + endofletter

	return result

def write_letter(filepath, results):
	# filepath needs to be something like /home/users/mghamsari/Documents/letter.txt
	f = open(filepath, 'w')
	for row in results:
    		f.write(row)
	
	f.close()

# Use the above two functions to create a letter promising lots of money 
result = dear_friend('a','a',21,'c','c',45,'44')
write_letter('test.txt',result)
