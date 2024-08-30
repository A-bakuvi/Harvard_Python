class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError()
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """
        number_cookies = self._size
        for u in number_cookies:
            return "🍪"
        """
        return "🍪"*self._size


    def deposit(self, n):
        add_cookies = n + self._size
        if add_cookies> self._capacity:
            raise ValueError()
        else:
            self._size += n


    def withdraw(self, n):
        if n>self._size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size
def main():

    jar1 = Jar(12)
    jar1.deposit(2)
    print(str(jar1))
    jar1.withdraw(1)
    print(str(jar1))

if __name__ == "__main__":
    main()