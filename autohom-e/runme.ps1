if (!(Test-Path -Path .\venv)) {
    python -m venv .\venv
}

.\venv\Scripts\pip3.exe install -r requirements.txt
.\venv\Scripts\python.exe main.py local