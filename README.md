# este va a ser el archivo readme 
# asi como tambien la documentacion del programa
"""
-> indicaciones de como usar el programa

Al iniciar la aplicación, te pedirá ingresar el número de máquinas. Supongamos que ingresamos 4 y presionamos "OK".

Luego, te pedirá ingresar el número de trabajos. Supongamos que ingresamos 3 y presionamos "OK".

A continuación, se abrirán tres ventanas emergentes para ingresar los detalles de cada trabajo:

a. Trabajo 1:

Nombre del trabajo: TrabajoA
Operaciones: O1, O2, O3
Tiempos de ejecución en cada máquina:
Para O1: 3.0, 4.0, 2.5, 3.5
Para O2: 5.0, 3.5, 6.0, 4.5
Para O3: 2.0, 2.5, 3.0, 2.0
b. Trabajo 2:

Nombre del trabajo: TrabajoB
Operaciones: O2, O4
Tiempos de ejecución en cada máquina:
Para O2: 5.0, 3.5, 6.0, 4.5
Para O4: 4.0, 5.0, 3.5, 2.5
c. Trabajo 3:

Nombre del trabajo: TrabajoC
Operaciones: O1, O3, O5
Tiempos de ejecución en cada máquina:
Para O1: 3.0, 4.0, 2.5, 3.5
Para O3: 2.0, 2.5, 3.0, 2.0
Para O5: 3.5, 4.0, 5.0, 3.0
Después de ingresar estos datos, presionas "OK" en cada ventana de entrada.

Finalmente, presionas el botón "Iniciar Simulación". Esto generará un gráfico de Gantt basado en los datos que ha introducido eñ usuario.

------- documentacion del programa -------

Este código implementa una aplicación de interfaz gráfica de usuario (GUI) en Tkinter para realizar la planificación de tareas y mostrar un diagrama de Gantt. A continuación, una breve explicación de cada parte:

Clase Operation: Representa una operación con un identificador (operation_id) y una lista de duraciones en cada máquina (durations).

Clase Job: Representa un trabajo con un identificador (job_id) y una cola de operaciones (operations). La cola de operaciones se implementa como un objeto deque para facilitar la manipulación.

Clase Machine: Representa una máquina con un identificador (machine_id). Tiene una cola de operaciones (queue) que se planificarán en la máquina y un tiempo de finalización (end_time) para llevar un seguimiento de cuándo termina la última operación en la máquina.

Método schedule_operation en Machine: Planifica una operación en la máquina, teniendo en cuenta el tiempo de inicio y finalización. Actualiza el tiempo de finalización de la máquina.

Método process_queue en Machine: Procesa la cola de operaciones de la máquina y devuelve un generador que proporciona información sobre las operaciones procesadas (máquina_id, trabajo_id, operación_id, tiempo_inicio, tiempo_fin).

Función start_simulation: Inicia la simulación y crea el gráfico de Gantt utilizando Matplotlib. Asigna operaciones a máquinas y genera el gráfico.

Ventana principal de Tkinter:

Solicita al usuario el número de máquinas y trabaja con máquinas creadas.
Solicita al usuario el número de trabajos y para cada trabajo:
Pide un nombre para el trabajo.
Pide las operaciones para ese trabajo (separadas por coma).
Para cada operación, solicita los tiempos de ejecución en cada máquina (separados por coma).
Botón para iniciar la simulación: Activa la función start_simulation cuando se hace clic.

Este código proporciona una forma interactiva para que el usuario introduzca el número de máquinas, trabajos y los detalles de cada trabajo, y luego visualice la planificación en un diagrama de Gantt. Además, utiliza un enfoque orientado a objetos para organizar la lógica de la simulación.

"""