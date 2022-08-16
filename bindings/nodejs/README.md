# IOTA Client Library - Node.js binding

Node.js binding to the iota.rs client library.

## Installation

- Using NPM:

```bash
$ npm i @iota/client
```

- Using yarn:

```bash
$ yarn add @iota/client
```

## Requirements

One of the following Node.js version: '14.x', '16.x', '18.x'

If there is no prebuilt binary available for your system you need `Rust` and `Cargo`, to build it yourself. Install them [here](https://doc.rust-lang.org/cargo/getting-started/installation.html).

## Getting Started

After you linked the library, you can create a `Client` instance and interface with it.

```javascript
const { Client } = require('@iota/client')

const client = new Client({
    nodes: ['https://api.testnet.shimmer.network'],
});

client.getInfo().then(console.log).catch(console.error)
```

Connecting to a MQTT broker using raw ip doesn't work with TCP. This is a limitation of rustls.
