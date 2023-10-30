# Music Generator

**Acerca de este proyecto**
- Este es un proyecto muy simple que se basa en redes neuronales, mas especificamente utiliza modelos LSTM para poder, dado una ***seed*** inicial, predecir como puede seguir una melodia.
- El proyecto puede ser mejorado significativamente ya que el nivel de complejidad musical tratada es muy poca si no es que solo  minima.
- El generador ha sido entrenado solo con musica clasica.


**Todos los iconos los saque de la siguiente pagina web** https://www.flaticon.es/

## Informacion general
Los archivos con los que se trabajan son .mid [[mis archivos los saque de este sitio](https://bitmidi.com/)]\
**Como usar los archivos principales?**
- **Por el momento el orden es el siguiente:**
- main.py (genera un archivo .keras (LSTM model))
- generator.py (genera una seria de numeros que reprentan notas musicales)
- music.py (genera un archivo .mid)

## Acerca del GUI ##
El GUI es muy simple y la ventaja es que hace el flujo de trabajo mucho mas intuitivo.
## Parametros Musicales ##
Como ya he mencionado la teoria musical es poca por lo que solo se podra modificar los siguienes aspectos
- Escalas
- Cuanto tiempo duran las notas (por defecto el valor se da en segundos)
- Parametros del generator.py (ya que es el encargado de genrar la sequencia como tal)
### Como cambio la duracion de las notas? ###
-***Me canse de escribir xd***
