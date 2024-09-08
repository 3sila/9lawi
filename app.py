import os
import math
import datetime
from flask import Flask, render_template, redirect, request, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'adverts'

ADS_PER_PAGE = 12

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
        if connection.is_connected():
            print("Connected to MySQL")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
@app.route('/home')
def home():
    if not total_view():
        return "Database connection failed", 500

    connection = get_mysql_connection()
    if connection is None:
        return "Database connection failed", 500

    cursor = connection.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM county")
        counties = cursor.fetchall()

        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()

        cursor.execute("SELECT * FROM total_view")
        views = cursor.fetchall()

        cursor.execute("SELECT * FROM advert ORDER BY views DESC LIMIT 4")
        top_ads = cursor.fetchall()

        cursor.execute("SELECT * FROM advert ORDER BY id DESC LIMIT 4")
        recent_adverts = cursor.fetchall()
    except Error as e:
        print(f"Error fetching data: {e}")
        return "Error fetching data", 500
    finally:
        cursor.close()
        connection.close()

    return render_template('home.html',
                           counties=counties,
                           categories=categories,
                           tittle="Home",
                           views=views,
                           top_ads=top_ads,
                           recent_adverts=recent_adverts)

def total_view():
    connection = get_mysql_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE total_view SET views = views + 1 WHERE id = %s", (1,))
        connection.commit()
    except Error as e:
        print(f"Error updating total views: {e}")
        return False
    finally:
        cursor.close()
        connection.close()
    return True

@app.route('/marketplace')
def marketplace():
    connection = get_mysql_connection()
    if connection is None:
        return "Database connection failed", 500

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM county")
        counties = cursor.fetchall()

        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()

        page_number = int(request.args.get('page', 1))
        ads_to_skip = (page_number - 1) * ADS_PER_PAGE

        cursor.execute("SELECT COUNT(*) FROM advert")
        ads_count = cursor.fetchone()['COUNT(*)']
        page_count = math.ceil(ads_count / ADS_PER_PAGE)
        page_numbers = range(1, page_count + 1)

        cursor.execute("SELECT * FROM advert ORDER BY views DESC LIMIT %s OFFSET %s", 
                       (ADS_PER_PAGE, ads_to_skip))
        ads_on_page = cursor.fetchall()
    except Error as e:
        print(f"Error fetching data: {e}")
        return "Error fetching data", 500
    finally:
        cursor.close()
        connection.close()

    return render_template('marketplace.html',
                           counties=counties,
                           categories=categories,
                           tittle="Marketplace",
                           adverts=ads_on_page,
                           ads=ads_on_page,
                           page=page_number,
                           pages=page_numbers,
                           total=page_count)

@app.route('/motors_and_vehicles')
def motors_and_vehicles():
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM county")
    counties = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    page_number = int(request.args.get('page', 1))
    ads_to_skip = (page_number - 1) * ADS_PER_PAGE

    cursor.execute("SELECT COUNT(*) FROM advert WHERE category_name = 'Motors and vehicles'")
    ads_count = cursor.fetchone()['COUNT(*)']
    page_count = math.ceil(ads_count / ADS_PER_PAGE)
    page_numbers = range(1, page_count + 1)

    cursor.execute("SELECT * FROM advert WHERE category_name = 'Motors and vehicles' ORDER BY views DESC LIMIT %s OFFSET %s", 
                   (ADS_PER_PAGE, ads_to_skip))
    ads_on_page = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('marketplace.html',
                           counties=counties,
                           categories=categories,
                           subtittle="Marketplace",
                           tittle="Motors and vehicles",
                           adverts=ads_on_page,
                           ads=ads_on_page,
                           page=page_number,
                           pages=page_numbers,
                           total=page_count)

@app.route('/home_garden_diy')
def home_garden_diy():
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM county")
    counties = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    page_number = int(request.args.get('page', 1))
    ads_to_skip = (page_number - 1) * ADS_PER_PAGE

    cursor.execute("SELECT COUNT(*) FROM advert WHERE category_name = 'Home, garden and DIY'")
    ads_count = cursor.fetchone()['COUNT(*)']
    page_count = math.ceil(ads_count / ADS_PER_PAGE)
    page_numbers = range(1, page_count + 1)

    cursor.execute("SELECT * FROM advert WHERE category_name = 'Home, garden and DIY' ORDER BY views DESC LIMIT %s OFFSET %s", 
                   (ADS_PER_PAGE, ads_to_skip))
    ads_on_page = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('marketplace.html',
                           counties=counties,
                           categories=categories,
                           subtittle="Marketplace",
                           tittle="Home, garden and DIY",
                           adverts=ads_on_page,
                           ads=ads_on_page,
                           page=page_number,
                           pages=page_numbers,
                           total=page_count)

