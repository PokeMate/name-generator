# Pokémon Name Generator

The code for generating pokemon names was forked from [this repository](https://github.com/simon-larsson/pokemon-name-generator). The generated model is used to expose its functionality as part of a REST API.

The model generates new unique Pokemon names with Keras using a recurrent neural network (LSTM). Written as a generic text generator that can be used to generate lines of poetry, other names, or just text in general. It all depends on what it gets input.

## Training the model

Train the model with the jupyter notebook in `./training/name_generator.ipynb`. It will produce a file which stores the model used to generate new names in `./training/model.h5`.

To start the jupyter notebook:

```bash
jupyter notebook
```

[Notebook with code and explainations](https://github.com/PokeMate/name-generator/blob/master/training/name_generator.ipynb)

### Sample Pokémon Names

|          |           |          |           |
| -------- | --------- | -------- | --------- |
| Purndew  | Chingoos  | Nodow    | Fregaycha |
| Magmagly | Cteenidel | Browodon | Noinga    |
| Ferfeon  | Midgeos   | Deowwar  | Harouthal |
| Spera    | Kleffas   | Picorno  | Suorthe   |
| Ponytau  | Jellpid   | Mewable  | Meetty    |
| Phound   | Passir    | Golduzon | Frislask  |

## API Installation

Copy the files that are used for training into the api application:

```bash
cp training/input/names.txt api/static
cp training/model.h5 api/static/
```

### Without Docker

Create a virtualenv and activate it:

```bash
python3 -m venv venv
. venv/bin/activate
```

Or windows:

```bash
py -3 -m venv venv
venv\Scripts\activate.bat
```

Install all the dependencies.

```bash
pip3 install -r requirements.txt
```

Start the API

```bash
python3 api/main.py
```

### With Docker

Build the Docker container.

```bash
docker build -t name-generator .
```

Run the docker container and map the internal port to external port-

```bash
docker run -p 5000:5000/tcp name-generator
```

### Run tests

```bash
coverage run -m pytest
```

### API

`/names?amount=<amount>`

**GET**
| Parameter | Type | Required | Default Value | Description |
| -------- | ---- | ----- | -- | ----------------------------------- |
| `amount` | `int` | `no` | `1` | amount of Pokemon names |

#### Example

```bash
http://localhost:5000/?amount=5
```

```json
["Goigon", "Tangros", "Kalmiphan", "Camermosh", "Wincino"]
```

### Swagger

Endpoints are documented using Swagger. To access the interactive documentation got to:

`/swagger`
