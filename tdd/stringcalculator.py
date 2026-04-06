class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        return sum(map(int, numbers.split(',')))
    def add(self, numbers):
        if not numbers:
            return 0
        normalized_numbers = numbers.replace('\n', ',')
        return sum(map(int, normalized_numbers.split(',')))