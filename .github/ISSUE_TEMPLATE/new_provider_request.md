---
name: 🔌 New Provider Request
about: Request support for a new affiliate network or merchant platform
title: '[PROVIDER] Add support for <Provider Name>'
labels: 'new provider'
assignees: ''
---

## 🛒 Provider / Network Name
Name of the affiliate network or merchant (e.g. ClickBank, BestBuy, Target, Partnerize, Pepperjam).

## 🌐 Network Website / Documentation
- Merchant / Network URL: `https://...`
- Developer / Link Builder Docs (if available): `https://...`

## 🔗 URL Pattern & Parameters
- **Sample Normal URL**: `https://www.example.com/product/123`
- **Required Credentials**: [e.g. `affiliate_id`, `sub_id`, `campaign_id`]
- **Sample Affiliate Link Format**: `https://www.example.com/product/123?affid=YOUR_ID`

## 💡 Usage Example
How you envision passing credentials via Python API or CLI:
```bash
python main.py "https://www.example.com/product/123" --mynetwork-id "my_tag"
```

## 📝 Additional Context
Any special handling required (e.g., deep linking wrappers, base64 encoding, redirect domains)?
