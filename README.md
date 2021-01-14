# Ulauncher UUID

> [Ulauncher](https://ulauncher.io/) Extension for generating UUID

## Screenshots
![media1](preview.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7
* uuid (`pip install uuid`)

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/fsevenm/ulauncher-uuid```
 

## Development

```shell script
git clone https://github.com/fsevenm/ulauncher-uuid
ln -s <clone_location> ~/.local/share/ulauncher/extensions/ulauncher-uuid
```

To start debugging the extension, run these debugging script:
```shell script
# run in different Terminal tab
ulauncher --no-extensions --dev -v
# run in different Terminal tab, you need to change PYTHONPATH value based on your local python config, change the USERNAME to yours
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-uuid PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/USERNAME/.local/share/ulauncher/extensions/ulauncher-uuid/main.py
```

When you made any changes to `main.py` or the other assets, you need to re-run debugging scripts above.

## Todos
- [x] Add gif preview (or screenshot)
- [ ] Add more namespaces for uuid v3 and v5
- [x] Optimize gif preview to smaller size
- [ ] Add different icon for each uuid version 

## License 

MIT @ Ayub Aswad
