
import stopwords as st
import urllib.request
from bs4 import BeautifulSoup
import plotly.graph_objects as go

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.bbc.com/news/uk-51991887'


stopword=[]
freq=[]
word=[]

response = urllib.request.urlopen(url)
html = response.read()
soup=BeautifulSoup(html)
text=soup.get_text(strip=True)
fullwordlist= st.stripNonAlphaNum(text)
stopword=st.stopwords()

# this algorithmn method still has some problem so i show it as comment first
# wordList=st.removeStopWord(fullwordlist,stopword)

wordlist =st.remove(fullwordlist,stopword)
dictionary = st.wordListToFreqDict(wordlist)
sorteddict = st.sortFreqDict(dictionary)

for t in sorteddict:
   freq.append(t[0])

for i in sorteddict:
    word.append(i[1])

print(sorteddict)


# this part is drawing the frequency of words which extract from website
fig = go.Figure()
fig.add_trace(go.Bar(x=word,
                y=freq,
                name='the frequency of words',
                marker_color='rgb(204, 0, 204)',
                width=20)
              )


fig.update_layout(
    title='the frequency of words',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='frequency',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
)

fig.write_html('first_figure.html', auto_open=True)
