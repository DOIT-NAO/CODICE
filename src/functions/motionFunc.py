from naoqi import ALProxy
sayParameters = ["192.168.163.214",9559]

def muovi(x,y,t):
    motion_module = ALProxy("ALMotion", *sayParameters)
    motion_module.wakeUp()
    motion_module.moveTo(x,y,t)
