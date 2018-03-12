# Middleware

- architecture client/serveur
- hétérogénéité: env de dev & d'exécution

## Interopérabilité

Capacité que possède un produit ou un système, dont les interfaces sont intégralement connues, à fonctionner avec d’autres produits ou systèmes existants ou futurs et ce sans restriction d’accès ou de mise en œuvre.

Il convient de distinguer __interopérabilité__ et __compatibilité__. On peut dire qu’il y a __compatibilité__ quand deux produits, systèmes ou organisation peuvent fonctionner ensemble et __interopérabilité__ quand chacun peut savoir pourquoi et comment. On ne peut donc parler d’interopérabilité d’un produit, d’un système ou d’une organisation que si on en connaît intégralement toutes ses interfaces, sans restriction d’accès ou de mise en œuvre.

---

-> env complet
-> intégration de composants !=, dev & exécutés dans des env !=

---

- __proxy__: image locale de l'objet distant (généré côté client)
	- produit à partir des définitions slice
	- inclut les fonctions de *marshalling*: sérialisation de structure de données complexes
- __squeleton__: intermédiaire entre le proxy & le serveur (généré côté serveur)
	- produit à partir des définitions slice
	- inclut aussi les fonctions de *marshalling*
- __object adapter__: côté serveur. 
	- responsable de l'*activation*: lien entre une requête et l'objet qui s'en charge
	- gestion des servants (Active Servant Map [ASM]) (fonctionnalités): activation à la demande, réveil, destruction après un certain moment... -> stratégie côté serveur. 
	- Génère les références (les proxy).

Langage de spécification: description de fonctionnalités à l'aide d'un formalisme, pas directement un langage de programmation.

---

Standardisation (par 1 seul industriel)

---

## Asynchronous Method Invocation (AMI)

Ne bloque pas le thread appelant
(Le serveur ne connait pas le mode d'invocation)

- oneway: aller simple vers le serveur
- twoway: aller retour (par défaut)

Objet structuré donnant des infos sur l'état d'avancement de la requête et les acteurs
Dissocie appel / retour
- begin(): méthode non bloquante
- end(): méthode de resynchronisation -> bloquante

(impossible en CORBA)

Ex:

begin_prepareTruc(); // appel non bloquant
...
end_getTruc(); // appel bloquant

---

Côté proxy: classe *AsyncResultPtr*

Encapsule les informations liées au processus asynchrone
+ Gestion d'une collection de requêtes en cours

Les requêtes sont empilées dans un buffer en attendant le transport... ces méthodes informent sur le dépilement de la requête

adapter->add(object, ic->stringToIdentity("Serveur")); // étiquette l'objet

Pointeur générique (`void*`): pointe sur un objet de n'importe quel type

checkedCast: convertit le pointeur générique en l'objet de type voulu

- synchrone, asynchrone ?
- déploiement (installation, configuration, ...)

Sécurité:
- threads (accès concurrents)
- architecture côté serveur


---

## Threads

Par défaut Ice: multithread (couche d'abstraction spécifique)

__Thread:__ processus léger hébergé dans un processus lourd. Il possède:
- pile d'exécution
- identifiant de thread
- pointeur d'instructions

Les threads issus d'un même processus partagent:
- code
- mémoire
- droits (unix)
- environnement (shell, répertoire de travail)

__Multithreading en Ice (package IceUtil):__
- gestion de la concurrence d'accès
- gestion des threads (création, suppression, contrôle, ...)

__Concurrence d'accès:__
- 1 thread par invocation
- problème: accès concurrent à une ressource critique:
	- drapeaux de verrouillage des sections critiques
	- mutex, remutex: exclusion mutuelle, récursive
	- Monitor, Gond: exclusions conditionnelles

__Thread Pools:__
__communicator:__ gestionnaire de canaux de communication (côté serveur ET client)
Gère 2 paquets de threads: client & server thread pool
Tous les adaptateurs d'un même communicator partagent ces pools


---

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

Calcul parallèle
exploitation de ressources de calcul

- découverte de nouvelles ressources
- découplage client/serveur
- équilibrage de charge
- réplciation de serveurs
- stratégies d'activation
- outils d'administration


---

## Storm

Service de messagerie de ice

- attente de message venant du client/serveur
- plusieurs serveurs de messagerie
