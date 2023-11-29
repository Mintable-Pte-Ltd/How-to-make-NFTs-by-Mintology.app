---
hidden: false
# slug: mint-claim
category: 64e5f94ae377a50070c31bc9
title: Minting and Claiming NFTs
description: Use the `/mint` endpoint to mint the NFT, including metadata as an object in the request body.
---

# Minting and Claiming NFTs

**IMPORTANT**: Before you start using the APIs, make sure that you have deployed your project and enabled Claiming and Minting through the **[Claim Config Update](https://docs.mintology.app/reference/projects-claim-update)** and **[Mint Config Update](https://docs.mintology.app/reference/projects-mint-update)** endpoints or through your Project Dashboard page on [Mintology web app](https://dashboard.mintology.app).

## How Minting and Claiming Works

Both `mint` and `claim` are designed to mint an NFT directly into a user's wallet. If you have enabled Mintable Wallets, you can mint into an email address: the system will check if the user already have a Mintable wallet, otherwise it will create one for them automatically.

### Mint

Use the **[Mint](https://docs.mintology.app/reference/mint)** endpoint to mint the NFT, including metadata as an object in the request body. Ideal for selling NFTs, targeted airdrops, or minting collectibles. Supports both custom Mintable Wallets and standard crypto wallets.

### Claim

Use the **[Claim](https://docs.mintology.app/reference/claim)** endpoint to mint a free NFT. This is the endpoint you should use for discount coupons, proof of attendance, and in general NFTs which you do not intend to sell.

**Note**: Keeping 'mint' and 'claim' endpoints separate simplifies analytics, making it easier to track each call's specific purpose.

## How to use the API

- If you don't pass in a metadata object—the system will create a random NFT using your pre-mint data you've set up through the API endpoints or dashboard.
- If you pass in a metadata object, it will mint a new NFT with the new metadata object you passed in.

### Minting NFTs

#### Endpoint

- **URL**: `https://api.mintology.app/v1/{projectId}/mint`
- **Method**: `POST`

#### Path Parameters

- `projectId` (string, required): Your project ID found on your dashboard.

#### Body Parameters

- `metadata` (object, optional): If absent, the metadata defined in the project will be used. Otherwise, it will mint a new NFT with the new metadata object you passed in.
  - `name` (string, required): Name of the item.
  - `image` (string, required): URL to the image of the item (350 x 350 recommended).
  - `animation_url` (string, optional): URL to a multimedia attachment for the item.
  - `description` (string, optional): A human-readable description of the item (Markdown supported).
  - `attributes` (array of objects, optional): Attributes for the item.
  - `title` (optional, string): Title of the NFT, used for listing the item for sales.
  - `subtitle` (optional, string): Short description or subtitle of the NFT, used for listing the item for sales.
- `wallet_address` (string, required): Wallet address to mint the token to.

#### Example Request

```curl
curl -X POST https://api.example.com/mint   -H "api-key: YOUR_API_KEY"   -d '{
    "project_id": "YOUR_PROJECT_ID",
    "wallet_address": "WALLET_ADDRESS",
    "metadata": {
      "name": "NFT_NAME",
      "description": "NFT_DESCRIPTION",
      "image": "IMAGE_URL",
      "attributes": [
        {
          "trait_type": "color",
          "value": "blue"
        }
      ],
      ....
    }
  }'
```

#### Example Request (Node.js)

```javascript
const axios = require("axios");

async function mintNFT() {
  const response = await axios.post(
    "https://api.mintology.app/v1/{projectId}/mint",
    {
      metadata: {
        name: "Unique NFT",
        image: "https://example.com/image.png",
      },
      wallet_address: "0x12345...",
    },
    {
      headers: {
        "Api-key": "YOUR_API_KEY",
      },
    }
  );
  console.log(response.data);
}

mintNFT();
```

After minting, check the event logs to confirm the NFT's status on the Mintology dashboard.

### Claiming NFTs

```plaintext
POST https://api.mintology.app/v1/{projectId}/claim
```

This endpoint will mint a free NFT to your user's wallet, which can be a Mintable Wallet or their existing crypto wallet. The mint and claim endpoints are kept separate to simplify analytics and track each call's specific purpose.

#### Path Parameters

- `projectId` (string, required): Your project ID found on your dashboard.

#### Body Parameters

- `wallet_address` (string, required): Wallet address to mint the token to.

#### Example Request (Node.js)

```javascript
const axios = require("axios");

async function claimNFT() {
  const response = await axios.post(
    "https://api.mintology.app/v1/{projectId}/claim",
    {
      wallet_address: "0x12345...",
    },
    {
      headers: {
        "Api-key": "YOUR_API_KEY",
      },
    }
  );
  console.log(response.data);
}

claimNFT();
```

After claiming, check the event logs to confirm the NFT's status on the Mintology dashboard.

---
