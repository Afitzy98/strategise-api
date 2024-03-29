# Strategize API

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

Create a python virtual environment

```bash
python -m venv ./
```

Activate the virtual environment

```bash
cd env/scripts
bash: source activate
cmd: activate.bat
```

Use the package manager to install the package requirements.

```bash
pip intstall -r requirements.txt
```

## Development

Start the development server using the uvicorn run: app command in a bash file containing the enviornment variables

```bash
sh start
```

## Documentation

View and use the interactive documentation by clicking [here](http://localhost:8000/docs) or opening the url below in your browser once the development server is running.

```bash
http://localhost:8000/docs
```

## Authentication

To gain access to the authenticated endpoints make a POST request to the /users endpoint (using the interactive docs) to create a new account.

## License

[BY-NC-ND 3.0](https://creativecommons.org/licenses/by-nc-nd/3.0/)
