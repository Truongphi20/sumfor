from fractions import Fraction
import argparse

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-d", "--degree")
parser.add_argument("-v",'--version', action='version', version='%(prog)s 2.0',help = 'show version')
parser.add_argument("-s", "--show",default = 'b', help = 'only showing the formula (f), triagle matrix (m) or both (b)[default]?')


# Read arguments from command line
args = parser.parse_args()

def listToString(s): #Convert list to string
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def find_for(val):
	# Find coefficient
	seri_x = list(range(1,val+2,1))
	seri_y = list(range(0,val+1,1))

	list_0 = [1]
	list_poli = []
	for i in range(1,val+2):
		list_tem = ['']*i
		list_poli.append(list_tem)

	list_poli[0][-1] = Fraction(1,1)
	for i in range(1,val+1):
		for k in range(1,i+1):
			list_poli[i][-k] = Fraction(list_poli[i-1][-k]/seri_x[i+1-k]*seri_y[i])
		
		sum_tem = 0
		for n in range(1,i+1):
			sum_tem += list_poli[i][-n]

		list_poli[i][-i-1] = 1 - sum_tem

	# Create a degree functional form
	pt = []
	for i in range(1,val+2):
		pt.append('*x^'+str(i))

	# Create a list sign
	dau = []
	for i in list_poli[-1]:
		if i < 0:
			dau.append('')
		else:
			dau.append('+')

	# Combine to create list result
	ketqua = []
	for i in range(len(dau)):
		ketqua.append(dau[i])
		ketqua.append(list_poli[-1][i])
		ketqua.append(pt[i])

	formula = listToString(list(map(lambda x :x.__str__(),ketqua))) 
	return formula

def chart(val):
		# Find coefficient
	seri_x = list(range(1,val+2,1))
	seri_y = list(range(0,val+1,1))

	list_0 = [1]
	list_poli = []
	for i in range(1,val+2):
		list_tem = ['']*i
		list_poli.append(list_tem)

	list_poli[0][-1] = Fraction(1,1)
	for i in range(1,val+1):
		for k in range(1,i+1):
			list_poli[i][-k] = Fraction(list_poli[i-1][-k]/seri_x[i+1-k]*seri_y[i])
		
		sum_tem = 0
		for n in range(1,i+1):
			sum_tem += list_poli[i][-n]

		list_poli[i][-i-1] = 1 - sum_tem

	# Create a degree functional form
	pt = []
	for i in range(1,val+2):
		pt.append('*x^'+str(i))

	# Create a list sign
	dau = []
	for i in list_poli[-1]:
		if i < 0:
			dau.append('')
		else:
			dau.append('+')

	# Combine to create list result
	ketqua = []
	for i in range(len(dau)):
		ketqua.append(dau[i])
		ketqua.append(list_poli[-1][i])
		ketqua.append(pt[i])

	poly_str = []
	for i in range(len(list_poli)):
		ta = []
		for k in range(len(list_poli[i])):
			ta.append(str(list_poli[i][k]))
		poly_str.append(ta)

	# Margin alignment

	for i in range(len(poly_str)):
		poly_str[i].insert(0,seri_y[i])

	space_list = []
	for i in range(len(poly_str)):
		ha = []
		for k in range(len(list_poli[i])):
			ha.append(len(str(list_poli[i][k])))
		space_list.append(ha)

	max_space = []
	for i in range(0,len(space_list)):
		tem = []
		for k in range(i,len(space_list)):
			tem.append(space_list[k][i])
		max_space.append(max(tem))

	max_index = []
	for i in range(len(seri_y)):
		max_index.append(len(str(seri_y[i])))
	max_space.insert(0,max(max_index))


	space = []
	for i in range(len(poly_str)):
		space_tem = []
		for k in range(len(poly_str[i])):
			space_tem.append('  '+ ' '*(max_space[k]-len(str(poly_str[i][k]))))
		space.append(space_tem)

	seri_x.insert(0,'')

	space_seri_x = []
	for k in range(len(seri_x)):
		space_seri_x.append('  '+ ' '*(max_space[k]-len(str(seri_x[k]))))

	# Print matrix triagle
	print('\nMatrix triagle is:')
	print('')
	print(listToString([val for pair in zip(space_seri_x, map(str,seri_x)) for val in pair]))
	print('')

	for i in range(len(poly_str)):
		    print(listToString([val for pair in zip(space[i], map(str,poly_str[i])) for val in pair]))

if args.show == 'f' :
	val = int(args.degree)
	formula = find_for(val)
	print('Sum formula of x^',val,'is: ',formula)
else:
	if args.show == 'm':
		val = int(args.degree)
		chart(val)
	else:
		if args.show == 'b':	
			val = int(args.degree)
			formula = find_for(val)
			print('Sum formula of x^',val,'is: ',formula)
			chart(val)
		else:
			print('only showing the formula (f), triagle matrix (m) or both (b)?')
