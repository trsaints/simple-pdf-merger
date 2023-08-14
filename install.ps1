Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
$script = New-Object Net.WebClient
$script.DownloadString("https://chocolatey.org/install.ps1")
Invoke-WebRequest https://chocolatey.org/install.ps1 -UseBasicParsing | Invoke-Expression
. $PROFILE
choco upgrade chocolatey
choco install -y --force python3
py -m pip install --upgrade pip
py -m pip install pymupdf
py -m py_compile gui.py
