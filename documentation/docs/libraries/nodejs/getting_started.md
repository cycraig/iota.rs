---
description: Getting started with the official IOTA Client Library Node.js binding.
image: /img/logo/iota_mark_light.png
keywords:
- Node.js
- dotenv
- install
- npm
- yarn
- security
---
# Getting Started with Node.js

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
const { ClientBuilder } = require('@iota/client')

const client = new ClientBuilder()
    .node('https://api.testnet.shimmer.network')
    .build()

client.getInfo().then(console.log).catch(console.error)
```

Connecting to a MQTT broker using raw ip doesn't work with TCP. This is a limitation of rustls.
