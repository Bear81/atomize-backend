# PP5 – Habit Tracker Build Log

_A structured development and assessment log for the Final Project – Advanced Front-End_

---

## 📋 Assessment Criteria Tracker

### ✅ Pass
- [ ] Front-End: JSX, components, styling, UX (LO1)
- [ ] Back-End: API, custom models, CRUD (LO3)
- [ ] Integration: Frontend consumes API, forms, auth, error handling (LO4)
- [ ] Agile: GitHub Projects, commits, planning (LO2)

### 🔷 Merit
- [ ] Clear app purpose, intuitive UI
- [ ] Custom models (not based on Moments)
- [ ] Hooks, advanced JS, search/filter
- [ ] All user stories mapped & documented

### 🔶 Distinction
- [ ] Original app, professional polish
- [ ] Custom hooks / many-to-many models
- [ ] Defensive design, error handling
- [ ] Custom automated tests (FE + BE)
- [ ] Advanced filtering, responsive UX

---

## 🧠 Design & Planning

### 🎯 Project Overview
- **App Name**: 
- **Domain**: Habit Tracker
- **Core Feature Summary**:

### 🗂️ Data Models & Relationships
- **User**
- **Habit**
- **Entry / Log**
- *(add additional models here)*

### 📊 ERD (Entity Relationship Diagram)
- *(link or ASCII diagram here)*

---

## 🔧 API Endpoints (DRF)

| Method | Endpoint        | Description                 | Auth Required |
|--------|------------------|-----------------------------|----------------|
| GET    | /habits/         | List all habits             | ✅             |
| POST   | /habits/         | Create new habit            | ✅             |
| PUT    | /habits/:id/     | Edit habit                  | ✅             |
| DELETE | /habits/:id/     | Delete habit                | ✅             |
| ...    | ...              | ...                         | ...            |

---

## 🧪 Testing Log

### 📝 Manual Testing
- [ ] Frontend UX walkthrough
- [ ] API CRUD tested via Postman
- [ ] Mobile responsiveness
- [ ] Auth routes tested

### 🧪 Automated Testing
- [ ] DRF model/view tests
- [ ] React component tests (if time allows)

---

## 📘 UX & Design Decisions

- **Wireframes Link**:
- **Component Layout Decisions**:
- **Accessibility Choices**:
- **Styling Framework**: (Bootstrap, custom CSS, etc.)

---

## 🚧 Development Log

| Date       | Area          | Summary                                     | Commit Ref |
|------------|---------------|---------------------------------------------|------------|
| 28 Jul 25  | Backend        | Started models.py – created Habit model     | ab123c     |
| ...        | Frontend       | Initial React setup & HomePage              | ...        |

---

## 🛠️ Issues to Investigate

- [ ] JWT logout bug on mobile
- [ ] Form validation feedback styling
- [ ] DRF permissions test failure

---

## 📝 TODO / Next Steps

- [ ] Define custom user profile fields
- [ ] Setup habit streak logic
- [ ] Add category filters to habit list
- [ ] Style mobile navbar
- [ ] Write README sections: Deployment, Features, Testing