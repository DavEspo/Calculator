# Function that makes a calculator
def Calculator(Stack):
    # 2 Stacks for Operators and Operands created
    # Number and Operator variables created
    OperatorStack = []
    OperandStack = []
    Number = 0
    Operator = '+'
    # Loop that goes through every element in the input Expression
    for i in Stack + 'i':
        # Case where the element in the expression is a digit
        if i.isdigit() == True:
            Number = (Number * 10) + int(i)
        # Case where the element in the expression is a space
        elif (i == ' '):
            continue
        # Case where the element in the expression is an operator
        else:
            # Adds the Operators in the expression to the Operator Stack
            OperatorStack.append(i)
            # Elements are placed on the Operand Stack depending on the operator
            # Gives precedence to multiplication and division so those operations are performed
            if (Operator == '+'):
                OperandStack.append(Number)
            if (Operator == '-'):
                OperandStack.append(Number)
            if (Operator == '*'):
                OperandStack.append(OperandStack.pop() * Number)
            if (Operator == '/'):
                OperandStack.append(int(OperandStack.pop() / Number))
            # Sets the Operator to be the current element in the input Expression
            # Also removes the Operator from the Operator Stack and sets the Number back to 0
            Operator = OperatorStack.pop()
            Number = 0
            # Adds back the plus and minus operators to the Operator Stack since those operations weren't performed
            if ((Operator == '+') or (Operator == '-')):
                OperatorStack.append(Operator)
    OperatorStack.reverse()
    OperandStack.reverse()
    # Loop that goes through every Operand in the Operand Stack
    # for i in OperandStack:
    while len(OperandStack) != 1:
        # Sets the Operator from the Operator Stack and 2 values from the Operand Stack
        Operator = OperatorStack.pop()
        val1 = OperandStack.pop()
        val2 = OperandStack.pop()
        # The operations for adding and subtracting are done and the results are placed in the Operand Stack
        if Operator == '+':
            Result = val1 + val2
            OperandStack.append(Result)
        if Operator == '-':
            Result = val1 - val2
            OperandStack.append(Result)
    # Returns the value in the Operand Stack
    return OperandStack
# User enters expression with operators and operands and optional spacing
Expression=input("Enter an expression:\n")

# Calls the calculator function
print(Calculator(Expression))

# The time complexity is O(n) because the programs runs through each item in the expression in the for loops
# The space complexity is O(n) because the stack could potentially be the length of the input expression in the worst case scenario

# If a deque  was used, it would let us add or remove elements from the beginning and the end
# But with deque, the code could be almost exactly the same since you could pop and append at the end in deque too