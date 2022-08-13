copy %RECIPE_DIR%\python\setup.py src\python
%PYTHON% -m pip install -v src\python --no-deps
if errorlevel 1 exit 1
