import stack

def check_parenthesis(s):
    st = stack.Stack()
    for ch in s:
        if ch == '(':
            st.push(ch)
        elif ch == ')':
            if st.is_empty() == True:
                return False
            else:
                st.pop()
    return st.is_empty()

def main():
    s = '(((())))'
    if check_parenthesis(s) == True:
        print ('Correct')
    else:
        print ('Incorrect')
    s = '(((()))))'
    if check_parenthesis(s) == True:
        print ('Correct')
    else:
        print ('Incorrect')
    s = '(((())()))'
    if check_parenthesis(s) == True:
        print ('Correct')
    else:
        print ('Incorrect')
    s = '(()))(()))('
    if check_parenthesis(s) == True:
        print ('Correct')
    else:
        print ('Incorrect')
main()
