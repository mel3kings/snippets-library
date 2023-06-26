# What?
- for local development usually when you try calling different domain names CORS will prevent you from doing so.
- you need to enable from Client CORS to enable application 

# How?
## React
- Add proxy to your Package.json
"proxy": "https://domain.execute-api.ap-southeast-2.amazonaws.com/",



## Python Flask Applications
```python
from flask_cors import CORS

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # Set maximum content length to 32MB
CORS(app)
```
