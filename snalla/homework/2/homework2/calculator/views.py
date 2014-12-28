from django.shortcuts import render
import operator


def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        }[op]

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def calculate(request):

	display = request.GET.get('display')
	selection = request.GET.get('selection')
	firstNumber = request.GET.get('firstNumber')
	secondNumber = request.GET.get('secondNumber')
	currentOperation = request.GET.get('currentOperation')

	context = {'digits' : range(10), 'operations' : ["+","-","*","/","="], 
			'display':"", 'firstNumber':None, 'currentOperation':None,
			'secondNumber':None}

	#Get request without parameters
	if (not selection):
		return render(request, 'index.html', context);

	#Get request with parameters

	context['display'] = display
	context['firstNumber'] = firstNumber
	context['secondNumber'] = secondNumber
	context['currentOperation'] = currentOperation

	if (selection.isdigit()):
		if (display == "" or isInt(display)):
			#the answer is in the display
			if (currentOperation == "="):
				context['display'] = selection
				context['firstNumber'] = selection
				context['currentOperation'] = None
			elif (str(currentOperation) == "None"):
				context['display'] = display + selection;
				context['firstNumber'] = context['display']
			#there is already an operation to be performed 
			else:
				#second number hasn't been entered yet
				if (not isInt(secondNumber)):
					context['display'] = selection
				else:
					context['display'] = display + selection;
				context['secondNumber'] = context['display']
	elif (selection in context['operations']):
		#it's an operation
		#there is a second Number already
		if (isInt(firstNumber) and isInt(secondNumber) 
			and (currentOperation in context['operations'])):
			f = get_operator_fn(currentOperation)
			context['display'] = f(int(firstNumber), int(secondNumber))
			context['firstNumber'] = context['display']
			context['secondNumber'] = None
		context['currentOperation'] = selection 
	else:
		pass


	return render(request, 'index.html', context);
