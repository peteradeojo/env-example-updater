# ENV-Example Updater

Developers who use environment variables a lot might forget to update their example files whenever new environment variables are added to the project. This script can be used to automate this operation.

## Installation
```sh
git clone https://github.com/peteradeojo/env-example-updater.git
```

```sh
pip install -r requirements.txt
```

On Linux, MacOS
```
source build.sh
```

## Usage
Move the output `envUpdater` to a place where it is easily accessible, or add it to your system PATH variable.

In your project directory run
```sh
envUpdater
```