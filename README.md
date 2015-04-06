# protopeter
minimal twitter-like thingie using a distributed hash table (prototype)

## demo

run separately

```
$ ./protopeter.py
Which port should I listen on? 2000
generating keys...
I'm the first node. Connect to me!
Choose a username: axel
['status', 'edit', 'lookup', 'help', 'quit']
> edit
nick: Axel
bio: floating around~
website: http://example.org
> status
text: Hi! This is my first status update.
59c6620b-cbd0-485e-8bc8-b6868ebf0ee4
> status
text: Hi! This is my second status update.
42b3ecaf-9e77-4291-9035-88238fd00e95
>
```

```
$ ./protopeter.py localhost 2000
Which port should I listen on? 2001
generating keys...
bootstrapping...
Choose a username: bernd
['status', 'edit', 'lookup', 'help', 'quit']
> lookup
username or status id: axel
{u'content': u'{"website": "http://example.org", "nick": "Axel", "last_status": "42b3ecaf-9e77-4291-9035-88238fd00e95", "bio": "floating around~"}',
 u'key': u'B011yLwqVU3b04r5chIqYMJqoVoNEPO+neABZxfPOoQ=',
 u'signature': u'JdaecXDdD7rTZ2a5GOl0cZu6GQdwJUDP5PBaxMB9OSJv4NNtUg5k8NEufKvqba7d1GTnaNCU8itHaA55oVVDAXsid2Vic2l0ZSI6ICJodHRwOi8vZXhhbXBsZS5vcmciLCAibmljayI6ICJBeGVsIiwgImxhc3Rfc3RhdHVzIjogIjQyYjNlY2FmLTllNzctNDI5MS05MDM1LTg4MjM4ZmQwMGU5NSIsICJiaW8iOiAiZmxvYXRpbmcgYXJvdW5kfiJ9'}
> lookup
username or status id: 42b3ecaf-9e77-4291-9035-88238fd00e95
{u'content': u'{"text": "Hi! This is my second status update.", "previous_status": "59c6620b-cbd0-485e-8bc8-b6868ebf0ee4", "author": "axel"}',
 u'key': u'B011yLwqVU3b04r5chIqYMJqoVoNEPO+neABZxfPOoQ=',
 u'signature': u'PMH8fVvtE3HabVjJd3yUUH9VtivgLVtxp1liZvFpxt8u/4tk5Ojr2pDi1P34lj6lW7sEZ1fSs1UOCUd4satrCHsidGV4dCI6ICJIaSEgVGhpcyBpcyBteSBzZWNvbmQiLCAicHJldmlvdXNfc3RhdHVzIjogIjU5YzY2MjBiLWNiZDAtNDg1ZS04YmM4LWI2ODY4ZWJmMGVlNCIsICJhdXRob3IiOiAiYXhlbCJ9'}
>
```
