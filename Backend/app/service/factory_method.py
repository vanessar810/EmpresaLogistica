from app.entity.envio_terrestre import EnvioTerrestre
from app.entity.envio_maritimo import EnvioMaritimo

class EnvioFactory:
    @staticmethod
    def crear_envio(tipo: str, **kwargs):
        if tipo == "terrestre":
            return EnvioTerrestre(**kwargs)
        elif tipo == "maritimo":
            return EnvioMaritimo(**kwargs)
        else:
            raise ValueError("Tipo de envío no soportado")