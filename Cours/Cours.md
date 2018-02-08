# Middleware

- architecture client/serveur
- hétérogénéité: env de dev & de l'exécution

-> env complet
-> intégration de composants !=, dev & exécutés dans des env !=

- __proxy__: image locale de l'objet distant
- __squeleton__: intermédiaire entre le proxy & le serveur
- __object adapter__: côté serveur. gestion des servants (fonctionnalités): activation à la demande, réveil, destruction après un certain moment... -> stratégie côté serveur

Langage de spécification: description de fonctionnalités à l'aide d'un formalisme, pas directement un langage de programmation.

## Asynchronous Method Invocation (AMI)

ne bloque pas le thread appelant
- oneway: aller simple vers le serveur
- twoway: aller retour

Standardisation (par 1 seul industriel)

objet structuré donnant des infos sur l'état d'avancement de la requête
Appel / retour:
- begin(): méthode non bloquante
- end(): méthode de resynchronisation -> bloquante


adapter->add(object, ic->stringToIdentity("Serveur")); // étiquette l'objet

Pointeur générique (`void*`): pointe sur un objet de n'importe quel type

checkedCast: convertit le pointeur générique en l'objet de type voulu

- synchrone, asynchrone ?
- déploiement (installation, configuration, ...)

Sécurité:
- threads (accès concurrents)
- architecture côté serveur



Serveur:
1 ou pls servants (qui offrent des fonctionnalités)

locator: lien proxy-servant (routage)

requête: proxy créer un objet
serveur: créer un servant qui répond à la requête avant de le détruire


Adapteur: attaché à un communicateur
interface serveur/bus de communication

---

Application serveur 1

- Servant 1 --> Adaptateur --> Communicateur
- Servant 2 --> 

Application serveur 2

- Servant 3 --> Adaptateur --> Communicateur
- Servant 4 --> 

---

## Grid

Facturer du temps de calcul aux utilisateurs.
Machines mutualisées

Machines != ; systèmes != ; ...
-> service en continu

---

## Storm

Service de messagerie de ice

- attente de message venant du client/serveur
- plusieurs serveurs de messagerie
