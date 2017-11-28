# Demo setup

```
python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current
```

```
python -m rasa_core.train -s data/stories.md -d domain.yml -o project/dialogue --epochs 300
```

```
python -m rasa_core.run -d project/dialogue -u project/nlu/current
```

