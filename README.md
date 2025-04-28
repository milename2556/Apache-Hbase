# Apache-Hbase
Tarea4
# Proyecto: Carga de datos en Apache HBase desde un CSV

Este proyecto carga datos de automóviles almacenados en un archivo CSV a una tabla HBase llamada `cars`, utilizando Python y HappyBase.

## Estructura del CSV

El archivo `CAR_DETAILS_FROM_CAR_DEKHO.csv` debe tener las siguientes columnas:

- name
- year
- selling_price
- km_driven
- fuel
- seller_type
- transmission
- owner

## Familias de Columnas en HBase

Se creará la tabla `cars` con estas familias de columnas:

- `details`: contiene year, selling_price, km_driven, fuel
- `seller_info`: contiene seller_type
- `transmission_info`: contiene transmission, owner

## Requisitos

- Apache HBase instalado y en ejecución
- Thrift Server de HBase iniciado (importante para usar HappyBase)
- Python 3
- Librería HappyBase instalada

Instalar HappyBase:

```bash
pip install happybase
