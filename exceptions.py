""" exceptions

Practice using exceptions and the debugger

"""

from collections.abc import Sequence

Number = int | float


# Change so an appropriate exception is raised with a helpful message
#     when `numbers` is empty
def max(numbers: Sequence[Number]) -> Number | None:
    """Finds the item in numbers with the highest value"""
    if len(numbers) < 1:
        raise ValueError("max() argument must have at least one number")
    max_value = numbers[0]
    for value in numbers:
        if max_value < value:
            max_value = value
    return max_value


# Change so an appropriate exception is raised with a helpful message
#     when numbers is empty, and use exception handling to initialize
#     the counter for each value (Run it and you'll see!)
def mode(numbers: Sequence) -> tuple[Number, ...]:
    """Returns a tuple of the most frequently appearing members of numbers"""
    if len(numbers) < 1:
        raise ValueError("mode() argument must have at least one number")
    counter: dict[Number, int] = {}
    for number in numbers:
        try:
            counter[number] += 1
        except KeyError:
            counter[number] = 1
    sorted_numbers = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
    mode_count = counter[sorted_numbers[0]]
    mode: tuple = ()
    for number in sorted_numbers:
        if counter[number] < mode_count:
            break
        mode = mode + (number,)
    return mode


# Change so that a non-existent or unreadable file returns an empty list of strings
def load_file(filename: str) -> list[str]:
    """Read in a file and return its contents"""
    with open(filename, 'r') as txtfile:
        contents = [line.rstrip() for line in txtfile]
    return contents
  

# This scytale function doesn't work. Try debugging it using Pycharm's debugger
def scytale(message: str, diameter: int, decrypt: bool = False) -> str:
    """Performs a basic transposition cipher on `message` with period `diameter`"""
    grid = []
    if decrypt:
        depth, stop = divmod(len(message), diameter)
        for start in range(diameter):
            if start < stop:
                grid += [message[start:start + depth + 1]]
            else:
                grid += [message[start:start + depth] + ' ']
        plaintext = ''
        for line in zip(*grid):
            plaintext += ''.join(line)
        return plaintext.rstrip()
    else:
        for start in range(diameter):
             grid +=[message[start::diameter]]
        return ''.join(grid)


if __name__ == "__main__":
    print(max(numbers = []))
    pass
    # Write a few excample cases for each function,
    #     and put them in a try/except statement