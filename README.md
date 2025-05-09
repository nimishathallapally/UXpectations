# Good vs. Bad UI Design – An HCI Case Study

This project explores how aligning or violating **user mental models** affects the usability of web interfaces. Through side-by-side comparisons of well-designed and poorly-designed UI components, this case study highlights the importance of Human-Computer Interaction (HCI) principles in building intuitive and user-friendly web applications.

---

## 💡 Objective

To demonstrate how different design choices—good and bad—impact user behavior, usability metrics, and satisfaction. This project analyzes design decisions using real user feedback, visual comparisons, and metrics such as time on task, error rate, and efficiency.

---

## 🔍 Key Concepts

* **Mental Models:** User expectations based on prior experience.
* **Usability Principles:** Design heuristics that ensure intuitive, efficient interaction.
* **Violations:** UI elements that break conventions or user expectations.

---

## 🧪 Case Study Highlights

### ✅ Good Design

* **Intuitive navigation**
* **Readable text & proper contrast**
* **Consistent button placement and shape**
* **Feedback mechanisms post interactions**
* **Correct use of colors for actions (e.g., red = error, green = success)**

### ❌ Bad Design

* Inconsistent layouts and spacing
* Poor readability due to color or casing
* Misleading button shapes and placements
* No feedback after critical interactions
* Incorrect UI metaphors (e.g., red = correct)

---

## 📊 Usability Metrics

* **⏱️ Time on Task** – Time taken to complete key tasks
* **❌ Error Rate** – Mistakes made due to confusing design
* **✅ Effectiveness** – Task completion success rate
* **⚡ Efficiency** – Completion time vs. complexity
* **😊 Satisfaction** – Based on qualitative user feedback

---

## 🗂️ Project Structure

```
.
├── static/
│   ├── css/
│   │   ├── bad/                   # Styles for bad design pages
│   │   ├── good/                  # Styles for good design pages
│   │   └── style.css              # Shared or base styles
│   ├── images/                    # Design comparison screenshots
│   └── js/
│       ├── bad/                  # JS scripts for bad designs
│       └── good/                 # JS scripts for good designs
│
├── templates/
│   ├── bad/
│   ├── good/
│   │   └── index.html          
│
├── app.py                         # Flask backend logic
├── README.md                      # Project documentation
```

---

## 🛠️ Technology Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python with Flask
* **Database:** None (uses localStorage for demonstration)

---

## 🚦 Key Mental Model Violations

| Category            | Violation Example                      | Expected Behavior                            |
| ------------------- | -------------------------------------- | -------------------------------------------- |
| Login/Signup        | Misplaced buttons (bottom-left)        | Top-right, hover feedback, clickable pointer |
| Date Input          | Format: `YYYYMMDD`                     | More familiar: `DD/MM/YYYY` or `MM/DD/YYYY`  |
| Scroll Behavior     | Scroll down moves content up           | Scroll direction should match system default |
| Feedback Colors     | Red = correct, Green = incorrect       | Red = wrong, Green = correct                 |
| Text Capitalization | ALL CAPS everywhere                    | Use sentence case for legibility             |
| Quiz Submission     | No scroll or feedback after submission | Auto-scroll to feedback section              |

---

## 📋 Usability Testing

User testing highlighted several issues in the bad design:

* **Poor form formatting**
* **Unintuitive navigation**
* **Incorrect visual cues (e.g., color)**
* **Missing feedback mechanisms**

These insights reinforced the importance of mental models and consistency in UI/UX.

---

## ✅ Conclusion

Designing for **mental models** is essential for usability and user satisfaction. This project emphasizes that small deviations from expectations can have major impacts on usability, and adhering to core HCI laws leads to more intuitive, efficient, and enjoyable digital experiences.

---
