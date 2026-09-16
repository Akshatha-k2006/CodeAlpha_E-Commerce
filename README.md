# CodeAlpha_E-Commerce
E-Commerce website 
# 🌿 PlantNest

**PlantNest** is a simple, India-focused e-commerce website dedicated to indoor plants. The platform allows users to browse plants, view detailed product information, add products to a shopping cart, register/login, and place orders.

The project is built to explore and strengthen practical skills in **HTML, CSS, JavaScript, Python, Django, and database management**.

---

## ✨ Features

* 🌱 Browse indoor plants
* 🔍 Search and explore products
* 📋 View detailed plant information
* 🛒 Add products to cart
* ➕ Increase or decrease product quantity
* 🗑️ Remove products from cart
* 👤 User registration and login
* 📦 Checkout and order processing
* 🧾 View previous orders
* 💰 Indian Rupee (₹) pricing
* 🇮🇳 India-focused delivery details
* ⚙️ Django admin panel for managing products and orders

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Django

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 🌱 Product Category

PlantNest focuses specifically on **indoor plants**.

Example products include:

* Snake Plant
* Money Plant
* Peace Lily
* Spider Plant
* ZZ Plant
* Aloe Vera
* Jade Plant
* Areca Palm
* Rubber Plant
* Lucky Bamboo

---

## 🗄️ Database

The application uses SQLite during development.

The main data entities include:

* **Users** – managed using Django Authentication
* **Products** – plant details, pricing, stock, and other information
* **Orders** – customer order and delivery information
* **Order Items** – products and quantities included in each order

---

## 📂 Project Structure

```text
PlantNest/
│
├── manage.py
│
├── plantnest/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── products.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── checkout.html
│   ├── login.html
│   ├── register.html
│   └── orders.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd PlantNest
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open the local development server in your browser.

---

## 🛒 Application Flow

```text
Home
  ↓
Browse Plants
  ↓
View Product Details
  ↓
Add to Cart
  ↓
Login / Register
  ↓
Checkout
  ↓
Place Order
  ↓
Order Confirmation
  ↓
My Orders
```

---

## 💰 India-Focused Shopping

PlantNest is designed specifically for customers in India.

The project uses:

* ₹ INR pricing
* Indian delivery addresses
* Indian PIN codes
* India-focused delivery charges
* Cash on Delivery / UPI payment selection

> Payment processing is currently designed as part of the project workflow and does not represent a live payment gateway.

---

## 🎯 Project Goals

The main goal of PlantNest is to gain practical experience in:

* Building responsive web interfaces
* Working with JavaScript interactions
* Understanding Django's MVT architecture
* Creating and managing database models
* Implementing user authentication
* Managing shopping cart functionality
* Processing orders
* Connecting frontend templates with a Django backend
* Using Git and GitHub for version control

---

## 🔮 Future Improvements

Possible future additions include:

* 💳 Online payment gateway integration
* 📧 Order confirmation emails
* ⭐ Product reviews and ratings
* ❤️ Wishlist functionality
* 📍 Order tracking
* 🔎 Advanced product filtering
* 📱 Improved mobile experience

---

## 📌 Project Status

**🚧 Currently in development**

PlantNest is being developed as a learning project to build practical full-stack web development skills using Django.

---

## 👩‍💻 Author

**Akshatha K**

B.E. Computer Science & Engineering Student

* GitHub: [Akshatha-K2006](https://github.com/Akshatha-K2006)
* LinkedIn: [Akshatha K](https://www.linkedin.com/in/akshatha-k-488961334/)

---

## 📄 License

This project is created for educational and learning purposes.


