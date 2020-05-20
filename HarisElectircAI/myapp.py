from flask import Flask, render_template,request, jsonify,send_file, redirect,session
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import warnings
warnings.filterwarnings("ignore",category=UserWarning)
app = Flask(__name__)


class Plots:
    def __init__(self):
        pass

    #-----------------------------------------------------------------
    #Pairwise Plot display on main page
    def exploratoryanalysis(self):
        df = pd.read_csv('dublin-city-residential-energy-in-each-small-area.csv')
        df.dropna(inplace=True)
        plt.figure(figsize=(10,8), dpi= 80)
        sns.set(style="ticks", color_codes=True)
        sns.pairplot(df, vars = ['Estimated Energy Use (kWh)', 'Estimated Cost of Energy', 'Total Floor Area'])
        #sns.pairplot(df, kind="reg", hue="AreaCode")
        plt.savefig('static/exploratory.png')
        plt.close('all')
   
    #-----------------------------------------------------------------
    #mid night Plot display
    def midnight(self):
        dataset = pd.read_csv('midNightAanalysis.csv')
        dataset.drop('zero', axis=1, inplace=True)
        plt.title('Appliances Usage', fontsize = 16)
        plt.xlabel('Total Usage' , fontsize = 16)
        plt.ylabel('Mid Night / Day Light')
        dataset.mean().plot(kind='bar')
        plt.savefig('static/midnight.png')
        plt.close('all')
       

    #-----------------------------------------------------------------    
    #Function for regression analysis
    def genrateplotforGeneralConsumption(self):
        #The specification for the size of the image
        plt.rcParams['figure.figsize'] = (20.0, 10.0)
        # Reading Data from the csv file
        data = pd.read_csv('dublin-city-residential-energy-in-each-small-area.csv')
        #The x and y coordinates of the plot
        X = data['Estimated Energy Use (kWh)'].values
        Y = data['Total Floor Area'].values
        # Here i will extracting the mean value
        meanX = np.mean(X)
        meanY = np.mean(Y)
        # count the number of values
        m = len(X)
        # formula for calculate numerator or denominator
        numer = 0
        denom = 0
        #a for loop for numerator or denomen
        for i in range(m):
            numer += (X[i] - meanX) * (Y[i] - meanY)
            denom += (X[i] - meanX) ** 2
            b1 = numer / denom
            b0 = meanY - (b1 * meanX)

        #coefficients
        maxX = np.max(X) + 100
        minX = np.min(X) - 100

        # Calculating line values x and y
        x = np.linspace(minX, maxX, 1000)
        y = b0 + b1 * x
        #The floor are plot line
        plt.plot(x, y, color='#FF0000', label='Regression Line')
        # Ploting Scatter Points
        plt.scatter(X, Y, c='#FF0000', label='Scatter Plot')
        plt.xlabel('Estimated Energy Use (kWh)')
        plt.ylabel('Total Floor Area')
        plt.savefig('static/scatter.png')
        plt.close('all')

    #-----------------------------------------------------------------    
    #Function for appliances analysis
    def appliancesAnalysis(self):
        dataset = pd.read_csv('YourAppliancesAnalysis.csv')
        dataset.drop('zero', axis=1, inplace=True)
        plt.title('Appliances Usage')
        plt.xlabel('Estimated Energy Use (kWh)' ,fontsize = 16)
        plt.ylabel('Category of Appliances' ,fontsize = 16)
        dataset.mean().plot(kind='bar')
        plt.savefig('static/apliances.png')
        plt.close('all')
       
    #-----------------------------------------------------------------
    #Time Series Analysis
    def timeSeriesAnalysisplot(self):
        plt.style.use('fivethirtyeight')
        # Above is a special style template for matplotlib, highly useful for visualizing time series data
        from pylab import rcParams
        rcParams['figure.figsize'] = 20, 10
        df = pd.read_csv('timeSeriesIrelandCon.csv')
        df.columns=['Year', 'Electric power consumption']
        df=df.dropna()
        df['Year'] = pd.to_datetime(df['Year'])
        df.set_index('Year', inplace=True) #set date as index
        #df.head()
        plt.xlabel("Year")
        plt.ylabel("Electric power consumption")
        plt.title("Consumption graph")
        plt.plot(df)
        df.plot(style='k.')
        plt.savefig('static/ts.png')
        plt.close('all')

   
    #-----------------------------------------------------------------------------
    #Utility function for plot generate
    def yourconsumption(self):
        #df = pd.read_csv('')
        df = pd.read_csv('yourAreaAanalysis.csv')
        df.drop('zero', axis=1, inplace=True)
        df.plot()  # plots all columns against index
        df.plot(kind='scatter',x='AreaSize',y='Consumption') # scatter plot
        df.plot(kind='density')  # estimate density function
        plt.title("Floor Area and Monthly Usage", fontsize = 24)
        plt.xlabel('Floor Area',fontsize = 16)
        plt.ylabel("Monthly Usage", fontsize = 16)
        plt.savefig('static/yourdailyconsumption.png')
        plt.close('all')


#-----------------------------------------------------------------------------
#Source Code for start the application Display the Welcome Page
@app.route('/', methods=['GET'])
def MainApplicaion():
    sessiondata()
    return render_template('MainApplicaion.html')

