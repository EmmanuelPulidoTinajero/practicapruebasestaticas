class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        normalized_numbers = numbers.replace('\n', ',')
        if normalized_numbers.endswith(','):
            raise ValueError("Invalid input: separator at the end is not allowed")
        return sum(map(int, normalized_numbers.split(',')))