---
hidden: false
# slug: pre-requisites
category: 64e5f94ae377a50070c31bc9
title: Pre-requisites
description: This are the the things you will need to do before using the APIs seamlessly. There is only one endpoint ([Project Info](https://docs.mintology.app/reference/info-project)) that can be called without the need for an API Key, the rest require an API Key.
---

# Pre-requisites

This are the the things you will need to do before using the APIs seamlessly. There is only one endpoint ([Project Info](https://docs.mintology.app/reference/meta-info)) that can be called without the need for an API Key, the rest require an API Key.

## How do I get an API key?

On [Mintology web app](https://dashboard.mintology.app), click on your profile at the top left corner and select "Settings", your Mintology Key will be present in the Settings page. You can copy and also refresh your key if you need to directly from there.

**IMPORTANT**: Make sure you have choosen the appropriate billing plan for your projects.

## Other Pre-requisites

The following section outlines the other essential pre-requisites you'll require to hit the ground running. Acquiring and understanding these elements will equip you with a solid foundation to explore, test, and implement our APIs seamlessly into your projects. Let's dive in and get you set up!

**Project ID**:

- **Description**: A unique identifier for a project within the Mintology platform.
- **How to Obtain**: Go to your Dashboard at [Mintology web app](https://dashboard.mintology.app), click on the project for the project_id you want. On your Project Dashboard, go to NFT Details, your "Project ID" will be there.

**Wallet Address**:

- **Description**: The public address of an Ethereum wallet.
- **How to Obtain**: Available within the cryptocurrency wallet application.

**Mintable Wallet** (If utilizing Mintable Wallets feature):

- **Description**: A wallet managed and secured by Mintology; it is mapped to the user's email address, and the user can interact with it through [Mintable](https://mintable.com).
- **How to Obtain**: Generated via the [Mintable Wallets endpoint](https://docs.mintology.app/reference/custodial-wallets-create) of the Mintology API. A Mintable wallet will also be automatically created when a user tried to `mint` or `claim` an NFT, if they do not already have one.

**Ethereum Layer 1 Account** (If utilizing IMX Endpoints):

- **Description**: An account on the main Ethereum blockchain.
- **How to Obtain**: Available within the cryptocurrency wallet application.

**Immutable X Layer 2 Account** (If utilizing IMX Endpoints):

- **Description**: An account on the Immutable X Layer 2 scaling solution for Ethereum.
- **How to Obtain**: Created via the [Register IMX User endpoint](https://docs.mintology.app/reference/imx-register) of the Mintology API.

**Metadata** (If pre-minting or updating metadata):

- **Description**: Information describing the NFTs including attributes like `name`, `image`, `animation_url`, etc.
- **How to Prepare**: As per the [Preminting NFTs](https://docs.mintology.app/reference/premints) and [Update NFT Metadata](https://docs.mintology.app/reference/metadata-update) endpoints documentation.

**OTP** (One-Time Password) (If exporting Mintable Wallet):

- **Description**: A single-use password required for certain authorization processes such as exporting a Mintable Wallet.
- **How to Obtain**: Typically sent to the registered email or phone number during the export process.

**Request ID** (If exporting Mintable Wallet):

- **Description**: A unique identifier for the export request, used to approve the export of a Mintable Wallet.
- **How to Obtain**: Generated during the [Request To Export process](https://docs.mintology.app/reference/custodial-wallets-exports-request).
