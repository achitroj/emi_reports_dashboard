from flask import Flask
from dash import Dash
import os


server = Flask('severn_filter')

# generate assets folder path
assets_path = os.getcwd() + '\\assets'

# BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
# BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/darkly/bootstrap.min.css"
# BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/litera/bootstrap.min.css"
# BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/minty/bootstrap.min.css"
# app = dash.Dash(external_stylesheets=[BS])

# I like this one below
BS = "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/minty/bootstrap.min.css"
print(assets_path)
app = Dash(__name__, server=server, suppress_callback_exceptions=True, external_stylesheets=[BS],
           assets_folder=assets_path)
