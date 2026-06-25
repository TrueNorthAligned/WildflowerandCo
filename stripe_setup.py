#!/usr/bin/env python3
"""
Wildflower & Co. — Stripe Product & Payment Link Setup Script

This script creates Stripe products and payment links for:
1. Individual monthly wildflower calendars ($6.00 each)
2. Full-year bundle of all 12 months ($18.00)

Usage:
    export STRIPE_SECRET_KEY="sk_live_..."
    python3 stripe_setup.py
    
Or pass the key as an argument:
    python3 stripe_setup.py --key sk_live_...
"""

import os
import sys
import argparse
import stripe


def main():
    parser = argparse.ArgumentParser(description="Create Wildflower & Co. products in Stripe")
    parser.add_argument("--key", help="Stripe secret key (or set STRIPE_SECRET_KEY env var)")
    args = parser.parse_args()

    api_key = args.key or os.environ.get("STRIPE_SECRET_KEY")
    if not api_key:
        print("ERROR: No Stripe secret key provided.")
        print("Set STRIPE_SECRET_KEY environment variable or pass --key.")
        sys.exit(1)

    stripe.api_key = api_key

    print("=== Wildflower & Co. — Stripe Product Setup ===\n")

    # --- Product 1: Individual Monthly Calendar ---
    print("Creating product: Monthly Wildflower Calendar...")
    monthly_product = stripe.Product.create(
        name="Monthly Wildflower Calendar",
        description=(
            "A beautifully illustrated, print-at-home wildflower calendar for one month. "
            "Each page features a hand-crafted botanical design celebrating the season's "
            "wildflowers — perfect for nature lovers, gardeners, and anyone who loves "
            "bringing the outdoors in."
        ),
        metadata={
            "business": "Wildflower & Co.",
            "type": "monthly-calendar",
            "format": "digital-download",
        },
        images=[],  # Add calendar cover image URL when available
        url="https://wildflowerandco.store/calendar/monthly",  # Update when website is live
    )
    print(f"  ✓ Created product: {monthly_product.id}")

    # Create price for monthly calendar ($6.00)
    monthly_price = stripe.Price.create(
        product=monthly_product.id,
        unit_amount=600,  # $6.00 in cents
        currency="usd",
        metadata={"type": "monthly-calendar"},
    )
    print(f"  ✓ Created price: {monthly_price.id} ($6.00)")

    # Create payment link for monthly calendar
    monthly_link = stripe.PaymentLink.create(
        line_items=[{"price": monthly_price.id, "quantity": 1}],
        metadata={"product": monthly_product.id, "type": "monthly-calendar"},
        after_completion={"type": "redirect", "redirect": {"url": "https://wildflowerandco.store/thank-you"}},
    )
    print(f"  ✓ Created payment link: {monthly_link.url}")
    print()

    # --- Product 2: Full-Year Bundle ---
    print("Creating product: Full-Year Wildflower Calendar Bundle...")
    bundle_product = stripe.Product.create(
        name="Full-Year Wildflower Calendar Bundle",
        description=(
            "All 12 months of Wildflower & Co. print-at-home calendars in one bundle! "
            "A full year of botanical beauty — from spring blossoms to winter evergreens. "
            "Each month features a unique wildflower design, ready to print and display. "
            "Save 75% compared to buying individual months!"
        ),
        metadata={
            "business": "Wildflower & Co.",
            "type": "yearly-bundle",
            "format": "digital-download",
            "months_included": "12",
        },
        images=[],  # Add bundle cover image URL when available
        url="https://wildflowerandco.store/calendar/yearly-bundle",
    )
    print(f"  ✓ Created product: {bundle_product.id}")

    # Create price for yearly bundle ($18.00)
    bundle_price = stripe.Price.create(
        product=bundle_product.id,
        unit_amount=1800,  # $18.00 in cents
        currency="usd",
        metadata={"type": "yearly-bundle"},
    )
    print(f"  ✓ Created price: {bundle_price.id} ($18.00)")

    # Create payment link for yearly bundle
    bundle_link = stripe.PaymentLink.create(
        line_items=[{"price": bundle_price.id, "quantity": 1}],
        metadata={"product": bundle_product.id, "type": "yearly-bundle"},
        after_completion={"type": "redirect", "redirect": {"url": "https://wildflowerandco.store/thank-you"}},
    )
    print(f"  ✓ Created payment link: {bundle_link.url}")
    print()

    # --- Summary ---
    print("=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print(f"\nProduct 1: Monthly Wildflower Calendar")
    print(f"  Stripe ID : {monthly_product.id}")
    print(f"  Price     : $6.00 ({monthly_price.id})")
    print(f"  Buy Link  : {monthly_link.url}")
    print(f"\nProduct 2: Full-Year Wildflower Calendar Bundle")
    print(f"  Stripe ID : {bundle_product.id}")
    print(f"  Price     : $18.00 ({bundle_price.id})")
    print(f"  Buy Link  : {bundle_link.url}")
    print(f"\n✅ Share these payment links with customers!")
    print(f"✅ Integrate them into the website at /home/agent-builder/storefront/")


if __name__ == "__main__":
    main()