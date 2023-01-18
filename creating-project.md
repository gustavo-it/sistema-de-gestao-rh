# Primeiro passos
* Instalar o Python em sua máquina
* Criar um ambiente virtual para o seu projeto e ativa-lo para instalar os pacotes necessários para rodar o projeto.


---

## Instalando o Django
```
pip install django
```  
---
## Comandos para iniciar o projeto
Na raiz do seu projeto execute o seguinte comando:
```
django-admin startproject gestao_rh .
```

Executar o comando migrate que é responsável por criar a base de dados:
```
python manage.py migrate
```

Criar um super usuário para área administrativa do framework:
```
python manage.py createsuperuser
```

Rodar o servidor do django:
```
python manage.py runserver
```

---
Acessando `localhost:8000/admin` você verá a área administrativa do framework. 
Onde é possível fazer login com o super usuário que você criou anteriormente.