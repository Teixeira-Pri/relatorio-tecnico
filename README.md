# Sistema de Relatório Técnico ICETAR

Sistema completo de geração de relatórios técnicos em campo com envio automático por e-mail.

## 🎯 Como Funciona

1. **Técnico em campo** acessa o formulário pelo celular
2. Preenche dados do serviço (cliente, equipamentos, fotos, assinaturas)
3. Clica em **"Gerar PDF"**
4. Sistema automaticamente:
   - Baixa o PDF no celular do técnico
   - Envia o PDF por e-mail para o gestor

## 🔗 Link do Formulário

```
https://teixeira-pri.github.io/relatorio-tecnico/ordem-de-servico.html
```

## 📁 Estrutura do Projeto

```
relatorio-tecnico/
├── ordem-de-servico.html    # Formulário completo (frontend)
├── app.py                    # Backend Flask (envio de e-mail)
├── requirements.txt          # Dependências Python
└── README.md                 # Este arquivo
```

## 🔒 Uso e Direitos Autorais

⚠️ **AVISO IMPORTANTE**

Este projeto foi desenvolvido como **solução interna para a ICETAR** e está disponível publicamente apenas para fins de **portfólio profissional** e **demonstração técnica**.

**Restrições:**
- ❌ Uso comercial não autorizado
- ❌ Cópia ou redistribuição do código
- ❌ Adaptação ou criação de trabalhos derivados
- ❌ Uso da marca ICETAR em outros contextos

**Permissões:**
- ✅ Visualizar o código-fonte
- ✅ Estudar a implementação técnica
- ✅ Referenciar como exemplo educacional

Para licenciamento comercial ou outros usos, entre em contato através do [LinkedIn](https://www.linkedin.com/in/priscila-teixeira) ou GitHub.

Todos os direitos reservados © 2024-2026 Priscila Teixeira

---

## 🚀 Deploy

### Frontend (GitHub Pages)
- **URL:** https://teixeira-pri.github.io/relatorio-tecnico/ordem-de-servico.html
- **Hospedagem:** GitHub Pages (gratuito)
- **Atualização:** Automática a cada commit na branch `main`

### Backend (Render.com)
- **URL:** https://relatorio-tecnico.onrender.com
- **Hospedagem:** Render.com (plano gratuito)
- **Variáveis de ambiente necessárias:**
  - `EMAIL_REMETENTE` - E-mail Gmail que envia
  - `EMAIL_SENHA_APP` - Senha de app do Gmail (16 caracteres)
  - `EMAIL_DESTINATARIO` - E-mail do gestor que recebe

## ⚙️ Configuração do Backend

### 1. Gerar Senha de App do Gmail

1. Acesse: https://myaccount.google.com/apppasswords
2. Ative verificação em 2 etapas (se ainda não ativou)
3. Crie uma senha de app:
   - Nome: "Relatorio ICETAR"
   - Copie a senha de 16 caracteres

### 2. Configurar Variáveis no Render

1. Acesse o painel do Render: https://dashboard.render.com
2. Selecione o serviço `relatorio-tecnico`
3. Vá em **Environment** no menu lateral
4. Configure as 3 variáveis:
   - `EMAIL_REMETENTE` → seu-email@gmail.com
   - `EMAIL_SENHA_APP` → senha-de-16-caracteres
   - `EMAIL_DESTINATARIO` → email-do-gestor@empresa.com
5. Clique em **Save Changes**

## 🔒 Segurança

- ✅ Nenhuma credencial está exposta no código público
- ✅ Todas as credenciais são lidas de variáveis de ambiente
- ✅ Backend usa HTTPS (comunicação criptografada)
- ✅ Senhas de app do Gmail são revogáveis a qualquer momento

## 🛠️ Desenvolvimento Local (Opcional)

Se quiser rodar o backend localmente para testes:

```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente (Windows)
set EMAIL_REMETENTE=seu-email@gmail.com
set EMAIL_SENHA_APP=sua-senha-de-app
set EMAIL_DESTINATARIO=email-gestor@empresa.com

# Rodar servidor
python app.py
```

O servidor vai rodar em `http://localhost:5000`

## 📝 Funcionalidades do Formulário

- ✅ Logo da ICETAR
- ✅ Dados do cliente e técnico
- ✅ Informações de equipamentos (compressor/vácuo)
- ✅ Upload de até 4 fotos
- ✅ Assinaturas digitais (técnico e cliente)
- ✅ Geração de PDF profissional
- ✅ Download automático do PDF
- ✅ Envio automático por e-mail com PDF anexado

## ⚡ Observações Importantes

- **Primeira requisição:** O backend no Render (plano gratuito) "dorme" após 15 minutos de inatividade. A primeira requisição após isso pode demorar ~30 segundos para acordar. Depois fica rápido.
- **Limite de e-mails:** Não há limite no sistema, mas o Gmail pode ter limites de envio (geralmente 500 e-mails/dia para contas pessoais).

## 🐛 Resolução de Problemas

### E-mail não está chegando?

1. Verifique se as variáveis de ambiente estão configuradas corretamente no Render
2. Confira a caixa de spam do destinatário
3. Verifique se a senha de app do Gmail está correta
4. Veja os logs no Render para identificar erros

### PDF não está sendo gerado?

1. Verifique se o formulário está sendo acessado via HTTPS (GitHub Pages)
2. Teste em outro navegador
3. Limpe o cache do navegador

## 📞 Suporte

Para dúvidas ou problemas, entre em contato com a equipe de TI da ICETAR.

---

## 📄 Licença

Este projeto está sob licença restritiva. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

**Copyright © 2024-2026 Priscila Teixeira - Todos os direitos reservados**

---

**Desenvolvido por Priscila Teixeira para ICETAR** | Sistema de Relatórios Técnicos v1.0

[LinkedIn](https://www.linkedin.com/in/priscila-teixeira) • [GitHub](https://github.com/Teixeira-Pri)
