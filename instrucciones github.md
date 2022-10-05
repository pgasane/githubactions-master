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