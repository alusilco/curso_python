
class Boligrafo:
    # constructor
    def __init__(self, marca: str, color: str):
        self.marca = marca
        self.color = color

    def escribir(self, contenido: str):
        print(f"El boli {self.color} ha escrito {contenido}")



if __name__ == "__main__":

    boli_verde = Boligrafo("BIC", "Verde") # instanciacion
    boli_rojo = Boligrafo("BIC", "Rojo")

    print(boli_rojo.color)
    print(boli_verde.marca)

    boli_verde.escribir("Hola Python")

