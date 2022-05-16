class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr(x):
        print(Math.add10(x))
    
Math.pr(5)
