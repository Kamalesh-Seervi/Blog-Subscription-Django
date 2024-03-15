# My Django Project

Welcome to my Django project! This project is a Blog Subscription App

## Installation

1. Clone the repository:

```
git clone https://github.com/Kamalesh-Seervi/Blog-Subscription-Django
```

2. Navigate into the project directory:

```
cd subplatform
```

3. Create virtual environment and activate it

```
python3 -m venv venv   
```

4. Activate the virtual environment:
- On Unix/macOS:
```
  source venv/bin/activate
```

5. Install dependencies:
```
pip install -r requirements.txt
```


6. Apply database migrations:
```
python manage.py migrate
```

## Usage

1. Create a superuser:
```
python3 manage.py createsuperuser
```


2. Run the development server:
```
python3 manage.py runserver
```

3. Access the admin interface:
- Visit `http://127.0.0.1:8000/admin/`
- Log in with the superuser credentials created in step 1.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Create a new Pull Request

## Credits

- Created by [Kamalesh-Seervi](https://github.com/Kamalesh-Seervi)
- Inspired by Medium Blog

