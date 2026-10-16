# Plain Day Studio — Official Multiplatform Website

> Official developer website for **Plain Day Studio** — an independent mobile app studio building focused applications for **Android (Google Play)** and **Apple iOS (App Store)**.

---

## 📱 Apps in Build & Closed Beta Testing

| App | Category | Storage Model | Pricing Model | Status |
| :--- | :--- | :--- | :--- | :--- |
| **SwimPulse Pro** | Sports / Swimming | Cloud Sync (Phone/Email) | Free / Pro Subscription | Closed Beta |
| **Do Nothing** | Mindfulness & Screen Time | 100% Offline | Free | Closed Beta |
| **Breathing** | Mindfulness & Breathwork | 100% Offline | Free | Closed Beta |
| **Stare** | Visual Mindfulness & Eye Rest | 100% Offline | Free | Closed Beta |
| **Pop** | Haptic Fidget & Stress Relief | 100% Offline | Free | Closed Beta |
| **One Thing** | Single-Task Focus (5/10/15m) | 100% Offline | Free | Closed Beta |
| **Wait** | Micro-Pauses & Intentionality | 100% Offline | Free | Closed Beta |
| **One Question** | Daily Thoughtful Journal | Local Only | Free | Closed Beta |
| **PhoneDown** | Sensor-Driven Phone Detox | 100% Offline | Free | Closed Beta |
| **SplitPlain** | Group Expense Splitting | Cloud Sync (Phone/Email) | Free / Pro Subscription | Closed Beta |

---

## 📁 Architecture & File Layout

```
website/
├── index.html       # Landing page (Hero, 10-App Beta Showcase, Filters, Beta Signup)
├── privacy.html     # Apple App Store & Google Play compliant Privacy Policy
├── terms.html       # Terms of Service, Subscriptions & Beta Testing Terms
├── contact.html     # Developer Support, Bug Tracker, & Beta Feedback Form
└── README.md        # Studio Documentation & Deployment Guide
```

---

## ⚡ Quick Preview

To preview the website right now on your Mac:
```bash
open index.html
```

Or start a local web server:
```bash
python3 -m http.server 3000
```
Then visit **`http://localhost:3000`** in your browser.

---

## 🛡️ Store Compliance Checklist

### Google Play Console
1. **Privacy Policy Link**: `https://yourdomain.com/privacy.html`
2. **Developer Contact**: `contact.plaindaystudio@gmail.com`
3. **Closed Testing Track (20 Testers)**: Collect tester emails via the beta form on `index.html`.

### Apple App Store & App Store Connect
1. **Privacy Policy URL**: `https://yourdomain.com/privacy.html`
2. **Support URL**: `https://yourdomain.com/contact.html`
3. **Marketing URL**: `https://yourdomain.com`
4. **Account Deletion Compliance (Guideline 5.1.1(v))**: Documented in `privacy.html` with in-app deletion and email-based deletion flow.
5. **Subscription Terms (Guideline 3.1.2)**: Auto-renewal, cancellation, and billing policies detailed in `terms.html`.
