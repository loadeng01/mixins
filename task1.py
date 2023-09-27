# Создайте  родительские классы: Smartphone и Watch. От этих классов  создайте дочерний класс Smartwatch. 
# В родительских классах должны быть методы: в Smartphone - метод call, который должен звонить на определенный номер, и 
# в Watch - метод see_time, который выдает вам реальное время на данный момент.  
# Создайте объект от класса SmartWatch и вызовите оба метода. 
# Также в обоих родительских классах должен быть реализован метод where_to_wear, который говорит вам, 
# где нужно носить данный гаджет. В классе Smartphone он выдает вам строку “You can keep me anywhere”, 
# а в классе Watch - строку “You should wear me on your hand”. 
# Данный метод наследуется и в дочернем классе, и должен выдавать вам строку “You should wear me on your hand”. 
# Вызовите и этот метод у объекта класса Smartwatch.


class Smartphone:
    def call(self, tel_number):
        return f'Call to number +{tel_number}'
    
    def where_to_wear(self):
        return 'You can keep me anywhere'
    

class Watch:
    def see_time(self):
        from datetime import datetime as time
        return time.strftime(time.now(), f'%H:%M:%S')
    
    def where_to_wear(self):
        return 'You should wear me on your hand'
        

class SmartWatch(Watch, Smartphone):
    pass


smart = SmartWatch()
print(smart.call(123144131))
print(smart.see_time())
print(smart.where_to_wear())
