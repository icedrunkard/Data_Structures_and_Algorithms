class ContextManager(object):
    def __init__(self):
        print('[initiating...]')
        self.name='ContextManager'
    def __enter__(self):
        print("[in __enter__] acquiring resources")
    def __del__(self):
        print('[deleting...]')
    def __exit__(self, exception_type, exception_value, traceback):
        print("[in __exit__] releasing resources")
        if exception_type is None:
            print("[in __exit__] Exited without exception")
        else:
            print("[in __exit__] Exited with exception: %s" % exception_value)
            return False
    def __str__(self):
        return self.name

with ContextManager() as c1:
    print("[in with-body] Testing")
    print(c1)

c2=ContextManager()
print(c2)