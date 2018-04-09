# DistribuitedMapReduce

Build by [Travis-ci](https://travis-ci.org):


[![Build Status](https://travis-ci.com/OussamaElazizi/DistribuitedMapReduce.svg?token=xtsm6Ui1qLPWyjTcRFmx&branch=master)](https://travis-ci.com/OussamaElazizi/DistribuitedMapReduce)

Code Coverage be [CodeCov](https://codecov.io):


[![codecov](https://codecov.io/gh/OussamaElazizi/DistribuitedMapReduce/branch/master/graph/badge.svg?token=SFNfd9sqPP)](https://codecov.io/gh/OussamaElazizi/DistribuitedMapReduce)


CodeHealth by [Codacy](https://codacy.com): 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f6392d2625814b4385c8cf79507835d4)](https://www.codacy.com/app/oussamaelazizi.opt/DistribuitedMapReduce?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=OussamaElazizi/DistribuitedMapReduce&amp;utm_campaign=Badge_Grade)

Este proyecto es una implementación de MapReduce en un sistema distribuido utilizando pyactor.
 Este modelo es una versión simplificada de la implementación de [Google](https://static.googleusercontent.com/media/research.google.com/es//archive/mapreduce-osdi04.pdf).
  
## Empezamos

El modelo se basa en un programa master, un reducer y un número indefinido de mappers.
El funcionamiento por defecto es el tratamiento de ficheros (contar paralabras y/o frecuencias de palabras), pero se puede adaptar el código para cumplir con otras necesidades.

Los componentes de la implementación son:
- **Registry.py**: Servicio de nombres del sistema.
- **Mapper.py**: Actor que controla el flujo y ejecuta la función de Map.
- **Reducer.py**: Actor que controla el flujo, aplica la función del reduce por cada mapper que acaba
y muestra el resultado por pantalla cuando acaba el último mapper.
- **functionsMapRed.py**: Contiene todos los métodos de Map, Reduce, formato de resultado y obtención de ficheros del servidor HTTP.
- **Main.py**: Programa principal que inicia la secuencia del proceso e inicia el servidor HTTP. 


El proceso de tratamiento tiene el siguiente flujo, primero se inician todos los componentes del sistema siguiendo el orden
en la sección de **Funcionamiento**. El _Main.py_ es el que inicia la secuencia de tratamiento
tal que, primero el main obtiene todos los mappers registrados y les hace _spawn_ y seguidamente empieza a partir 
el fichero a tratar sobre el número de mappers creados. Finalmente se hace elegir la función de Map y se empieza la ejecución; cada Mapper
descarga el trozo de fichero que le pertenece de un servidor HTTP. 
   

### Prerequisitos

El modelo implementado utiliza el middleware pyactor.

```
pip install pyactor
```
Puede encontrar más información en [Pyactor](https://github.com/pedrotgn/pyactor)
### Terminología y uso

Para poder explicar como se utiliza se tiene que definir una terminología:

- IP_LOCAL_PC: Dirección IP del ordenador que en un momento inicia un script.
- IP_REGISTRY: Dirección IP del ordenador que corre el Registry.py.
- WORKER_NUM: Número identificador del mapper, que se utiliza para buscar el trabajo que tiene que cumplir.
- FILE_NAME: Nombre del fichero que se va a tratar.

Se tienen que seguir las siguientes reglas para que el sistema funcione sin problemas.

1. Siempre se tiene que cumplir con el orden de inicio de los componentes.
2. El número identificador del mapper es único e incremental, de 0 a X.

### Funcionamiento

El sistema está pensado para ser ejecutado en diferentes máquinas. Para ello se tienen que seguir los siguientes pasos:


1-  Iniciar el Registry

```
python Registry.py IP_LOCAL_PC
```

2-  Iniciar el Reducer 

```
python Reducer.py IP_REGISTRY IP_LOCAL_PC
```

3-  Iniciar los Mappers

```
python Mapper.py WORKER_NUM IP_REGISTRY IP_LOCAL_PC
```

4-  Iniciar Main

```
python Main.py FILE_NAME IP_REGISTRY IP_LOCAL_PC
```

## Authors

* **Amanda Gómez Gómez** - [amandagomez](https://github.com/amandagomez)
* **Oussama El Azizi** - [OussamaElazizi](https://github.com/OussamaElazizi)
