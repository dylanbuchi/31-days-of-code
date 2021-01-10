# Calculator
import sys


class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.substract,
            '*': self.multiply,
            '/': self.divide,
        }

    def get_operations(self):
        return self.operations

    def add(self, n1, n2):
        return n1 + n2

    def substract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        try:
            return n1 / n2
        except ZeroDivisionError as err:
            print("Error, Can't divide by zero")
            sys.exit()
