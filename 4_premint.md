---
hidden: false
# slug: premints
category: 64e5f94ae377a50070c31bc9
title: Preminting NFTs
description: Pre-minting is the process of preparing NFT metadata and assets before the actual on-chain minting happens.
---

# Preminting NFTs

Pre-minting is the process of preparing NFT metadata and assets before the actual on-chain minting happens.

**IMPORTANT**: Please note that your users will not be able to mint or claim more items than what you have preminted. You can add more items anytime, even after the project has been deployed.

## Why Premint?

There are several benefits to preminting NFTs:

- It allows you to prepare and organize all the NFT metadata ahead of time. This includes properties like name, description, image, attributes etc.
- The preminted metadata can be reviewed and validated before minting. This prevents errors in the actual on-chain NFT data.
- It separates the metadata preparation from the blockchain minting. The metadata can be prepared offline and uploaded in bulk.
- Pre-minting enables features like white-listing and pre-sale for NFT drops by assigning slots to users before minting.
- It provides more flexibility in the actual on-chain minting process. The metadata can be uploaded in batches based on priorities.

## How Pre-Minting Works

The preminting process typically involves uploading NFT metadata like name, description, images to Mintology: this can be done using the [Mintology web app](https://dashboard.mintology.app), or the API. When ready to mint, the preminted metadata is retrieved and used to mint NFTs on-chain.

## How to use the API

### NFT Metadata

Please note that the metadata will either need to be self-hosted or you can create or add it via the platform and we will store the metadata on our end. The NFT metadata includes name, image url, animation url (optional), description (optional), other attributes (optional).

Note: We also offer a 10 year guarantee for data hosted on our server

### Preminting NFT

You can find the API documentation under **[Premints](https://docs.mintology.app/reference/premints)**.

Here's how you can create a premint NFT:

#### Endpoint:

- **URL**: `https://api.mintology.dev/{projectId}/premints`
- **Method**: `POST`

#### Path Parameters:

- `projectId` (required, string): The Project ID from your Mintology dashboard.

#### Body Parameters:

- `premint_id` (optional, string): Creates a new preminted NFT data set.
- `quantity` (required, number): Specifies the number of NFTs to create with this data set.
- `metadata` (required, object): The metadata for the NFT pre-mint data.

##### Metadata Object:

- `name` (required, string): Name of the item.
- `image` (required, string): URL to the image of the item. Supports various image types, including SVG.
- `animation_url` (optional, string): URL to a multimedia attachment for the item. Supported file extensions include GLTF, GLB, WEBM, MP4, M4V, OGV, OGG, MP3, WAV, and OGA. HTML pages are also supported for rich experiences and interactive NFTs.
- `description` (optional, string): A human-readable description of the item. Markdown is supported.
- `attributes` (optional, array of objects): Attributes for the item, displayed on the item page on Mintology and other marketplaces.
- `title` (optional, string): Title of the NFT, used for listing the item for sales.
- `subtitle` (optional, string): Short description or subtitle of the NFT, used for listing the item for sales.

#### Example Request (Node.js):

```javascript
const axios = require("axios");

async function createPremint() {
  const response = await axios.post(
    "https://api.mintology.app/v1/{projectId}/premints",
    {
      quantity: 10,
      metadata: {
        name: "Exclusive Artwork",
        image: "https://example.com/image.png",
        description: "Limited edition digital artwork",
        title: "Exclusive Artwork",
        subtitle: "Limited edition digital artwork by renowned artist",
      },
    },
    {
      headers: {
        "Api-Key": "Your API Key",
      },
    }
  );

  console.log(response.data);
}

createPremint();
```

You can either create items one by one, using the **[Create](https://docs.mintology.app/reference/premints-create)** endpoint above, or in bulk, using the **[Import](https://docs.mintology.app/reference/premints-import)** endpoint. The latter allows you to use a file (JSON or CSV) with all the details, or send all the parameters when you call the endpoint.

Once you have created (or imported) all the required premints, you can enable minting on your project. When your users mint or claim one of your NFTs, a random item among the premints will be selected.

Let us know if you have any other questions!

---
