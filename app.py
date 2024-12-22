# Import necessary libraries
from flask import Flask, render_template, request
import model 

application = Flask('__name__')

# List of valid user IDs
allowed_user_ids = ['00sab00', '1234', 'zippy', 'zburt5', 'joshua', 'dorothy w', 'rebecca', 
                    'walker557', 'samantha', 'raeanne', 'kimmie', 'cassie', 'moore222']

@application.route('/')
def home_page():
    """Render the home page."""
    return render_template('index.html')

@application.route('/get_recommendations', methods=['POST'])
def fetch_top5_recommendations():
    """Handle recommendations request."""
    print(request.method)
    input_username = request.form['User Name']
    print('Provided Username =', input_username)
    
    if input_username in allowed_user_ids and request.method == 'POST':
        top_products = recommender_model.suggest_products(input_username)
        print(top_products.head())
        top5_recommendations = recommender_model.top_rated_products(top_products)
        
        return render_template(
            'index.html', 
            column_names=top5_recommendations.columns.values, 
            row_data=list(top5_recommendations.values.tolist()), 
            zip=zip, 
            text='Recommended products'
        )
    elif input_username not in allowed_user_ids:
        return render_template('index.html', text='No recommendations found for the user')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    application.debug = False
    application.run()