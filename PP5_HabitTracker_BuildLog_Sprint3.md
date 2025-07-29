## ✅ Sprint 3 – Habits & Logs Foundations

### 🎯 Goal
Introduce core models and endpoints for tracking user habits and associated logs.

---

### 🔧 Tasks Completed

- Created `habits` app and registered in `INSTALLED_APPS`
- Defined `Habit` model with:
  - `owner` (FK to `User`)
  - `title`, `description`, `goal_type`, `is_active`, `created_at`
- Created `HabitSerializer` and `HabitList` / `HabitDetail` views using DRF generic CBVs
- Added `habits/urls.py` with paths for:
  - `/habits/` – list + create
  - `/habits/<id>/` – retrieve + update + delete
- Included `habits.urls` in root project `urls.py`
- Confirmed `/habits/` endpoint works and returns correct data

---

### 🧱 LogEntry Planning

- Planned `LogEntry` model with fields:
  - `habit` (FK), `owner` (FK), `timestamp`, `status`, `note`
- Encountered naming conflict with Django Admin’s `LogEntry`
  - ✅ Fixed by setting `related_name='log_entries'` on FK to `User`
- Updated `Habit.owner` to use `related_name='habits'` to avoid collision

---

### 🐛 Bug Fixes

1. **Reverse accessor conflict with Django’s `admin.LogEntry`**
   - ✅ Fixed by renaming related_name on `LogEntry.owner`

2. **Collision between `Habit.owner` and `LogEntry.owner`**
   - ✅ Fixed by assigning distinct `related_name` values for each

3. **404 on `/logs/`**
   - ✅ Cause: LogEntry views were routed without being defined
   - ✅ Solution: Removed views from `urls.py` until implemented

---

### 🛠️ Notes

- Decided to follow Code Institute walkthrough patterns using:
  - Class-based views (ListCreateAPIView / RetrieveUpdateDestroyAPIView)
  - App-level `urls.py` and manual route wiring
- Deferred ERD until data model is finalized
- Deferred LogEntry views until next session

---

✅ Sprint 3 in progress — Habit API working, logs scaffold next.