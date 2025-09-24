# Generate the first 25 perfect squares
squares = [n**2 for n in range(1, 26)]

# Compute successive differences
differences = [squares[i+1] - squares[i] for i in range(len(squares) - 1)]

# Display results
print("First 25 squares:", squares)
print("Successive differences:", differences)
