class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    def devolver(self):
        self.disponible = True
class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamanioMB):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamanioMB = tamanioMB
    def prestar(self):
        return True
class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def listar_libros(self):
        for l in self.libros:
            estado = "Disponible" if l.disponible else "Prestado"
            print(l.titulo, "-", l.autor, "-", estado)
    def buscar_por_autor(self, autor):
        for l in self.libros:
            if l.autor == autor:
                print(l.titulo)
    def prestar_libro(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                if l.prestar():
                    print("Libro prestado")
                else:
                    print("Libro no disponible")
                return
        print("Libro no encontrado")
b = Biblioteca()
b.agregar_libro(Libro("Libro A", "Autor 1", 2020))
b.agregar_libro(Libro("Libro B", "Autor 2", 2021))
b.agregar_libro(Libro("Libro C", "Autor 1", 2019))
b.agregar_libro(LibroDigital("Libro D", "Autor 3", 2022, "PDF", 5))
b.agregar_libro(LibroDigital("Libro E", "Autor 3", 2023, "EPUB", 3))
b.listar_libros()
b.prestar_libro("Libro A")
b.prestar_libro("Libro A")
for i in range(5):
    b.prestar_libro("Libro D")
b.buscar_por_autor("Autor 1")