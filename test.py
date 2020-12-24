import config
ss="test"
exec ('conf = config.%s' % ss)
print(conf.python_path)