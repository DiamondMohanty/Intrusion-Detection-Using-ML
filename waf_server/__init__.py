from app import config, app
app.run(port=config['PORT'], debug=config['DEBUG'])