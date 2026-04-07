class MinStack:
    

    def __init__(self):
        self.st=[]
        self.minSt=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minSt or self.minSt[-1]>=val:
            self.minSt.append(val)
        

    def pop(self) -> None:
        if not self.st:
            return -1
        p=self.st.pop()

        if self.minSt[-1]==p:
            self.minSt.pop()
        

    def top(self) -> int:
        return self.st[-1] if self.st else -1
        

    def getMin(self) -> int:
        return self.minSt[-1] if self.minSt else -1
        
