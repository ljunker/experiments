# tryStuff

Dieses Projekt ist als Sammelplatz für isolierte Experimente aufgebaut.

## Idee

- Jedes Experiment lebt in seinem eigenen Ordner unter `experiments/`.
- Gestartet wird immer direkt die jeweilige Datei, zum Beispiel:
  - `uv run experiments/mein_test/main.py`
- Dadurch ist für Python primär nur der jeweilige Experiment-Ordner auf dem Import-Pfad.
- Die Experimente teilen sich dieselbe `.venv`, sehen aber nicht automatisch den Code anderer Experimente.

## Neues Experiment anlegen

```bash
uv run tools/new_experiment.py mein_test
```

Danach starten mit:

```bash
uv run experiments/mein_test/main.py
```

## Struktur

- `experiments/_template/`: Vorlage für neue Experimente
- `experiments/<name>/`: ein einzelnes Experiment
- `tools/new_experiment.py`: legt neue Experimente aus der Vorlage an

## Regel

Wenn du die Isolation behalten willst:

- keine gemeinsamen Python-Packages im Projekt-Root anlegen
- Experimente immer über ihre eigene `main.py` starten
- gemeinsame Hilfen nur bewusst in einen separaten Shared-Ordner auslagern
