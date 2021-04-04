class Stack(object):
    p = 998244353
    size = 0
    def __init__(object):
        self.stack = []

    def push(self, value):
        if size <= 1000000:
            self.stack.append(value % self.p)
            size += 1
        else:
            print("STACK_OVERFLOW")
    def pop(self):
        if self.stack:
            self.stack.pop()
            size -= 1
        else:
            print("STACK_UNDERFLOW")

    def is_empty(self):
        return bool(self.stack)

    def top(self):
        if is_empty():
            print("ILLEGAL_ACCESS")
        else:
            return self.stack[-1]
    
    def length(self):
        return self.size

        
def gsn(a):
    if a == 'A':
        return 0
    elif a == 'B':
        return 1
    else:
        return 2
def main():
    A = []
    A.append(Stack())
    A.append(Stack())
    A.append(Stack())
    f = open('a.txt')
    common_list = f.read().split('\n')
    line = 0
    c = 0
    while c <= 1000000:
        common = common_list[line].split(' ')
        c += 1
        if common[0] == 'PUS':
            A[gsn(common[1])].push(int(common[2]))
            line = int(common[3])
        elif common[0] == 'POP':
            A[gsn(common[1])].pop()
            line = int(common[2])
        elif common[0] == 'MOV':
            A[gsn(commom[1])].push(A[gsn(common[2])].top())
            A[gsn(common[2])].pop()
            line = int(common[3])
        elif common[0] == 'CPY':
            A[gsn(commom[1])].push(A[gsn(common[2])].top())
            line = int(common[3])
        elif common[0] == 'ADD':
            A[gsn(common[1])].push(A[gsn(common[2])].top() + A[gsn(common[3])].top())
            line = int(common[4])
        elif common[0] == 'SUB':
            A[gsn(common[1])].push(A[gsn(common[2])].top() - A[gsn(common[3])].top())
            line = int(common[4])
        elif common[0] == 'MUL':
            A[gsn(common[1])].push(A[gsn(common[2])].top() * A[gsn(common[3])].top())
            line = int(common[4])
        elif common[0] == 'DIV':
            if A[gsn(common[3])].top() != 0:
                A[gsn(common[1])].push(A[gsn(common[2])].top() - A[gsn(common[3])].top())
            else:
                print("DIVIDE_BY_ZERO")
            line = int(common[4])
        elif common[0] == 'MOD':
            if A[gsn(common[3])].top() != 0:
                A[gsn(common[1])].push(A[gsn(common[2])].top() - A[gsn(common[3])].top())
            else:
                print("DIVIDE_BY_ZERO")
            line = int(common[4])
        elif common[0] == 'EMP':
            if A[gsn(common[1])].is_empty():
                line = int(common[2])
            else:
                line = int(common[3])
        elif common[0] == 'CMP':
            if A[gsn(common[1])].top() <= A[gsn[common[2]]].top():
                line = int(common[3])
            else:
                line = int(common[4])
        elif common[0] == 'TER':
            break
    
