# 🧠 Advanced HR Simulation Platform

An AI-powered HR evaluation system that automates the final round of recruitment through audio analysis, LLM-based scoring, and eye-tracking heatmaps for behavioral assessment.

🚀 Features

🎙️ Automated Audio Transcription using OpenAI Whisper for real-time candidate response conversion.

🧩 LLM Evaluation with Gemini Flash 1.5, providing context-aware scoring and feedback on clarity, confidence, and relevance.

👁️ Gaze Tracking & Heatmaps built with MediaPipe FaceMesh, detecting focus, attention drift, and multiple-face cheating.

🧮 Modular Streamlit Interface — seamless workflow for HRs to transcribe, evaluate, and visualize results.

🗄️ MongoDB Integration for secure storage of questions, transcriptions, and evaluations.


🧰 Tech Stack

Frontend: Streamlit

Backend: Python, Whisper, Gemini Flash 1.5 API

Computer Vision: OpenCV, MediaPipe FaceMesh

Database: MongoDB

Visualization: Matplotlib, NumPy

⚙️ How It Works

Transcription Stage: Converts candidate audio responses (.mp3) into text using Whisper.

Evaluation Stage: Gemini Flash 1.5 evaluates answers based on predefined HR criteria.

Heatmap Stage: Snapshots are analyzed to generate gaze heatmaps and detect anomalies.

Result Dashboard: HRs can view transcripts, AI feedback, and visual attention reports in one interface.


👩‍💼 Use Cases

Final HR rounds in recruitment processes.

Automated candidate screening for soft-skill evaluation.

Research on AI-based behavioral analysis and fairness in assessments.


🧩 Future Scope

Real-time webcam monitoring during interviews.

Integration with emotion recognition modules.


# 🏁 Getting Started
#Clone this repository
git clone https://github.com/Nagpravin/HR-simulation.git

cd advanced-hr-simulation

#Install dependencies

pip install -r requirements.txt

#Run the Streamlit app

streamlit run main.py
