@ECHO OFF
@ECHO Python Django Service is Starting ...
@ECHO.

cd ..
python manager.py runserver 127.0.0.1:9001

@ECHO.
pause
