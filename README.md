[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Flask template

This project contains set of instructions to start working with **flask** micro-web framework (for reference mostly).

**Tools**
- [python 3.8](https://www.python.org/downloads/release/python-380)
- [flask](http://flask.palletsprojects.com)
- [pytest](https://pypi.org/project/pytest)

## Usage
Run script from the root directory of the project and open [http://localhost:4000](http://localhost:4000) url in your WEB browser:
```bash
~ flask run
```

Please modify [.flaskenv](.flaskenv) file to set your own application environment variables.

**Endpoints:**
- `/` - get home page
    ```bash
    curl -X GET http://0.0.0.0:4000/
    ```
- `/details` - get details page
    ```bash
    curl -X GET http://0.0.0.0:4000/details
    ```
- `/joke` - get random joke
    ```bash
    curl -X GET http://0.0.0.0:4000/joke
    ```
- `/pokemon` - get pokemon list by color
    ```bash
    curl -X GET http://0.0.0.0:4000/pokemon
    curl -X POST http://0.0.0.0:4000/pokemon
    curl -X POST -d 'pokecolor=black' http://0.0.0.0:4000/pokemon
    ```


## Demo
> It's just a quick sample, please don't write front-end like this :)

![Screenshot](src/img/page.png)

### Run unittests
Please execute command below to launch unittests:
```bash
~ pytest -v
```

### Meta

Author – Volodymyr Yahello

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
