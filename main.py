from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def landing_page():
  return render_template('main.html')

@app.route('/homegrown')
def homegrown_page():
  f = open('contents/basics.txt', "r")
  content_1 = f.read()
  f.close()

  f = open('contents/legalities.txt', "r")
  content_2 = f.read()
  f.close()
  
  return render_template('homegrown.html', 
                         content_1=content_1,
                         content_2=content_2
                        )

@app.route('/aboutus')
def aboutus_page():
  return render_template('aboutus.html')
  
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

@app.route('/img_1.png')
def sitemap_img():
    return send_from_directory(app.static_folder, 'img_1.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
