_callbacks = {}

def register(hook=0):
    def register_callback(func):
        return func
    return register_callback