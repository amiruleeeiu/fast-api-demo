
python -m venv env
source env/Scripts/activate

pip install -r requirements.txt

uvicorn main:app --reload --port 5000
