import smtplib
from email.message import EmailMessage
import time
import random

nombre = {
    "mail":'joelmarinos8@gmail.com',
    "paswword":'ojky tpcr ejxx vfjs',
    "destino":["marinosjoel@ceautonomo.edu.co"]
}   
# nombre["destino"].append()

#FUNCIÓN 
def enviar_alerta_facturacion(saldo_actual):
    try:
        mensaje = EmailMessage()
        mensaje['Subject'] = '📌 Problema de facturación - Servicio iCloud+'
        mensaje['From'] =nombre["mail"]
        mensaje['To'] = nombre["destino"]

        # HTML del mensaje con estilo centrado y logo
        html_contenido = f"""
        <html>
        <body style="font-family: Arial, sans-serif; text-align: center; background-color: #f9f9f9; padding: 40px;">
            <div style="background-color: #ffffff; display: inline-block; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); max-width: 500px;">
                <p style="color: #111111;">Hola Joel,</p>
                <p style="color: #111111;">Detectamos un problema de facturación en tu cuenta <strong>iCloud+</strong>.</p>
                <p style="color: #111111;">Tu saldo actual es de <strong>${saldo_actual:.2f} CLP</strong>, lo cual no es suficiente para cubrir la suscripción mensual de <strong>$3.900 CLP</strong>.</p>
                <p style="color: #111111;">Para evitar la interrupción del servicio, por favor actualiza tu información de pago o incrementa el saldo de tu cuenta.</p>
                <a href="#" style="display: inline-block; margin-top: 20px; background-color: #0071e3; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold;">Actualizar información de pago</a>
                <p style="margin-top: 40px; color: #888;">Atentamente,<br>Soporte Apple</p>
            </div>
        </body>
        </html>
        """


        mensaje.add_alternative(html_contenido, subtype='html')

        #Enviar el correo
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(nombre["mail"], nombre["paswword"])
            smtp.send_message(mensaje)
            print("Correo HTML de alerta de facturación enviado correctamente.")
    except Exception as e:
        print(f" Error al enviar el correo: {e}")
# SIMULACIÓN 
saldo_minimo = 3900
intentos = 5

print(" Monitoreo de facturación iniciado...")

while intentos > 0:
    saldo_simulado = random.randint(1000, 5000)
    print(f" Saldo actual detectado: ${saldo_simulado}")

    if saldo_simulado < saldo_minimo:
        print(" Saldo insuficiente. Enviando alerta de facturación...")
        enviar_alerta_facturacion(saldo_simulado)
        break
    else:
        print(" Facturación al día.")

    intentos -= 1
    time.sleep(2)

print("Fin del monitoreo.")
