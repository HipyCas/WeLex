if [ ! -f requirements.txt ]; then
    pip freeze > requirements.txt
fi
cat requirements.txt | egrep "[a-zA-Z\-]+[0-9]?" -oh > packages.txt