@app.route('/electronics')
def electronics():
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM county")
    counties = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    page_number = int(request.args.get('page', 1))
    ads_to_skip = (page_number - 1) * ADS_PER_PAGE

    cursor.execute("SELECT COUNT(*) FROM advert WHERE category_name = 'Electronics, mobile and PC'")
    ads_count = cursor.fetchone()['COUNT(*)']
    page_count = math.ceil(ads_count / ADS_PER_PAGE)
    page_numbers = range(1, page_count + 1)

    cursor.execute("SELECT * FROM advert WHERE category_name = 'Electronics, mobile and PC' ORDER BY views DESC LIMIT %s OFFSET %s", 
                   (ADS_PER_PAGE, ads_to_skip))
    ads_on_page = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('marketplace.html',
                           counties=counties,
                           categories=categories,
                           subtittle="Marketplace",
                           tittle="Electronics, mobile and PC",
                           adverts=ads_on_page,
                           ads=ads_on_page,
                           page=page_number,
                           pages=page_numbers,
                           total=page_count)

@app.route('/search', methods=['GET', 'POST'])
def search():
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM county")
    counties = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    query = request.args.get('search')
    county = request.args.get('county')

    if not county:
        cursor.execute("SELECT * FROM advert WHERE advert_description LIKE %s", ('%' + query + '%',))
    elif not query:
        cursor.execute("SELECT * FROM advert WHERE location = %s", (county,))
    else:
        cursor.execute("SELECT * FROM advert WHERE advert_description LIKE %s AND location = %s", ('%' + query + '%', county))
    
    results = cursor.fetchall()
    results_number = len(results)

    cursor.close()
    connection.close()

    return render_template('search.html',
                           query=query,
                           counties=counties,
                           categories=categories,
                           results=results,
                           results_number=results_number)


@app.route('/view_advert/<advert_id>')
def view_advert(advert_id):
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM county")
    counties = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM advert WHERE id = %s", (advert_id,))
    advert = cursor.fetchone()

    view_count(advert_id)

    cursor.close()
    connection.close()

    return render_template('view_advert.html',
                           counties=counties,
                           categories=categories,
                           tittle="Advert info",
                           advert=advert)

def view_count(advert_id):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE advert SET views = views + 1 WHERE id = %s", (advert_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return True

@app.route('/add_advert')
def add_advert():
    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Fetch categories from the database
    cursor.execute("SELECT name FROM categories")
    categories = cursor.fetchall()

    cursor.close()
    connection.close()

    # Pass categories to the template
    return render_template('add_advert.html', categories=categories)




@app.route('/insert_advert', methods=['POST'])
def insert_advert():
    connection = get_mysql_connection()
    cursor = connection.cursor()

    # Check if "uploads" directory exists, if not create it
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    advert_image = None
    if "advert_image" in request.files:
        advert_image = request.files['advert_image']
        file_path = os.path.join(upload_folder, advert_image.filename)
        advert_image.save(file_path)

    currentDT = datetime.datetime.now()

    cursor.execute("""
        INSERT INTO advert (category_name, advert_name, advert_description, price, contact_info, location, image, date_posted)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        request.form.get('category_name'),
        request.form.get('advert_name'),
        request.form.get('advert_description'),
        request.form.get('price'),
        request.form.get('contact_info'),
        request.form.get('location'),
        advert_image.filename if advert_image else None,
        currentDT
    ))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('home'))

@app.route('/file/<path:filename>')
def file(filename):
    return send_from_directory('your_upload_directory', filename)

@app.route('/county_search', methods=['POST'])
def county_search():
    connection = get_mysql_connection()
    if connection is None:
        return "Database connection failed", 500

    cursor = connection.cursor(dictionary=True)

    try:
        # Fetch counties and categories for form select options
        cursor.execute("SELECT * FROM county")
        counties = cursor.fetchall()

        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()

        # Get the county from the form submission
        county_id = request.form.get('county')

        # Perform a search query based on the selected county
        cursor.execute("SELECT * FROM advert WHERE county_id = %s", (county_id,))
        results = cursor.fetchall()
        results_number = len(results)

    except Error as e:
        print(f"Error fetching data: {e}")
        return "Error fetching data", 500
    finally:
        cursor.close()
        connection.close()

    # Render a template with the search results
    return render_template('search_results.html',
                           counties=counties,
                           categories=categories,
                           results=results,
                           results_number=results_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
