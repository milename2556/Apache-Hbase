# Apache-Hbase
Tarea4

# Proyecto: Carga de Datos de Coches en HBase

Este proyecto tiene como objetivo cargar un conjunto de datos de coches desde un archivo CSV a HBase y realizar varias operaciones sobre los datos almacenados en HBase.

## 1. Cargar los datos en HBase

El archivo de datos `CAR DETAILS FROM CAR DEKHO.csv` contiene información sobre diferentes coches, como nombre, año, precio, kilometraje, tipo de combustible, vendedor, etc.

### Estructura de la tabla en HBase:

- `details:name`: Nombre del coche
- `details:year`: Año del coche
- `details:selling_price`: Precio de venta
- `details:km_driven`: Kilometraje
- `details:fuel`: Tipo de combustible
- `details:seller_type`: Tipo de vendedor
- `details:transmission`: Tipo de transmisión
- `details:owner`: Número de propietarios anteriores

### Script utilizado para cargar los datos

Se utilizó el script `load_cars_to_hbase.py` para leer el archivo CSV y cargar los datos en HBase.

```python
import csv
from happybase import Connection

# Conectar a HBase
connection = Connection('localhost')
connection.open()

# Crear una tabla si no existe
table_name = 'cars'
if table_name not in [t.name for t in connection.tables()]:
    connection.create_table(table_name, {
        'details': dict()  # Familia de columnas 'details'
    })

# Abrir el archivo CSV y cargar los datos
with open('CAR DETAILS FROM CAR DEKHO.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row_key = row['name']
        # Insertar los datos en HBase
        connection.table(table_name).put(row_key, {
            'details:name': row['name'],
            'details:year': row['year'],
            'details:selling_price': row['selling_price'],
            'details:km_driven': row['km_driven'],
            'details:fuel': row['fuel'],
            'details:seller_type': row['seller_type'],
            'details:transmission': row['transmission'],
            'details:owner': row['owner']
        })
# Para ejecutar el script, utiliza el siguiente comando en tu terminal:
python load_cars_to_hbase.py

# consultar un coche específico
get 'cars', 'Honda Civic'

#Filtrar los coches que utilizan Petrol como combustible
scan 'cars', {FILTER => "ValueFilter(=, 'binary:Petrol')"}

# Actualizar el precio de un coche
put 'cars', 'Honda Civic', 'details:selling_price', '16000'


#Eliminar un coche:
delete 'cars', 'Honda Civic'

#Recorrer todos los coches:
scan 'cars'

# Cerrar la conexión
connection.close()
