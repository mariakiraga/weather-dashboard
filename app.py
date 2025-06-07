import os
import config
import requests
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24) # Ustaw losowy klucz sesji dla flash messages

OPENWEATHER_API_KEY = config.API_KEY
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = request.form.get('city') if request.method == 'POST' else 'Kraków' # Domyślne miasto

    if city:
        params = {
            'q': city,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric', # Jednostki metryczne (Celsjusz)
            'lang': 'pl'       # Język polski
        }
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status() # Wyrzuć wyjątek dla statusów 4xx/5xx

            data = response.json()

            if data.get('cod') == 200: # Sprawdź, czy kod odpowiedzi to 200 (OK)
                weather_data = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'description': data['weather'][0]['description'].capitalize(),
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed']
                }
            else:
                flash(f"Nie znaleziono danych pogodowych dla miasta: {city}. Sprawdź pisownię.", 'error')
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                flash(f"Miasto '{city}' nie zostało znalezione.", 'error')
            else:
                flash(f"Błąd HTTP podczas pobierania danych: {e}", 'error')
        except requests.exceptions.ConnectionError:
            flash("Błąd połączenia: Sprawdź swoje połączenie internetowe lub spróbuj ponownie później.", 'error')
        except requests.exceptions.Timeout:
            flash("Upłynął limit czasu połączenia z serwerem OpenWeatherMap.", 'error')
        except requests.exceptions.RequestException as e:
            flash(f"Wystąpił nieznany błąd podczas zapytania do API: {e}", 'error')
        except Exception as e:
            flash(f"Wystąpił nieoczekiwany błąd: {e}", 'error')

    return render_template('index.html', weather=weather_data, current_city=city)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='19999') # host='0.0.0.0' pozwala na dostęp z zewnątrz
