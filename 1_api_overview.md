---
hidden: falsegi
# slug: overview
category: 64e5f94ae377a50070c31bc9
title: Mintology API Overview
description: Here's a overview of the Mintology API, covering various endpoints and processes
---

test changes

# Mintology API Overview

Here's a overview of the Mintology API, covering various endpoints and processes:

### Authorization

1. **[Authorize](https://docs.mintology.app/reference/authorize)**:
   - **Purpose**: Validates the legitimacy of token ownership.
   - **Parameters**: Utilizes Mintology API Key and Project ID for validation.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/authorize).
2. **[List Authorized Tokens](https://docs.mintology.app/reference/authorize-inventory)**:
   - **Purpose**: This endpoint is used to get the list of tokens that a user owns from a particular collection.
   - **Parameters**: Utilizes Mintology API Key and Project ID for validation.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/authorize-inventory).

### Projects Management

1. **[List Projects](https://docs.mintology.app/reference/projects-list)**:
   - **Action**: Enumerates all created projects.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-list).
2. **[Create Projects](https://docs.mintology.app/reference/projects-create)**:
   - **Action**: Generates a new project with designated details.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-create).
3. **[Retrieve Projects](https://docs.mintology.app/reference/projects-show)**:
   - **Action**: Fetches project specifics identified by its Project ID.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-show).
4. **[Update Projects](https://docs.mintology.app/reference/projects-update)**:
   - **Action**: Modifies a specific project with new details.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-update).
5. **[Remove Projects](https://docs.mintology.app/reference/projects-remove)**:
   - **Action**: Extinguishes a specified project from the platform.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-remove).
6. **[Mint Config Update](https://docs.mintology.app/reference/projects-mint-update)**:
   - **Action**: This operation allows enabling or disabling of the mint. However, this can only be toggled after the project has been successfully deployed.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-mint-update).
7. **[Claim Config Update](https://docs.mintology.app/reference/projects-claim-update)**:
   - **Action**: This operation allows enabling or disabling of the claim. However, this can only be toggled after the project has been successfully deployed.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-claim-update).
8. **[Deploy Projects](https://docs.mintology.app/reference/projects-deploy)**:
   - **Action**: Launches a specified project for token minting.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/projects-deploy).

### Mintable Wallets

1. **[Create Mintable Wallet](https://docs.mintology.app/reference/custodial-wallets-create)**:
   - **Action**: Establishes a new Mintable Wallet and Mintable account, enabling users to claim private key custody.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/custodial-wallets-create)​`​.
2. **[Request To Export](https://docs.mintology.app/reference/custodial-wallets-exports-request)**:
   - **Action**: Commences the process for user custody claim of their Mintable Wallet.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/custodial-wallets-exports-request)​`​.
3. **[Approve Export](https://docs.mintology.app/reference/custodial-wallets-exports-approve)**:
   - **Action**: Transmits the Mintable wallet private key to the user, necessitating a request_id and OTP for authorization.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/custodial-wallets-exports-approve)​`.
4. **[Remove Mintable Wallet](https://docs.mintology.app/reference/custodial-wallets-remove)**:
   - **Action**: Irrevocably deletes the private key from Mintology's systems post user custody claim of their Mintable Wallet.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/custodial-wallets-remove)​`.

### Preminting NFTs

1. **[List Premints](https://docs.mintology.app/reference/premints-list)**:
   - **Action**: Yields a list of premint items, arrayed by updated date with latest premints at the forefront.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/premints-list)​​.
2. **[Create Premints](https://docs.mintology.app/reference/premints-create)**:
   - **Action**: Fashions token details like name, image, animation_url, etc. for premint items.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/premints-create)​.
3. **[Retrieve Premints](https://docs.mintology.app/reference/premints-retrieve)**:
   - **Action**: Fetches premint details like name, image, animation_url, etc. for specified premint items.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/premints-retrieve)​.
4. **[Remove Premints](https://docs.mintology.app/reference/premints-remove)**:
   - **Action**: Extinguishes a specified premint entity.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/premints-remove)​​.
5. **[Import Premints](https://docs.mintology.app/reference/premints-import)**:
   - **Action**: Import token details like name, image, animation_url and etc.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/premints-import)​.

### IMX (Immutable X) Endpoints

1. **[Register IMX User](https://docs.mintology.app/reference/imx-register)**:
   - **Action**: Constructs an Immutable X layer 2 user account for an Ethereum layer 1 account.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/imx-register)​.
2. **[Mint IMX Item](https://docs.mintology.app/reference/imx-mint)**:
   - **Action**: Mints a distinct digital asset on an IMX blockchain, typically on the Ethereum network.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/imx-mint).
3. **[Transfer IMX Item](https://docs.mintology.app/reference/imx-transfer)**:
   - **Action**: Transfers an NFT, sending ownership of the digital asset from one address on the IMX blockchain to another.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/imx-transfer)​.

### Info Endpoints

1. **[Project Info](https://docs.mintology.app/reference/meta-info)**:
   - **Usage**: Procures project information such as details and configuration.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/meta-info)​​.

### Metadata Endpoints

1. **[Update NFT Metadata](https://docs.mintology.app/reference/metadata-update)**:
   - **Usage**: Alters NFT metadata encompassing details like token name, image, animation_url, etc., recommended to be invoked from the back-end.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/metadata-update).

### Mint Endpoints

1. **[Mint](https://docs.mintology.app/reference/mint)**:
   - **Purpose**: Facilitates the minting process of NFTs directly into a user's wallet.
   - **Compatibility**: Supports both custom Mintable Wallets and standard cryptocurrency wallets.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/mint).

### Claim Endpoints

1. **[Claim](https://docs.mintology.app/reference/claim)**:
   - **Purpose**: Grants a complimentary NFT to the user's wallet.
   - **Use Cases**: Suitable for purposes like discount vouchers or proof of attendance tokens.
   - **Reference**: [Documentation Source](https://docs.mintology.app/reference/claim).
