C:\Users\USER\Documents\pln_app>flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: While importing 'app', an ImportError was raised:

Traceback (most recent call last):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\cli.py", line 245, in locate_app
    __import__(module_name)
  File "C:\Users\USER\Documents\pln_app\app\__init__.py", line 4, in <module>
    from flask_login import LoginManager
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\__init__.py", line 12, in <module>
    from .login_manager import LoginManager
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\login_manager.py", line 33, in <module>
    from .utils import _create_identifier
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 14, in <module>
    from werkzeug.urls import url_decode
ImportError: cannot import name 'url_decode' from 'werkzeug.urls' (C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\werkzeug\urls.py)