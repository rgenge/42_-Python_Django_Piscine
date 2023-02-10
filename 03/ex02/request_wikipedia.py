import requests
import dewiki
import sys

def exec_wiki(input):

    print(input)
    wiki_url = "https://en.wikipedia.org/w/api.php"
    wiki_params = {
    "action": "parse",
    "format": "json",
    "page": input,
    "prop" : "wikitext",
    "redirects" : True 
    }
    try:
        response = requests.get(wiki_url, wiki_params)
        response.raise_for_status()
    except:
        print ("Status code != 200")
        exit()

    response = response.json()
    try:
        request = response['parse']['wikitext']["*"]
    except:
        print('Error, wiki page not found')
        exit()
        
    res = dewiki.from_string(request)
    return(res)


def main():

    if (len(sys.argv) == 2):
        wiki_file = exec_wiki(sys.argv[1])
    else:
        exit("Type 2 arguments")
    output = sys.argv[1] + '.wiki'
    f = open(output, 'w')
    f.write(wiki_file)
    f.close
    
if __name__ == "__main__":
    main()