class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        normalized_numbers = numbers.replace('\n', ',')
        if normalized_numbers.endswith(','):
            raise ValueError("Invalid input: separator at the end is not allowed")
        return sum(map(int, normalized_numbers.split(',')))
        # Handle custom delimiter syntax
        if numbers.startswith('//'):
            delimiter_end = numbers.find('\n')
            if delimiter_end == -1:
            raise ValueError("Invalid input: missing newline after delimiter declaration")
            
            delimiter = numbers[2:delimiter_end]
            numbers_part = numbers[delimiter_end + 1:]
            
            if not delimiter:
            raise ValueError("Invalid input: empty delimiter")
            
            # Check for mismatched delimiters
            for i, char in enumerate(numbers_part):
            if char not in [delimiter, ',', '\n'] and char.isdigit() == False:
                raise ValueError(f"I expected {delimiter} but found {char} at position {i}")
            
            normalized_numbers = numbers_part.replace('\n', ',').replace(delimiter, ',')
            if normalized_numbers.endswith(','):
            raise ValueError("Invalid input: separator at the end is not allowed")
            return sum(map(int, normalized_numbers.split(',')))

                # Check for negative numbers
                numbers_list = list(map(int, normalized_numbers.split(',')))
                negatives = [str(n) for n in numbers_list if n < 0]
                if negatives:
                    raise ValueError(f"Negative number(s) not allowed: {','.join(negatives)}")
                
                return sum(numbers_list)