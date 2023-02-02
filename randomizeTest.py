import unittest
import json
import random
from flask import Flask, request
from flask_testing import TestCase

# Définition de la classe pour tester la génération de nombres aléatoires
class RandomizeTestCase(TestCase):

    # Définition de la méthode pour tester la génération de nombres aléatoires sans bornes
    def test_randomize(self):
        # Envoi d'une requête GET à la route "/myMath/randomize"
        response = self.client.get("/myMath/randomize")
        # Vérification du code de statut de la réponse (devrait être 200 pour "Succès")
        self.assertEqual(response.status_code, 200)
        # Décodage de la réponse en format JSON
        result = json.loads(response.data.decode("utf-8"))
        # Vérification de la présence du champ "result" dans le dictionnaire
        self.assertIn("result", result)
        # Vérification que la valeur du champ "result" se trouve bien entre les bornes inférieure et supérieure (0 et 100 par défaut)
        self.assertGreaterEqual(result["result"], 0)
        self.assertLessEqual(result["result"], 100)

    def test_randomize_with_bounds(self):
        # Définition des bornes inférieure et supérieure pour la génération aléatoire
        lower_bound = 10
        upper_bound = 20

        # Envoi d'une requête HTTP GET pour la génération aléatoire en utilisant les bornes définies
        response = self.client.get("/myMath/randomize?lower_bound={}&upper_bound={}".format(lower_bound, upper_bound))

        # Vérification que la réponse reçue a un statut HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Décodage des données de la réponse pour obtenir un dictionnaire Python
        result = json.loads(response.data.decode("utf-8"))

        # Vérification que le dictionnaire reçu contient une clé "result"
        self.assertIn("result", result)

        # Vérification que la valeur associée à la clé "result" est supérieure ou égale à la borne inférieure
        # et inférieure ou égale à la borne supérieure
        self.assertGreaterEqual(result["result"], lower_bound)
        self.assertLessEqual(result["result"], upper_bound)

    if __name__ == "__main__":
        unittest.main()