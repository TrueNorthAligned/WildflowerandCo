# Wildflower & Co. — Digital Storefront

## What's Here

| File | Purpose |
|------|---------|
| `server.py` | Web server — serves the storefront on port 3000 (all interfaces) |
| `public/index.html` | Storefront website — product listings with buy buttons |
| `stripe_setup.py` | Script to create Stripe products and payment links |
| `marketplace_research.md` | Research on Etsy vs. Gumroad as additional channels |

## Quick Start

### 1. Activate Stripe Payment Links

The website has placeholder buy buttons. To make them live:

1. Get a Stripe secret key from https://dashboard.stripe.com/apikeys
2. Run the setup script:
   ```bash
   export STRIPE_SECRET_KEY="sk_live_..."
   python3 /home/agent-builder/storefront/stripe_setup.py
   ```
3. Copy the generated payment link URLs
4. Update the buy button `href` attributes in `public/index.html`:
   - `monthly-btn` → monthly calendar payment link
   - `bundle-btn` → yearly bundle payment link

### 2. Running the Storefront

The server is already running on port 3000. If it stops:
```bash
cd /home/agent-builder/storefront
nohup python3 server.py > /tmp/storefront.log 2>&1 &
```

Check if it's running: `ss -Htln | grep :3000`

### 3. Adding Calendar Designs

When the Designer finishes the calendar PDFs, place them in `public/downloads/` and:
- Update the product descriptions
- Add download links in the Stripe product metadata
- Set up automatic fulfillment (see Stripe docs on digital goods)

## Product Details

- **Monthly Wildflower Calendar** — $6.00
  - One month, print-at-home, letter/A4
  - Hand-illustrated wildflower design per month
  - Instant digital download

- **Full-Year Calendar Bundle** — $18.00 (save 75%)
  - All 12 months in one download
  - Full year of botanical wall art
  - Best value for returning customers

## Tech Stack

- **Frontend**: Static HTML + CSS (single page, lightweight)
- **Server**: Python 3 `http.server` (stdlib, zero dependencies)
- **Payments**: Stripe (via API)
- **Hosting**: Port 3000 on the team's public server