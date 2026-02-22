# 🐍 Vallam Kali Simulation Engine

A simple physics-based simulation engine that predicts the performance of a snake boat (Vallam Kali). This tool allows users to input boat details, crew strength, and weather conditions to estimate race time and boat speed.

This project was built as part of a hackathon to demonstrate how physics and programming can be used to simulate real-world sports.

---

# 🚀 Features

- Simulates snake boat race performance
- Takes crew strength and stroke rate as input
- Includes fatigue effect over time
- Simulates wind and water current conditions
- Predicts race time and final velocity
- Easy to modify and extend
- Beginner-friendly code structure

---

# 🛠️ Requirements

- Python 3
- Flask
- Google GenAI
- Gunicorn
- NumPy

Install NumPy using:

```bash
pip install numpy
```

---

# ▶️ How to Run

Run the simulation file:

```bash
python app.py
```

Enter the required values when prompted.

Example:

```
Enter boat length (meters): 30
Enter number of rowers: 50
Enter force per rower (Newtons): 320
Enter stroke rate (strokes/min): 32
Enter wind speed (m/s): 3
Enter wind direction (1=tailwind, -1=headwind): 1
Enter water current speed (m/s): 0.4
```

Output:

```
--- Simulation Result ---
Race time: 212.34 seconds
Final velocity: 5.21 m/s
```

---

# 📁 Project Structure

```
vallam-kali-simulation/
│
├── app.py
├── index.html
├── gunicorn_config.py
├── requirements.txt
└── README.md
```

---

# 🎯 What This Project Does

This simulation calculates how fast a snake boat can complete a race based on:

- Boat size
- Number of rowers
- Strength of each rower
- Stroke rate
- Wind conditions
- Water current
- Fatigue over time

---

# 🔮 Future Improvements

- Add graphical visualization
- Create a web interface
- Add AI-based optimization
- Compare multiple boats

---

# 👤 Author

Vitthal Singh
Anagh Singh
Simran Singh
Varnika Gupta
Navya Chawla
**Critical Hit🔥🔥**

---
---

# ⭐ If you like this project, consider giving it a star!
