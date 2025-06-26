# 📝 Mark - Éditeur de Texte Enrichi

Mark est un éditeur de texte moderne et intuitif développé en Python avec PyQt6. Il permet de créer, modifier et exporter des documents en HTML (compatible Markdown). Pensé pour une expérience fluide, il propose de nombreuses fonctionnalités utiles et une interface élégante.

---

![](ui/bg.png)

---

## 🎯 Fonctionnalités principales

### 🧰 Édition de texte
- Mise en forme : **gras**, *italique*, souligné, ~~barré~~
- Titres de niveau H1 à H4
- Citations, séparateurs, et listes à puces / numérotées / checklist
- Alignement : gauche, centre, droite, justifié
- Indentation : augmentation et diminution des retraits

### 🔗 Insertion de contenu
- **Liens** personnalisés avec texte et URL
- **Images** locales insérées avec `<img>`
- **Emojis** via une popup visuelle
- **Tableaux** simples insérés en HTML

### 📂 Gestion des fichiers
- Nouveau document (ouvre une nouvelle fenêtre)
- Ouvrir un fichier `.md` (Markdown)
- Sauvegarde automatique en `.html` enrichi
- Export possible vers d'autres formats

### 📊 Informations et statistiques
- Nom, chemin, format, taille, nombre de mots/caractères
- Langue détectée (ex : Français (France))
- Heure de dernière modification
- Statistiques de session : temps d'édition, historique court

### 🧪 Débogage & logs
- Système de logs automatique (dans `/logs`)
- Toutes les actions principales sont enregistrées
- Les logs sont horodatés et lisibles

---

## 🎨 Interface
- Interface sombre moderne (Dark mode)
- Icônes visuelles pour chaque fonction
- Boutons avec effet hover
- Popups personnalisées sans bordure pour les entrées (liens, emojis...)

---

## 🚀 Lancement de l'application

Assurez-vous d’avoir installé PyQt6 :
```bash
pip install PyQt6
````

Puis exécutez :

```bash
python main.py
```

---

## 📁 Arborescence

```
Mark/
├── main.py
├── logs/
├── ui/
│   └── icons/
├── README.md
```

---

## 📌 Remarques

* L'éditeur génère du HTML lisible par Markdown (pas besoin de conversion manuelle)
* Les fichiers enregistrés peuvent être ouverts dans n'importe quel navigateur ou éditeur Markdown
* Toutes les actions sont pensées pour imiter le comportement de Word, avec un style plus sobre

---

## 🧑‍💻 Développé par

**Arthur Songwa-Nkuiga**

Étudiant en ingénierie informatique, passionné de développement, design et productivité.
📧 [arthursongwa@gmail.com](mailto:arthursongwa@gmail.com)
