from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name":"Jeans - Classic Denim", "price":"100/=", "img":"https://images.unsplash.com/photo-1542272604-787c3835535d", "cat":"Jeans"},
    {"name":"Jeans - Slim Fit", "price":"200/=", "img":"https://images.unsplash.com/photo-1541099649105-f69ad21f3246", "cat":"Jeans"},
    {"name":"T-shirt - Black", "price":"300/=", "img":"https://images.unsplash.com/photo-1583743814966-8936f5b7be1a", "cat":"T-shirts"},
    {"name":"T-shirt - Grey", "price":"350/=", "img":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab", "cat":"T-shirts"},
    {"name":"Ankle Socks - 3 pack", "price":"200/=", "img":"https://images.unsplash.com/photo-1586350977771-b3b0abd50c82", "cat":"Ankle socks"},
    {"name":"Ankle Socks - White", "price":"100/=", "img":"https://images.unsplash.com/photo-1584302052179-2e90841dad6a", "cat":"Ankle socks"},
    {"name":"Hoodie - Black", "price":"750/=", "img":"https://images.unsplash.com/photo-1556821840-3a63f95609a7", "cat":"Hoodie"},
    {"name":"Hoodie - Grey", "price":"600/=", "img":"https://images.unsplash.com/photo-1578768079052-aa76e52ff62e", "cat":"Hoodie"},
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run()
