# 🚀 Deploy to Railway - Quick Guide

## Step 1: Get Your MongoDB Atlas Connection String

1. Go to [MongoDB Atlas](https://cloud.mongodb.com)
2. Select your `cluster0`
3. Click **"Connect"**
4. Choose **"Connect your application"**
5. Copy the connection string (it looks like this):
   ```
   mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```

## Step 2: Deploy to Railway

1. Go to [Railway.app](https://railway.app)
2. Click **"New Project"**
3. Choose **"Deploy from GitHub repo"**
4. Select your chatbot repository
5. Railway will auto-detect Python and deploy

## Step 3: Set Environment Variables in Railway

In your Railway project dashboard:

1. Go to **"Variables"** tab
2. Add these variables:

   **MONGODB_URI**
   ```
   mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/chatbot_db?retryWrites=true&w=majority
   ```

   **GOOGLE_API_KEY**
   ```
   AIzaSyDw_gWd3Fs2OMlYwDieY1nb5cTUSzHv9OY
   ```

3. Click **"Deploy"**

## Step 4: Your App is Live! 🎉

Railway will give you a URL like: `https://your-project-name.up.railway.app`

## Test Your Deployed App

```bash
# Test the health endpoint
curl https://your-project-name.up.railway.app/

# Test the chat endpoint
curl -X POST https://your-project-name.up.railway.app/chat \
  -H "Content-Type: application/json" \
  -d '{"conversation_id": "test123", "message": "Hello!"}'
```

## View Your Data

Connect MongoDB Compass to your Atlas cluster to see conversations:
- Use the same connection string from Step 1
- Database: `chatbot_db`
- Collection: `conversations`

---

**That's it! Your chatbot is now live and persistent!** 🚀