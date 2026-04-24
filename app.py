from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import base64
import os
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": [
            "https://teixeira-pri.github.io",
            "http://localhost:*",
            "http://127.0.0.1:*"
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Configurações de e-mail (lidas das variáveis de ambiente do Render)
EMAIL_REMETENTE = os.environ.get('EMAIL_REMETENTE')
EMAIL_SENHA_APP = os.environ.get('EMAIL_SENHA_APP')
EMAIL_DESTINATARIO = os.environ.get('EMAIL_DESTINATARIO')

def enviar_email_com_pdf(pdf_base64, filename, dados):
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
    
    # Decodificar base64 e anexar PDF
    pdf_data = base64.b64decode(pdf_base64)
    parte = MIMEBase('application', 'pdf')
    parte.set_payload(pdf_data)
    encoders.encode_base64(parte)
    parte.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(parte)
    
    # Enviar via SMTP
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(EMAIL_REMETENTE, EMAIL_SENHA_APP)
    servidor.send_message(msg)
    servidor.quit()

@app.route('/enviar-relatorio', methods=['POST'])
def enviar_relatorio():
    """Endpoint que recebe PDF em base64 e envia por e-mail"""
    
    try:
        dados = request.json
        
        # Validação
        if not dados.get('pdf_base64'):
            return jsonify({'erro': 'PDF não foi enviado'}), 400
        
        if not dados.get('cliente') or not dados.get('tecnico'):
            return jsonify({'erro': 'Dados incompletos'}), 400
        
        # Enviar e-mail
        enviar_email_com_pdf(
            dados['pdf_base64'], 
            dados['filename'],
            {
                'cliente': dados['cliente'],
                'tecnico': dados['tecnico'],
                'data': dados['data']
            }
        )
        
        return jsonify({
            'sucesso': True,
            'mensagem': 'PDF enviado por e-mail com sucesso!'
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/teste', methods=['GET'])
def teste():
    """Endpoint de teste"""
    return jsonify({'status': 'Backend funcionando!', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
