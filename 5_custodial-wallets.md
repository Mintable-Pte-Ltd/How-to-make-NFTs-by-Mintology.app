---
hidden: false
# slug: mintable-wallets
category: 64e5f94ae377a50070c31bc9
title: Mintable Wallets
description: Once you have preminted NFTs, you would need to create wallets for your users to store the NFTs. Mintology provides a way to create custodial wallets, where users can later claim custody of their private keys. This process also creates a Mintable account for the users.
---

# Mintable Wallets

Once you have preminted NFTs, you would need to create wallets for your users to store the NFTs. Mintology provides a way to create custodial wallets, where users can later claim custody of their private keys. This process also creates a Mintable account for the users.

## What are Mintable Wallets

### The Issue

A crypto wallet is basically at its core is a set of keys (private keys, to be precise) that need to be kept ultra-secret and are used to sign messages. There are lots of noncustodial wallets (like Metamask, Coinbase, and more) out there, but they demand your users to be crypto-savvy and take the whole responsibility of keeping their private key or seed under wraps.

### Mintology's solution

Mintology allows you to offer custodial wallets to your users. No crypto jargon, no extra knowledge needed, it's just like having an extra account. They can stick to their fave login methods (Google, Apple, you name it) and they’re good to go.

### The User’s Journey

Some users might get curious and want to dive deeper, deciding to take charge of their assets by themselves. They can do this right from their profile page on [Mintable](https://mintable.com), but you can control the entire process from your own website using the Mintology API. Designed with security at its core, the API ensures your users have truly taken control of their key before it gets deleted from our system.

## How to use the APIs

**IMPORTANT**: Before you start using the APIs, make sure that you have enabled Mintable Wallets on your Settings page on [Mintology web app](https://dashboard.mintology.app)

Below are the steps to create a custodial wallet:

#### Endpoint:

- **URL**:`https://api.mintology.app/v1/custodial-wallets`
- **Method**: `POST`
- **Important**: Make this call from the back-end.

#### Body Parameters:

- `email` (required, string): The email address of the user for whom the wallet is being created.

- `username` (optional, string): The username associated with a Mintable.com account. If omitted, a random username will be generated, which the user can later change on Mintable.com.

#### Example Request (Node.js):

```javascript
const axios = require('axios');

async function createWallet() {
  const response = await axios.post(
    'https://api.mintology.app/v1/custodial-wallets',
    {
      email: 'user@example.com',
      username: 'user123', // Optional
    },
    {
      headers: {
        'Api-Key': 'Your API Key',
      },
    }
  );
  console.log(response.data);
}

createWallet();
```

#### Response:

Upon a successful wallet creation, a response will be received with the following data:

- `email` (string): The email address tied to the wallet.

- `username` (string): The username tied to this wallet, generated randomly if not provided.

- `wallet_address` (string): The created wallet address.

With the wallet created, you can now proceed to either mint or claim NFTs into these wallets.

## Helping a User to take custody of their wallet

If you choose to let your users take control of their key from your website, here’s the path to follow:

1. Kickstart the private key claim process with the **[Request To Export](https://docs.mintology.app/reference/custodial-wallets-exports-request)** endpoint: Doing this sends an email from Mintable to the user with an OTP. This OTP is our safety check to ensure your user genuinely wants to take control of their key.

2. Get the user to share the OTP received from Mintable, and pass it to the **[Approve Export](https://docs.mintology.app/reference/custodial-wallets-exports-approve)** endpoint.

3. Hand over the key to your user, making sure they grasp the big deal of taking control and have jotted down their key somewhere safe. **Remember, it's crucial to spell this out to them clearly, and this is your responsibility!**

4. Ask Mintology to erase the private key from Mintable's database through **[Remove Mintable Wallets](https://docs.mintology.app/reference/custodial-wallets-remove)** endpoint.

## A Peek into Encryption Technicalities 🔐

To amp up the security, we’ll hand you an encrypted private key. You’ll need to decrypt it before showing it to the user. Your decryption process will need your Mintology API Key (a secret you already know) and the `encrypt_iv` parameter (a fresh secret), which is returned to you by the _Approve Export_ endpoint. Here's a little code snippet to show you how to decrypt the key.

```ts
const { createDecipheriv } = require('crypto');

const IV_INPUT = 'YOUR_IV';

const PRIVATEKEY_INPUT = 'ENCRYPTED_PRIVATE_KEY';

const ENCRYPTION_SECRET_INPUT = 'YOUR_API_KEY';

const iv = Buffer.from(IV_INPUT);

const encryptedText = Buffer.from(PRIVATEKEY_INPUT);

const encryptionSecret = Buffer.from(ENCRYPTION_SECRET_INPUT);

const decipher = createDecipheriv('aes-256-cbc', encryptionSecret, iv);

let decrypted = decipher.update(encryptedText);

decrypted = Buffer.concat([decrypted, decipher.final()]);

console.log('decrypted private key', decrypted.toString());
```

To tie up loose ends, you’ll need to provide a SHA256 hash (a variant of SHA-2) of the last 8 characters of the private key. This ensures that if you goof up the decryption, the key won't be deleted from the Mintable database by mistake.

Letting a user claim custody of their wallet is a bit complex, do reach out to [Mintology support](https://dashboard.mintology.app/contact-us) anytime!
