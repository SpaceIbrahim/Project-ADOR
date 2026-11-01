import time
import mujoco
import mujoco.viewer
import mujoco_menagerie as mm

# 1. Get the editable specifications for both models
arm_spec = mm.get('kinova_gen3').spec()
gripper_spec = mm.get('robotiq_2f85').spec()

# 2. Locate the mounting point on the Kinova arm
mounting_site = arm_spec.find_site('attachment_site')

# 3. Attach the gripper to the arm's site
arm_spec.attach(gripper_spec, site=mounting_site, prefix='gripper_')

# 4. Compile the combined specification into a runnable model
model = arm_spec.compile()
data = mujoco.MjData(model)

# Launch the passive interactive viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    print("Viewer started. Press ESC to close.")
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)