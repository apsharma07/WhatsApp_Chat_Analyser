# WhatsApp Chat Analyzer

## 📌 Overview

The **WhatsApp Chat Analyzer** is a Python-based tool that processes and analyzes WhatsApp chat data. It provides insights such as:

- Message statistics
- Most active users
- Word cloud visualization
- Commonly used words
- Emoji analysis
- Monthly & daily activity trends
- Weekly and hourly heatmaps

## 🚀 Features

- **Total Messages & Words Count**: Get the number of messages and words exchanged.
- **Media & Links Shared**: Identify media files and URLs shared in the chat.
- **Most Active Users**: Find out who sends the most messages.
- **Word Cloud Generation**: Visualize frequently used words.
- **Emoji Analysis**: Detect and count emojis used.
- **Time-Based Analysis**:
  - Daily & Monthly Message Trends
  - Weekly Activity Trends
  - Heatmap of Active Hours

## 🛠 Installation & Setup

### 1️⃣ Prerequisites

Ensure you have **Python 3.x** installed on your system. Install dependencies using:

```sh
pip install pandas wordcloud emoji urlextract matplotlib seaborn streamlit
```

### 2️⃣ Download the Project

Clone the repository or download the project files:

```sh
git clone https://github.com/your-repo/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis
```

### 3️⃣ Run the Application

```sh
streamlit run app.py
```

## 📂 File Structure

```
whatsapp-chat-analysis/
│── app.py             # Main Streamlit app
│── preprocessor.py    # Chat data preprocessing
│── helper.py          # Statistical and visualization functions
│── stop_hinglish.txt  # Stop words file for better analysis
│── README.md          # Project Documentation
```

## 📊 How to Use

### 1️⃣ Export WhatsApp Chat Data

1. Open WhatsApp.
2. Go to the chat you want to analyze.
3. Click on **More > Export Chat** (Without Media).
4. Save the **.txt** file.

### 2️⃣ Upload Chat File

1. Run the **Streamlit app**.
2. Upload the exported **.txt** file.
3. Select the **user** or choose "Overall".
4. View insights and visualizations!

## 📝 Notes

- Works best with **WhatsApp chats exported without media**.
- The **stop\_hinglish.txt** file contains common stop words to improve word cloud accuracy.
- Make sure your `emoji` package is up-to-date.

## 🤖 Future Improvements

- Sentiment analysis of messages
- Support for **multi-language analysis**
- Real-time chat analytics

## 💡 Contributing

Feel free to submit **issues, pull requests, and suggestions** to improve this project!

## 📜 License

This project is **open-source** under the MIT License.

---

🚀 **Developed by Ankit Kumar**

