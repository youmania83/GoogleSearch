try:
    from googlesearch import search
except ImportError:
    print("no Module Found")

query="salons in Gurgaon"
with open('xyz.txt', 'w') as textfile:
  for i in search(query,tld="com",num=10,stop=100,pause=2):
    outp = i + "\n"
    textfile.write(outp)