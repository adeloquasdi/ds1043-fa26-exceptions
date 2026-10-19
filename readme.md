# What could go wrong?

Quite a lot, actually.

For a full list of the built-in exceptions, see
<https://docs.python.org/3/library/exceptions.html>.

Common exceptions you may want to make use of include:

- `TypeError`
- `ValueError`
- `IndexError`
- `KeyError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `PermissionError`
- `FileExistsError`
- `IsADirectoryError`
- `IsNotADirectoryError`

# Raising Exceptions

Often we need to be able to signal from one function to another than
something has gone wrong. For this we use the `raise` keyword with the
appropriate exception type.

``` python
raise Exception
```

In this case, `Exception` is the constructor for an `Exception` object.
You can pass arguments to this constructor to give more information
about why the exception has been raised.

``` python
raise ValueError("min() argument is empty")
```

# Handling Exceptions

The full syntax for handling exceptions is as follows:

``` python
try:
    # some code that may raise an exception
except Exception:
    # some code that handles the given exception
except ZeroDivisionError:
    # you can have multiple `except` blocks for different exceptions
except (IndexError, KeyError):
    # you can specify a tuple of errors for an `except` block
except ValueError as ve:
    # you can assign a name to the exception for use in the `except` block
else:
    # some code that will run if there are no exceptions
finally:
    # some code that will run regardless
    # this block is typically used to clean up after whatever was tried
```

You do not need all of these blocks in any given statement. At minimum,
you only need a `try` and either an `except` or `finally` block.

# Best Practices

- Try to use the most relevant or specific exceptions both when raising
  them and when handling them.
- Many exceptions exist which indicate a bug in your code. Rather than
  handling these exceptions, you should try to find the bug and fix it.
- Exceptions are best used for reacting to things external to the piece
  of code you are working on. Things like validating input or errors or
  events arising from systems such as files and network resources.
