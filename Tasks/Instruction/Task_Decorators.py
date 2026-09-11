# ==========================================================
# DECORATOR EXERCISES
# ==========================================================
#
# Setup:
# Create two files:
#
# decorators.py
# decorators_test.py
#
# Define the decorators in decorators.py
# Test them in decorators_test.py
#
# ==========================================================


# ----------------------------------------------------------
# TASK 1
#
# Write a decorator called:
#
# with_logging
#
# It should print:
#
# Calling <name>
#
# before calling the decorated function.
# ----------------------------------------------------------


def with_logging(func):
    # TODO: define a wrapper that accepts any arguments
    #       (*args, **kwargs)

    # TODO: inside the wrapper, print the target
    #       function's name (hint: func.__name__),
    #       then call and return the function

    # TODO: return the wrapper
    pass


# ----------------------------------------------------------
# TASK 2
#
# Create a decorator that logs information to:
#
# audit.log
#
# Each time the decorated function is called,
# write the following:
#
# - current date
# - current time
# - function name
# - positional arguments
# - keyword arguments
#
# Hint:
#
# You may want:
#
# from datetime import datetime
#
# and:
#
# *args
# **kwargs
# ----------------------------------------------------------


def audit_log(func):
    # TODO: open audit.log in APPEND mode ("a") inside the
    #       wrapper and write the date/time, function name,
    #       and the arguments, then call the function
    pass


# ----------------------------------------------------------
# TRY THEM OUT
# ----------------------------------------------------------

# TODO: decorate a function with @with_logging, another with
#       @audit_log, call both, and inspect audit.log
