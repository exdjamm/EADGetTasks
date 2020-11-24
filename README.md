# EADGetTasks
Um script de web scrapping para pegar os dados de novas tarefas do sistema EAD de minha escola e criar tarefas atraves da API do Google Task.


## Como usar ?
### Com Google Tasks

Para funcionar com o Google Tasks, aplicativo de tarefas do Google, primeiramente será necessario criar uma API. 

- Acesse URL : https://developers.google.com/tasks/quickstart/python e sega o passo 1.

O proprio Google faz tudo automaticamente, então não é necessario outras configurações, assim clique em **next**, depois **create**, ele dará a opção de baixar um arquivo. 
Baixe clicando em **DOWNLOAD CLIENT CONFIGURATION** e coloque na pasta onde esta o arquivo *main.py*.

- Siga para o passo dois e rode a instalação pedida.

> Dependendo do Sistema Operacional e versão do python o comando pode ser diferente URL : https://www.treinaweb.com.br/blog/gerenciando-pacotes-em-projetos-python-com-o-pip/

Agora rode o *main.py*, ele irá pedir seu login e senha na primeira vez que rodar, apos isso ele ira pegar suas atividades e outros do EAD IFMS. Apos ele pegar todas as atividades, ele ira abrir uma aba no navegador e pedir para logar com o Google, aceite e logo apos ele ira mandar para o seu Google Tasks.

### Como parte de outra aplicação

O codigo ainda não esta bem estruturado, então, peço que caso necessite estude o codigo fonte e tenha boa sorte.

## Esquema de Classes
### ScrapEAD(username, password)

- username

> User's login 

- password 

> User's password

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

