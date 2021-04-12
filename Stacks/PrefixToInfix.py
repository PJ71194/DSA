def prefixToInfix(prefix):
	stack = []
	n = len(prefix)
	for idx in range(n-1, -1, -1):
		if prefix[idx].isalpha():
			stack.append(prefix[idx])
		else:
			operand1 = stack.pop()
			operand2 = stack.pop()
			infix = '(' + operand1 + prefix[idx] + operand2 + ')'
			stack.append(infix)

	print(stack.pop())
	return

if __name__=='__main__':
	prefix = input()
	prefixToInfix(prefix)