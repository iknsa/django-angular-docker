*****
TEST python + Django + angular
*****

Using Python Django REST framework Angular, do an application allowing to:

1. Start project with django `docker <https://docs.docker.com/compose/django/>`_.
2. Use DjangoREST framework (improve django docker setup)
3. Allow to subscribe as a django/user using the authorization of google allowing to access emails
    * https://github.com/omab/python-social-auth
    * http://django-social-auth.readthedocs.io/en/latest/backends/google.html
4. Calls the last 100 emails
    * https://developers.google.com/gmail/api/quickstart/python
    * don't forget to init credential on google
    * https://console.developers.google.com/apis/dashboard
5. Display the 100 emails
6. Allow to logout
6. Allow to logback in

You will provide the source code of your app so that it can be tested