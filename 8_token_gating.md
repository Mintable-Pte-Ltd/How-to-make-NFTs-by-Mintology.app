# Token Gating

**IMPORTANT:** Before you start using the APIs for Token Gating, make sure that you have a Wallet ready with the token to test it out, if not follow the flow mentioned at the end of [Quickstart]()

## How Token Gating Works

Using these APIs, developers can restrict access to specific content, ensuring only those with a particular NFT can view it. This functionality can be leveraged for exclusive content, premium experiences, and more.

## How to use the API

In order to demonstrate authorization based on NFT ownership and grant access accordingly, we'll be utilizing the Authorize endpoint. This endpoint validates token ownership using the Mintology API Key and Project ID. The guide will walk through a scenario where a developer needs to check if a certain email address has been minted a specific NFT, and if so, grant access to a special page, product, or discount.

## Authorization Based on NFT Ownership

### Step 1: Set up the Authorization Check

Firstly, you'll need to make a request to the Authorize endpoint to check for NFT ownership based on the user's email address.

#### Endpoint:

- **URL**: `https://api.mintology.app/v1/{projectId}/authorize`
- **Method**: `POST`
- **Important**: Make this call from the back-end.

#### Parameters:

- `projectId` (string, required): Your project ID found on your dashboard.
- `email` (string, required): The email address of the user you want to check NFT ownership for.
- `token_id` (string, optional): This is the token id of the specific NFT token within the contract and it is optional; if absent, any token in the contract will authorize the wallet.

#### Example Request (Node.js):

```javascript
const axios = require('axios');

async function checkNFTOwnership() {
  const response = await axios.post(
    'https://api.mintology.app/v1/{projectId}/authorize',
    {
      walletAddress: 'walletAddress',
    },
    {
      headers: {
        'Api-Key': 'Your API Key',
      },
    }
  );
  return response.data;
}

checkNFTOwnership();
```

### Step 2: Grant Access Based on Authorization Result

The response from the Authorize endpoint will tell you if the specified email address has a specific NFT. Based on the response, you can then program your application to grant or deny access to the special page, product, or discount.

```javascript
async function grantAccess() {
  const ownershipData = await checkNFTOwnership();

  if (ownershipData.authorized) {
    // User has the NFT, grant access
    console.log('Access granted');
    // Redirect to special page, grant discount, etc.
  } else {
    // User does not have the NFT, deny access
    console.log('Access denied');
    // Redirect to a different page, show an error message, etc.
  }
}

grantAccess();
```

### Alternatives

You can also use the **[List Authorised Tokens](https://docs.mintology.app/reference/authorize)** endpoint to get the list of tokens that a user owns from a particular collection and modify what is accessible for the user through it.
