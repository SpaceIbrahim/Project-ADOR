import time
import mujoco
import mujoco.viewer

# Gen3 Lite xml files
arm_spec = mujoco.MjSpec.from_file('model/kinova_gen3_lite/gen3_lite.xml')

model = arm_spec.compile()
data = mujoco.MjData(model)

# Start in the 'home' pose so the arm doesn't collapse under gravity
mujoco.mj_resetDataKeyframe(model, data, model.key('home').id)

# Synchronize the motor targets with the current physical joint positions
data.ctrl[:model.nu] = data.qpos[:model.nu]

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        step_start = time.time()
        mujoco.mj_step(model, data)
        viewer.sync()
        dt = model.opt.timestep - (time.time() - step_start)
        if dt > 0:
            time.sleep(dt)