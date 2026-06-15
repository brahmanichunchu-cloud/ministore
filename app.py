import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0.0

# -------------------------------------------------
# PRODUCTS
# -------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 79.99,
        "description": "Premium noise-cancelling headphones with 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 149.99,
        "description": "Track fitness, heart rate and notifications.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 89.99,
        "description": "Lightweight shoes for running and workouts.",
        "category": "Fashion"
    },
    {
        "name": "Leather Backpack",
        "price": 59.99,
        "description": "Stylish backpack for travel and office use.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 99.99,
        "description": "Automatic coffee maker with programmable timer.",
        "category": "Home"
    },
    {
        "name": "Desk Lamp",
        "price": 29.99,
        "description": "LED lamp with adjustable brightness.",
        "category": "Home"
    }
]

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    padding: 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.product-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.price {
    color: green;
    font-size: 22px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("🛍 Categories")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.radio(
    "Browse Products",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")

st.sidebar.write(
    f"Items: {st.session_state.cart_count}"
)

st.sidebar.write(
    f"Total: ${st.session_state.cart_total:.2f}"
)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛒 MiniStore</h1>
    <h3>Your One-Stop Online Shopping Destination</h3>
    <p>Discover amazing products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# WELCOME
# -------------------------------------------------
st.header("Welcome to MiniStore")

st.write("""
Explore our collection of electronics,
fashion and home products.
""")

# -------------------------------------------------
# FILTER PRODUCTS
# -------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product
        for product in products
        if product["category"] == selected_category
    ]

# -------------------------------------------------
# PRODUCTS
# -------------------------------------------------
st.subheader("⭐ Featured Products")

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(
            f"""
            <div class="product-card">
                <h3>{product['name']}</h3>
                <p class="price">${product['price']}</p>
                <p>{product['description']}</p>
                <p><b>Category:</b> {product['category']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart_count += 1
            st.session_state.cart_total += product["price"]
            st.success(
                f"{product['name']} added to cart!"
            )

# -------------------------------------------------
# SUPPORT BUTTON
# -------------------------------------------------
st.markdown("---")

if st.button("💬 Open Support Chatbot"):
    st.switch_page("pages/Support_Chatbot.py")