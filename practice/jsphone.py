# Stack Machine
# -Primitives: [string|int]
# -Memory: stack
# -Programs: array of instructions
#
# Push [string|int]: pushes primitive onto stack
# Pop: removes top of stack
# Print: prints, doesn't remove, top of stack
# Add: removes top two elements, pushes "sum"
# - Both ints -> integer addition
# - Either string -> convert both to strings, string concatenation
# Jump [int]: unconditionally moves execution instruction @idx
# Jnz [int]: Jump if top of stack is Not integer ZeroDivisionError
#
# 0: Push 100
# 1: Push -1
# 2: Add
# 3: Print
# 4: Jnz 1

class StackMachine:
    def __init__(self, vals=None):
        self.vals = vals or []

    def push(self, n):
        self.vals.append(n)
        return

    def pop(self):
        return self.vals.pop()

    def print(self):
        if len(self.vals) > 0:
            print(self.vals[-1])
            return
        print("stack is empty")
        return

    def add(self):
        if len(self.vals) >= 2:
            a = self.pop()
            b = self.pop()
            if type(a) == type(b):
                self.push(a + b)
                return
            self.push(b)
            self.push(a)
            print("Wrong types")
            return
        print("Less than 2 elements in stack")
        return


st = StackMachine()
st.push(100)
st.push(-1)
st.add()
st.print()
st.push("10")
st.push("100")
st.add()
st.print()