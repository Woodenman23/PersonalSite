from website import create_app
from website import Flask


app = Flask(__name__)


app = create_app()

# only run server when i run this py file (not if it is inc as an import)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
