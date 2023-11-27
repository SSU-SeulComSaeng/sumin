

def light_on() :  
    import os #포트 개별적으로 제어 불가능
    os.system("sudo uhubctl -l 2 -a 1")  #전원 켜기

def light_off() :   
    import os #포트 개별적으로 제어 불가능
    os.system("sudo uhubctl -l 2 -a 0")  #전원 끄기

