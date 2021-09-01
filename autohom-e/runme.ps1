$Venv = '.\venv'

if (!(Test-Path -Path $Venv)) {
    python -m venv $Venv
}

Start-Process $Venv\Scripts\activate.bat

pip install -r requirements.txt

python main.py local