from .user_controller import user_bp
from .sensor_controller import sensor_bp
from .consumption_controller import consumption_bp

# Exporta los Blueprints para registro en routes.py
__all__ = ['user_bp', 'sensor_bp', 'cosumption_bp']