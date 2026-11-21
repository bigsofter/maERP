# maERP

[Русский](README.md) · [English](README.en.md) · [Français](README.fr.md) · **Español**

maERP es un sistema de gestión empresarial para la plataforma 1C:Enterprise 8.5: ventas, compras, almacén,
producción, venta minorista con caja, tesorería y contabilidad en una sola base. Lo desarrolla TinyCIO. La interfaz
y los impresos están en ruso, francés, inglés y español; la configuración fiscal está orientada a Marruecos
y se completa con los tipos del país al crear la base.

Los archivos listos para instalar (`.cf` y `.cfu`) están en [Releases](https://github.com/bigsofter/maERP/releases);
el historial de cambios está en [docs/CHANGELOG.md](docs/CHANGELOG.md).

## Funciones

| Área | Contenido |
|---|---|
| Ventas | Ofertas, pedidos de clientes, albaranes y facturas fiscales, devoluciones, descuentos por importe y por porcentaje, control de crédito y bloqueo de envíos, pestaña «Artículos» con las líneas de los documentos en la lista |
| Minorista | Puesto de caja, turnos de caja, tiques, verificador de precios, etiquetas, necesidades de los puntos de venta, sector «Teléfonos y accesorios» con control por número de serie (IMEI) |
| Compras | Pedidos a proveedores, licitaciones, recepciones, devoluciones a proveedores, planificación de compras según la necesidad, puesto de compras |
| Almacén | Traslados, almacenes con órdenes, inventarios con inventario valorado y hoja de diferencias, lotes y su trazabilidad, recepción y recuento móviles |
| Producción | Listas de materiales, producción bajo pedido, vales de materiales, partes de producción, subcontratación para varios pedidos, coste del producto, gestión de máquinas: carga, paradas, mantenimiento, eficiencia (OEE) |
| Tesorería | Caja y banco, liquidaciones con clientes y proveedores, documentos en divisa, deudas vencidas, flujo de caja |
| Contabilidad e impuestos | Plan de cuentas y asientos, contabilidad de gestión y fiscal separadas, zonas de IVA y exención, retención del IVA en origen, registros de facturas fiscales |
| Nóminas y RR. HH. | Empleados, control horario, cálculo de nóminas e informes |
| Servicio | Intercambio entre bases maERP por carpeta compartida o HTTPS, importación desde Excel, atributos adicionales, permisos por rol, ventana «Novedades», actualización automática de los datos |

La configuración tiene 54 tipos de documentos, 70 informes y 26 roles. Los impresos son corporativos, con el logotipo
de la empresa, vista previa y salida en el idioma de la contraparte.

## Instalación y actualización

Se necesita la plataforma 1C:Enterprise 8.5.1 y sus licencias. Se adquieren a 1C y a sus socios y no forman parte
de maERP.

- **Base nueva.** Crear la base a partir de `maERP-<versión>.cf`. Al primer inicio se abre un asistente: empresa,
  país, sector, usuarios.
- **Actualización.** Cargar `maERP-<versión>.cfu` (actualización desde las versiones publicadas) o el `.cf` completo.
  En el primer acceso del administrador el programa actualiza los datos y muestra «Novedades».
- **Despliegue sin interfaz** (servidor, cliente web): [docs/DEPLOY.md](docs/DEPLOY.md), en ruso.

Haga una copia de seguridad de la base de producción antes de actualizar.

## Para desarrolladores

Las fuentes están en formato 1C:EDT: un árbol de archivos de texto (`.mdo` para los metadatos, `.bsl` para el código).
El archivo `.cf` es un producto de compilación y no se versiona. La documentación del proyecto está en ruso.

El desarrollo se hace en `develop`; `main` solo recibe los estados de versión. Requisitos: plataforma 1C 8.5.1.1150,
1C:EDT (véase [docs/EDT-SETUP.md](docs/EDT-SETUP.md)) y Java 17, incluido con EDT.

## Licencias

- **Código y materiales de maERP** — © TinyCIO, bajo la
  [GNU Affero General Public License versión 3](LICENSE) (AGPL-3.0). El programa se puede usar, estudiar, modificar
  y redistribuir libremente. Quien distribuya una versión modificada o dé acceso a ella por la red debe publicar su
  código fuente en las mismas condiciones. El programa se entrega sin garantía alguna.
- **Componentes de terceros** — controladores de equipos de venta y bibliotecas de 1C — pertenecen a sus
  desarrolladores. No están cubiertos por la licencia de maERP, y su uso requiere un acuerdo aparte con sus
  titulares. TinyCIO no responde de ese uso. La lista y el permiso adicional para la ejecución en la plataforma 1C
  están en [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) (en ruso).
- **La plataforma 1C:Enterprise** se licencia aparte por 1C.
- **El nombre y el logotipo de maERP** no están cubiertos por la licencia del código.

## Contacto

Implantación, soporte y condiciones comerciales: TinyCIO, [tinycio.ru](https://tinycio.ru).
