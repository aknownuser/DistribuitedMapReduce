# DistribuitedMapReduce
[![Build Status](https://travis-ci.com/OussamaElazizi/DistribuitedMapReduce.svg?token=xtsm6Ui1qLPWyjTcRFmx&branch=master)](https://travis-ci.com/OussamaElazizi/DistribuitedMapReduce)
[![codecov](https://codecov.io/gh/OussamaElazizi/DistribuitedMapReduce/branch/master/graph/badge.svg?token=SFNfd9sqPP)](https://codecov.io/gh/OussamaElazizi/DistribuitedMapReduce)

Este proyecto es una implementación de MapReduce en un sistema distribuido utilizando pyactor.

## Empezamos

El modelo se basa en un programa master, un reducer y un numero indefinido de mappers.
El funcionamiento por defecto del modelo es el tratamiento de ficheros (contar paralabras o frequencias),
pero se puede adaptar el código para cumpliar con otras necesidades que implican utilizar Map Reduce.


### Prerequisitos

El modelo implementado utiliza el midleware pyactor.

```
pip install pyactor
```
### Terminologia e uso

Para poder explicar como se utiliza se tiene que definir un terminología:

-IP_LOCAL_PC: Dirección IP del ordenador que en un momento inicia un script.
-IP_REGISTRY: Dirección IP del ordenador que corre el Registry.py.
-WORKER_NUM: Numero identificador del mapper, que se utiliza para buscar el trabajo que tiene que cumplir.
-FILE_NAME: Nombre del fichero que se a va a tratar.

Se tienen que seguir las siguintes reglas para que el sistema funcione sin problema.

1. Siempre se tiene que cumplir con el orden de inicio de los componentes
2. El numero identificador del mapper es único e incremental.

### Funcionamiento

El sistema esta pensado para ser ejecudo en diferentes maquinas independientes. Para ello se tiene que seguir
lo siguintes pasos:

1.  Iniciar el servidor HTTP, en el directorio raíz de **parted**

```
python -m SimpleHTTPServer
```

2.  Iniciar el Registry

```
python Resgitry.py IP_LOCAL_PC
```

3.  Iniciar el Reducer

```
python Reducer.py IP_REGISTRY IP_LOCAL_PC
```

4.  Iniciar los Mappers

```
python Mapper.py WORKER_NUM IP_REGISTRY IP_LOCAL_PC
```

5.  Iniciar Main

```
python Main.py FILE_NAME IP_REGISTRY IP_LOCAL_PC
```


