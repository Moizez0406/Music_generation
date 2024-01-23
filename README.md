# Acerca de *Music Generator*

- El tiempo es lo que mas es notorio en este projecto taking around 120 min -> 2h
- Este es un proyecto muy simple que se basa en redes neuronales, mas especificamente utiliza modelos LSTM para poder, dado una ***seed*** inicial, predecir como puede seguir una melodia.
- El proyecto puede ser mejorado significativamente ya que el nivel de complejidad musical tratada es muy poca si no es que solo  minima.
- El generador ha sido entrenado solo con musica clasica.


**Todos los iconos los saque de la siguiente pagina web** https://www.flaticon.es/

# Estructura de folders
Los archivos con los que se trabajan son .mid [[mis archivos los saque de este sitio](https://bitmidi.com/)]\
Los folder mas importantes son:

- `data`: Lugar donde se debe subir los archivos con los que se desa entrenar al modelo
- `models`: Parametros para el LSTM 
- `GUI`: Interfaz para usuarios mas casuales 

Por otro lado, todos los archivos generados iran al folder `out` por defecto.

# Uso de codigos .py
- **Por el momento el orden es el siguiente:**
  1. `main.py` (genera un archivo .keras (LSTM model))
  2. `generator.py` (genera una seria de numeros que reprentan notas musicales)
  3. `music.py` (genera un archivo .mid)

# Acerca del GUI 
El GUI es muy simple y la ventaja es que hace el flujo de trabajo mucho mas intuitivo.
- Por ahora el archivo gui.py solo se puede correr dentro de la carpeta Gui (no puede ejecutarse de manera relativa)
# Parametros Musicales 
Como ya he mencionado la teoria musical es poca por lo que solo se podra modificar los siguienes aspectos
- Escalas
- Cuanto tiempo duran las notas (por defecto el valor se da en segundos)
- Parametros del `generator.py` (ya que es el encargado de genrar la sequencia como tal)
### Como cambio la duracion de las notas? ###
-***Me canse de escribir xd***


<!--
# About *Music Generator*

- This is a super simple project that relies on neural networks, specifically using LSTM models to predict how a melody could continue given an initial seed.
- The project has a lot of room for improvement because the musical complexity it handles right now is quite low, if not downright basic.
- The generator has only been trained with classical music.

**All icons were taken from the following website:** https://www.flaticon.com/

# Folder Structure
The files we're working with are .mid files [[I got my files from this site](https://bitmidi.com/)].\
The most important folders are:

- `data`: This is where you need to upload the files you want to train the model with.
- `models`: Parameters for the LSTM model.
- `GUI`: User-friendly interface for more casual users.

Also, all the files generated will go to the `out` folder by default.

# How to Use the .py Files
- **For now, the order is as follows:**
  1. `main.py` (generates a .keras file (LSTM model))
  2. `generator.py` (produces a series of numbers representing musical notes)
  3. `music.py` (creates a .mid file)

# About the GUI
The GUI is really simple, but the advantage is that it makes the workflow much more intuitive.
- For now, the `gui.py` file can only be run from within the Gui folder (it can't be executed relatively).

# Musical Parameters
As I mentioned earlier, the music theory applied here is limited. As a result, you can only modify the following aspects:
- Scales
- How long the notes last (the default value is in seconds)
- Parameters in generator.py (since it's responsible for generating the actual sequence)
### How do I change the duration of the notes? ###
- ***I got tired of writing, lol!***
-->
