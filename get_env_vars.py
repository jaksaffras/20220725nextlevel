import os

for variable_name in 'ORACLE_SID', 'BLUB', 'SPAM', 'USER', 'LANG', 'DJANGO_READ_DOT_ENV_FILE':
    print(variable_name, os.getenv(variable_name))
