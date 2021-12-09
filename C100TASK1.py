class Car(object):
    def _init_(self, color):
        self.color=color
    def start(self):
        print('started')
    def stop(self):
        print('stop')
    def accelerate(self):
        print('accelerating!')
    def changeGear(self, gearType):
        self.gearType=gearType
        print('gear changed to:', gearType)
class Plane(object):
    def _init_(self, PlaneCompany):
        self.PlaneCompany = PlaneCompany
    def engines(self, on):
        print('engines are:', on)
    def taxi(self, no):
        print('you are', no , 'taxing')
    def permission(self, perm):
        print('you have', perm, 'to take off')
    def landPerm(self, LPerm):
        print('you have', LPerm, 'to land')
plane = Plane()
plane.PlaneCompany = 'jet2'
plane.engines('on')
plane.taxi(' ')
plane.permission('permission')
plane.landPerm('permission')
'''car = Car()
car.color = 'red'
car.start()
car.accelerate()
car.changeGear(2)
car.stop()
print(car.color)'''