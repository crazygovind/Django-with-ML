from django.shortcuts import render

# our home page view
def home(request):
    return render(request, 'index.html')

#custom method for generating predictions
def getPredictions(Year,Present_Price,Kms_Driven,Fuel_Type,Transmission,Owner):
    import pickle
    model = pickle.load(open("C:\Python_Projects\car_price\car_price_predictor\car_price_predictor\car_price_predictor_model.pkl", "rb"))
    prediction = model.predict([[Year,Present_Price,Kms_Driven,Fuel_Type,Transmission,Owner]])
    #print(prediction)
    return prediction

# our result page view
def result(request):
    if request.method == 'POST':
        Year = int(request.POST['Year'])
        Present_Price = float(request.POST['Present_Price'])
        Kms_Driven = int(request.POST['Kms_Driven'])
        Fuel_Type = int(request.POST['Fuel_Type'])
        Transmission = int(request.POST['Transmission'])
        Owner = int(request.POST['Owner'])
        
        result = getPredictions(Year,Present_Price,Kms_Driven,Fuel_Type,Transmission,Owner)
        
        
        return render(request, 'result.html', {'result':result})
    else:
        return render(request, 'index.html')
    
