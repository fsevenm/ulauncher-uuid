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

```
git clone https://github.com/fsevenm/ulauncher-uuid
cd ~/.cache/ulauncher_cache/extensions/ulauncher-uuid
ln -s <repo_location> ulauncher-uuid
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## Todos
- [x] Add gif preview (or screenshot)
- [ ] Add more namespaces for uuid v3 and v5
- [ ] Optimize gif preview to smaller size
- [ ] Add different icon for each uuid version 

## License 

MIT
