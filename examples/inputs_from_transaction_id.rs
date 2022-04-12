// Copyright 2021 IOTA Stiftung
// SPDX-License-Identifier: Apache-2.0

//! cargo run --example inputs_from_transaction_id --release

use iota_client::{
    bee_message::payload::transaction::TransactionId, node_api::high_level::GetTransactionInputsBuilder, Client, Result,
};

/// In this example we will fetch all inputs from a given transaction id.

#[tokio::main]
async fn main() -> Result<()> {
    let client = Client::builder()
        .with_node("http://localhost:14265")?
        .with_node_sync_disabled()
        .finish()
        .await?;

    let transaction_id = "0xaf7579fb57746219561072c2cc0e4d0fbb8d493d075bd21bf25ae81a450c11ef"
        .parse::<TransactionId>()
        .unwrap();

    let inputs = GetTransactionInputsBuilder::new(&client)
        .transaction_inputs(&transaction_id)
        .await?;

    println!("Transaction inputs {:?}", inputs);

    Ok(())
}
