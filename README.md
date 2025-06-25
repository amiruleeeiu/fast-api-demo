
python -m venv env

//windows
source env/Scripts/activate

//ubuntu
source env/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload --port 5000
