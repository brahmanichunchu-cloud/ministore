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
# SESSION STATE
# -----------------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0.0

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
        "description": "Track fitness, heart rate, and notifications.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 89.99,
        "description": "Lightweight running shoes for daily workouts.",
        "category": "Fashion"
    },
    {
        "name": "Leather Backpack",
        "price": 59.99,
        "description": "Durable backpack for travel and office use.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 99.99,
        "description": "Automatic coffee maker with timer functionality.",
        "category": "Home"
    },
    {
        "name": "Desk Lamp",
        "price": 29.99,
        "description": "LED desk lamp with adjustable brightness.",
        "category": "Home"
    }
]

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    padding: 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.product-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.price {
    color: green;
    font-size: 22px;
    font-weight: bold;
}

.support-btn {
    position: fixed;
    bottom: 25px;
    right: 25px;
    z-index: 999;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🛍 Product Categories")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
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
    <h3>Your One-Stop Online Shopping Destination</h3>
    <p>Discover amazing products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# WELCOME SECTION
# -----------------------------
st.header("Welcome to MiniStore")

st.write(
    """
    Explore our collection of high-quality products across
    electronics, fashion, and home essentials.
    """
)

st.markdown("---")

# -----------------------------
# PRODUCT FILTER
# -----------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product
        for product in products
        if product["category"] == selected_category
    ]

# -----------------------------
# PRODUCT DISPLAY
# -----------------------------
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
                <p><strong>Category:</strong> {product['category']}</p>
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
            st.success(f"{product['name']} added to cart!")

# -----------------------------
# SUPPORT CHATBOT LINK
# -----------------------------
st.page_link(
    "pages/Support_Chatbot.py",
    label="💬 Open Support Chatbot",
    icon="💬"
)

# Floating Button
st.markdown("""
<div class="support-btn">
</div>
""", unsafe_allow_html=True)
import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Chatbot")

# -----------------------------
# PRODUCT KNOWLEDGE BASE
# -----------------------------
products = {
    "wireless headphones": {
        "price": "$79.99",
        "category": "Electronics"
    },
    "smart watch": {
        "price": "$149.99",
        "category": "Electronics"
    },
    "running shoes": {
        "price": "$89.99",
        "category": "Fashion"
    },
    "leather backpack": {
        "price": "$59.99",
        "category": "Fashion"
    },
    "coffee maker": {
        "price": "$99.99",
        "category": "Home"
    },
    "desk lamp": {
        "price": "$29.99",
        "category": "Home"
    }
}

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "Hello! Welcome to MiniStore Support. How can I help you today?"
        }
    ]

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# CHATBOT LOGIC
# -----------------------------
def get_response(user_input):

    query = user_input.lower()

    # Product Questions
    for name, details in products.items():

        if name in query:

            return (
                f"{name.title()} costs {details['price']} "
                f"and belongs to the {details['category']} category."
            )

    # Delivery Questions
    if "delivery" in query or "shipping" in query:
        return (
            "Standard delivery takes 3-5 business days. "
            "Express delivery takes 1-2 business days."
        )

    # Refund Questions
    if "refund" in query:
        return (
            "Refunds are processed within 5-7 business days "
            "after approval."
        )

    # Return Questions
    if "return" in query:
        return (
            "Products can be returned within 30 days of purchase."
        )

    # Payment Questions
    if (
        "payment" in query
        or "pay" in query
        or "card" in query
    ):
        return (
            "We accept UPI, Visa, Mastercard, "
            "Net Banking, and PayPal."
        )

    # Order Status
    if "order" in query and "status" in query:
        return (
            "For this demo, all orders are currently "
            "marked as Processing."
        )

    # Greetings
    if "hello" in query or "hi" in query:
        return (
            "Hello! I can help you with products, "
            "delivery, refunds, returns, payments, "
            "and order status."
        )

    return (
        "I can help with product information, delivery, "
        "refunds, returns, payment methods, and order status."
    )

# -----------------------------
# USER INPUT
# -----------------------------
prompt = st.chat_input("Ask your question here...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)