#------------------------------------------------------------------------
#Function to redirect to time analysis page
def sessiondata():
    #update the dataset
        dfupdate = pd.read_csv('yourAreaAanalysis.csv')
        #Update the global variables
        session['AreaSize']=dfupdate["AreaSize"].mean()
        session['Consumption']=dfupdate["Consumption"].mean()
        #update the dataset
        dfupdate = pd.read_csv('YourAppliancesAnalysis.csv')
        #Update the global variables
        session['Coffeemaker']=dfupdate["Coffeemaker"].mean()
        session['Blender']=dfupdate["Blender"].mean()
        session['Microwave']=dfupdate["Microwave"].mean()
        session['Toaster']=dfupdate["Toaster"].mean()
        session['Washing']=dfupdate["Washing"].mean()
        session['Iron']=dfupdate["Iron"].mean()
        session['Dishwasher']=dfupdate["Dishwasher"].mean()
        session['Electricboiler']=dfupdate["Electricboiler"].mean()
        session['Dryer']=dfupdate["Dryer"].mean()
        session['TV']=dfupdate["TV"].mean()
        session['Computer']=dfupdate["Computer"].mean()
        session['Heater']=dfupdate["Heater"].mean()
        session['AC']=dfupdate["AC"].mean()
       
        #update the dataset
        dfupdate = pd.read_csv('midNightAanalysis.csv')
        #Update the global variables
        session['MidNight']=dfupdate["midnight"].mean()
        session['DayConsumtion']=dfupdate["day"].mean()
   
#------------------------------------------------------------------------
#Function to redirect to time analysis page
@app.route('/timeSeriesAnalysis', methods=['GET'])
def timeSeriesAnalysis():
    return render_template('timeSeriesAnalysis.html')

#------------------------------------------------------------------------
#Function to redirect to Public Data Analysis
@app.route('/publicDataAnalysis', methods=['GET'])
def publicDataAnalysis():
    return render_template('publicDataAnalysis.html')


#------------------------------------------------------
#Function for saviing the daily consumption
@app.route('/YourOwnConsumption', methods=['GET', 'POST'])
def YourOwnConsumption():
    #if user submit the form for saving the data
    if request.method == 'POST':
        areasize = request.form['areasize']
        totalconsumtion = request.form['totalconsumtion']
        data = [[areasize,totalconsumtion]]
        #Assign the values to local dataset
        df = pd.DataFrame(data)
        #Saving the data set to csv file
        df.to_csv('yourAreaAanalysis.csv',mode='a',header=0)
        #Redirect to another page
        return redirect('/')
    return render_template('YourOwnConsumption.html')

#--------------------------------------------------------------
#Function for saviing the diffrent appliances electric usage
@app.route('/YourAppliances',methods=['GET', 'POST'])
def YourAppliances():
     #if user submit the form for saving the data
     if request.method == 'POST':
        Coffeemaker = request.form['Coffeemaker']
        Blender = request.form['Blender']
        Microwave = request.form['Microwave']
        Toaster=request.form['Toaster']
        Washing=request.form['Washing']
        Iron = request.form['Iron']
        Dishwasher = request.form['Dishwasher']
        Electricboiler = request.form['Electricboiler']
        Dryer=request.form['Dryer']
        TV=request.form['TV']
        Computer=request.form['Computer']
        Heater=request.form['Heater']
        AC=request.form['AC']
        #Assign the values to local dataset
        data = [[Coffeemaker, Blender, Microwave,Toaster,Washing,Iron,Dishwasher,Electricboiler,Dryer,TV,Computer,Heater,AC]]
        df = pd.DataFrame(data)
        #Saving the data set to csv file
        df.to_csv('YourAppliancesAnalysis.csv',mode='a',header=0)
        #Redirect to another page
        return redirect('/')
     return render_template('YourAppliances.html')
   
#----------------------------------------------------------------
#Function for saviing the mid night and day usage
@app.route('/EnergySaving', methods=['GET', 'POST'])
def EnergySaving():
    #if user submit the form for saving the data
    if request.method == 'POST':
        midnight = request.form['midnight']
        day = request.form['day']
        data = [[midnight,day]]
        #Assign the values to local dataset
        df = pd.DataFrame(data)
        #Saving the data set to csv file
        df.to_csv('midNightAanalysis.csv',mode='a',header=0)
        #Redirect to another page
        return redirect('/')
    return render_template('EnergySaving.html')

#----------------------------------------------------------------
#Function to check your status
@app.route('/CheckYourStatus', methods=['GET', 'POST'])
def CheckYourStatus():
    #if user submit the form for saving the data
    if request.method == 'POST':
        sessiondata()
        return render_template('CheckYourStatus.html')
    return render_template('CheckYourStatus.html')
       
#------------------------------------------------------------------
#Main function to start the application
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
    myplt =Plots()
    #Create image for appliances
    myplt.appliancesAnalysis()
    #genrate the consumption
    myplt.timeSeriesAnalysisplot()
    myplt.yourconsumption()
    #Create Main Page images scatter Plot
    myplt.genrateplotforGeneralConsumption()
    #Create Main Page image detail plot
    myplt.exploratoryanalysis()
    #Create the mid night plot
    myplt.midnight()
