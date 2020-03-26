import urllib.request
import ssl
from bs4 import BeautifulSoup




#this method is extracting the stop words from one of website
def stopwords():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://www.ranks.nl/stopwords'
    stopword=[]
    response=urllib.request.urlopen(url)
    html = response.read()
    soup=BeautifulSoup(html)
    tlist=soup.find_all('td')

    for tr in tlist:
        info=tr.stripped_strings
        for t in info:
            stopword.append(t)
    return stopword


# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def stripNonAlphaNum(text):
    import re
    text=re.findall('[a-zA-Z]+',text)
    return text



def wordListToFreqDict(wordlist):
    wordfreq = dict((p,wordlist.count(p))for p in set(wordlist))
    return wordfreq

def sortFreqDict(freqdic):
    aux=[(freqdic[key],key) for key in freqdic]
    aux.sort()
    aux.reverse()
    return aux

def removeStopWord(wordList,stopwords):
    for st in stopwords:
        result=Rabin_Karp_Matcher(wordList,st,256,11)
        for s in result:
            del wordList[result[s]]

    return wordList



def Rabin_Karp_Matcher(text, pattern, d, q):
        n = len(text)
        m = len(pattern)
        h = pow(d, m - 1) % q
        p = 0
        t = 0
        result = []
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        for s in range(n - m + 1):
            if p == t:
                match = True
                for i in range(m):
                    if pattern[i] != text[s + i]:
                        match = False
                        break
                if match:
                    result = result + [s]
            if s < n - m:
                t = (t - h * ord(text[s])) % q  # remove letter s
                t = (t * d + ord(text[s + m])) % q  # add letter s+m
                t = (t + q) % q  # make sure that t >= 0
        return result

def remove(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]
