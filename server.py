from app import app 

from app.controllers.dojos import dojos
from app.controllers.ninjas import ninjas

app.register_blueprint(dojos)
app.register_blueprint(ninjas)

if __name__ == "__main__":
    app.run(debug=True)