class celular():
    def __init__(self, marca, sistema_operativo, year, ram, almacenamiento, timbrar, encender, apagar):
        self.marca = marca
        self.sistema_operativo = sistema_operativo
        self.year = year
        self.ram = ram
        self. almacenamiento = almacenamiento
        self.timbrar = timbrar
        self.encender = encender
        self.apagar = apagar
    def timbrar(self):
        self.timbrar = True
    def encender(self):
        self.encender = True
    def apagar(self):
        self.apagar = True

celphone = celular("Huawei", "Android 9", 2019, "3 GB", "64 GB", True, True, False)
print(celphone.marca)
print(celphone.sistema_operativo)
print(celphone.year)
print(celphone.ram)
print(celphone.almacenamiento)
print(celphone.timbrar)
print(celphone.encender)
print(celphone.apagar)