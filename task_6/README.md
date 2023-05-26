Consider a library. In the library, there are many books. Each book has a title, author, and a list of chapters. Each chapter has a title and a body (which is just text).

Your task is to:

1. Create classes to represent the library, book, and chapter using Python's object-oriented programming features.

2. Use the collections.abc package to ensure your library can be iterated over, yielding all books in the library. Similarly, make sure each book can be iterated over to yield all chapters.

3. Generate a simple HTML page for each book in the library using the mako package. The page should contain the book's title, author, and the titles and bodies of all chapters in the book.

4. Write a function using lxml to parse the generated HTML pages and verify that they contain the right information (i.e. the book title, author, and chapters' titles and bodies).