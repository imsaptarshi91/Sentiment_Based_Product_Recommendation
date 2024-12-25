#from cgitb import text
import nltk 
print("NLTK Version:", nltk.__version__)
# Download NLTK corpora before starting the app
nltk.download('punkt')  # Replace with the corpora you need, e.g., 'stopwords', 'wordnet'
nltk.download('punkt_tab') # This line is added to download the missing resource.

from flask import Flask,render_template,request
import model 
app = Flask('__name__')

valid_userid = ['00sab00','1234','zippy','zburt5','joshua','dorothy','rebecca','walker557','samantha','raeanne','kimmie','cassie','moore222']
@app.route('/')
def view():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend_top5():
    print(request.method)
    user_name = request.form['User Name']
    print('User name=',user_name)
    
    if  user_name in valid_userid and request.method == 'POST':
            top20_products = model.suggest_products(user_name)
            print(top20_products.head())
            get_top5 = model.top_rated_products(top20_products)
            #return render_template('index.html',tables=[get_top5.to_html(classes='data',header=False,index=False)],text='Recommended products')
            return render_template('index.html',column_names=get_top5.columns.values, row_data=list(get_top5.values.tolist()), zip=zip,text='Recommended products')
    elif not user_name in  valid_userid:
        return render_template('index.html',text='No Recommendation found for the user')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.debug=False

    app.run()