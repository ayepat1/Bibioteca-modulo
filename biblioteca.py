from abc import ABC, abstractmethod

# Clase abstracta para los libros
class Libro(ABC):
    def __init__(self, id_libro, titulo, autor, anio_publicacion):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    @abstractmethod
    def mostrar_info(self):
        """Método abstracto para mostrar la información del libro."""
        pass

    @abstractmethod
    def actualizar_info(self, titulo=None, autor=None, anio_publicacion=None):
        """Método abstracto para actualizar los detalles del libro."""
        pass

# Implementación concreta de la clase Libro
class LibroConcreto(Libro):
    def __init__(self, id_libro, titulo, autor, anio_publicacion):
        super().__init__(id_libro, titulo, autor, anio_publicacion)

    def mostrar_info(self):
        return f"{self.titulo} de {self.autor} ({self.anio_publicacion})"
    
    def actualizar_info(self, titulo=None, autor=None, anio_publicacion=None):
        if titulo:
            self.titulo = titulo
        if autor:
            self.autor = autor
        if anio_publicacion:
            self.anio_publicacion = anio_publicacion

# Clase para gestionar la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro: Libro):
        """Agrega un libro a la biblioteca."""
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
            print(f"Libro '{libro.titulo}' agregado correctamente.")
        else:
            print(f"El libro con ID {libro.id_libro} ya existe.")

    def eliminar_libro(self, id_libro):
        """Elimina un libro de la biblioteca por ID."""
        if id_libro in self.libros:
            eliminado = self.libros.pop(id_libro)
            print(f"Libro '{eliminado.titulo}' eliminado correctamente.")
        else:
            print(f"El libro con ID {id_libro} no se encuentra en la biblioteca.")
    
    def actualizar_libro(self, id_libro, titulo=None, autor=None, anio_publicacion=None):
        """Actualiza la información de un libro por ID."""
        if id_libro in self.libros:
            libro = self.libros[id_libro]
            libro.actualizar_info(titulo, autor, anio_publicacion)
            print(f"Libro '{libro.titulo}' actualizado correctamente.")
        else:
            print(f"El libro con ID {id_libro} no se encuentra en la biblioteca.")
    
    def mostrar_libros(self):
        """Muestra todos los libros de la biblioteca."""
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro in self.libros.values():
                print(libro.mostrar_info())

# Función principal para interactuar con la biblioteca
def main():
    biblioteca = Biblioteca()

    # Crear algunos libros
    libro1 = LibroConcreto(1, "Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = LibroConcreto(2, "Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    libro3 = LibroConcreto(3, "1984", "George Orwell", 1949)

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Mostrar todos los libros
    print("\nLibros en la biblioteca:")
    biblioteca.mostrar_libros()

    # Actualizar un libro
    print("\nActualizando libro con ID 1...")
    biblioteca.actualizar_libro(1, titulo="Cien años de soledad (Edición Especial)")

    # Mostrar todos los libros después de la actualización
    print("\nLibros en la biblioteca después de la actualización:")
    biblioteca.mostrar_libros()

    # Eliminar un libro
    print("\nEliminando libro con ID 2...")
    biblioteca.eliminar_libro(2)

    # Mostrar todos los libros después de la eliminación
    print("\nLibros en la biblioteca después de la eliminación:")
    biblioteca.mostrar_libros()

if __name__ == "__main__":
    main()
