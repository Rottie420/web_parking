from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def landing_page():
  return render_template('main.html')

@app.route('/homegrown')
def homegrown_page():
  f_1 = open('contents/basics.txt', encoding='utf-8', mode='r')
  content_1 = f_1.read()
  f_1.close()

  f_2 = open('contents/legalities.txt', encoding='utf-8', mode='r')
  content_2 = f_2.read()
  f_2.close()

  return render_template('homegrown.html', 
                         content_1=content_1,
                         content_2=content_2
                        )

@app.route('/blockchain')
def blockchain_page():
  f_1 = open('contents/blockchain_1.txt', encoding='utf-8', mode='r')
  content_1 = f_1.read()
  f_1.close()

  f_2 = open('contents/blockchain_2.txt', encoding='utf-8', mode='r')
  content_2 = f_2.read()
  f_2.close()

  f_3 = open('contents/blockchain_3.txt', encoding='utf-8', mode='r')
  content_3 = f_3.read()
  f_3.close()

  f_4 = open('contents/blockchain_4.txt', encoding='utf-8', mode='r')
  content_4 = f_4.read()
  f_4.close()

  
  return render_template('blockchain.html', 
                         content_1=content_1,
                         content_2=content_2,
                         content_3=content_3,
                         content_4=content_4
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
