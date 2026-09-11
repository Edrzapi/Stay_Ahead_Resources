# ==========================================================
# SOLUTION - DECORATOR EXERCISES
# ==========================================================

from datetime import datetime


# ----------------------------------------------------------
# TASK 1 - with_logging
# ----------------------------------------------------------
# A decorator is a function that takes a function and returns
# a replacement. The wrapper adds behaviour (the print), then
# hands off to the original.

def with_logging(func):
    def wrapper(*args, **kwargs):
        # *args / **kwargs let the wrapper accept whatever
        # the decorated function accepts - fully generic.
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)   # forward the result
    return wrapper


# ----------------------------------------------------------
# TASK 2 - audit_log
# ----------------------------------------------------------
# Same shape; the added behaviour is a file write. Append
# mode ("a") means each call adds a record instead of wiping
# the log. datetime.now() carries BOTH date and time, so one
# timestamp covers the first two requirements.

def audit_log(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        with open("audit.log", "a") as file:
            file.write(
                f"Date: {now:%Y-%m-%d}\n"
                f"Time: {now:%H:%M:%S}\n"
                f"Function: {func.__name__}\n"
                f"Arguments: {args}\n"
                f"Keyword arguments: {kwargs}\n"
                f"---\n"
            )
        return func(*args, **kwargs)
    return wrapper


# ----------------------------------------------------------
# TRY THEM OUT
# ----------------------------------------------------------

@with_logging
def greet(name):
    print(f"Hello, {name}")


@audit_log
def add(a, b, round_result=False):
    result = a + b
    return round(result) if round_result else result


greet("Ed")                            # prints: Calling greet / Hello, Ed
print(add(2.4, 3.2, round_result=True))  # logs to audit.log, prints 6

with open("audit.log") as f:           # show what was written
    print(f.read())


# ----------------------------------------------------------
# Notes from the live version, worth knowing:
# - datetime.now().minute gives ONLY the minute number (an int);
#   format the full datetime instead, as above.
# - The task names the file audit.log, so write to that exact
#   name rather than audit_log.txt.
# - Let the wrapper RETURN the result rather than printing it;
#   printing inside the wrapper surprises any caller that
#   wanted the value.
# - Stretch: functools.wraps(func) on the wrapper preserves
#   func.__name__ through the decoration - without it, every
#   decorated function reports its name as "wrapper".
# ----------------------------------------------------------
