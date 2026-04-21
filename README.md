# 🔧 Ordem de Serviço — Relatório Técnico de Campo

Formulário web responsivo para técnicos registrarem atendimentos em campo, coletar assinaturas digitais do cliente e do técnico, e gerar um PDF profissional automaticamente — tudo sem depender de internet ou aplicativo instalado.

---

## ✨ Funcionalidades

- **Fluxo em 4 etapas guiadas:** Dados do cliente e técnico → Detalhes do serviço → Assinaturas digitais → Revisão e geração do PDF
- **Validação em tempo real** com alertas toast antes de avançar cada etapa
- **Assinatura digital via toque ou mouse** para cliente e técnico, com canvas de alta resolução
- **Status do atendimento** com seleção visual: Concluído, Pendente ou Não Resolvido
- **Geração de PDF A4** com cabeçalho, seções organizadas, miniaturas das assinaturas e rodapé com número da OS e timestamp
- **Número de OS automático** gerado a cada abertura do formulário (ex.: `OS-4271`)
- **100% offline** após o primeiro carregamento — sem backend, sem banco de dados
- **Design responsivo** otimizado para smartphones (viewport fixo, touch-action configurado)

---

## 📋 Campos do Formulário

**Etapa 1 — Dados**
- Nome / Empresa do cliente *(obrigatório)*
- Telefone e CPF/CNPJ
- Endereço *(obrigatório)*
- Nome do técnico *(obrigatório)*, matrícula e data *(obrigatório)*

**Etapa 2 — Serviço**
- Tipo de serviço: Instalação, Manutenção Preventiva, Manutenção Corretiva, Configuração, Visita Técnica ou Outro *(obrigatório)*
- Equipamento / local atendido
- Descrição do problema relatado pelo cliente
- Serviço executado *(obrigatório)*
- Peças e materiais utilizados
- Status do atendimento *(obrigatório)*
- Horário de início e término

**Etapa 3 — Assinaturas**
- Assinatura digital do cliente
- Assinatura digital do técnico

**Etapa 4 — Revisar e Gerar PDF**
- Resumo completo da OS
- Miniaturas das assinaturas para conferência
- Botão para gerar e baixar o PDF

---

## 🚀 Como usar

1. Abra o arquivo `ordem-de-servico.html` diretamente no navegador do celular ou computador — **não é necessário servidor**
2. Preencha as 4 etapas do formulário
3. Colete a assinatura do cliente e assine como técnico
4. Revise os dados e clique em **"Gerar PDF e Finalizar"**
5. O PDF é baixado automaticamente com o nome `OS-XXXX_NomeCliente.pdf`

> **Dica:** Salve o arquivo na tela inicial do celular (PWA-like) para acesso rápido em campo.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| HTML5 | Estrutura e semântica |
| CSS3 | Layout responsivo, variáveis, animações |
| JavaScript (ES6+) | Lógica, validação, canvas e geração do PDF |
| [jsPDF 2.5.1](https://github.com/parallax/jsPDF) | Geração do documento PDF no navegador |
| Google Fonts — IBM Plex Sans / Mono | Tipografia |

Nenhum framework, nenhuma dependência local. Um único arquivo `.html`.

---

## 📄 Estrutura do PDF gerado

```
┌─────────────────────────────────────┐
│  ORDEM DE SERVIÇO   OS-XXXX  Data   │  ← Cabeçalho azul
├─────────────────────────────────────┤
│  DADOS DO CLIENTE                   │
│  TÉCNICO RESPONSÁVEL                │
│  SERVIÇO EXECUTADO                  │
│  ASSINATURAS  [Cliente] [Técnico]   │
├─────────────────────────────────────┤
│  OS-XXXX · Gerado em DD/MM/AAAA HH:MM │  ← Rodapé
└─────────────────────────────────────┘
```

---

## 📁 Estrutura do repositório

```
relatorio-tecnico/
└── ordem-de-servico.html   # Aplicação completa (HTML + CSS + JS)
```

---

## 🔒 Privacidade

Todos os dados são processados **localmente no navegador**. Nenhuma informação é enviada para servidores externos. O PDF é gerado e salvo diretamente no dispositivo do usuário.

---

## 📌 Compatibilidade

Testado nos navegadores móveis modernos: Chrome para Android, Safari para iOS e Firefox. Requer conexão à internet apenas no primeiro acesso, para carregar a fonte IBM Plex e a biblioteca jsPDF via CDN.
