# Rocio_Greco_2023
# Descripcion
    La aplicacion se llama TOSKA Cervecería.
    Somos un emprendimiento que se dedica a la produccion y venta de Cerveza artesanal.
# Apps
    #Cliente :
        Tiene por objetivo registrar todas las personas / empresas que alguna vez adquirieron nuestro producto.
        Detalle : Nombre/Apellido/Lugar de entrega/fecha de nacimiento.
    #Home :
        Interfaz con el usuario. Pagina principal .
        Posee 5 tarjetas que detallan los estilos fabricados (boton:ampliar).
        Logo de la companía.
        Vinculo a Whatsapp (boton:whatsapp).
        Barra de navegacion principal : Login / Logout /Avatar /Nosotros / Clientes/ Productos/ Ventas. (acceso restringido en funcion del usuario).
            About: quienes somos, donde estamos, precios y contactos.
                    Vinculo a ubicacion (google maps), Whatsapp e Instagram.
    #Producto :
        Detalle de las presentaciones en la que ofrecemos nuestro producto: Chopera / Botella 0,5 y 1 L.
        Productos por presentacion : estilos . Blonde Ale, Scottish, Stout, Apa, Ipa.
    #Ventas :
        Registro de vendedores (cadena de distribucion corta: generalmente no hay intermediarios entre el fabricante y el consumidor).
        Ventas : Por producto /presentacion / precio.
# Usuarios
    Hay 3 tipos de usuarios registrados :
        1. Superuser: admin / 1234 ( Acceso a todas las funciones : Crear/borrar y actualizar Categoria de productos, Lista de Productos, vendedores y ventas y además al panel de administracion ).
        2. Activo :Rafael / Pala1234 ( Acceso restringido : Visualizar Lista de Productos, vendedores y Ventas).
        3. Staff: Liliana / Lili1234 (Acceso a todas las funciones con posibilidad de Crear/borrar y actualizar pero no tiene acceso al panel de administracion.)
    Cada uno con distintos niveles de acceso.

# Video

https://drive.google.com/drive/folders/1jXKExnJ7JeOCXQiugRCpIhxYDfhfoPcJ?role=writer

# Errores conocidos

No se puede asignar mas de un producto por venta (tipo carrito).
