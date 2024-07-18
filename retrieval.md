# Guide for Using the Hyperbee Retrieval Product
Welcome to the Hyperbee retrieval product guide. This document will help you navigate the platform and utilize its features effectively. You can create collections, upload documents, obtain an API key, and interact with your documents using both the platform and the chat interface.
## Overview
Hyperbee consists of two main pages: the **Platform** and **Chat**. Here’s a step-by-step guide to get you started:
### 1. Creating and Managing Collections
1. **Login to Platform:**
   Visit [platform.hyperbee.ai](https://platform.hyperbee.ai) and log in to your account.
2. **Create a Collection:**
   Navigate to the **Collections** section.
3. **Upload Documents:**
   Click on the upload button to add your documents to the collection. After the upload is complete, you will receive a confirmation email.
4. **Access Confirmation Email:**
   Check your email for a confirmation message indicating that your collection is ready.
### 2. Using the Chat Interface
Once you have created a collection on the platform, you can interact with your documents via the chat interface.
1. **Login to Chat:**
   Go to [chat.hyperbee.ai](https://chat.hyperbee.ai) and log in with the same account used for the platform.
2. **Select Your Collection:**
   After logging in, choose your collection to start interacting with your documents.
### 3. Maximizing Performance
For optimal performance, we recommend upgrading to the **Advance plan** from the pricing section on the chat page. This plan provides access to premium models for the best results.
## Using the API
If you prefer to use the API, follow these steps after setting up your collection:
1. **Create an API Key:**
   After receiving the confirmation email, go back to the platform and generate an API key.
2. **Get Collection ID:**
   In the **Collections** section, click the three-dot button next to your collection and select "Copy ID" to obtain the collection ID.
3. **Make a cURL Request:**
   Use the following cURL command to interact with your documents via the API:
   ```sh
   curl --location 'https://api-rag.hyperbee.ai/v1/chat/completions' \
   --header 'Content-Type: application/json' \
   --header 'Authorization: Bearer <YOUR_API_KEY>' \
   --data '{
     "namespace": "<YOUR_NAMESPACE_ID>",
     "messages": [
       {"role": "user", "content": "Which countries have players about different sports?"}
     ],
     "model": "hive",
     "optimization": "quality"
   }'
   ```
Replace `<YOUR_API_KEY>` with your API key and `<YOUR_NAMESPACE_ID>` with your collection ID.

## Using the Python Client
TODO

## Summary
1. **Login to platform.hyperbee.ai** and create your collection.
2. **Upload your documents** and wait for the confirmation email.
3. **Login to chat.hyperbee.ai** and select your collection to start interacting.
4. **For API use**, generate an API key and obtain your collection ID from the platform.
For maximum performance, consider subscribing to the **Advance plan** for access to premium models.
Feel free to reach out if you have any questions or need further assistance. Enjoy using Hyperbee!