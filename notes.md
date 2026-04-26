# Glossaire AI Engineer

## SDK (Software Development Kit)
Boîte à outils fournie par un service pour utiliser son API 
facilement dans un langage donné.
Exemple : le SDK Groq est une surcouche Python qui parle 
à l'API Groq sous le capot.

## API (Application Programming Interface)
Le contrat d'interface entre deux systèmes.
Analogie : l'API c'est la porte, le SDK c'est la clé.

## Temperature
Contrôle créativité vs déterminisme du LLM.
- 0 = réponse déterministe et reproductible (code, juridique)
- 1 = réponse créative et variée (brainstorming, rédaction)

## Context Window
Quantité maximale de texte qu'un LLM peut traiter en une fois.
Si dépassée : le modèle tronque les messages les plus anciens.
≠ Hallucination (le modèle invente des infos qui n'existent pas)

## Function Calling / Tool Use
Mécanisme par lequel le LLM décide quel outil appeler 
et avec quels arguments. C'est ton code qui exécute 
réellement la fonction — le LLM est le cerveau, 
ton code est le bras.

## Zero-shot
Appel au LLM sans exemple. Pour tâches simples.
Exemple prod : classifier un email spam/non-spam.

## Few-shot
Appel au LLM avec exemples dans le prompt. 
Pour format précis attendu.
Exemple prod : extraire des données structurées 
d'un texte juridique.

## Chain of Thought
Demander au LLM de raisonner étape par étape.
Pour raisonnements complexes.
Exemple prod : calcul de prix avec TVA, remises, 
conditions multiples.