<!--
Contributing V0.1
-->

# Contributing
Pull Requests setzen voraus, dass wir uns an die Wiki vereinbarten Regeln halten. 

Wir verwenden Issues in GitHub und setzen, wenn wir das Issue bearbeiten auf "in progress".


## Branching model

Unser Hauptentwicklungszweig ist `develop`.
Der Zweig `master` enthält die aktuell "stabile" Version des Tutorials.


## Development flow

- **Fork** Python-Tutorial on GitHub
- Klone deinen fork:

```
git clone git@github.com/<username>/Python-Tutorial
```

- Optional kann noch das Original-Repository als Remote eingefügt werden, um so aktuelle Änderungen abrufen zukönnen.

```
git remote add upstream git@github.com:Informatik-HS-KL/Python-Tutorial.git
```

- Erstelle einen  Feature-Branch:

```
git checkout -b feature/<kurze Beschreibung>
```

- Füge deine Änderungen ein und schiebe sie auf **dein** Repository:

```
git push origin <Feature-Branch>
```

- Erstelle einen  Pull-Request gegen den `develop`  vom <Informatik-HS-KL/Python-Tutorial> Repository. 

Der Pull-Request wird dann überprüft.
Nach dem erstellen des Pull-Requests können durch pushen auf den eigenen Feature-Branch  weiterhin Commits hinzugefügt werden. 

- Wenn man während des Pull-Request Reviews an anderen Stellen weiterarbieten möchte, sollte ein neuer Branch erstellt werden! 
