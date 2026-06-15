import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------
# PRODUCT DATA
# -----------------------------
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

# -----------------------------
# SESSION STATE
# -----------------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0.0

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.hero{
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    padding:40px;
    border-radius:15px;
    color:white;
    text-align:center;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.price{
    color:green;
    font-size:20px;
    font-weight:bold;
}

.support-btn{
    position:fixed;
    bottom:20px;
    right:20px;
    z-index:999;
}

.support-btn a{
    background:#4f46e5;
    color:white;
    text-decoration:none;
    padding:15px 20px;
    border-radius:50px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🛍 Categories")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.radio(
    "Browse Products",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")
st.sidebar.write(f"Items: {st.session_state.cart_count}")
st.sidebar.write(f"Total: ${st.session_state.cart_total:.2f}")

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="hero">
<h1>🛒 MiniStore</h1>
<h3>Your One-Stop Shopping Destination</h3>
<p>Discover amazing products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

st.header("Featured Products")

# -----------------------------
# FILTER PRODUCTS
# -----------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# -----------------------------
# PRODUCT GRID
# -----------------------------
cols = st.columns(3)

for i, product in enumerate(filtered_products):

    with cols[i % 3]:

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
            st.success("Added to cart")

# -----------------------------
# SUPPORT CHATBOT NAVIGATION
# -----------------------------
st.page_link(
    "pages/Support_Chatbot.py",
    label="💬 Open Support Chatbot"
)

# Floating Button
st.markdown("""
<div class="support-btn">
<a href="/Support_Chatbot" target="_self">
💬 Support
</a>
</div>
""", unsafe_allow_html=True)
import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Chatbot")

products = {
    "wireless headphones": "$79.99",
    "smart watch": "$149.99",
    "running shoes": "$89.99",
    "leather backpack": "$59.99",
    "coffee maker": "$99.99",
    "desk lamp": "$29.99"
}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def chatbot_response(user_input):

    text = user_input.lower()

    for product, price in products.items():
        if product in text:
            return f"{product.title()} costs {price}."

    if "delivery" in text or "shipping" in text:
        return "Standard delivery takes 3-5 business days."

    if "refund" in text:
        return "Refunds are processed within 5-7 business days."

    if "return" in text:
        return "Products can be returned within 30 days."

    if "payment" in text or "pay" in text:
        return "We accept UPI, Visa, Mastercard and PayPal."

    if "order" in text and "status" in text:
        return "Demo orders are currently marked as Processing."

    return "I can help with products, delivery, refunds, returns, payments and order status."

prompt = st.chat_input("Ask a question...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = chatbot_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)