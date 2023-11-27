---
hidden: false
# slug: getting-started
category: 64e5f94ae377a50070c31bc9
title: Quickstart Guide
description: Welcome to the Mintology APIs! As you embark on your journey to integrate and interact with our robust suite of APIs, there are some key items and information you'll need to have on hand. We've designed our APIs with ease of use in mind, ensuring a smooth onboarding process for developers.
---

# Quickstart Guide

## Getting Started with Mintology APIs

Welcome to the Mintology APIs! As you embark on your journey to integrate and interact with our robust suite of APIs, there are some key items and information you'll need to have on hand. We've designed our APIs with ease of use in mind, ensuring a smooth onboarding process for developers.

## Getting started

### Basic Pre-requisites

Before making any API calls, ensure you're authorized. Include the following headers in your API requests:

```json
{
  "Api-Key": "YOUR_API_KEY"
}
```

To find out how to get your API Key and other pre-requisites, look through **[Pre-requisites](https://docs.mintology.app/docs/2_pre-requisites)**:

## Creating Projects

Creating a project is the initial step to operate on the Mintology platform. A project acts as a container for your NFTs and associated operations.

There are 3 types of projects:

- #### Shared
  Mint to the Mintology shared contract. Your NFTs will be visible in the shared Mintology store.
- #### Dedicated
  Create dedicated contract for your NFTs. You will have your own store on our marketplace.
- #### Existing
  Mint your NFTs to your existing smart contracts created on Mintology.

### Creating a project using API:

Create a project using the [Create Projects](https://docs.mintology.app/reference/projects-create) endpoint, this method of creating a project gives more options that can be customised.

#### Endpoint:

- **URL**: `https://api.mintology.app/v1/projects`
- **Method**: `POST`
- **Important**: Make this call from the back-end.

#### Headers:

```json
{
  "Api-Key": "YOUR_API_KEY"
}
Request Body:
{
  "name": "Your Project Name",  // required
  "description": "Description of your project",  // required
  "mint_limit_per_address": 10,  // optional
  "contract_type": "Shared",  // required
  "wallet_type": "Both",  // required
  "base_uri": "https://yourbaseuri.com",  // optional
  "contract_name": "YourContractName",  // required if contract_type is "Dedicated"
  "symbol": "YCN",  // required if contract_type is "Dedicated"
  "royalty": 10,  // optional
  "total_supply": 100,  // optional
  "contract_address": "0xYourExistingContractAddress",  // optional
  "owner_address": "0xYourAddress",  // required if contract_type is "Dedicated"
  "network": 1,  // required
  "chain": "eth"  // required
}

Returns:

{
  "project_id": "your-project-id"
}


-> Replace parameter description parts
```

#### Response:

Upon successful project creation, you'll receive a response containing the `project_id`, which is crucial for further interactions with the Mintology API.

```json
{
  "project_id": "your-project-id"
}
```

### Creating a project using Dashboard:

You can also create a project though the [Mintology web app](https://dashboard.mintology.app) which will have less inputs available, you can also find your Project ID there.

## Using Mintology

With a project created, you can now proceed to do any of the following, you can follow the recommended flow in the given order:

- [Premint NFTs](https://docs.mintology.app/docs/4_premint)
- [Create Mintable Wallets](https://docs.mintology.app/docs/5_custodial-wallets)
- [Mint and Claim NFTs](https://docs.mintology.app/docs/6_mint_and_claim)
- [NFT Metadata](https://docs.mintology.app/docs/7_nft_metadata)
- [Token Gating](https://docs.mintology.app/docs/8_token_gating) (you will need claimed or minted NFTs for this)
- [Immutable X Integration](https://docs.mintology.app/docs/9_imx_integration)
