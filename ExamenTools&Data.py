# Opdracht:

# Bepalingen:
#  - Je moet gebruik maken van de aangeleverde variable(n)
#  - Je mag deze variable(n) niet aanpassen
#  - Het is de bedoeling dat je op het einde 1 programma hebt
#  - Als inlever formaat wordt een public git url verwacht die gecloned kan worden

# / 5 ptn 1 - Maak een public repository aan op jouw gitlab/github account voor dit project
# /10 ptn 2 - Gebruik python om de gegeven joke_url aan te spreken
# /10 ptn 3 - Gebruik regex om de volgende data te extracten:
#             - De eerste 20 tekens van de joke
# /15 ptn 4 - Verzamel onderstaande data en output alles als yaml. Een voorbeeld vind je hieronder.
# /10 ptn 5 - Doe een post naar de post_url.
#             - Stuur in de post een parameter genaamd "naam" mee met als waarde jouw voornaam
#             - Output het hele antwoord naar de terminal
#             - Haal uit het antwoord van de call jouw ip adres (origin) en geef dit weer met een f string

# Totaal  /50ptn
# """

# """ voorbeeld yaml output
# jokes:
#   - intro: <met regex extracted intro>
#     joke: <joke>
#     id: <joke id>
#   - .. <tot aantal jokes bereikt is>

joke_url = "https://icanhazdadjoke.com"
amount_of_jokes = 5

# https://httpbin.org/#/HTTP_Methods/post_post
post_url = "https://httpbin.org/post"



import requests 
import re 
import yaml

joke_get = requests.get(joke_url, headers={"Accept": "application/json"})

joke_intro =  r"(?P<intro>.{20})"

joke = joke_get.json()

output = {
     "jokes": joke_intro,
          "- intro": "" ,
            "joke": joke["joke"],
            "id": joke["id"]
                           }

    
print(yaml.dump(output))

    
post = requests.post(post_url, params={"Naam": "Bjorn"})
post_response = post.json()
origin = post_response["origin"]

print(post_response)
print(f"Je IP-adres is {origin}")
