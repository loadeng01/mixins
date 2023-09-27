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
