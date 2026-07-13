# ⏳ Countdown Timer

A simple, interactive countdown timer application built with **Streamlit** and **Python**.

---

## 📋 About This Project

This is my first Git repository! It contains a beginner-friendly countdown timer that displays a real-time countdown with hours, minutes, and seconds. The timer provides a clean, user-friendly interface with visual feedback.

**Author**: [@Mynk.rth](https://github.com/mynk-rth)

---

## ✨ Features

- ⏱️ **Customizable countdown** - Enter any duration in seconds
- 📊 **Real-time display** - Shows time in `HH:MM:SS` format with large, easy-to-read text
- 🎉 **Completion notification** - Visual celebration and toast message when timer finishes
- 🎨 **Clean UI** - Built with Streamlit for a modern, responsive interface
- 🔄 **Auto-reset** - Ready to use again immediately after completion

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mynk-rth/Firstgit.git
   cd Firstgit
   ```

2. **Install required dependencies**:
   ```bash
   pip install streamlit
   ```

### Running the Application

Start the countdown timer with:
```bash
streamlit run Timer.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 📖 How to Use

1. Open the application
2. Enter the desired countdown duration in **seconds** using the number input field
   - Default: 10 seconds
   - Minimum: 1 second
   - Step increment: 10 seconds
3. Click the **"Start Timer"** button to begin the countdown
4. Watch the real-time countdown in the dialog box
5. When the timer reaches zero, you'll see a celebration message 🎉

---

## 🛠️ Technologies Used

- **Python 3** - Programming language
- **Streamlit** - Web app framework for rapid UI development
- **Time module** - For timing functionality

---

## 📁 Project Structure

```
Firstgit/
├── README.md          # This file
├── Timer.py           # Main countdown timer application
└── .gitignore         # (Optional) Git ignore rules
```

---

## 💡 Code Overview

**Timer.py** includes:
- Input field to set countdown duration
- Session state management to track timer completion
- `@st.dialog` popup for the countdown display
- Time conversion logic (seconds to HH:MM:SS format)
- Completion message and notification with auto-reset

---

## 🎓 Learning Purpose

This project demonstrates:
- Basic Python scripting
- Streamlit app development
- Using Git for version control
- State management in Streamlit applications
- HTML styling within Streamlit

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests with improvements!

---

## 📝 License

This project is open source and available for educational purposes.

---

## 📧 Connect

If you have any questions or suggestions, feel free to reach out!

**Happy coding!** 😊
