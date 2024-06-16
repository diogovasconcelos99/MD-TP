# Trabalho prático da UC de Mineração de Dados 2023/24

Desenvolvimento de um chatbot relativo a restaurantes e menus nos Estados Unidos da América, utilizando Python e tecnologia de inteligencia artificial generativa, através de dados obtidos da plataforma Uber Eats.

---

Membros do grupo:
- pg47153 Diogo Paulo Lopes de Vasconcelos
- pg39294 Nayana Júlia de Araújo Moreira
- pg52702 Ricardo Pereira Fonseca
- pg54708 Sérgio Manuel da Costa Ribeiro

---

Para preparar a base de dados vetorial, seguir os seguinte passos:

1. Fazer download dos datasets no link https://www.kaggle.com/datasets/ahmedshahriarsakib/uber-eats-usa-restaurants-menus?select=restaurants.csv, criar uma pasta denominada de 'datasets' e colocar os 2 CSVs transferidos na pasta

2. Correr o script 'code/dataset-preprocessing.py'

3. Correr o script 'code/csv-utf8-converter.py'

4. Correr o script 'code/vectorize-data.py' \
Opcional: Se quiser uma base de dados mais pequena, correr o script 'csv-illinois.py' e alterar o nome do csv no ficheiro 'vectorize-data.py'

> Nota: Estes scripts podem ser lentos.

---

Para correr a aplicação, utilizar o comando:

> streamlit run {pathfile}/code/app.py 

ou ir ao pathfile da pasta do código e correr

> streamlit run app.py 