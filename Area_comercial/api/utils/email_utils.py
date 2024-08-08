from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email(subject, to_email, context, html_template, text_template=None):
    from_email = 'barrientosantiago1090@gmail.com'  # Cambia esto por tu correo desde el cual enviarás los correos

    # Renderiza las plantillas HTML y de texto
    html_content = render_to_string(html_template, context)
    text_content = strip_tags(html_content) if text_template is None else render_to_string(text_template, context)
    
    # Crea el correo en ambos formatos
    email = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        [to_email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
