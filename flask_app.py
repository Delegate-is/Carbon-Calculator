from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Placeholder emission factors (tonnes CO2 per unit)
EMISSION_FACTORS = {
    'electricity': 0.45,
    'gas': 2.1,
    'flights': 0.2,
    'car': 0.14,
    'bus_rail': 0.05,
    'secondary': 1.5,  # Arbitrary value for shopping, entertainment, etc.
    'average_country': 2.0,  # Average tonnes CO2 per capita
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/house', methods=['GET', 'POST'])
def house():
    if request.method == 'POST':
        electricity = float(request.form.get('electricity', 0))
        gas = float(request.form.get('gas', 0))
        house_emissions = (electricity * EMISSION_FACTORS['electricity']) + (gas * EMISSION_FACTORS['gas'])
        return redirect(url_for('results', house_emissions=house_emissions))
    return render_template('house.html')

@app.route('/flights', methods=['GET', 'POST'])
def flights():
    if request.method == 'POST':
        flights = int(request.form.get('flights', 0))
        flight_emissions = flights * EMISSION_FACTORS['flights']
        return redirect(url_for('results', flight_emissions=flight_emissions))
    return render_template('flights.html')

@app.route('/car', methods=['GET', 'POST'])
def car():
    if request.method == 'POST':
        distance = float(request.form.get('distance', 0))
        car_emissions = distance * EMISSION_FACTORS['car']
        return redirect(url_for('results', car_emissions=car_emissions))
    return render_template('car.html')

@app.route('/bus_rail', methods=['GET', 'POST'])
def bus_rail():
    if request.method == 'POST':
        distance = float(request.form.get('distance', 0))
        bus_rail_emissions = distance * EMISSION_FACTORS['bus_rail']
        return redirect(url_for('results', bus_rail_emissions=bus_rail_emissions))
    return render_template('bus_rail.html')

@app.route('/secondary', methods=['GET', 'POST'])
def secondary():
    if request.method == 'POST':
        expense = float(request.form.get('expense', 0))
        secondary_emissions = expense * EMISSION_FACTORS['secondary']
        return redirect(url_for('results', secondary_emissions=secondary_emissions))
    return render_template('secondary.html')

@app.route('/results')
def results():
    house_emissions = float(request.args.get('house_emissions', 0))
    flight_emissions = float(request.args.get('flight_emissions', 0))
    car_emissions = float(request.args.get('car_emissions', 0))
    bus_rail_emissions = float(request.args.get('bus_rail_emissions', 0))
    secondary_emissions = float(request.args.get('secondary_emissions', 0))

    total_emissions = house_emissions + flight_emissions + car_emissions + bus_rail_emissions + secondary_emissions

    return render_template('results.html', total_emissions=total_emissions,
                           house_emissions=house_emissions,
                           flight_emissions=flight_emissions,
                           car_emissions=car_emissions,
                           bus_rail_emissions=bus_rail_emissions,
                           secondary_emissions=secondary_emissions,
                           average_country=EMISSION_FACTORS['average_country'])

if __name__ == '__main__':
    app.run(debug=True)
