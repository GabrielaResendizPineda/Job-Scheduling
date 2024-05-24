import tkinter as tk
from tkinter import ttk, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

class Operation:
    def __init__(self, operation_id, durations):
        self.operation_id = operation_id
        self.durations = durations

class Job:
    def __init__(self, job_id, operations):
        self.job_id = job_id
        self.operations = deque(operations)  

class Machine:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.queue = []  
        self.end_time = 0

    def schedule_operation(self, job, operation, start_time):
        operation_duration = operation.durations[self.machine_id]
        end_time = start_time + operation_duration
        self.queue.append((start_time, end_time, job, operation))
        self.end_time = max(self.end_time, end_time)

    def process_queue(self):
        self.queue.sort(key=lambda x: x[0])
        for start_time, end_time, job, operation in self.queue:
            yield (self.machine_id, job.job_id, operation.operation_id, start_time, end_time)

def start_simulation():
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)

    # Asignar operaciones a máquinas y simular
    for job in jobs:
        current_time = 0
        for operation in job.operations:
            best_machine = min(machines, key=lambda m: m.end_time)
            best_machine.schedule_operation(job, operation, best_machine.end_time)
    
    # Colores para el gráfico
    color_map = plt.cm.get_cmap('tab20', len(jobs))

    # Dibujar el gráfico de Gantt
    for machine in machines:
        for machine_id, job_id, operation_id, start_time, end_time in machine.process_queue():
            job = next((job for job in jobs if job.job_id == job_id), None)
            if job:
                color = color_map(jobs.index(job))
                ax.broken_barh([(start_time, end_time - start_time)],
                               (machine_id * 10, 9),
                               facecolors=color,
                               edgecolor='black',
                               label=operation_id)
                ax.text(start_time, machine_id * 10 + 5, f'{start_time:.1f}', va='center', ha='right', color='black')
                ax.text(end_time, machine_id * 10 + 5, f'{end_time:.1f}', va='center', ha='left', color='black')

    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Máquina')
    ax.set_yticks([m.machine_id * 10 + 5 for m in machines])
    ax.set_yticklabels([f'M{m.machine_id + 1}' for m in machines])
    ax.set_title('Diagrama de Gantt de la Planificación de Tareas')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Planificación de Tareas")

# Solicitar número de máquinas al usuario
machine_count = simpledialog.askinteger("Número de Máquinas", "Ingrese el número de máquinas:")
machines = [Machine(i) for i in range(machine_count)]

# Solicitar número de trabajos al usuario
job_count = simpledialog.askinteger("Número de Trabajos", "Ingrese el número de trabajos:")
jobs = []

# Solicitar datos para cada trabajo
for i in range(job_count):
    job_name = simpledialog.askstring("Nombre del Trabajo", f"Ingrese el nombre para el trabajo {i+1}:")
    operation_ids = simpledialog.askstring("Operaciones", f"Ingrese las operaciones para el trabajo {job_name} (separadas por coma):")
    operations = []
    
    for operation_id in operation_ids.split(','):
        durations_input = simpledialog.askstring("Tiempos de Ejecución", f"Ingrese los tiempos de ejecución para {operation_id} en cada máquina (separados por coma):")
        durations = [float(time) for time in durations_input.split(',')]
        operations.append(Operation(operation_id, durations))
    
    jobs.append(Job(job_name, operations))

# Botón para iniciar la simulación y mostrar el gráfico de Gantt
start_button = ttk.Button(root, text="Iniciar Simulación", command=start_simulation)
start_button.pack()

# Ejecutar el bucle principal de Tkinter
root.mainloop()
