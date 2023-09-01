## End To End ML Porject

### Create Environment and activate

```
conda create -p new_house python==3.8 -y
conda activate new_house/
```
### Install all necessary libraries

```
pip install -r requirements.txt
```
### Install setup.py

```
pip install -r requirements.txt
python setup.py install # For independent installation
```

### Create src folder

```
src folder contains the entire ML pipeline
```

#### We will be having __init__.py inside src

```
The reason we will be having __init__.py is becz we want this src to be imported and used somewhere else also.
Like the way we have the methods of pandas such as pandas,read_csv(),
Similarly we can import the src package for that we need __init__.py
```

### We will create another folder named notebooks in which we will be keeping all the EDA activities

```
This won't go as a package for the deployment
```

### We will be having utils.py under src

```
utils.py will have all the generic functionalities coded
```

### Now we can create the pipeline folder

```
Under pipeline folder we need to have the files for training_pipeline.py and validation_pipeline.py
```

