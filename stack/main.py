from class_stack import Stack


def balance_check(brackets: str):
    stack_first = Stack()
    for bracket in brackets:
        stack_first.push(bracket)
    if stack_first.size() % 2 == 0:
        stack_second = Stack()
        while stack_first.is_empty() == False and stack_first.size() != 1:
            second = stack_first.pop()
            first = stack_first.peek()
            comb = first + second
            if comb == "()" or comb == "[]" or comb == "{}":
                stack_first.pop()
                while stack_second.is_empty() == False:
                    el = stack_second.pop()
                    stack_first.push(el)
            else:
                stack_second.push(second)
        if stack_first.is_empty() == True:
            print("Brackets are balanced")
            return
        if stack_first.is_empty() == False:
            print("Brackets are NOT balanced")
            return
    else:
        print("Brackets are NOT balanced")
        return
