from plyer import notification


def enviar_notificacion(titulo, mensaje):
    notification.notify(
        title=titulo,
        message=mensaje
    )