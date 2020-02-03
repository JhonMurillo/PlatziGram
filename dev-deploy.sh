echo "Installing virtual env platzigram..."
python3 -m venv platzigram
echo "Activate Virtual Env for: " $OSTYPE "..."

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    source platzigram/bin/activate
elif [[ "$OSTYPE" == "darwin"* ]]; then
    source platzigram/bin/activate
elif [[ "$OSTYPE" == "cygwin" ]]; then
    /platzigram/Scripts/activate
elif [[ "$OSTYPE" == "msys" ]]; then
    /platzigram/Scripts/activate
elif [[ "$OSTYPE" == "win32" ]]; then
    /platzigram/Scripts/activate
elif [[ "$OSTYPE" == "freebsd"* ]]; then
    /platzigram/Scripts/activate
else
    /platzigram/Scripts/activate
fi

echo "Installing requirements..."
pip install -r requirements.txt

echo "Making migrations..."
python manage.py makemigrations

echo "Migrating..."
python manage.py migrate

echo "Deploy server..."
python manage.py runserver