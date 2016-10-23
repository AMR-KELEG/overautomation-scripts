BaseName = 'C:\\Users\\amr\\Desktop\\lectures\\'
BaseURL0 = 'https://web.stanford.edu/class/cs143/lectures/lecture0'
BaseURL1 = 'https://web.stanford.edu/class/cs143/lectures/lecture1'

import requests


for i in range(1,10):
    link=BaseURL0+str(i)+'.pdf'
    book_name = link.split('/')[-1]
    with open(book_name, 'wb') as book:
        a = requests.get(link, stream=True)

        for block in a.iter_content(512):
            if not block:
                break

            book.write(block)

for i in range(0,9):
    link=BaseURL1+str(i)+'.pdf'
    book_name = link.split('/')[-1]
    with open(book_name, 'wb') as book:
        a = requests.get(link, stream=True)

        for block in a.iter_content(512):
            if not block:
                break

            book.write(block)
