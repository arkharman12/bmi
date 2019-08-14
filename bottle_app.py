from bottle import default_app, route, template, post, request

@route('/')
def showForm():
    return template ("index.html")              #returning the form that's in index.html file

@post('/bmi')
def showResponse():
    weight = request.forms.get("Wei")           #requesting all three forms
    weight = int(weight)                        #converting user input into an integer
    feet = request.forms.get("Ft")
    feet = int(feet)
    inches = request.forms.get("In")
    inches = int(inches)
    height = int((feet * 12) + inches)
    bmi = (weight / (height)**2) * 703          #bmi formula
    floatbmi = ("{:.1f}").format(bmi)           #rounding to 1 decimal place

    if bmi < 18.5:
        status = "underweight"

    elif bmi >= 18.5 and bmi <= 24.9:
        status = "normal"

    elif bmi > 25 and bmi <= 29.9:
        status = "overweight"

    else:
        status = "obese"

    return template("bmi.html", name = floatbmi, name1 = status)            #returning the name and name 1 variables for later use in html

application = default_app()


