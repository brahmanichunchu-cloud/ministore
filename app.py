import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>

.hero{
    background: linear-gradient(135deg,#4f46e5,#7c3aed);
    color:white;
    padding:40px;
    border-radius:15px;
    text-align:center;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.price{
    color:green;
    font-size:20px;
    font-weight:bold;
}

.category{
    background:#eef2ff;
    color:#4338ca;
    padding:5px 10px;
    border-radius:8px;
    display:inline-block;
}

.support-button{
    position:fixed;
    bottom:25px;
    right:25px;
    z-index:9999;
}

.support-button button{
    background:#4f46e5;
    color:white;
    border:none;
    border-radius:50px;
    padding:15px 20px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------
products = [
    {
        "name":"Wireless Headphones",
        "price":79.99,
        "description":"Premium noise cancelling headphones.",
        "category":"Electronics"
    },
    {
        "name":"Smart Watch",
        "price":149.99,
        "description":"Track fitness and notifications.",
        "category":"Electronics"
    },
    {
        "name":"Running Shoes",
        "price":89.99,
        "description":"Lightweight performance shoes.",
        "category":"Fashion"
    },
    {
        "name":"Leather Backpack",
        "price":59.99,
        "description":"Stylish and durable backpack.",
        "category":"Fashion"
    },
    {
        "name":"Coffee Maker",
        "price":99.99,
        "description":"Automatic coffee brewing system.",
        "category":"Home"
    },
    {
        "name":"Desk Lamp",
        "price":29.99,
        "description":"LED lamp with brightness control.",
        "category":"Home"
    }
]

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
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

st.sidebar.write(
    f"Items: {st.session_state.cart_count}"
)

st.sidebar.write(
    f"Total: ${st.session_state.cart_total:.2f}"
)

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.markdown("""
<div class="hero">
<h1>🛒 MiniStore</h1>
<h3>Your One-Stop Online Shopping Destination</h3>
<p>Discover premium products at unbeatable prices.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.header("Welcome to MiniStore")

st.write("""
Explore electronics, fashion and home products
carefully selected for quality and value.
""")

# --------------------------------------------------
# FILTER PRODUCTS
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------
st.subheader("⭐ Featured Products")

cols = st.columns(3)

for idx, product in enumerate(filtered_products):

    with cols[idx % 3]:

        st.markdown(
            f"""
            <div class="product-card">
            <h3>{product['name']}</h3>
            <p class="price">${product['price']}</p>
            <p>{product['description']}</p>
            <span class="category">
            {product['category']}
            </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"Add {product['name']}",
            key=product["name"]
        ):
            st.session_state.cart_count += 1
            st.session_state.cart_total += product["price"]
            st.success("Added to cart")

# --------------------------------------------------
# FLOATING SUPPORT BUTTON
# --------------------------------------------------
st.markdown("""
<div class="support-button">
<a href="/Support_Chatbot" target="_self">
<button>💬 Support</button>
</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 MiniStore")import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Assistant")

# --------------------------------------------------
# PRODUCT KNOWLEDGE
# --------------------------------------------------
products = {
    "wireless headphones": "$79.99",
    "smart watch": "$149.99",
    "running shoes": "$89.99",
    "leather backpack": "$59.99",
    "coffee maker": "$99.99",
    "desk lamp": "$29.99"
}

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"Hello! Welcome to MiniStore Support. How can I help you today?"
        }
    ]

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --------------------------------------------------
# RULE BASED CHATBOT
# --------------------------------------------------
def chatbot_response(user_input):

    text = user_input.lower()

    # Product Questions
    for product, price in products.items():
        if product in text:
            return f"{product.title()} is available for {price}."

    # Delivery
    if "delivery" in text or "shipping" in text:
        return (
            "Standard delivery takes 3-7 business days."
        )

    # Refunds
    if "refund" in text:
        return (
            "Refunds are processed within 5-7 business days."
        )

    # Returns
    if "return" in text:
        return (
            "Products can be returned within 30 days of purchase."
        )

    # Payments
    if "payment" in text or "pay" in text:
        return (
            "We accept Visa, Mastercard, UPI, Net Banking and PayPal."
        )

    # Order Status
    if "order" in text and "status" in text:
        return (
            "For demo purposes, all orders are marked as 'Processing'."
        )

    # Greeting
    if "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"

    return (
        "I can help with products, delivery, refunds, returns, payments and order status."
    )

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
prompt = st.chat_input("Ask a question...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = chatbot_response(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)