Manual de Usuario para el Script de Procesamiento de Archivos de Chat de WhatsApp
Descripción del Script
Este script permite procesar archivos de chat de WhatsApp en formato .txt y extraer los mensajes que se encuentran dentro de un rango de fechas específico. Los datos procesados se guardan en un archivo Excel (.xlsx), lo que facilita su análisis y almacenamiento.

Requisitos
Python 3.x
Librerías:
pandas
openpyxl
re
datetime
os
Funcionalidades
Procesamiento de Archivos de Chat: El script lee archivos de texto de WhatsApp (.txt) y extrae las conversaciones en un formato organizado.
Rango de Fechas Personalizado: Permite al usuario seleccionar un rango de fechas para filtrar los mensajes de los chats.
Generación de Reportes en Excel: Los mensajes extraídos se almacenan en un archivo Excel (.xlsx), que incluye las columnas de "Fecha y Hora", "Remitente" y "Mensaje".
Instrucciones de Uso

1. Preparación del Entorno
Instala Python 3.x en tu sistema.
Instala las librerías necesarias ejecutando el siguiente comando:
pip install pandas openpyxl

3. Estructura de los Archivos de Chat
El script procesa archivos de chat de WhatsApp en formato .txt. Estos archivos contienen los mensajes en un formato estándar, que incluye la fecha, hora, remitente y mensaje. El patrón de los mensajes es el siguiente:
dd/mm/yyyy, hh:mm am/pm - Remitente: Mensaje

4. Ejecución del Script

Paso 1: Ejecuta el Script
Abre una terminal o línea de comandos.
Navega hasta el directorio donde se encuentra el script.

Ejecuta el script con el siguiente comando:
python script_name.py

Paso 2: Selección de Archivos de Chat
Cuando se ejecute el script, el usuario deberá ingresar la ruta del directorio donde se encuentran los archivos .txt de los chats que desea procesar. El sistema buscará automáticamente los archivos con extensión .txt en el directorio proporcionado.

Paso 3: Definir el Rango de Fechas
Se solicitará al usuario que ingrese dos fechas: fecha de inicio y fecha de fin en formato dd/mm/yyyy. Estos parámetros se utilizarán para filtrar los mensajes que se encuentren dentro de ese rango de fechas.

Paso 4: Procesamiento de los Datos
El script procesará los archivos de chat, extrayendo los mensajes de acuerdo con las fechas proporcionadas. Los datos procesados se organizarán en tres columnas:

Fecha y Hora: Fecha y hora del mensaje.
Remitente: Nombre del remitente del mensaje.
Mensaje: Contenido del mensaje.

Paso 5: Generación del Reporte
Una vez procesados los datos, el script generará un archivo Excel con los mensajes filtrados. El archivo se guardará con el nombre WhatsApp_Chat_Export_YYYY-MM-DD.xlsx, donde YYYY-MM-DD corresponde a la fecha actual.

Paso 6: Verificación de Errores
Si hay algún error durante el procesamiento, como fechas inválidas o archivos mal formateados, el script mostrará mensajes de advertencia o error. Asegúrese de seguir las instrucciones para corregir los problemas.

4. Ejemplo de Salida
Una vez completado el proceso, el archivo Excel generado tendrá un formato similar al siguiente:

Fecha y Hora	       Remitente	    Mensaje
01/01/2023 10:15 am	 Juan	          Hola, ¿cómo estás?
01/01/2023 10:16 am	 Pedro	        Bien, gracias. ¿Y tú?
01/01/2023 10:17 am	 Juan	          Todo bien, ¿tienes novedades?

5. Notificaciones
Durante la ejecución, el sistema mostrará mensajes de progreso y notificaciones al usuario:

Procesando archivo: Indicará qué archivo de chat está siendo procesado.
Datos guardados: Confirmará que los datos se han guardado correctamente en el archivo Excel.
Errores: Si ocurre algún problema (por ejemplo, formato de fecha inválido), el script lo notificará al usuario con un mensaje de error.

6. Consideraciones
Formato de los Archivos de Chat: El script asume que los archivos de chat siguen el formato estándar de WhatsApp. Si los archivos no tienen este formato, el script podría no procesarlos correctamente.
Rango de Fechas: Asegúrate de ingresar las fechas en el formato correcto (dd/mm/yyyy). El script no aceptará fechas en otros formatos.
Archivos Vacíos: Si no se encuentran mensajes dentro del rango de fechas especificado, el archivo Excel generado estará vacío, pero se notificará al usuario.

Preguntas Frecuentes (FAQ)
1. ¿Qué hago si el script no encuentra archivos .txt?
Verifica que la ruta del directorio esté correctamente escrita y que los archivos de chat tengan la extensión .txt.

2. ¿Cómo puedo modificar el formato de salida?
Actualmente, el formato de salida está fijo como un archivo Excel con tres columnas. Para realizar modificaciones, necesitarás ajustar el código del script.

3. ¿Qué sucede si ingreso un rango de fechas inválido?
Si las fechas ingresadas no son válidas, el script mostrará un mensaje de error indicando que el formato es incorrecto o que la fecha de inicio no puede ser mayor que la de fin.
