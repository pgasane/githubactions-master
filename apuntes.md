# ls ${{ github.workspace }}
Es muy importante porque indica la ruta pública del Repositorio en GitHub

# Cada indentación implica jerarquías
jobs, steps y acciones (name, uses)

# Todo el trabajo que se puede hacer con GitHub Actions está en el GitHub Marketplace
Contiene muchos ejemplos: github.com/marketplace
Cuesta crearlo al principio, pero luego sirve para todos los proyectos
En definitiva, permite crear Flujos de Trabajo potentes de distribución de paquetes CI/CD 

# Para comentar en YML se usa la almohadilla

# GITHUB CLAVE DE ACCESO
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

# GITHUB ENTORNO DE EJECUCIÓN
El código se ejecuta en un CONTENEDOR con la configuración específica que se necesita de forma transparente al programador (no tenemos que preocuparnos del hard ni del entorno)

# PARA VER EN VIVO LA EJECUCIÓN DEL RUN
"git run watch" va siguiendo el proceso con una presentación muy chula
(base) GSN:gh-master pgasane$ gh run list
STATUS  TITLE                                                                   WORKFLOW             BRANCH  EVENT  ID          ELAPSED  AGE
✓       Push para ver el funcionamiento de "git run watch"                      Building             master  push   3190884986  29s      4m
✓       pgasane is testing out GitHub Actions 🚀                                GitHub Actions Demo  master  push   3190884983  9s       4m
✓       pgasane is testing out GitHub Actions 🚀                                GitHub Actions Demo  master  push   3190860983  21s      9m
✓       Añadimos instalar poetry, ejecutar poetry build y mostrar la ruta del…  Building             master  push   3190860980  37s      9m
✓       Añadir instalación de Poetry al build.yml y Ejecutar ls {{ github.wor…  Building             master  push   3190795652  16s      20m
✓       pgasane is testing out GitHub Actions 🚀                                GitHub Actions Demo  master  push   3190795648  17s      20m
✓       pgasane is testing out GitHub Actions 🚀                                GitHub Actions Demo  master  push   3190638203  13s      46m
✓       Carga Apuntes Verificar GitHub funciona                                 Building             master  push   3190638202  11s      46m
✓       pgasane is testing out GitHub Actions 🚀                                GitHub Actions Demo  master  push   3187496862  14s      10h

# RELEASES. ETIQUETANDO VERSIONES
- ETIQUETADO: se usa para subir los BINARIOS de nuestro trabajo
- Usaremos github-actions para automatizar el proceso
- Podemos subir binarios sin códigos fuente o incluirlos (decisión del autor)
- Los archivos yml se ejecutan todos si están en la carpeta workflows
- No existe orden ni interdependencia entre ellos. En nuestro caso build.yml y menganito.yml NO tiene relación alguna
- Diferencia entre JOB y WORKFLOWS: los workflows se pueden ejecutar en PARALELO. Los STEPS son secuenciales
- Nota Profesor: recomiendo que git push siempre lo hagan a mano
- gh run watch
- gh run list
- Todos los desarrollos de software usan GIT
- Material de Lectura GIT: https://git-scm.com/book/en/v2
- # TAG: se usa para establecer LAS NUEVAS VERSIONES de un desarrollo
- # IMPORTANTE: GIT no mira el código del proyecto. Por eso necesita la ETIQUETA para saber la Versión
- # ETIQUETAS ANOTADAS (Annotated Tags): permiten poner comentarios
    git tag -a V1.4 -m "my version 1.4"
    git log # Vemos los tag creados
    git push --follow-tags  # Revisa los commit y solo sube las ANOTADAS que no se hayan subido. La idea es ANOTAR LAS TAGS IMPORTANTES
- # RECOMENDACIÓN PROFESOR: 
    git push --global push.followTags true. # Esto hace que las anteriores tag anotadas olvidadas se suban al hacer el push de la tag
- # git push origin v1.5 NO SUBE LA RAMA MÁSTER... No recomendada

# BORRANDO LOS FICHEROS ANTIGUOS DE LA CARPETA DIST
- Se añade gitignore para eliminar toda la "basura" de las ejecuciones e instalaciones








