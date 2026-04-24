# Sistema de Relatório Técnico ICETAR

Sistema web para geração de relatórios técnicos em campo, com preenchimento via celular, geração automática de PDF e envio por e-mail com anexo.

## 🎯 Objetivo

Automatizar o processo de relatórios técnicos, reduzindo retrabalho manual, padronizando os registros e agilizando o envio das informações para gestão.

## 🚀 Como funciona

1. O técnico acessa o formulário pelo celular  
2. Preenche os dados do atendimento  
3. Adiciona fotos e assinaturas digitais  
4. Clica em **Gerar PDF**  
5. O sistema:
   - baixa o PDF no dispositivo  
   - envia automaticamente o PDF por e-mail para o gestor  

## 🔗 Link do formulário

https://teixeira-pri.github.io/relatorio-tecnico/ordem-de-servico.html

## 🛠️ Tecnologias utilizadas

- HTML  
- CSS  
- JavaScript  
- jsPDF  
- Python  
- Flask  
- Flask-CORS  
- SMTP (Gmail)  
- GitHub Pages  
- Render  

## 📁 Estrutura do projeto
relatorio-tecnico/
├── ordem-de-servico.html # Frontend do formulário
├── app.py # Backend Flask para envio de e-mail
├── requirements.txt # Dependências Python
└── README.md # Documentação do projeto


## ⚙️ Deploy

### Frontend

- Hospedagem: GitHub Pages  
- URL: https://teixeira-pri.github.io/relatorio-tecnico/ordem-de-servico.html  

### Backend

- Hospedagem: Render  
- URL: https://relatorio-tecnico.onrender.com  

## 🔐 Variáveis de ambiente

O backend utiliza variáveis de ambiente para proteger as credenciais de envio de e-mail:
EMAIL_REMETENTE
EMAIL_SENHA_APP
EMAIL_DESTINATARIO


Nenhuma credencial sensível fica exposta no código público.

## 📝 Funcionalidades

- Formulário responsivo para uso em celular  
- Dados do cliente e equipamento  
- Registro do serviço executado  
- Upload de fotos  
- Assinatura digital do técnico e do cliente  
- Geração automática de PDF  
- Download do PDF no dispositivo  
- Envio automático do PDF por e-mail  

## 💻 Como rodar localmente

Instale as dependências:

pip install -r requirements.txt

Configure as variáveis de ambiente (Windows):

set EMAIL_REMETENTE=seu-email@gmail.com
set EMAIL_SENHA_APP=sua-senha-de-app
set EMAIL_DESTINATARIO=email-do-gestor@empresa.com

Execute o backend:
python app.py

O servidor será iniciado em:
http://localhost:5000

## ⚠️ Observações

O backend hospedado no plano gratuito do Render pode entrar em modo de espera após um período de inatividade. Por isso, a primeira requisição pode demorar alguns segundos.

📌 Status do projeto
✅ Projeto em produção
✅ Utilizado em campo
✅ Versão inicial funcional


## 👩‍💻 Desenvolvido por

Priscila Teixeira

Projeto desenvolvido para automatizar um processo real de relatórios técnicos em campo na ICETAR.
