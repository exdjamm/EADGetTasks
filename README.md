# EADGetTasks
Um script de web scrapping para pegar os dados de novas tarefas do sistema EAD de minha escola e criar tarefas atraves da API do Google Task.

## Classes
### ScrapEAD
#### Variables
#### Methods
- getCourses()
Return the following schema of dict:
```python
{
    'Course Name' : 
    {
        'tasks' :
        [
            {
                'title' : 'Task Name', 
                'note'  : 'by default is the task's link'
            }
            ...
        ]
    }
    ...
}
```
