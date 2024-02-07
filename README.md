# Map_Target

## Descrição
Map_Target é um projeto Django que permite gerenciar alvos geográficos (pontos no mapa) através de um CRUD (Create, Read, Update, Delete).

## Funcionalidades
- Visualização de alvos em um mapa interativo.
- Adição, edição e exclusão de alvos.
- Detalhes completos de cada alvo, incluindo identificador, nome, latitude, longitude e data de expiração.

## Tecnologias Utilizadas
- Django
- PostgreSQL

## Configuração do Ambiente Local
1. Clone o repositório: `git clone https://github.com/Lf-hub/map_target.git`
2. Crie e ative um ambiente virtual: `python -m venv env` e `source env/bin/activate` (ou use `Scripts\activate` no Windows).
3. Instale as dependências: `pip install -r requirements.txt`
4. Aplique as migrações: `python manage.py migrate`
5. Crie um superusuário: `python manage.py createsuperuser`
6. Inicie o servidor: `python manage.py runserver`

Acesse a aplicação em (http://localhost:8000/) e o painel de administração em (http://localhost:8000/admin/).

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou fazer pull requests.

