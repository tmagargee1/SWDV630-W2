from datetime import date
from email.headerregistry import Address


class CheckingAccount:
    def __init__(self, firstName, lastName, address, accountNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.accountNumber = accountNumber
        self._balence = 0.00
        self.dateOpenend = date.today()

    def deposit(self, amount):
        self._balence += amount

    def withdrawl(self, amount):
        self._balence -= amount

    def checkBalence(self):
        return self._balence

    def __str__(self):
        return "Account #"+ self.accountNumber + ", Opened: " + str(self.dateOpenend) + "\n" +\
            "Name: " + self.firstName + " " + self.lastName + ", Address:" + self.address + "\n" +\
            "Balence: " + str(self.checkBalence())
