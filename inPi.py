from flask import Flask, jsonify
from threading import Lock
import json

# App initialization
app = Flask(__name__)

robotState = {
        "up": False,   
        "down": False,
        "left": False,
        "right”: False
}

try:
    with open('status.json', 'r') as file:
        data = json.load(file)
        robotState.update(data)
    # print(data)
    print(f"left: {data['left']}")
except FileNotFoundError:
    print("No status.json file")
Except json.JSONDecodeError:
    print(“json file corrupted”)
def check_robot_direction(status):
    # Attempt to get robot's status
    return data[f'{status}']

def saveStateToFile():
    try:
        with open(‘status.json’, ‘w’) as file:
            json.dump(robotState, file, indent=4)

def change_directions(status):
    #loading file:
    try:
        with open('status.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No status.json file")
    # Flip status
    if data[f'{status}'] == True:
        data[f'{status}'] = False
        with open('status.json', 'w') as file:
            json.dump(data, file)
    else:
        data[f'{status}'] = True
        with open('status.json', 'w') as file:
            json.dump(data, file)

    return data[f'{status}']


@app.route('/check_status/<status>', methods=['GET'])
def get_motor_position(status):
    # Returns motor's position
    with stateLock:
        return jsonify(robotState)
@app.route('/change_status/<status>', methods=['POST'])
def set_motor_position():
    """Explicitly SETS the robot's movement state using the request body.""" # 1. Validate incoming JSON data
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"message": "Invalid JSON format"}), 400
    # 2. Safely update the state using the Lock
    with stateLock:
    # Iterate over the received data and update ONLY valid keys
    for key in ["up", "down", "left", "right"]:
        if key in data and isinstance(data[key], bool):
            robotStatus[key] = data[key]
    # 3. Save the updated state to the file
    saveStateToFile()
    print(f"New Robot State: {robotStatus}")
    return jsonify({"message": "Robot state updated", "current_state": robotStatus})


if __name__ == '__main__':
    app.run(debug=True)
