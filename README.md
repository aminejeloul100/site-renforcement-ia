# Site — Renforcement des compétences en IA (enseignants)

Site avec connexion obligatoire. La page d'accueil présente un résumé du
rapport (une carte par chapitre avec icône), une vidéo d'introduction pour
ceux qui préfèrent regarder plutôt que lire, et un bouton pour télécharger
le rapport complet en PDF.

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Structure

```
site_renforcement_ia/
├── app.py           # connexion + page d'accueil
├── auth.py          # inscription / connexion (comptes stockés localement)
├── contenu.py        # texte des cartes + lien de la vidéo
├── requirements.txt
└── data/
    ├── users.json                                  # créé automatiquement
    └── Renforcement_competences_enseignants_IA_v2.pdf  # rapport complet, déjà inclus
```

## Personnaliser

- **Changer la vidéo** : modifie `VIDEO_URL` dans `contenu.py` (accepte tout lien YouTube)
- **Modifier les textes des chapitres** : édite la liste `CHAPITRES` dans `contenu.py`
- **Remplacer le PDF** : mets ton propre fichier dans `data/` et ajuste `PDF_PATH` dans `app.py` si le nom change

## Limite

Pas d'images photo dans ce prototype (pour rester dans le cadre du droit
d'auteur, aucune image trouvée sur internet n'est réutilisée sans licence) —
seulement des icônes emoji et la vidéo intégrée. Si tu as tes propres
images libres de droit, je peux t'aider à les intégrer.
