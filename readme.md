# SISTEMA DE GESTÃO RH
* Multi-tenant
  * Seu software vendido como serviço
  * Multiplas empresas utilizando a sua plataforma  

##
* Multi-database
    * A aplicação se comunica com mais de um banco de dados ao mesmo tempo
    * Comunicação com aplicações legadas.
      * Comunicação com banco de dados existentes
      * Criação de Models com Django para mapear tabelas ed bancos de dados de outros sistemas

##
* Bancos de dados mais relevantes do mercado
   * Oracle
   * MS SQL Server
   * MySQL
   * Postgres
   * Sqlite3 ( Para desenvolvimento local )

##
* Multi-idioma
* Multi-location
   * Moedas
   * Formato de datas
   * Fuso-horarios

##
* Celery para tarefas assincronas
  * Geração de relatorios
    * PDF
    * EXCEL
    * CSV
  * Uso de HTTP Stream para geração de relatórios em tempo real

##
* Interações com o servidor via Ajax
  * Popular campos
  * Filtrar select fields
  * Buscar informações no servidor
  * Salvar informções no servidor

##
* Interações do servidor com o frontend via Websocket
  * Notificações para os usuários sem atualizar a págia
  * Notificar quando uma tarefa tenha sido executada pelo Celery
* Django Messages Framework

##
* Expondo uma Rest API para parte do sistema
  * Django Rest Framework
  * Conceitos mais importantes
  * Permissões e segurança

##
* Deploy nos maiores players do mercado
  * Amazon AWS, Digital Ocean e Linode
  * Deploy em Linux Ubuntu
  * Apache + Nginx + uWSGI
  * Logcheck

* Monitoramento do servidor com Webmin
* Sistemas de alertas via Logcheck
  * Envios de emails
* Arquivos estáticos com S3 ou CDN

##
* Requisitos do sistema
  * Registro de todos os funcionarios da empresa
  * Controle de departamentos
  * Controle de ferias
  * Banco de horas
  * Registros de documentos ( Atestados médicos, contratos, scanner de documentos )

* Relatórios
  * Listagem de funcionários
  * Listagem de funcionarios por departamento
  * Listagem de funcionários de férias
  * Relatório de banco de horas