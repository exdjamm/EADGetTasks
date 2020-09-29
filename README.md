# EADGetTasks
Um script de web scrapping para pegar os dados de novas tarefas do sistema EAD de minha escola e criar tarefas atraves da API do Google Task.

## Classes
### ScrapEAD()
> Send a username and a password ```python newScrap = ScrapEAD(username, passoword)```
#### Variables
- No one for now :(
#### Methods
- setToken()
> To hide
- login()
> To hide
- setSessionKey()
> To hide
- setCourses()
> To hide
- setCoursesTasks()
> To hide
- getCourses()
> Return the following schema of dict:
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

- [] Set to send configs in the paraments of the class
     - Like if will save
     - Another things
