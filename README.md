
# giford-api

API for giford module


## setup
python 3.10.7
i suggest pyenv, but whatever will work
```
pip install -e .
```

dev
```
pip install -e .[dev]
```

deploy utils
```
pip install -e .[deploy]
```

## run
```
python -m giford_api.main:app
```

## test
included is a launch.json for vscode
this will run the app and give ability to debug

this command will upload an image to a URL, super handy for testin
```
curl -F 'img=@./test_data/orange.png' http://localhost:8000/slide
```

ironically enough, the giford image is not supported by giford
