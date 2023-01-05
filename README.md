# Test très simple de redpanda

## Introduction

L'objectif est de :
- mettre en place un docker redpanda.
- créer un consommateur (python) de message dans un topic
- créer un producteur (python) de message dans un topic

Le topic : user_signups

le port d'écoute de redpanda : localhost:9092

## Installer les pré-requis
- le fichier redpanda.yml
- le module python
- créer les deux programmes python : producteur.py et consommateur.py

## Quelques commandes utiles
```
docker exec -it redpanda-1 bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Names}}"
rpk topic list
rpk group list
rpk topic consume user_signups
rpk topic consume -n 1 user_signups
```

