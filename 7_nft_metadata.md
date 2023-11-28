---
hidden: false
# slug: metadata
category: 64e5f94ae377a50070c31bc9
title: NFT Metadata
description: Use the NFT metadata endpoints to update your NFT metadata and also retrieve it ('Retrieve' coming soon).
---

# NFT Metadata

**IMPORTANT**: Please note that NFT Metadata endpoints work on minted tokens, for premit NFT please refer to **[Premint](https://docs.mintology.app/reference/premints)** endpoints.

## What it is?

Use the NFT metadata endpoints to update your NFT metadata and also retrieve it ('Retrieve' coming soon).

## How to use the API

**[Update NFT Metadata](https://docs.mintology.app/reference/metadata-update)** endpoint alters NFT metadata encompassing details like token name, image, animation_url, etc. You will need the Project ID and Token ID of the NFT metadata you want to update.

- **URL**:`https://api.mintology.dev/{projectId}/metadata/{tokenId}`
- **Method**: `PUT`
- **Important**: Make this call from the back-end.

#### Path Parameters:

- `projectId` (string, required): Your project ID found on your dashboard.

#### Body Parameters:

- `metadata` (object, optional): If absent, the metadata defined in the project will be used. Otherwise, it will mint a new NFT with the new metadata object you passed in.
  - `name` (string, required): Name of the item.
  - `image` (string, required): URL to the image of the item (350 x 350 recommended).
  - `animation_url` (string, optional): URL to a multimedia attachment for the item.
  - `description` (string, optional): A human-readable description of the item (Markdown supported).
  - `attributes` (array of objects, optional): Attributes for the item.
  - `title` (optional, string): Title of the NFT, used for listing the item for sales.
  - `subtitle` (optional, string): Short description or subtitle of the NFT, used for listing the item for sales.

#### Example Request (Node.js):

```javascript
const axios = require('axios');

async function updateNFT() {
  const response = await axios.post(
    'https://api.mintology.app/v1/{projectId}/metadata/{tokenId}',
    {
      metadata: {
        name: 'Unique NFT',
        image: 'https://example.com/image.png',
      },
    },
    {
      headers: {
        'Api-Key': 'Your API Key',
      },
    }
  );
  console.log(response.data);
}

updateNFT();
```
