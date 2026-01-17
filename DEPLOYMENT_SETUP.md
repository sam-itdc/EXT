# Cloudflare R2 Deployment Setup

This repository is configured to automatically deploy to Cloudflare R2 when changes are pushed to the main branch.

## GitHub Secrets Required

The following secrets must be configured in the repository settings:

### Required Secrets

1. **R2_ACCESS_KEY_ID**
   - Description: Cloudflare R2 Access Key ID
   - How to get: Cloudflare Dashboard → R2 → Manage R2 API Tokens

2. **R2_SECRET_ACCESS_KEY**
   - Description: Cloudflare R2 Secret Access Key
   - How to get: Cloudflare Dashboard → R2 → Manage R2 API Tokens

3. **R2_ENDPOINT**
   - Description: R2 API endpoint URL
   - Format: `https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com`
   - How to get: Cloudflare Dashboard → R2 → Settings

4. **R2_BUCKET**
   - Description: R2 bucket name
   - Example: `your-bucket-name`

5. **R2_DEV_URL** (Optional)
   - Description: R2 development URL for PR comments
   - Format: `https://pub-YOUR_BUCKET_HASH.r2.dev`
   - How to get: Cloudflare Dashboard → R2 → Bucket Settings → Public Development URL

6. **CUSTOM_DOMAIN_URL** (Optional)
   - Description: Custom domain URL for PR comments
   - Format: `https://your-domain.com`

## R2 Bucket Configuration

Configure your R2 bucket with the following settings:

- **Region**: Choose the region closest to your users (e.g., APAC, ENAM, WEUR)
- **Public Access**: Enable if you want the bucket to be publicly accessible
- **Custom Domain**: Configure your custom domain in Cloudflare R2 settings

## Deployment Workflow

The GitHub Actions workflow (`.github/workflows/deploy-to-r2.yml`) will automatically:

1. Trigger on push to `main` branch
2. Sync all files to R2 bucket
3. Post a comment on the merged PR with deployment information

## Accessing the Website

After deployment, your website will be accessible via:

- **R2 Development URL**: `https://pub-YOUR_BUCKET_HASH.r2.dev`
- **Custom Domain**: `https://your-domain.com` (if configured)

## Setup Instructions

1. Go to repository Settings → Secrets and variables → Actions
2. Add all required secrets listed above
3. Push changes to `main` branch to trigger deployment
4. Check GitHub Actions tab for deployment status

## Troubleshooting

- If deployment fails, check GitHub Actions logs
- Verify all secrets are correctly configured
- Ensure R2 bucket exists and is accessible
- Check R2 API token permissions
