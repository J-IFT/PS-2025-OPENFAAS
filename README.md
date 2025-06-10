# PS-2025-OPENFAAS

*PS = Projet Scolaire*

## 📚 Projet Scolaire | TP OPENFAAS

Juin 2025

Groupe : Juliette

### 📌 Consignes du projet :

Ce projet combine deux travaux pratiques autour du développement et déploiement d'applications serverless avec OpenFaaS sur Kubernetes :
TP 1 : Application Serverless de Base
Objectif : Développer une application serverless composée de deux fonctions déployées avec OpenFaaS.
Fonctions à implémenter :

get-quote : Fonction HTTP GET retournant aléatoirement une citation depuis un tableau statique
save-feedback : Fonction HTTP POST sauvegardant un message dans Redis avec timestamp

Compétences ciblées :

Déploiement d'OpenFaaS sur Kubernetes
Développement de fonctions Python serverless
Intégration avec Redis
Supervision avec Prometheus

TP 2 : Chaîne de Traitement Automatisée
Objectif : Créer une chaîne de traitement de commandes e-commerce pour DataRetailX avec architecture événementielle.
Fonctions à implémenter :

daily-fetcher : Planification CRON quotidienne (8h) publiant sur NATS
file-transformer : Traitement de fichiers CSV via SFTP avec transformations métier
status-checker : API HTTP de vérification du statut des traitements

Compétences ciblées :

Déclencheurs multiples (HTTP, CRON, NATS)
Intégration SFTP et traitement de fichiers
Architecture événementielle distribuée# Projet OpenFaaS sur Kubernetes

## 📋 Résumé des consignes

Ce projet combine deux travaux pratiques autour du développement et déploiement d'applications serverless avec OpenFaaS sur Kubernetes :

### TP 1 :
**Objectif :** Développer une application serverless composée de deux fonctions déployées avec OpenFaaS.

**Fonctions à implémenter :**
- **`get-quote`** : Fonction HTTP GET retournant aléatoirement une citation depuis un tableau statique
- **`save-feedback`** : Fonction HTTP POST sauvegardant un message dans Redis avec timestamp

**Compétences ciblées :**
- Déploiement d'OpenFaaS sur Kubernetes
- Développement de fonctions Python serverless
- Intégration avec Redis
- Supervision avec Prometheus

### TP 2 :
**Objectif :** Créer une chaîne de traitement de commandes e-commerce pour DataRetailX avec architecture événementielle.

**Fonctions à implémenter :**
- **`daily-fetcher`** : Planification CRON quotidienne (8h) publiant sur NATS
- **`file-transformer`** : Traitement de fichiers CSV via SFTP avec transformations métier
- **`status-checker`** : API HTTP de vérification du statut des traitements

**Compétences ciblées :**
- Déclencheurs multiples (HTTP, CRON, NATS)
- Intégration SFTP et traitement de fichiers
- Architecture événementielle distribuée

### 🐱 Mon projet :

#### 🎯 Fonctions TP1
- ✅ **get-quote** : Service de citations aléatoires
  - Template Python OpenFaaS
  - 5 citations prédéfinies
  - Endpoint HTTP GET
  
- ✅ **save-feedback** : Sauvegarde de commentaires
  - Intégration Redis
  - Stockage avec timestamp
  - Endpoint HTTP POST JSON

#### 🔄 Fonctions TP2
- ✅ **daily-fetcher** : Déclencheur planifié
  - Configuration CRON (8h quotidien)
  - Publication NATS sur `orders.import`
  - Payload JSON avec date courante

- ✅ **file-transformer** : Processeur de commandes
  - Abonnement NATS `orders.import`
  - Connexion SFTP sécurisée
  - Transformations CSV :
    - `customers` → upperCase
    - `product` → lowerCase
    - Ajout `Processed-Date` (datetime)
    - Ajout `process_by` (identifiant)

- ✅ **status-checker** : Monitoring des traitements
  - API HTTP de statut
  - Comptage fichiers SFTP `/USX/depot`
  - Retour JSON du nombre de fichiers traités

### 💻 Applications et langages utilisés :

+ Visual studio code, Docker Desktop
+ Docker, Kubernetes, OpenFaas, Python...

## 🌸 Merci !
© J-IFT
