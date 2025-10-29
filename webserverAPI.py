from fastapi import FastAPI
from threading import Lock
app = FastAPI()
@app.get("/")
def root():
        return 0
robotState = {
        "up": False,   
        "down": False,
        "left": False,
        "right”: False
}
stateLock = Lock()
        
@app.put("/control/set")
async def update_controls(data: ControlData):
        global robotState
        with stateLock:
                robotState["up"] = data.up
                robotState["down"] = data.down
                robotState["left"] = data.left
                robotState["right"] = data.right
        print(f"GUI Updated State: {robotState}")
        return {"message": "Updated"}
@app.get("/control/status")

