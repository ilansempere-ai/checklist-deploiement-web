# Web Deploy Check

Un petit outil pour vérifier qu'une page web répond après un déploiement.
Il suit les redirections et vérifie le statut HTTP de la réponse finale.
Tu peux aussi vérifier la présence d'un texte attendu, comme le titre de la page,
pour repérer une page d'erreur qui renverrait quand même un statut 200.

## Utilisation

Python 3 est nécessaire. Aucune dépendance à installer.

```sh
python3 check.py https://example.com --contains "Example Domain"
```

Le statut attendu est 200 par défaut. Pour vérifier une page 404,
ajoute `--status 404`. L'option `--contains` cherche dans le premier
mébioctet de la réponse. Le script renvoie 0 si la vérification réussit
et 1 si le site ne répond pas ou si la réponse diffère de celle attendue.

## Licence

MIT.
