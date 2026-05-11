# AssertCode
<div align="center">
<img src="assets/logo.png" width="65%" height="">
</div>

<div align="center">

# **AssertCode**
![Django](https://img.shields.io/badge/Django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

</div>

AssertCode est une application web de génération de QR Codes personnalisés développée avec Django.  
Elle permet de générer instantanément des QR codes stylisés avec choix de couleurs, et de les télécharger facilement.

---

## 🎯 Fonctionnalités principales

- 🔗 Génération de QR Code à partir d’un lien
- 🎨 Personnalisation des couleurs (QR + fond)
- 📥 Téléchargement direct des QR générés
- ⚡ Interface rapide et responsive (Bootstrap 5)

---

## 🚀 Accès au projet

https://assertcode.hodindorian.com

---

## ⚙️ Installation en local

### 1. Cloner le projet
```bash
git clone https://github.com/ton-repo/assertcode.git
cd assertcode/src
```

### 2. Créer l’environnement virtuel
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Lancer le serveur
```bash
python manage.py runserver
```

---

## 🐳 Docker

### Build
```bash
docker compose build
```

### Run
```bash
docker compose up -d
```

---

## 🧠 Architecture

```
src/
├── assertcode_back/
├── assertcode_front/
│   ├── services/
│   ├── templates/
│   ├── static/
├── media/
├── Dockerfile
├── docker-compose.yml
└── manage.py
```

---

## 🛠️ Technologies

- Django
- Python
- qrcode / Pillow
- Bootstrap
- Docker
- Gunicorn
- WhiteNoise


## 📜 License

Projet personnel – usage éducatif et portfolio.
