
    def divisorSum(n):
        raise NotImplementedError
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        pass
        x = []
        for i in range(1, n+1):
            if n % i == 0:
                x.append(i)
            else:
                pass
        return sum(x)

