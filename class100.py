class Car(object):
 def __init__(self,model,color,company,speed_limit):
    self.color=color
    self.company=company
    self.model=model
    self.speed_limit=speed_limit
 def start(self):
     print("started")
 def stop(self):
     print("stopped")
 def accelerate(self):
     print("acelerated")

Ford=Car("ford","blue","ford",170)
print(Ford.start())
print(Ford.stop())
print(Ford.accelerate())
Ford.color
print(Ford.color)