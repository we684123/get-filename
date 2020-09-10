# 打包指令

標準：
```
python setup.py sdist
```

wheel：
```
python setup.py sdist bdist_wheel
```

easy_install：
```
python setup.py bdist_egg
```

# 上傳指令

```
python twine upload dist/*
```
or
```
python c:\users\{username}\appdata\roaming\python\{python38}\site-packages/twine upload dist/*
```

如果要上傳到 test-pypi
```
python twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

# setup readme注意
```
long_description_content_type='text/markdown',
```
