# 🌍 Automatic Language Translation System with User Feedback

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.x-lightgrey)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A web application that provides real-time language translation (English, French, Spanish, German) while learning from user corrections to improve accuracy.


## ✨ Features

- **AI-Powered Translations** using Hugging Face MarianMT
- **User Feedback System** (correct translations + 5-star ratings)
- **Translation History** with timestamps
- **Active Learning** - Improves based on user input

## 🛠 Tech Stack

| Component       | Technology |
|----------------|------------|
| Frontend       | HTML5, CSS, Bootstrap |
| Backend        | Python Flask |
| AI Model       | Hugging Face Transformers (MarianMT) |
| Database       | SQLite (Flask-SQLAlchemy) |
| Deployment     | Docker (Optional) |


### Prerequisites
- Python 3.8+
- pip package manager

### Steps
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/translation-system.git
   cd translation-system
