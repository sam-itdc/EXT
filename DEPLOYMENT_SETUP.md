# Cloudflare R2 Deployment Setup

This repository is configured to automatically deploy to Cloudflare R2 when changes are pushed to the main branch.

## GitHub Secrets Required

The following secrets must be configured in the repository:

- `R2_ACCESS_KEY_ID`: Cloudflare R2 Access Key ID
- `R2_SECRET_ACCESS_KEY`: Cloudflare R2 Secret Access Key

## R2 Bucket Information

- **Bucket Name**: scoutmac
- **Account ID**: 54911001cd87addf755fbc08be3c974f
- **Region**: APAC
- **R2 Dev URL**: https://pub-877186fb13fa408c849c9c182ea49cfc.r2.dev
- **Custom Domain**: https://scoutmac.wpang.net

## Deployment Workflow

The GitHub Actions workflow will automatically sync all files to R2 when changes are pushed to main.

## Accessing the Website

- **R2 Development URL**: https://pub-877186fb13fa408c849c9c182ea49cfc.r2.dev/index.html
- **Custom Domain**: https://scoutmac.wpang.net
