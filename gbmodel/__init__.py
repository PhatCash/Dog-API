# Specifies and returns the correct model 
#model_backend = 'pylist'
#model_backend = 'sqlite3'
#model_backend = 'datastore'
#model_backend = 'firestore'
model_backend = 'dog'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
elif model_backend == 'pylist':
    from .model_pylist import model
elif model_backend == 'datastore':
    from .model_datastore import model
elif model_backend == 'firestore':
    from .model_firestore import model
elif model_backend == 'dog':
    from .model_dog import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
