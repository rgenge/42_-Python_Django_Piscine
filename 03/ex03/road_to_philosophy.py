import requests
import sys
from bs4 import BeautifulSoup


def exec_wiki(input):

    n = 2
    wiki_url = "https://en.wikipedia.org" + input
    infinite_test = [wiki_url]
    while wiki_url  != 'https://en.wikipedia.org/wiki/Philosophy':
        response = requests.get(wiki_url)
        if not response or response.status_code != 200:
            return("It leads to a dead end !")   
        soup = BeautifulSoup(response.text, 'html.parser')
        x = 0
        for link in soup.find_all('p'):
            if x == 1:
                break
            for a in link.find_all('a', href=True):
                if '/wiki/' in a['href'] and not 'Help' in a['href'] and not '/File:' in a['href']:
                    response = requests.get("https://en.wikipedia.org" + a['href'])
                    if response and response.status_code == 200:
                        wiki_url = "https://en.wikipedia.org" + a['href']
                        print(a['href'][6:])
                        x = 1
                        if wiki_url in infinite_test:
                            return("It' leads to an infinite loop")
                        else:
                            break
                infinite_test.append(wiki_url)
        n += 1
    print_screen = str(n) + " roads from " + input[6:] + " to philosophy !"
    return (print_screen)

    
def main():

    if (len(sys.argv) == 2):
        print(sys.argv[1])
        wiki_file = exec_wiki('/wiki/' + sys.argv[1])
        print(wiki_file)
    else:
        exit("Type 2 arguments")
        
    
if __name__ == "__main__":
    main()