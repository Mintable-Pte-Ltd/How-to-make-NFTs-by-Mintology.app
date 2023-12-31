---
hidden: false
# slug: imx
category: 64e5f94ae377a50070c31bc9
title: Immutable X Integration
description: Immutable X (IMX) is a layer-2 scaling solution for Ethereum, aimed at reducing the environmental impact of NFT transactions while ensuring instant trade confirmation, massive scalability, and no gas fees without compromising user custody. Integration with Immutable X can significantly enhance the user experience by making transactions faster and more cost-effective.
---

# Immutable X Integration

## What is IMX?

Immutable X (IMX) is a layer-2 scaling solution for Ethereum, aimed at ensuring instant trade confirmation, massive scalability, and no gas fees without compromising user custody. Please check the official pages by [Immutable](https://www.immutable.com/) to understand the differences and implications of using this platform rather than Ethereum.

## How to use the API

You can find the API documentation under **[IMX](https://docs.mintology.app/reference/imx)**.

The integration involves registering an IMX user, minting, and transferring IMX items. Below are the steps to achieve this integration:

### Step 1: Register IMX User

Registering a user on Immutable X is the initial step for IMX integration. This is done through the `Register IMX User` endpoint.

#### Endpoint:

- **URL**: `https://api.mintology.app/v1/{projectId}/imx/register`
- **Method**: `POST`
- **Important**: Make this call from the back-end.

#### Path Parameters:

- `projectId` (string, required): Your project ID found on your dashboard.

#### Body Parameters:

- `email` (string, required): The email of the user you want to register for.
- `username` (string, optional): The username that will be tied to this private key/wallet.

#### Example:

```javascript
const axios = require('axios');

async function registerIMXUser() {
  const response = await axios.post(
    'https://api.mintology.app/v1/{projectId}/imx/register',
    {
      username: 'optionalUsername', // Optional username
      email: 'user@example.com', // replace with the user's email
    },

    {
      headers: {
        'Api-Key': 'Your API Key',
      },
    }
  );
  console.log(response.data);
}

registerIMXUser();
```

### Step 2: Mint IMX Item

Once the user is registered on IMX, the next step is to mint an IMX item using the `Mint IMX Item` endpoint.

#### Example:

```javascript
async function mintIMXItem() {
  const response = await axios.post(
    'https://api.mintology.app/v1/{projectId}/imx/mint',
    {
      metadata: {
        // Add other metadata properties as needed
      },
      token_id: 'uniqueTokenId', // Token id of the NFT being minted
      wallet_address: 'walletAddress', // The wallet address of the user minting the NFT
    },
    {
      headers: {
        'Api-Key': 'Your API Key',
      },
    }
  );
  console.log(response.data);
}

mintIMXItem();
```

### Step 3: Transfer IMX Item

The final step in IMX integration is transferring the minted IMX item to another user using the Transfer IMX Item endpoint.

#### Example:

```javascript
async function transferIMXItem() {
  const response = await axios.post(
    'https://api.mintology.app/v1/{projectId}/imx/transfer',
    {
      from_wallet_address: 'fromWalletAddress', // The wallet address owns the token at the contract address
      to_wallet_address: 'toWalletAddress', // The recipient of the token
      token_id: 'uniqueTokenId', // The token id to transfer, must exist and belong to from_wallet_address
    },
    {
      headers: {
        'Api-Key': 'Your API Key',
      },
    }
  );
  console.log(response.data);
}

transferIMXItem();
```
