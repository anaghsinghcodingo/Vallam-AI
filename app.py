from flask import Flask, request, jsonify
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv

# -------------------------------
# LOAD ENV VARIABLES
# -------------------------------

load_dotenv()
genai.configure(api_key="AIzaSyDxvQ2d-5kwJ_nyso6qJD8r1ZImPFnIXR0")

app = Flask(__name__)

from flask_cors import CORS
CORS(app)


# -------------------------------
# SIMULATION ENGINE
# -------------------------------
def run_simulation(data):

    boat_length = float(data["boat_length"])
    num_rowers = int(data["num_rowers"])
    force_per_rower = float(data["force_per_rower"])
    stroke_rate = float(data["stroke_rate"])
    wind_speed = float(data["wind_speed"])
    wind_direction = int(data["wind_direction"])
    water_current = float(data["water_current"])

    boat_mass = boat_length * 30
    boat_area = 0.05 * boat_length**2

    water_density = 1000
    drag_coeff = 0.8
    wind_coeff = 0.3

    fatigue_rate = 0.002
    race_distance = 1000
    dt = 0.1

    time = 0
    velocity = 0
    position = 0
    max_velocity = 0

    while position < race_distance:
        fatigue_factor = np.exp(-fatigue_rate * time)
        stroke_multiplier = stroke_rate / 30

        total_force = num_rowers * force_per_rower * fatigue_factor * stroke_multiplier

        drag_force = 0.5 * water_density * drag_coeff * boat_area * velocity**2
        wind_force = wind_coeff * wind_speed * wind_direction * boat_area

        net_force = total_force - drag_force + wind_force
        acceleration = net_force / boat_mass

        velocity += acceleration * dt
        velocity = max(velocity, 0)

        max_velocity = max(max_velocity, velocity)

        effective_velocity = velocity + water_current
        position += effective_velocity * dt

        time += dt

    race_time = time
    final_velocity = velocity
    average_velocity = race_distance / race_time
    final_fatigue_factor = np.exp(-fatigue_rate * race_time)

    return {
        "race_time": round(race_time, 2),
        "final_velocity": round(final_velocity, 2),
        "average_velocity": round(average_velocity, 2),
        "max_velocity": round(max_velocity, 2),
        "final_fatigue_factor": round(final_fatigue_factor, 4)
    }

# -------------------------------
# GEMINI AI ANALYSIS
# -------------------------------
def generate_ai_analysis(simulation_result):

    prompt = f"""
You are VallamAI, an AI performance analyst for Kerala’s snake boat race.
Keep response under 120 words.
Be analytical and structured.

Race Time: {simulation_result['race_time']} sec
Final Velocity: {simulation_result['final_velocity']} m/s
Average Velocity: {simulation_result['average_velocity']} m/s
Max Velocity: {simulation_result['max_velocity']} m/s
Final Fatigue Factor: {simulation_result['final_fatigue_factor']}
"""

    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 250,
        }
    )

    response = model.generate_content(prompt)

    return response.text

    response = model.generate_content(system_prompt + user_prompt)

    return response.text

# -------------------------------
# API ROUTES
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "VallamAI Backend Server",
        "status": "running",
        "endpoints": {
            "simulate": "POST /simulate - Run boat race simulation"
        }
    })

@app.route("/simulate", methods=["GET"])
def simulate():

    data = request.json

    simulation_result = run_simulation(data)
    ai_analysis = generate_ai_analysis(simulation_result)

    return jsonify({
        "simulation": simulation_result,
        "ai_analysis": ai_analysis
    })

# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
