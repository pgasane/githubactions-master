Comprobar en consola:

- git: instalar con conda
- gh: instalar con conda
- poetry: se instala con pip

conda install gh  --channel conda-forge 

pip install poetry

Si os sale este error: ImportError: `pip install --upgrade pywin32==228`

# Loguearnos en GitHub
gh auth login
1. GitHub.com
2. SSH
3.A. Generate a new SSH key to add to your GitHub account? Y
3.B. Ya hay una clave y la elegís (normalmente primera opción)
4. Title. Pulsar Enter
5. Login with a web browser

# Para comprobar GH:
gh ssh-key list

# Comandos de git

Crear un repositorio: `git init`
Crear repositorio en GH: `gh repo create`
    1. Push an existing local repository to GitHub
    2. Path to local repository: Pulsad ENTER
    3. Nombre del repositorio: El que queráis: gh, githubactions, proyecto, ...
    4. Descripción: Pulsad ENTER
    5. Visibility: Elegid "Public"
    6. Add a remote: Y
    7- What should the new remote be called?: ENTER

Ya debería funcionar. En tu página web de GitHub ya tienes un repositorio. Copia la URL en el chat.

# "Commit = Cambio"
- Creáis un fichero llamdo README.md
- Escribid: "Este es nuestro primer proyecto con CI/CD"
- Guardar fichero (CTRL+S o CMD+S)
- Escribimos git status en consola
- `git add README.md`
- git commit -m "primer commit"

Si os pide esto: 
git config --global user.email "alex@alex.com"
git config --global user.name "Alejandro"

Poned vuestro nombre y haced el commit

# Push: enviar a github mis commits
- `git push`. Si es la primera vez te pide que
ejecutes un comando más largo

- Id a la página de vuestro github para ver el fichero README

Si os pide: "Are you sure you want to continue connecting (yes/no/[fingerprint])?": yes

# ¿Qué hacemos cuando el github se desconecta?
# "gh auth refresh -h github.com -s admin:public_key"
- (base) GSN:gh-master pgasane$ gh ssh-key list
HTTP 404: Not Found (https://api.github.com/user/keys?per_page=100)
This API operation needs the "admin:public_key" scope. To request it, run:  gh auth refresh -h github.com -s admin:public_key

- (base) GSN:gh-master pgasane$ "gh auth refresh -h github.com -s admin:public_key"

! First copy your one-time code: E875-B532
Press Enter to open github.com in your browser... 
✓ Authentication complete.

- (base) GSN:gh-master pgasane$ gh ssh-key list
TITLE       ID        KEY                                                                               ADDED
GitHub CLI  71700713  ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINy/i/Q/EgFo3ujPXpQ7WcG9fzGa0x41/vF/+L5A+tP/  6d

- (base) GSN:gh-master pgasane$ git push
Enumerating objects: 25, done.
Counting objects: 100% (25/25), done.
Delta compression using up to 4 threads
Compressing objects: 100% (21/21), done.
Writing objects: 100% (21/21), 2.42 KiB | 2.42 MiB/s, done.
Total 21 (delta 7), reused 0 (delta 0)
remote: Resolving deltas: 100% (7/7), completed with 1 local object.
To github.com:pgasane/githubactions-master.git
   14ac9c6..04ae209  master -> master

# DOCKER gh auth login
# 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
(base) jovyan@c86d58b943e0:~$ gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations? SSH
? Upload your SSH public key to your GitHub account? /home/jovyan/.ssh/id_ed25519.pub
? Title for your SSH key: GitHub CLI
? How would you like to authenticate GitHub CLI? Paste an authentication token
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
The minimum required scopes are 'repo', 'read:org', 'admin:public_key'.
? Paste your authentication token: ****************************************
- gh config set -h github.com git_protocol ssh
✓ Configured git protocol
✓ Uploaded the SSH key to your GitHub account: /home/jovyan/.ssh/id_ed25519.pub
✓ Logged in as pgasane
