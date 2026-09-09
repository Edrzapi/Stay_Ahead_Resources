# Advanced OOP Exercises

1. Create two files, one named classes.py and the other named classes_test.py. Each of the classes described below should be defined in classes.py and tested in classes_test.py. Each class should be named as you see fit.

## Circles

2. Code and test a class whose instances represent **circles**. Each circle has a radius from which the circle's diameter, circumference, and area may be derived. The formulas for circumference and area are provided below.

    - `Circumference: 2 * PI * r`
    - `Area: PI * r * r`

## Bank Loans

3. Code and test a class whose instances represent **bank loans**. Each loan has an amount, a term, and an interest rate from which the loan's total amount repayable and monthly repayment amount may be derived. The term should be expressed as a number of years, and the interest rate as a percentage. The formulas for the total amount repayable and monthly repayment amount are provided below.

    - `Total amount repayable: amount * interest rate / 100 + amount`
    - `Monthly repayment amount: total amount repayable / (term * 12)`

## eCommerce

4. Code and test two classes - one whose instances represent **products** (as in a store) and the other whose instances represent **baskets**. Each product has an ID, name, and price. Each basket has a container of products and quantities from which the total number of products and total price of all products may be derived.

5. Implement the following product and basket business rules:
    - a product must not be writable after creation
    - a basket's contents must not be directly writable
    - a basket must not contain duplicate products 

6. Code and test a class whose instance is responsible for maintaining an **inventory** of products. It should have two methods - one that accepts a product and returns the quantity of said product in stock, and the other that accepts a product and a quantity and attempts to reduce the stock of said product by the given quantity. The inventory data should be stored in a text file (for now).

7. Should basket objects be responsible for checking and updating the inventory? Why/why not?

8. What other class(es) might the eCommerce application require, if any?

## Tabular Data

Pandas is a popular Python package used for data analysis. The principle class is the DataFrame and its instances represent tabular data.

9. Code and test a class whose instances represent **columns** of data. Hint: a Pandas Series wraps a list. The class should have methods to compute the min, max, and mean values provided the column data is numeric.

10. Code and test a class whose instances represent **tables** of data. Hint: a Pandas DataFrame wraps a dict where each key is a column header, and each value is a Series. Instances of the class should be subscriptable, that is, one should be able to extract a column using the square bracket notation, e.g. `email_col = my_table["email"]` where `"email"` is a column header. Hint: the dunder `__getitem__` method is used to make instances of a class subscriptable.

    Assuming an instance named `orders` with a column named `"total price"` the following line of code should produce the average total price:

    `orders["total price"].mean()`

