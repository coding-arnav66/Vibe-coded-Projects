# Clap-Controlled Web Navigator 

A Python project that lets you control web navigation using **hand claps** as input.  
Each clap combination triggers a different action — from opening YouTube to searching Google, Reddit, or even ChatGPT.

---

## Features

- Detects claps using microphone input (`sounddevice` + `numpy`)
- Provides voice feedback using `gTTS` + `pygame`
- Opens websites automatically in your browser
- Supports multiple clap combinations for different actions

---

## 🎛 Clap Combinations

| Claps | Action |
|-------|--------|
| 1     | YouTube search (with query) |
| 2     | Open YouTube homepage |
| 3     | Open Reddit |
| 4     | Google search (with query) |
| 5     | Open GitHub |
| 6     | Open Gmail |
| 7     | Open WhatsApp Web |
| 8 + 1 | Image search (Google Images) |
| 8 + 2 | Product shopping search |
| 8 + 3 | News search |
| 8 + 4 | Wikipedia article search |
| 8 + 5 | Poki Games |
| 8 + 6 | ChatGPT |

---

## 📦 Requirements

Install dependencies with:

```bash
pip install sounddevice numpy pygame gTTS
