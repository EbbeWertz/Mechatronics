import math
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# --- Initialize Cameras ---
left_cam = robot.getDevice('camera_left')
right_cam = robot.getDevice('camera_right')

# Enable them (the argument is the sampling period in ms)
left_cam.enable(timestep)
right_cam.enable(timestep)

# --- Initialize Motors ---
left_motor = robot.getDevice('left_wheel_motor')
right_motor = robot.getDevice('right_wheel_motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Setting speeds (using your RPM to Rad/s logic)
left_motor.setVelocity((400/60)*2*math.pi)
right_motor.setVelocity((300/60)*2*math.pi)

while robot.step(timestep) != -1:
    # Optional: Get image data if you want to process it later
    # image = left_cam.getImage() 
    pass