# Maximiliano Maurente
# CIS 4930

import easygui as e
import fractions as f
import operator as o
import random
import re  #To parse user input for solver an
import sys #Prints out what errors 

class noReplyError(Exception):
	pass
class badFormError(Exception):
	pass

opfunc ={	'+':o.add,
			'-':o.sub,
			'*':o.mul
		}
def apply_op(a,b,op):
		return opfunc[op](a,b)


####################################################################
###  3/55 + 6/80    ##   9/1 * 8/2
###  /5 + 8/9       ##   1/0 * 0/1
###  1 + 2          ##
###  5/w + 5        ##
###  5 * 8          ##
###  5/10 - 1/10    ##
###                 ##
####################################################################


def solver():
	while(1):
		msg = ("Enter a fraction expression to solve" 
			+ "using +,-, or *")
		reply = e.enterbox(msg, title="Solver")

		try:
			#Either Blank, Cancel, Or information(which can be proper form or inproper form)
			if(reply == ""):
				raise noReplyError
			elif(reply == None):
				return
			else:
				L = re.split(r'([*+-])',reply)
				sF1 = f.Fraction(L[0])
				sF2 = f.Fraction(L[2])
				#print(L)
				#print(str(sF1) +  str(sF2))
				#print(str(type(sF1)) +  str(type(sF2)))
				#handle improper form.
				if(sF1 == None and sF2 == None):
					ermsg = (ermsg + "----" + sF1)
					raise badFormError

				ans = apply_op(sF1,sF2,L[1])
				msg = (str(sF1) + L[1] + str(sF2) + " = " + str(ans))
				choices = ["Solve Another!!!", "Home Page"]
				reply2 = e.buttonbox(msg, title="Solver", choices=choices)
				if (reply2 == "Try Again"): continue
				if (reply2 == "Home Page"): return

		except noReplyError:
			emsg = "There was no User Input \nPlease press Try Again and enter a fraction expression."
			choices = ["Try Again", "Home Page"]
			b = e.buttonbox(emsg, title="Error", choices=choices)
			if (b == "Try Again"): continue
			if (b == "Home Page"): return
		except badFormError:
			#print("ERROR --> " + str(sys.exc_info()[0]))		
			choices = ["Try Again", "Home Page"]
			ermsg = ("***Improper Form*** Caused: " + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]))
			b = e.buttonbox(ermsg, title="Error", choices=choices)
			if (b == "Try Again"): continue
			if (b == "Home Page"): return
		except: #Most errors here will come from the fractions module
			#print("ERROR Other --> " + str(sys.exc_info()[0]))
			choices = ["Try Again", "Home Page"]
			emsg1 = ("***Improper Form*** Caused: " + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]))
			b = e.buttonbox(emsg1, title="Error", choices=choices)
			if (b == "Try Again"): continue
			if (b == "Home Page"): return

##############################################################################
##############################################################################
###   Quizzer                      ###########################################
##############################################################################	

def grade(userAns, fz, m):
	# Correctness tested with strings because Fraction() will simplify it
	# Most simplified answer will match Fraction
	if(userAns == str(fz)):
		msg = ("CORRECT!!!!\n" + m + str(fz))
		b = e.msgbox(msg, title="Results")
		return 100
	#It could be incorrect or 'correct but unsimplified'. Fraction will simplify for me
	else:
		uF = f.Fraction(userAns)
		if(uF == fz):
			msg = ("Correct but not simplified...\n" + m + str(fz)
					+"\nYour answer : " + userAns)
			b = e.msgbox(msg, title="Results")
			return 50
		else:
			msg = ("WRONG...\n" + m + str(fz)
					+ "\nYour answer : " + userAns)
			b = e.msgbox(msg, title="Results")
			return 0	

def quizzer():
	while(1):
		msg = "Choose a fraction operation to take a quiz"
		choices = ["+","-","*","Home Page"]
		reply = e.buttonbox(msg, title="Quizzer", choices=choices)
		if(reply == "Home Page"): return
		else:
			# x/y <> a/b
			f1 = f.Fraction(random.randint(-15,15), random.randint(1,15))
			f2 = f.Fraction(random.randint(-15,15), random.randint(1,15))
			fz = apply_op(f1,f2,reply)

			msg1 = str(str(f1) + reply + str(f2) + " = ")
			
			try:
				userAns = e.enterbox(msg1, title="Quizzer", strip=True)

				#Either Blank, Cancel, Or information(which can be proper form or inproper form)
				if(userAns == ""):
					raise noReplyError
				elif(userAns == None):
					continue
				else:
					#print(f.Fraction(userAns))
					grade(userAns, fz, msg1)
			except noReplyError:
				emsg = ("There was no User Input.\n\nThe answer was " + msg1 + str(fz))
				choices = ["Try Again", "Home Page"]
				b = e.buttonbox(emsg, title="Error", choices=choices)
				if (b == "Try Again"): continue
				if (b == "Home Page"): return
				#print(str(f1) + reply + str(f2))
			except:
				ermsg = ("***Improper Form*** Caused: " + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]))
				choices = ["Try Again", "Home Page"]
				b = e.buttonbox(ermsg, title="Error", choices=choices)
				if (b == "Try Again"): continue
				if (b == "Home Page"): return
				

if __name__ == "__main__":
	while(1):
		msg = "WELCOME TO FRACTIONS\n\nMax Maurente\nU49553112"
		choices = ["Solver","Quizzer","Quit"]
		reply = e.buttonbox(msg, title="HOME", choices=choices)

		if(reply == "Solver"):
			solver()
		if(reply == "Quizzer"):
			quizzer()
		if(reply == "Quit"):
			break;
			
