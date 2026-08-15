# Python Projects Collection 🐍✨

A collection of four interactive Python projects showcasing automation, GUI dashboards, and computer vision.  
Each project is self-contained but follows a clean structure with documentation and requirements.

---

## 📂 Projects

### 1. Clap-Controlled Web Navigator 👏🌐
Control your browser using **hand claps** detected via microphone.

- **Features:**
  - Clap once → YouTube search
  - Clap twice → YouTube homepage
  - Clap thrice → Reddit
  - Clap 4 → Google search
  - Clap 5 → GitHub
  - Clap 6 → Gmail
  - Clap 7 → WhatsApp Web
  - Clap 8 + extra claps → Image search, Shopping, News, Wikipedia, Games, ChatGPT

- **Dependencies:** `sounddevice`, `numpy`, `pygame`, `gTTS`

---

### 2. Interactive Dictionary 📖🔍
Look up word meanings, synonyms, and examples using APIs or scraping.

- **Features:**
  - Static dictionary mode
  - API lookup (Wordnik, Free Dictionary API)
  - Web scraping fallback (Vocabulary.com)

- **Dependencies:** `requests`, `beautifulsoup4`

---

### 3. Mini Tech Dashboard 🖥️📊
A Tkinter-based dashboard showing latest **Dev.to articles**, **Hacker News stories**, and **GitHub repos**.

- **Features:**
  - Tabbed interface with clickable links
  - Bar chart of top GitHub repos by stars
  - Scrollable list of repositories
  - Refresh button for live updates

- **Dependencies:** `requests`, `matplotlib`

---

### 4. Nose-Controlled Mouse 🖱️👃
Control your mouse pointer using **nose movements** detected via webcam.

- **Features:**
  - Tracks nose tip with FaceMesh (`cvzone`)
  - Cursor moves with **super-high sensitivity**
  - Inverted horizontal movement (right ↔ left)
  - Cursor freezes when mouth is open

- **Dependencies:** `cvzone`, `opencv-python`, `pyautogui`

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/username/python-projects.git
cd python-projects
pip install -r requirements.txt
