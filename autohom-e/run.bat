if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
	Powershell.exe -executionpolicy remotesigned -File  .\runme.ps1
exit