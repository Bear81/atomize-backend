## ✅ Sprint 2 – User & Profile Foundations

### 🎯 Goal
Extend the Django User model with a Profile to store additional user information and enable access via authenticated API endpoints.

---

### 🔧 Tasks Completed

- **Created `accounts` app** and added to `INSTALLED_APPS`
- **Defined `Profile` model** with `bio`, `image`, `name`, and timestamps
- Linked `Profile` to `User` via `OneToOneField`
- Added `Profile` to `admin.py`
- **Created Django signal** to auto-generate `Profile` on user registration
- Registered signal in `apps.py` and updated `INSTALLED_APPS` to use `AccountsConfig`
- **Created custom `CurrentUserSerializer`** extending `UserDetailsSerializer`
  - Exposes `profile_id` and `profile_image` in `/dj-rest-auth/user/`
- Updated `REST_AUTH_SERIALIZERS` to use custom serializer
- Tested registration, login, and profile fetching via DRF browsable API

---

### 🧪 Testing

- Registered test users via `/dj-rest-auth/registration/`
- Verified automatic `Profile` creation using Django shell and `/admin/`
- Confirmed successful responses from:
  - `/dj-rest-auth/login/`
  - `/dj-rest-auth/user/`
- Confirmed `profile_id` and `profile_image` included in user response

---

### 🐛 Bug Fixes

1. **Missing `_has_phone_field` on RegisterSerializer**
   - ⚠️ Cause: Incompatible `dj-rest-auth` + `allauth` versions
   - ✅ Fix: Downgraded `dj-rest-auth` to `2.2.5`
   - 📚 Reference: https://stackoverflow.com/questions/44234597/django-drf-token-authentication

2. **Missing `send_email_confirmation` after downgrade**
   - ⚠️ Cause: `dj-rest-auth==2.2.5` incompatible with `django-allauth==65.x`
   - ✅ Fix: Downgraded `django-allauth` to `0.51.0` (stable with dj-rest-auth)

3. **Missing `AccountMiddleware` in downgraded allauth**
   - ⚠️ Cause: Middleware was added in allauth >=65
   - ✅ Fix: Removed `'allauth.account.middleware.AccountMiddleware'` from `MIDDLEWARE`

4. **Registration triggered `ConnectionRefusedError`**
   - ⚠️ Cause: Email backend not configured
   - ✅ Fix: Set email config in `settings.py`:
     ```python
     ACCOUNT_EMAIL_VERIFICATION = 'none'
     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
     ```
   - 📚 Reference: https://docs.djangoproject.com/en/5.2/topics/email/

---

✅ Sprint 2 completed and committed.