import os
import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

# définition de l'adresse de l'API
api_address = "my_api"
# port de l'API
api_port = 8000


# requêtes
r_alice = session.get(
    "http://my_api:8000/random_forest/score", auth=HTTPBasicAuth("alice", "wonderland")
)

r_andre = session.get(
    "http://my_api:8000/random_forest/score",
    auth=HTTPBasicAuth("andre", "ehouman"),
)

output = """
============================
    Authentication test
============================

request done at "/random_forest/score"
| username={username}
| password={password}

expected result = {expected_result}
actual restult = {status_code}

==>  {test_status}

"""


# statut de la requête pour alice
status_code_alice = r_alice.status_code

# affichage des résultats
if status_code_alice == 200:
    test_status_alice = "SUCCESS"
else:
    test_status_alice = "FAILURE"


# statut de la requête pour clementine
status_code_andre = r_andre.status_code

# affichage des résultats
if status_code_andre == 401:
    test_status_andre = "SUCCESS"
else:
    test_status_andre = "FAILURE"


# impression dans un fichier
if os.environ.get("LOG") == str(1):
    with open("logs/api_test_authorization.log", "a") as file:
        file.write(
            output.format(
                username="alice",
                password="wonderland",
                expected_result=200,
                status_code=status_code_alice,
                test_status=test_status_alice,
            )
        )
        file.write(
            output.format(
                username="andre",
                password="ehouman",
                expected_result=401,
                status_code=status_code_andre,
                test_status=test_status_andre,
            )
        )
