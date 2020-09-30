from flask import Blueprint 

bp = Blueprint('main',__name__)
# print(__name__)  app.main
from app.main import routes