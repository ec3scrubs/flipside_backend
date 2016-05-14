from bs4 import BeautifulSoup
import re

def strip_nonascii(s):
    import string
    printable = set(string.printable)
    ss = filter(lambda x: x in printable, s)
    return ss

def main():
    cnt = 1
    for i in xrange(1, 10):
        fi = open(str(i))
        html_doc = fi.read()
        fi.close()
        soup = BeautifulSoup(html_doc, 'html.parser')
        reviews = soup.find_all('p', {'itemprop': 'description'})
        for review in reviews :
            # review = str(review.encode('utf-8').strip())
            review = (strip_nonascii(str(review)))
            review = review.split("<br><br>")
            review = "\n".join(review)[36:-4]
            review = review.replace("<br>", "\n")
            review = review.replace("</br>", "")
            print review
            ff = open('output/' + str(cnt), 'w')
            ff.write(review)
            cnt += 1


if __name__ == "__main__":
    main()
