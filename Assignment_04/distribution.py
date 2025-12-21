# distribution.py
class distribution:
    def __init__(self):
        self.d = [0]

    def add(self, number):
        if len(self.d) < number + 1:
            for i in range(number + 1 - len(self.d)):
                self.d.append(0)
        self.d[number] += 1

    def print_dist(self):
        print(self.d)

    def get(self):
        return str(self.d)