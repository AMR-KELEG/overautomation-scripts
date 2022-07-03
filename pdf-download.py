import requests

BaseName = "BASE_DIRECTORY"
BaseURL0 = "https://web.stanford.edu/class/cs143/lectures/lecture0"
BaseURL1 = "https://web.stanford.edu/class/cs143/lectures/lecture1"

# Download lectures [01, 09]
for i in range(1, 10):
    link = BaseURL0 + str(i) + ".pdf"
    book_name = link.split("/")[-1]
    with open(book_name, "wb") as book:
        a = requests.get(link, stream=True)

        for block in a.iter_content(512):
            if not block:
                break

            book.write(block)

# Download lectures [10, 18]
for i in range(0, 9):
    link = BaseURL1 + str(i) + ".pdf"
    book_name = link.split("/")[-1]
    with open(book_name, "wb") as book:
        a = requests.get(link, stream=True)

        for block in a.iter_content(512):
            if not block:
                break

            book.write(block)
