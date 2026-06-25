# Marketplace Research: Etsy vs. Gumroad for Wildflower & Co.

## Recommendation

**Start with both Etsy AND Gumroad** — they serve different customer acquisition roles:

| | **Etsy** | **Gumroad** |
|---|---|---|
| **Audience** | Built-in buyer traffic (millions/month) | Creator-focused, smaller but engaged |
| **Discovery** | ✅ Strong organic search (SEO) | ❌ No built-in marketplace |
| **Fees** | $0.20 listing + 6.5% transaction | 0% listing fee, ~3.5% + $0.30 transaction (free tier) |
| **Digital delivery** | Built-in (auto-download after purchase) | Built-in (auto-download + email) |
| **Custom domain** | No (subdomain only) | Yes (own domain) |
| **Marketing tools** | Etsy Ads, coupons, sales | Email lists, discount codes, affiliates |
| **Ease of setup** | Guided wizard | Simple, developer-friendly |
| **Best for** | Customer acquisition & discovery | Direct sales & repeat customers |

## Strategy: Use Both as a Funnel

### Etsy — Top of Funnel (Acquisition)
- **Why**: Etsy already has millions of shoppers searching for "printable calendar", "botanical wall art", "wildflower decor". You get organic discovery.
- **Setup Steps**:
  1. Create an Etsy shop: `etsy.com/your/shop`
  2. Create listings for:
     - "Monthly Wildflower Calendar — Printable PDF" ($6)
     - "Full Year Wildflower Calendar Bundle — 12 Months" ($18)
  3. Use keywords: printable wildflower calendar, botanical wall art, nature calendar, flower calendar PDF
  4. Upload cover image + one sample month as listing photos
  5. Set up automatic digital delivery
- **Fees per $6 sale**: $0.20 listing + $0.39 Etsy fee + ~$0.21 payment processing ≈ **$0.80 in fees** (~13%)

**Etsy Sample Listing Description:**
> Bring the beauty of wildflowers into your home with our print-at-home wildflower calendar! Each month features a stunning hand-illustrated botanical design that celebrates the season's natural blooms. Perfect for nature lovers, gardeners, and anyone who wants to add a touch of calm, natural beauty to their wall.
>
> 🌸 Instant digital download — print on your own paper
> 🌿 Standard letter/A4 size
> 🌻 Beautiful botanical illustrations
> 🖨️ Print at home, office, or local print shop
>
> Simply purchase, download, print, and enjoy!

### Gumroad — Direct Sales (Retention)
- **Why**: Lower fees, no listing fees, full control over customer relationship. Better for repeat buyers and bundles.
- **Setup Steps**:
  1. Create a Gumroad account at `gumroad.com`
  2. Set up products:
     - "Monthly Wildflower Calendar" ($6)
     - "Full-Year Wildflower Calendar Bundle" ($18)
  3. Enable Gumroad's email list to notify customers when new months drop
  4. Use Gumroad's license keys for version management
  5. Offer discount codes for repeat customers
- **Fees per $6 sale (free tier)**: ~$0.21 + ~$0.30 = **~$0.51 in fees** (~8.5%)

### Our Own Stripe-powered Site — Highest Margin
- **Why**: Zero platform fees beyond Stripe processing (2.9% + $0.30)
- **Fees per $6 sale**: ~$0.17 + $0.30 = **~$0.47 in fees** (~7.8%)
- **Setup**: Already built at `/home/agent-builder/storefront/` — just add Stripe payment links

## Pricing Strategy Comparison

| Channel | Monthly Price | Bundle Price | Customer Benefit |
|---------|:-----------:|:-----------:|:----------------|
| Stripe (our site) | $6.00 | $18.00 | Best price (no platform markup) |
| Etsy | $6.00 | $18.00 | Etsy buyer protection & discovery |
| Gumroad | $6.00 | $18.00 | Cross-sell & email updates |

## Recommended Action Items

1. **Immediate**: Get a Stripe secret key and run `stripe_setup.py` to activate payment links on the storefront
2. **This week**: Set up the Gumroad store — it's fast (15 min) and you own the customer list
3. **Next week**: Set up Etsy shop — takes longer but drives organic traffic
4. **Ongoing**: 
   - Upload real calendar designs as listing photos once ready
   - Add customer reviews to build social proof
   - Consider seasonal promotions (spring bundle, holiday gift guide)

## Technical Requirements

- **Digital file delivery**: All three platforms support auto-delivery of PDFs after purchase
- **File hosting**: Upload the calendar PDFs to the platform directly (no external host needed)
- **Fulfillment**: Fully automated — customer pays, gets the download link, prints at home
- **No inventory**: Digital goods, zero stock management needed