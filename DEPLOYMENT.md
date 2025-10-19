# 🚀 Deployment Guide for Render

This guide will help you deploy your House Price Predictor to Render.

## 📋 Prerequisites

1. A GitHub account with your code pushed to a repository
2. A Render account (free tier available at https://render.com)
3. Ensure `model.pkl` is committed to your repository

## 📦 Required Files for Deployment

Your repository must include these files (already created):

- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python version specification
- ✅ `Procfile` - Tells Render how to run your app
- ✅ `.gitignore` - Excludes unnecessary files from git
- ✅ `script.py` - Updated to use PORT environment variable
- ✅ `model.pkl` - Your trained ML model
- ✅ `index.html` - Frontend interface

## 🔧 Step-by-Step Deployment

### 1. Commit and Push All Files

```bash
# Add all deployment files
git add requirements.txt runtime.txt Procfile .gitignore script.py model.pkl index.html

# Commit changes
git commit -m "Add deployment files for Render"

# Push to GitHub
git push origin main
```

### 2. Create Web Service on Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:

   **Basic Settings:**
   - **Name**: `house-price-predictor` (or your preferred name)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   
   **Build Settings:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn script:app`
   
   **Instance Type:**
   - Select **"Free"** (sufficient for demo/personal projects)

5. Click **"Create Web Service"**

### 3. Wait for Deployment

- Render will automatically build and deploy your app
- Initial deployment takes 2-5 minutes
- You'll see build logs in real-time

### 4. Access Your App

Once deployed, Render provides a URL like:
```
https://house-price-predictor-xxxx.onrender.com
```

## 🔍 Troubleshooting

### Issue: "Could not open requirements file"
**Solution**: Ensure `requirements.txt` exists and is pushed to GitHub

### Issue: "Model file not found"
**Solution**: Make sure `model.pkl` is committed to git (check `.gitignore` doesn't exclude it)

### Issue: "Application failed to respond"
**Solution**: 
- Check build logs on Render dashboard
- Ensure `script.py` uses `PORT` environment variable
- Verify all dependencies are in `requirements.txt`

### Issue: "Module not found" errors
**Solution**: Add missing package to `requirements.txt` and redeploy

### Issue: Cold starts (slow first request)
**Note**: Free tier on Render sleeps after 15 minutes of inactivity. First request after sleep takes 30-60 seconds.

## 📊 Important Notes

### Model File Size
- Your `model.pkl` is relatively small and suitable for git
- If your model exceeds 100MB, consider:
  1. Using Git LFS (Large File Storage)
  2. Downloading model from external storage on startup
  3. Upgrading to paid Render tier with persistent disk

### Environment Variables
If needed, you can add environment variables in Render dashboard:
- Go to your service → **Environment** tab
- Add variables like `FLASK_ENV`, `SECRET_KEY`, etc.

### Custom Domain
On Render's paid tiers, you can add a custom domain:
- Go to **Settings** → **Custom Domains**
- Follow instructions to configure DNS

## 🔄 Continuous Deployment

Render automatically redeploys when you push to GitHub:

```bash
# Make changes to your code
git add .
git commit -m "Update model/feature"
git push origin main

# Render automatically detects push and redeploys
```

## 💰 Free Tier Limitations

Render Free Tier includes:
- ✅ 750 hours/month (enough for one service)
- ✅ Automatic HTTPS
- ✅ Custom domains (with verification)
- ⚠️ Service spins down after 15 min inactivity
- ⚠️ 512 MB RAM limit
- ⚠️ Shared CPU

## 🚀 Alternative Deployment Platforms

If Render doesn't meet your needs, consider:

### Heroku
```bash
# Similar setup, uses Procfile
heroku create house-price-predictor
git push heroku main
```

### Railway
- Similar to Render, supports Procfile
- More generous free tier
- https://railway.app

### PythonAnywhere
- Good for Flask apps
- Free tier available
- https://www.pythonanywhere.com

### AWS Elastic Beanstalk
- More complex setup
- Better for production/enterprise
- Requires AWS account

## 📝 Post-Deployment Checklist

- [ ] App accessible via Render URL
- [ ] Homepage loads correctly
- [ ] Prediction form works
- [ ] API endpoint `/predict` responds correctly
- [ ] Test on mobile devices
- [ ] Monitor error logs in Render dashboard
- [ ] Set up custom domain (optional)
- [ ] Add SSL certificate (automatic on Render)

## 🎯 Testing Your Deployed App

```bash
# Test the API endpoint
curl -X POST https://your-app.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Area": 2500,
    "Bedrooms": 4,
    "Bathrooms": 3,
    "Floors": 2,
    "YearBuilt": 2010,
    "Location": "Suburban",
    "Condition": "Good",
    "Garage": "Yes"
  }'
```

## 📧 Support

- **Render Docs**: https://render.com/docs
- **Render Community**: https://community.render.com
- **Your GitHub Issues**: Create issues in your repo for tracking

---

**Congratulations! Your ML web app is now live! 🎉**

Share your deployment URL and let others try your house price predictor!
