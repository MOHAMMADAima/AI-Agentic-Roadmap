# Interview Prep — Questions & Réponses

## J-2 — Fondamentaux LLM

**Q : À quoi sert le paramètre `temperature` ?**
Contrôle créativité vs déterminisme.
- 0 = déterministe, reproductible (code, juridique, médical)
- 1 = créatif, varié (brainstorming, rédaction)
≠ précision — c'est créativité vs prévisibilité.

**Q : Différence entre rôle `system` et rôle `user` ?**
- `system` = définit le comportement et les contraintes du LLM. 
  Écrit par le développeur.
- `user` = message de l'utilisateur final.

**Q : Pourquoi mettre la clé API dans `.env` ?**
Sécurité. Une clé dans le code pushé sur GitHub public 
est accessible à tous. Le `.env` est exclu via `.gitignore`.

---

## J-3 — SDK, API, Function Calling

**Q : C'est quoi un client SDK ?**
Instance du SDK — objet Python qui encapsule l'auth, 
la construction des requêtes HTTP et la gestion des erreurs.
On ne réécrit pas `requests.post(...)` à la main — 
le SDK le fait pour toi.

**Q : Différence API vs SDK ?**
- API = le contrat d'interface entre deux systèmes. La porte.
- SDK = Software Development Kit. La boîte à outils 
  fournie pour utiliser l'API facilement. La clé.
Analogie : l'API c'est la porte, le SDK c'est la clé toute faite.

**Q : Zero-shot vs Few-shot vs Chain of Thought ?**
- Zero-shot = pas d'exemple. Pour tâches simples.
  Exemple prod : classifier un email spam/non-spam.
- Few-shot = avec exemples dans le prompt. Pour format précis.
  Exemple prod : extraire données structurées d'un texte juridique.
- Chain of thought = raisonnement étape par étape. Pour complexité.
  Exemple prod : calcul de prix avec TVA, remises, conditions multiples.

**Q : Rôle du LLM dans le function calling ?**
Le LLM décide quel outil appeler et avec quels arguments.
C'est le code Python qui exécute réellement la fonction.
LLM = le cerveau. Ton code = le bras.

**Q : `tool_choice="auto"` vs `tool_choice="none"` ?**
- auto = le LLM décide seul s'il appelle un outil
- none = le développeur force le LLM à ne jamais 
  appeler d'outil. Réponse en texte uniquement.
- required = force le LLM à toujours utiliser un outil.

---

## J-4 — Agent, Tool Call, Sécurité

**Q : Pourquoi un deuxième appel API après l'outil ?**
Le LLM a besoin de voir le résultat de l'outil pour formuler 
une réponse en langage naturel.
Sans ça : il sait qu'il a appelé l'outil mais ne connaît 
pas le résultat — il ne peut pas répondre à l'utilisateur.

**Q : Rôle du `tool_call_id` ?**
Associe le résultat d'un outil à l'appel spécifique 
qui l'a demandé. Crucial quand le LLM appelle plusieurs 
outils en parallèle — sans cet ID, le LLM ne saurait pas 
quel résultat correspond à quel appel.
= Mécanisme de traçabilité, pas de sélection.

**Q : Pourquoi `eval()` est dangereux en production ?**
`eval()` exécute n'importe quel code Python.
Un utilisateur malveillant peut injecter du code système :
`eval("__import__('os').system('rm -rf /')")`
= Faille de sécurité critique. Jamais en prod.

**Correction : utiliser `ast.literal_eval()`**
```python
import ast
def calculate(expression):
    try:
        return str(ast.literal_eval(expression))
    except:
        return "Expression invalide"
```
`ast` évalue uniquement des expressions mathématiques
sans exécuter de code arbitraire.