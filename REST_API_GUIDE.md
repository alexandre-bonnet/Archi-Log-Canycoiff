# Guide REST API - ArchiLog

Ce guide documente la migration de votre application vers une architecture REST avec JSON et JavaScript côté client.

## 🚀 Démarrage du serveur

```bash
$env:FLASK_APP = "main.py"
$env:FLASK_ENV = "development"
flask run
```

Le serveur démarre sur `http://127.0.0.1:5000`

## 📋 Architecture

### Endpoints disponibles

#### Authentification
- **POST `/api/login`** - Connexion utilisateur
- **POST `/api/logout`** - Déconnexion (efface la session)

#### Utilisateurs
- **POST `/api/users`** - Créer un compte utilisateur

#### Clients
- **POST `/api/clients`** - Enregistrer les informations du client (nom, téléphone)

#### Chiens
- **GET `/api/dogs`** - Lister tous les chiens de l'utilisateur
- **POST `/api/dogs`** - Ajouter un chien (accepte JSON ou multipart form-data)

#### Sorties
- **GET `/api/sorties`** - Lister toutes les sorties de l'utilisateur
- **POST `/api/sorties`** - Ajouter une sortie

---

## 📚 Exemples d'utilisation

### 1. Créer un compte
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"user":"alice","password":"pwd123"}' \
  http://127.0.0.1:5000/api/users
```

**Réponse succès (200):**
```json
{"code": 200, "message": "Account created !"}
```

---

### 2. Connexion
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"user":"alice","password":"pwd123"}' \
  http://127.0.0.1:5000/api/login
```

**Réponse succès (201):**
```json
{"code": 201, "message": "Welcome to your account !", "user_id": 1}
```

> **Note:** La session est stockée via un cookie HTTP (géré automatiquement par le navigateur)

---

### 3. Enregistrer les infos client
```javascript
fetch('/api/clients', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({name: "Alice Dupont", number: "0612345678"}),
  credentials: 'same-origin'
})
.then(r => r.json())
.then(data => console.log(data))
```

---

### 4. Lister les chiens
```javascript
fetch('/api/dogs', {credentials: 'same-origin'})
  .then(r => r.json())
  .then(data => console.log(data.dogs))
```

**Réponse:**
```json
{
  "dogs": [
    {"Nom": "Rex", "Race": "Labrador", "Photo": "rex.jpg", "id": 1},
    {"Nom": "Luna", "Race": "Golden", "Photo": "luna.jpg", "id": 2}
  ]
}
```

---

### 5. Ajouter un chien (avec upload fichier)
```javascript
const fd = new FormData();
fd.append('nom', 'Rex');
fd.append('race', 'Labrador');
fd.append('photo', fileInput.files[0]);  // élément <input type="file">

fetch('/api/dogs', {
  method: 'POST',
  body: fd,
  credentials: 'same-origin'
})
.then(r => r.json())
.then(data => console.log(data.message))
```

---

### 6. Ajouter une sortie
```javascript
fetch('/api/sorties', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    date_sortie: "2026-07-15",
    chien_id: 1
  }),
  credentials: 'same-origin'
})
.then(r => r.json())
.then(data => console.log(data.message))
```

---

## 🔐 Authentification

- **Session basée sur cookie**: Chaque requête inclut automatiquement la session via `credentials: 'same-origin'`
- **Endpoints sécurisés**: Les endpoints `/api/clients`, `/api/dogs`, `/api/sorties` requièrent une session active
- **Erreur 401**: Si l'utilisateur n'est pas authentifié

```javascript
// Exemple réponse 401
{
  "error": "Authentication required"
}
```

---

## 🎨 Pages modifiées

Toutes les pages utilisent maintenant les endpoints REST en JavaScript :

| Page | Endpoint | Action |
|------|----------|--------|
| `connexion.html` | POST `/api/login` | Login AJAX → redirection `/espaceperso` |
| `createAcount.html` | POST `/api/users` | Create account AJAX → affiche message |
| `clientInformation.html` | POST `/api/clients` | Register info AJAX → redirection `/espaceperso` |
| `espaceperso.html` | GET/POST `/api/dogs` | Charge et ajoute chiens AJAX |
| `sortie.html` | GET/POST `/api/sorties` | Charge et ajoute sorties AJAX |

---

## 📂 Structure des fichiers

```
ArchiLog/
├── main.py                           # Flask app + endpoints REST
├── Models/
│   ├── chienModel.py
│   ├── sortieModel.py
│   └── userModel.py
├── Services/
│   ├── chienServices.py
│   ├── sortieServices.py
│   └── userServices.py
├── templates/
│   ├── connexion.html                 # ✅ Mise à jour: fetch /api/login
│   ├── createAcount.html              # ✅ Mise à jour: fetch /api/users
│   ├── clientInformation.html         # ✅ Mise à jour: fetch /api/clients
│   ├── espaceperso.html               # ✅ Mise à jour: fetch /api/dogs
│   ├── sortie.html                    # ✅ Mise à jour: fetch /api/sorties
│   └── ...
└── static/
    ├── style.css
    └── ...
```

---

## 🐛 Sécurité

- **Noms de fichiers**: Utilise `secure_filename()` pour nettoyer les uploads
- **JSON parsing**: Force le parsing JSON avec `silent=True` pour éviter les crashs
- **Session/Cookie**: Stockage côté serveur avec clé secrète `CanycoiffAdmin123`

---

## ✅ Codes HTTP de réponse

| Code | Signification |
|------|---------------|
| 200 | Account created |
| 201 | Welcome / Client registered / Dog added |
| 202 | Dog added (API) |
| 203 | Date valid (sortie) |
| 204 | Dog added to sortie |
| 205 | New sortie created |
| 400 | Username already in use |
| 401 | Auth required / Username too long |
| 402 | Username not found |
| 403 | Password wrong |
| 405 | Name too long |
| 407 | Date has passed |
| 408 | Date too far in future |

---

## 🔗 Fallback serveur

Les pages conservent le rendu serveur comme fallback :
- Les formulaires continuent de fonctionner même si JavaScript échoue
- Le JS intercepte simplement les soumissions pour une UX plus fluide
- Les redirections et messages de succès fonctionnent côté client

---

## 📝 Notes

- Les cookies de session sont **HttpOnly** par défaut (plus sûr)
- Chaque utilisateur a son propre contexte via `session['user_id']`
- Les uploads de photos sont nettoyés automatiquement avec `secure_filename`
- Pour les requêtes cross-site, envisager l'ajout de tokens CSRF

