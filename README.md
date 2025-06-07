# Weather Dashboard

This is a simple Flask-based web application that displays current weather information for a specified city using the OpenWeatherMap API.

---

## Features

* **Current Weather:** Get real-time weather data including temperature, "feels like" temperature, description, humidity, and wind speed.
* **City Search:** Easily search for weather in any city worldwide.
* **User-Friendly Interface:** Clean and intuitive design.
* **Error Handling:** Provides informative messages for various issues like city not found, API errors, or network problems.

---

## Setup and Installation

Follow these steps to get your Weather Dashboard up and running.

### Prerequisites

* Python 3.7+
* An API key from [OpenWeatherMap](https://openweathermap.org/api)

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Create a `config.py` file

```python
API_KEY = 'your_openweathermap_api_key_here'
```

Replace `'your_openweathermap_api_key_here'` with your actual API key obtained from OpenWeatherMap.

### 3. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:19999` by default.

---

## Running with Docker
You can also run this application using Docker. A Docker image is available on GitHub Container Registry.

### 1. Pull the Docker Image

```bash
docker pull ghcr.io/mariakiraga/weather-dashboard:latest
```

### 2. Run the Docker Container

```bash
docker run -d -p 19999:19999 --restart unless-stopped ghcr.io/mariakiraga/weather-dashboard:latest
```

This command will:
- `-d`: Run the container in detached mode (in the background).
- `-p 19999:19999`: Map port `19999` of your host to port `19999` inside the container.
- `--restart unless-stopped`: Configure the container to restart automatically unless it is explicitly stopped.
After running the command, the application will be available at `http://localhost:19999`.

---

## Technologies used
- Flask: Web framework for Python.
- Requests: HTTP library for making API calls.
- OpenWeatherMap API: Provides weather data.
