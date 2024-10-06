from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion Functions
def voltage(current, resistance):
    return current * resistance

def current(voltage, resistance):
    return voltage / resistance

def resistance(voltage, current):
    return voltage / current

def power(voltage, current):
    return voltage * current

def capacitance(charge, voltage):
    return charge / voltage

def inductance(voltage, di_dt):
    return voltage / (di_dt * 0.001)  # di/dt is in mA/s

def charge(current, time):
    return current * time

def frequency(time_period):
    return 1 / time_period

def energy(power, time):
    return power * time

def impedance(resistance, reactance):
    return (resistance ** 2 + reactance ** 2) ** 0.5

def conductance(resistance):
    return 1 / resistance

def magnetic_flux(magnetic_field, area):
    return magnetic_field * area

# Home route for index page
@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

# Unit Converter route
@app.route('/unit_converter', methods=['GET', 'POST'])
def unit_converter():
    """Render the unit converter page."""
    result = None
    if request.method == 'POST':
        conversion_type = request.form.get('conversion_type')
        input1 = float(request.form.get('input1', 0))
        input2 = float(request.form.get('input2', 0))
        input3 = request.form.get('input3')  # Optional third input for some calculations

        # Print statements for debugging
        print(f"Conversion Type: {conversion_type}, Input1: {input1}, Input2: {input2}, Input3: {input3}")

        try:
            if conversion_type == "voltage":
                result = voltage(input1, input2)  # Current and Resistance
            elif conversion_type == "current":
                result = current(input1, input2)  # Voltage and Resistance
            elif conversion_type == "resistance":
                result = resistance(input1, input2)  # Voltage and Current
            elif conversion_type == "power":
                result = power(input1, input2)  # Voltage and Current
            elif conversion_type == "capacitance":
                result = capacitance(input1, input2)  # Charge and Voltage
            elif conversion_type == "inductance":
                result = inductance(input1, input2)  # Voltage and di/dt
            elif conversion_type == "charge":
                result = charge(input1, input2)  # Current and Time
            elif conversion_type == "frequency":
                result = frequency(input1)  # Time Period
            elif conversion_type == "energy":
                result = energy(input1, input2)  # Power and Time
            elif conversion_type == "impedance":
                result = impedance(input1, input2)  # Resistance and Reactance
            elif conversion_type == "conductance":
                result = conductance(input1)  # Resistance
            elif conversion_type == "magnetic_flux":
                result = magnetic_flux(input1, input2)  # Magnetic Field and Area
            else:
                result = "Invalid conversion type"
        except Exception as e:
            result = str(e)

    return render_template('unit.html', result=result)

# Number System Converter route
@app.route('/number_converter', methods=['GET'])
def number_converter():
    """Render the number system converter page."""
    return render_template('number.html')

# Resistor Color Code route
@app.route('/resistor_color_code')
def resistor_color_code():
    """Render the resistor color code calculator page."""
    return render_template('resistor_color.html')

if __name__ == '__main__':
    app.run(debug=True)
