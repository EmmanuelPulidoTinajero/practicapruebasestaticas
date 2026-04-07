class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        
        errors = []
        delimiter = ','
        numbers_part = numbers
        
        # Handle custom delimiter syntax
        if numbers.startswith('//'):
            delimiter_end = numbers.find('\n')
            if delimiter_end == -1:
                errors.append("Invalid input: missing newline after delimiter declaration")
            else:
                delimiter = numbers[2:delimiter_end]
                numbers_part = numbers[delimiter_end + 1:]
                
                if not delimiter:
                    errors.append("Invalid input: empty delimiter")
        
        # Normalize and validate
        if not errors:
            normalized_numbers = numbers_part.replace('\n', ',').replace(delimiter, ',')
            if normalized_numbers.endswith(','):
                errors.append("Invalid input: separator at the end is not allowed")
            else:
                # Check for negative numbers
                try:
                    numbers_list = list(map(int, normalized_numbers.split(',')))
                    negatives = [str(n) for n in numbers_list if n < 0]
                    if negatives:
                        errors.append(f"Negative number(s) not allowed: {','.join(negatives)}")
                    else:
                        if errors:
                            raise ValueError('\n'.join(errors))
                        return sum(numbers_list)
                except ValueError as e:
                    if "invalid literal" in str(e):
                        errors.append("Invalid input: non-numeric value")
        
        if errors:
            raise ValueError('\n'.join(errors))