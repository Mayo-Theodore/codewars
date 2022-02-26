class Divisors():
    def is_greater(self, n):
        if n <= 1:
            return "Integer must be greater than 1"
        else:
            return "Integer is greater than 1"

    def divisible_by(self, n):
        array = []
        i = 100000
        while i >= 2:
            if n == i:
                pass
            elif n % i == 0:
                array.append(int(n / i))
            i -= 1

        return array

    def is_prime(self, n):
        array = []
        i = 100000
        while i >= 2:
            if n == i:
                pass
            elif n % i == 0:
                array.append(int(n / i))
            i -= 1

        if not array:
            return f"{n} is prime"
        

