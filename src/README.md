#Exemplo de criação de uma API python

1º Necessario ter o python instaldo          
    - https://www.python.org/downloads/
2º intalar o framwWork do flask pelo cmd     
    - pip install flask  
3º  Para rodar a aplicação usar o camando no direotrio do projeto 
    - python .\_init_.py


4º Rota padrão
    - http://127.0.0.1:5000/

5° Rota de simulação de cadastro
    - http://127.0.0.1:5000/Cadastra/Aluno
    
    Exemplo Request[body-json]
    {
	    "Nome":"João",
	    "Sobrenome": "Felipe"
    }