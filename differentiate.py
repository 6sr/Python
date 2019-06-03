listTrigo = ["sin","cos","tan","cosec","sec","cot"]
def XpowerN(y):
	curr = y.split("^")
	power = int(curr[1])
	if power == 2:
		return "2x"
	ans = str(power) + "x^" + str(power - 1)
	return ans

def isTrigo(y):
	global listTrigo
	for i in listTrigo:
		if y.count(i) != 0:
			return i
	return None

def Trigo(y):
	curr = ""
	if y.count("^") != 0:
		power = re.findall('\S+([0-9])\S+',y)
		curr = XpowerN("x^" + power[0])
	trigoFunc = ""
	if isTrigo(y) != None:
		trigoFunc = isTrigo(y)
	if curr == "2x":
		return "2" + trigoFunc
	numInCurr = re.findall('([0-9])',curr)
	return (str(numInCurr[0]) + trigoFunc + "^" + str(numInCurr[1]) + "x")
	
def Log(y):
	if y.count("^") == 0:
		return "1/x"
	if y.count("^") == 2:
		ans = ""
		power = re.findall('([0-9])',y)
		expLog = XpowerN("x^" + str(power[0]))
		expX = XpowerN("x^" + str(power[1]))
		if expLog == "2x":
			return "(2)" + expX + "logx^" + str(power[1])
		expLog.replace("x","log")
		expLog = "(" + expX + "/" + "x^" + str(power[1]) ")" + expLog + "x^" + str(power[1])


def differentiateExp(y):
	# If input is const
	if y.count("x") == 0:
		return "0"
	# If input is variable
	numExp = 0
	if y.count("(") == y.count(")"):			# considering basic input where every exp is in different bracket
		numExp = y.count("(")

	expList = y.split(")(")
	firstExp = expList[0]
	lastExp = expList[numExp - 1]
	expList[0] = firstExp[1:len(firstExp)]
	expList[numExp - 1] = lastExp[0:len(lastExp) - 1]

	coefficient = ""
	varList = []
	for i in expList:						# i is curr exp
		if i.count("x") == 0:				# If curr exp is const
			coefficient = coefficient + "(" + i + ")"
		else:
			varList.insert(i)

	ans = differentiateExpRec(varList)
	ans = coefficient + ans
	return ans

def differentiateExpRec(expList):
	if len(expList) <= 1:
		#diff for one exp base case
		#return "(" + exp + ")"

	ans = ""
	flag = 0
	for i in expList:
		if flag == 1:
			ans = ans + " + "
		flag = 1
		for j in expList:
			if i == j:
				ans = ans + "(" + differentiateExpRec([j]) + ")"
			else:
				ans = ans + "(" + j + ")"

def differentiateSingleExp(exp):
	if exp.startswith("x^"):				# If curr exp is x^n
		return XpowerN(exp)					# Ans returned without bracket
	if isTrigo(exp):
		return Trigo(exp)
	if exp.count("log") != 0:
		Log(exp)



y = str(input())
#y = x^n

print(differentiateExp(y))
#if y.find("sin") != -1:

