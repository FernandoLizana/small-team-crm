import os

CONTENT_TEMPLATES = {
    "lanzamiento": {
        "label": "Lanzamiento",
        "tema": "Presentación de un producto o servicio nuevo del negocio",
        "hashtags": "#novedad #lanzamiento #pyme #emprendimiento",
    },
    "cliente": {
        "label": "Caso de cliente",
        "tema": "Historia breve de un cliente y el problema que resolvió",
        "hashtags": "#clientes #testimonio #pyme #servicio",
    },
    "tip": {
        "label": "Tip útil",
        "tema": "Consejo práctico relacionado con el rubro del negocio",
        "hashtags": "#tips #consejos #pyme #aprende",
    },
    "equipo": {
        "label": "Detrás de escena",
        "tema": "Cómo trabaja el equipo en el día a día",
        "hashtags": "#equipo #detrasdeescena #pyme #trabajo",
    },
    "servicio": {
        "label": "Promo servicio",
        "tema": "Invitación suave a agendar o comprar el servicio principal",
        "hashtags": "#servicio #agenda #pyme #emprendimiento",
    },
}


def brand_signature() -> str:
    return (os.environ.get("BRAND_SIGNATURE") or "").strip()


def template_by_key(key: str | None):
    if not key:
        return None
    return CONTENT_TEMPLATES.get(key)
