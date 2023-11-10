from dadata import Dadata

class MyApi():

    #Для инициализации класса понадобится токен DaData
    def __init__(self, token: str):
        self.myDadata = Dadata(token)

    #Метод, позволяющий получить ближайшее отделение почты России
    def getPostByCoordinates(self, shirota: float, dolgota: float):
        street: str = self.myDadata.geolocate(name="address", lat=shirota, lon=dolgota)[0]['value'].split(',')[1] + self.myDadata.geolocate(name="address", lat=shirota, lon=dolgota)[0]['value'].split(',')[2]
        index: str = self.myDadata.geolocate(name="address", lat=shirota, lon=dolgota)[0]['data']['postal_code']
        post_addres: str = self.myDadata.find_by_id("postal_unit", index)[0]['data']['address_str']
        #return "На{} работает почтовое отделение Почты России c индексом {} и адресом: {} ".format(street, index, post_addres)
        return [street, index, post_addres]
