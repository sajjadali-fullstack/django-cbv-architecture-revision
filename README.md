## Django Class Based Views (CBV) Demo Project

A beginner-friendly Django project demonstrating the implementation of **Function Based Views (FBV)** and **Class Based Views (CBV)** using Django's built-in generic views.

## 📌 Features

* Function Based Home View
* Class Based View (CBV) Example
* TemplateView Example
* Context Data Passing using CBV
* Bootstrap 5 Responsive UI
* Clean Navigation Dashboard

---

## 🛠️ Technologies Used

* Python
* Django
* HTML5
* CSS3
* Bootstrap 5

---

## 📂 Project Structure

```text
project/
│
├── testapp/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── testapp/
│   │       ├── index.html
│   │       ├── result.html
│   │       └── outcome.html
│
└── manage.py
```

---

## 🎯 Implemented Views

### 1️⃣ Function Based View (FBV)

```python
def home_view(request):
    return render(request, 'testapp/index.html')
```

Displays the home page with navigation buttons.

---

### 2️⃣ Class Based View (CBV)

```python
class HelloWorld(View):
    def get(self, request):
        return HttpResponse('This response is coming from CBV')
```

Returns a direct HTTP response using a Class Based View.

---

### 3️⃣ TemplateView Example

```python
class TemplateCBV(TemplateView):
    template_name = 'testapp/result.html'
```

Renders a template using Django's generic TemplateView.

---

### 4️⃣ Passing Context Data Using CBV

```python
class TemplateCBV2(TemplateCBV):
    template_name = 'testapp/outcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'Sajjad Ali'
        context['rollno'] = 128
        context['course'] = 'Full Stack Python'

        return context
```

Demonstrates how to pass dynamic data from a CBV to a template.

---

## 🖥️ Home Page Navigation

The home page provides quick navigation to:

* Direct View Response
* Template Result
* Student Registry Context

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/django-cbv-demo.git
```

### Move to Project Folder

```bash
cd django-cbv-demo
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 📚 Learning Objectives

This project helps beginners understand:

* Function Based Views (FBV)
* Class Based Views (CBV)
* Django Generic Views
* Template Rendering
* Context Data Handling
* URL Routing
* Bootstrap Integration

---

## 👨‍💻 Author

**Sajjad Ali**

Full Stack Python Developer

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub and share it with other Django learners.
