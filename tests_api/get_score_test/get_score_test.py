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
r_alice_random_forest = session.get(
    "http://my_api:8000/random_forest/score", auth=HTTPBasicAuth("alice", "wonderland")
)

r_alice_gradient_boosting = session.get(
    "http://my_api:8000/gradient_boosting/score", auth=HTTPBasicAuth("alice", "wonderland")
)

r_alice_logistic_regression = session.get(
    "http://my_api:8000/logistic_regression/score", auth=HTTPBasicAuth("alice", "wonderland")
)

output = """
============================
    Get Score test
============================

request done at {route}
| username={username}
| password={password}

score = {score}

"""


# statut de la requête pour alice
score_test_random_forest = r_alice_random_forest.json()
score_test_gradient_boosting = r_alice_gradient_boosting.json()
score_test_logistic_regression = r_alice_logistic_regression.json()

# impression dans un fichier
if os.environ.get("LOG") == str(1):
    with open("logs/api_test_get_score_test.log", "a") as file:
        file.write(
            output.format(
                route = "/random_forest/score",
                username="alice",
                password="wonderland",
                score = score_test_random_forest
            )
        )
        file.write(
            output.format(
                route = "/gradient_boosting/score",
                username="alice",
                password="wonderland",
                score = score_test_gradient_boosting
            )
        )
        file.write(
            output.format(
                route = "/logistic_regression/score",
                username="alice",
                password="wonderland",
                score = score_test_logistic_regression
            )
        )
