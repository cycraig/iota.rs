---
description: Getting started with the official IOTA Client Library Python binding.
image: /img/logo/iota_mark_light.png
keywords:
- Python
- install
- pip
- unpack
---
# Getting Started with IOTA Client Python Binding

## Security

:::warning
In a production setup, do not store passwords in the host's environment variables or in the source code. See our [backup and security recommendations](https://wiki.iota.org/chrysalis-docs/guides/backup_security) for production setups.
:::

## Requirements

[Python 3.x](https://www.python.org) & [pip](https://pypi.org/project/pip)

`Rust` and `Cargo`, to compile the binding. Install them [here](https://doc.rust-lang.org/cargo/getting-started/installation.html).

## Installation

- Go to `iota.rs/bindings/python/native`

### Create a virtual environment and use it (optional)
- `python3 -m venv iota_client_venv`
- `source iota_client_venv/bin/activate`; Windows: `.\iota_client_venv\Scripts\activate`

### Install required dependencies and build the wheel
- `pip install -r requirements-dev.txt`
- `pip install .`

### Run examples
`python3 example/[example file]`

Example: 
- `python3 examples/00_get_info.py`

### To deactivate the virtual environment (optional)
- `deactivate`

## Getting Started

After you installed the library, you can create a `IotaClient` instance and interface with it.

```python
from iota_client import IotaClient

# Create an IotaClient instance
client = IotaClient({'nodes': ['https://api.testnet.shimmer.network']})

# Get the node info
node_info = client.get_info()
print(f'{node_info}')
```
