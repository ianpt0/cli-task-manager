from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt
from rich.style import Style
from rich.table import Table

# Criando um console
console = Console()
console.size = (None, 20)

# Definindo os estilos para a interface do usuário
panel_style = Style(bgcolor='black', color='#d600ff')
table_style = Style(bgcolor='black', color='white')

# Criando a tabela para as tarefas
table = Table(show_header=True, header_style=table_style)
table.add_column('Tarefa', style=table_style)
table.add_column('Concluída', style=table_style)

# Adicionando tarefas à tabela
tasks = []
while True:
    task_name = Prompt.ask('Digite o nome da tarefa (ou ENTER para finalizar a lista)')
    if task_name == '':
        break
    tasks.append({'name': task_name, 'completed': False})

# Exibindo as tarefas na tabela
for task in tasks:
    while True:
        completed_input = Prompt.ask(f'{task["name"]} concluída? (S/N)').lower()
        if completed_input == 's':
            task['completed'] = True
            break
        elif completed_input == 'n':
            break
        else:
            console.print('Por favor, insira S para sim ou N para não.')

    table.add_row(task['name'], 'Sim' if task['completed'] else 'Não')

# Criando um painel para a tabela
panel = Panel(table, title='Lista de Tarefas', style=panel_style)

# Definindo a disposição dos painéis
layout = Layout()
layout.split(
    Layout(name='header', size=3),
    Layout(name='body', ratio=1),
)

# Adicionando os painéis ao layout
layout['header'].update(Panel('CLI Task Manager', style=panel_style))
layout['body'].update(panel)

# Exibindo o layout na tela
console.print(layout)

# Exibindo um resumo com o número total de tarefas e o número de tarefas concluídas
total_tasks = len(tasks)
completed_tasks = sum([task['completed'] for task in tasks])
console.print(f'Total de tarefas: {total_tasks} | Tarefas concluídas: {completed_tasks}')
