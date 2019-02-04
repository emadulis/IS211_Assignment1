#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week1 assignment part 2"""


class Book(object):
    """This is a book class"""

    author = ''
    title = ''

    def __init__(self, author, title):
        """Constructor for a book.
        Args:
            author: name of author
            title: name of book
        Attritubtes:
            title (str): title of the book
            author (str): author of the book
        """

        self.author = author
        self.title = title

    def display(self):
        """shows text of a certain format.
        Args: None
        Return: None
        """
        output = '{}, written by {}.'.format(self.title, self.author)
        return output


Book1 = Book('John Steinback', 'Of Mice and Men')
Book2 = Book('Harper Lee', 'To Kill a Mockingbird', )
print(Book1.display())
print(Book2.display())
