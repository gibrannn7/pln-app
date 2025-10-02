C:\Users\USER\Documents\pln_app>flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
[2025-10-02 06:06:26,501] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 2190, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 1486, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 1484, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 1469, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 284, in decorated_view
    elif not current_user.is_authenticated:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\werkzeug\local.py", line 311, in __get__
    obj = instance._get_current_object()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\werkzeug\local.py", line 515, in _get_current_object
    return get_name(local())
                    ^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 25, in <lambda>
    current_user = LocalProxy(lambda: _get_user())
                                      ^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 370, in _get_user
    current_app.login_manager._load_user()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\login_manager.py", line 364, in _load_user
    user = self._user_callback(user_id)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\Documents\pln_app\app\__init__.py", line 57, in load_user
    return User.query.get(int(user_id))
           ^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_sqlalchemy\model.py", line 30, in __get__
    return cls.query_class(
           ^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\query.py", line 275, in __init__
    self._set_entities(entities)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\query.py", line 288, in _set_entities
    coercions.expect(
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\sql\coercions.py", line 389, in expect
    insp._post_inspect
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 1253, in __get__
    obj.__dict__[self.__name__] = result = self.fget(obj)
                                           ^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2711, in _post_inspect
    self._check_configure()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2388, in _check_configure
    _configure_registries({self.registry}, cascade=True)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4204, in _configure_registries
    _do_configure_registries(registries, cascade)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4245, in _do_configure_registries
    mapper._post_configure_properties()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2405, in _post_configure_properties
    prop.init()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\interfaces.py", line 584, in init
    self.do_init()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\relationships.py", line 1647, in do_init
    self._generate_backref()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\relationships.py", line 2075, in _generate_backref
    raise sa_exc.ArgumentError(
sqlalchemy.exc.ArgumentError: Error creating backref 'user' on relationship 'User.officer': property of that name exists on mapper 'Mapper[Officer(officers)]'
127.0.0.1 - - [02/Oct/2025 06:06:26] "GET / HTTP/1.1" 500 -
Error on request:
Traceback (most recent call last):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 2190, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 1486, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 1484, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 1469, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 284, in decorated_view
    elif not current_user.is_authenticated:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\werkzeug\local.py", line 311, in __get__
    obj = instance._get_current_object()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\werkzeug\local.py", line 515, in _get_current_object
    return get_name(local())
                    ^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 25, in <lambda>
    current_user = LocalProxy(lambda: _get_user())
                                      ^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 370, in _get_user
    current_app.login_manager._load_user()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\login_manager.py", line 364, in _load_user
    user = self._user_callback(user_id)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\Documents\pln_app\app\__init__.py", line 57, in load_user
    return User.query.get(int(user_id))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_sqlalchemy\model.py", line 30, in __get__
    return cls.query_class(
           ^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\query.py", line 275, in __init__
    self._set_entities(entities)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\query.py", line 288, in _set_entities
    coercions.expect(
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\sql\coercions.py", line 389, in expect
    insp._post_inspect
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 1253, in __get__
    obj.__dict__[self.__name__] = result = self.fget(obj)
                                           ^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2711, in _post_inspect
    self._check_configure()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2388, in _check_configure
    _configure_registries({self.registry}, cascade=True)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4204, in _configure_registries
    _do_configure_registries(registries, cascade)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4245, in _do_configure_registries
    mapper._post_configure_properties()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2405, in _post_configure_properties
    prop.init()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\interfaces.py", line 584, in init
    self.do_init()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\relationships.py", line 1647, in do_init
    self._generate_backref()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\relationships.py", line 2075, in _generate_backref
    raise sa_exc.ArgumentError(
sqlalchemy.exc.ArgumentError: Error creating backref 'user' on relationship 'User.officer': property of that name exists on mapper 'Mapper[Officer(officers)]'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\werkzeug\serving.py", line 364, in run_wsgi
    execute(self.server.app)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\werkzeug\serving.py", line 325, in execute
    application_iter = app(environ, start_response)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 2213, in __call__
    return self.wsgi_app(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 2193, in wsgi_app
    response = self.handle_exception(e)
               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 1399, in handle_exception
    server_error = self.ensure_sync(handler)(server_error)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\Documents\pln_app\app\routes\main.py", line 43, in internal_error
    return render_template('errors/500.html'), 500
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\templating.py", line 151, in render_template
    return _render(app, template, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\templating.py", line 128, in _render
    app.update_template_context(context)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask\app.py", line 737, in update_template_context
    context.update(func())
                   ^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 405, in _user_context_processor
    return dict(current_user=_get_user())
                             ^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\utils.py", line 370, in _get_user
    current_app.login_manager._load_user()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_login\login_manager.py", line 364, in _load_user
    user = self._user_callback(user_id)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\Documents\pln_app\app\__init__.py", line 57, in load_user
    return User.query.get(int(user_id))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\flask_sqlalchemy\model.py", line 30, in __get__
    return cls.query_class(
           ^^^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\query.py", line 275, in __init__
    self._set_entities(entities)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\query.py", line 288, in _set_entities
    coercions.expect(
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\sql\coercions.py", line 389, in expect
    insp._post_inspect
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 1253, in __get__
    obj.__dict__[self.__name__] = result = self.fget(obj)
                                           ^^^^^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2711, in _post_inspect
    self._check_configure()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 2388, in _check_configure
    _configure_registries({self.registry}, cascade=True)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4204, in _configure_registries
    _do_configure_registries(registries, cascade)
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\site-packages\sqlalchemy\orm\mapper.py", line 4241, in _do_configure_registries
    raise e
sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'Mapper[User(users)]'. Original exception was: Error creating backref 'user' on relationship 'User.officer': property of that name exists on mapper 'Mapper[Officer(officers)]'