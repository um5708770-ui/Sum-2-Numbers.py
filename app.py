from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

PRODUCTS = [
    {
        "id": 1,
        "name": "Wireless Noise-Cancelling Headphones",
        "description": "Experience pure sound with active noise cancellation and 30-hour battery life.",
        "price": 299.99,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80"
    },
    {
        "id": 2,
        "name": "Smart Watch Series 8",
        "description": "Track your fitness, monitor your health, and stay connected on the go.",
        "price": 399.00,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&q=80"
    },
    {
        "id": 3,
        "name": "Professional DSLR Camera",
        "description": "Capture stunning moments with this 24.2 MP camera and 4K video recording.",
        "price": 899.50,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&q=80"
    },
    {
        "id": 4,
        "name": "Ultra-Slim Laptop",
        "description": "Lightweight, powerful, and ready for anything with an M2 chip and 16GB RAM.",
        "price": 1299.99,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&q=80"
    },
    {
        "id": 5,
        "name": "Mechanical Gaming Keyboard",
        "description": "RGB backlit mechanical keyboard with tactile switches for the ultimate gaming experience.",
        "price": 129.99,
        "image": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&q=80"
    },
    {
        "id": 6,
        "name": "Ergonomic Office Chair",
        "description": "Designed for comfort during long work hours with adjustable lumbar support.",
        "price": 249.99,
        "image": "https://images.unsplash.com/photo-1505843490538-5133c6c7d0e1?w=500&q=80"
    },
    {
        "id": 7,
        "name": "4K Ultra HD Smart TV",
        "description": "Immerse yourself in cinematic visuals with HDR10+ and built-in streaming apps.",
        "price": 699.00,
        "image": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&q=80"
    },
    {
        "id": 8,
        "name": "Portable Bluetooth Speaker",
        "description": "Waterproof design with 360-degree sound, perfect for outdoor adventures.",
        "price": 89.99,
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&q=80"
    },
    {
        "id": 9,
        "name": "Smartphone Pro Max",
        "description": "The ultimate smartphone with a pro camera system and all-day battery.",
        "price": 1099.00,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&q=80"
    },
    {
        "id": 10,
        "name": "Wireless Charging Pad",
        "description": "Fast charge your devices simultaneously with this sleek charging pad.",
        "price": 49.99,
        "image": "https://images.unsplash.com/photo-1586816879360-004f5b0c51e3?w=500&q=80"
    }
]

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.json
    a = data.get("a", 0)
    b = data.get("b", 0)
    result = a + b
    return jsonify({"sum": result})

@app.get("/")
def home():
    return render_template('index.html', products=PRODUCTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
