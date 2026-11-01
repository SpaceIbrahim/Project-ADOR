import time
import mujoco
import mujoco.viewer
import mujoco_menagerie as mm

# Pulls the official Kinova Gen 3 MJCF and compiles it
model = mm.load('kinova_gen3')
data = mujoco.MjData(model)

# Launch the passive interactive viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    print("Viewer started. Press ESC to close.")
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        # Maintain real-time simulation speed
        time.sleep(model.opt.timestep)