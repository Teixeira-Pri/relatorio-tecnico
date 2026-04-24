from flask import Flask, request, jsonify
from flask_cors import CORS
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configurações de e-mail (VOCÊ VAI SUBSTITUIR ESSES VALORES)
EMAIL_REMETENTE = "seu-email@gmail.com"
EMAIL_SENHA_APP = "sua-senha-de-app-aqui"  # Senha de app do Gmail, não a senha normal
EMAIL_DESTINATARIO = "email-do-gestor@empresa.com"

def gerar_pdf(dados):
    """Gera PDF com os dados do relatório"""
    
    filename = f"RST_{dados['cliente'].replace(' ', '_')}_{datetime.now().strftime('%d-%m-%Y')}.pdf"
    filepath = f"/tmp/{filename}"
    
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    
    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height - 50, "RELATÓRIO DE SERVIÇO TÉCNICO")
    
    # Linha divisória
    c.line(30, height - 60, width - 30, height - 60)
    
    y = height - 90
    
    # Dados do cliente
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "CLIENTE:")
    c.setFont("Helvetica", 11)
    c.drawString(40, y - 20, dados['cliente'])
    y -= 50
    
    # Dados do técnico
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "TÉCNICO RESPONSÁVEL:")
    c.setFont("Helvetica", 11)
    c.drawString(40, y - 20, dados['tecnico'])
    y -= 50
    
    # Data
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "DATA:")
    c.setFont("Helvetica", 11)
    c.drawString(40, y - 20, dados['data'])
    y -= 50
    
    # Serviço executado
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "SERVIÇO EXECUTADO:")
    c.setFont("Helvetica", 10)
    
    # Quebra de texto longo
    texto = dados.get('servico', 'Não informado')
    max_width = width - 80
    palavras = texto.split(' ')
    linha_atual = ""
    y -= 25
    
    for palavra in palavras:
        teste = linha_atual + palavra + " "
        if c.stringWidth(teste, "Helvetica", 10) < max_width:
            linha_atual = teste
        else:
            c.drawString(40, y, linha_atual)
            y -= 15
            linha_atual = palavra + " "
            if y < 100:  # Nova página se acabar o espaço
                c.showPage()
                y = height - 50
    
    if linha_atual:
        c.drawString(40, y, linha_atual)
    
    y -= 40
    
    # Rodapé
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawCentredString(width/2, 30, f"Gerado automaticamente em {datetime.now().strftime('%d/%m/%Y às %H:%M')}")
    
    c.save()
    
    return filepath, filename

def enviar_email_com_anexo(pdf_path, pdf_filename, dados):
    """Envia e-mail com PDF anexado via SMTP"""
    
    # Configurar mensagem
    msg = MIMEMultipart()
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg['Subject'] = f"Novo Relatório Técnico - {dados['cliente']}"
    
    # Corpo do e-mail
    corpo = f"""
    Olá,
    
    Um novo relatório técnico foi gerado:
    
    Cliente: {dados['cliente']}
    Técnico: {dados['tecnico']}
    Data: {dados['data']}
    
    O PDF está em anexo.
    
    ---
    Sistema de Relatórios ICETAR
    """
    
    msg.attach(MIMEText(corpo, 'plain'))
    
    # Anexar PDF
    with open(pdf_path, 'rb') as arquivo:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(arquivo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={pdf_filename}')
        msg.attach(parte)
    
    # Enviar via SMTP
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(EMAIL_REMETENTE, EMAIL_SENHA_APP)
    servidor.send_message(msg)
    servidor.quit()

@app.route('/enviar-relatorio', methods=['POST'])
def enviar_relatorio():
    """Endpoint que recebe dados, gera PDF e envia por e-mail"""
    
    try:
        dados = request.json
        
        # Validação básica
        if not dados.get('cliente') or not dados.get('tecnico'):
            return jsonify({'erro': 'Cliente e técnico são obrigatórios'}), 400
        
        # Gerar PDF
        pdf_path, pdf_filename = gerar_pdf(dados)
        
        # Enviar e-mail
        enviar_email_com_anexo(pdf_path, pdf_filename, dados)
        
        # Limpar arquivo temporário
        os.remove(pdf_path)
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'PDF gerado e enviado com sucesso!',
            'arquivo': pdf_filename
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/teste', methods=['GET'])
def teste():
    """Endpoint de teste para verificar se o servidor está rodando"""
    return jsonify({'status': 'Backend funcionando!', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
