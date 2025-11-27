import streamlit as st

st.set_page_config(page_title="ArtGallery", layout="wide")
st.markdown("""
<style>
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

st.session_state.setdefault("page", "home")
st.session_state.setdefault("user", None)
st.session_state.setdefault("user_role", None)
st.session_state.setdefault("cart", [])

_query = st.query_params
if "page" in _query:
    st.session_state.page = _query["page"]

def goto(page):
    st.session_state.page = page
    st.query_params = {"page": page}
    st.rerun()

# --- CSS ---
def load_css():
    st.markdown("""
    <style>
    :root{
        --bg:#000000; 
        --surface:#111111; 
        --text:#ffffff;
        --muted:#bbbbbb; 
        --border:#333333;
    }
    *{box-sizing:border-box}
    body{
        font-family:Inter,system-ui;
        background:var(--bg) !important;
        color:var(--text);
        margin:0;
    }

    /* NAV */
    .nav{width:100%;border-bottom:1px solid var(--border);background:var(--surface);padding:16px 0;}
    .nav-inner{display:flex;justify-content:space-between;align-items:center;}
    .container{max-width:1000px;margin:0 auto;padding:0 20px;}

    /* HERO */
    .bw-hero{text-align:center;padding:40px 0}
    .bw-hero h1{font-size:32px;margin-bottom:8px;color:var(--text);}
    .sub{color:var(--muted)}

    /* GALLERY */
    .gallery-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px;margin-top:24px}
    .card{background:var(--surface);border:1px solid var(--border);padding:16px;border-radius:12px}
    .thumb{width:100%;height:180px;background:#222;border-radius:10px}
    .muted{color:var(--muted);font-size:14px}

    /* AUTH CARD */
    .auth-card{
        width:100%;max-width:380px;background:var(--surface);
        padding:32px;border-radius:20px;
        box-shadow:0 8px 30px rgba(0,0,0,0.3);
        text-align:center;margin:40px auto;
        color:var(--text);
    }
    .auth-card .icon{font-size:44px;margin-bottom:10px}
    .auth-card h2{font-size:22px;margin:0;font-weight:600;color:var(--text);}
    .auth-card p.sub{font-size:14px;margin-top:6px;color:var(--muted)}

    .radio-group{margin:8px 0 20px;text-align:left;color:var(--text);}
    .radio-group label{display:flex;gap:8px;margin-bottom:6px}
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
def navbar():
    st.markdown("""
    <style>
        .nav-wrapper {
            width: 100%;
            padding: 16px 0;
            background: #111;
            border-bottom: 1px solid #333;
        }
        .nav-inner {
            max-width: 1000px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        .nav-group {
            display:flex;
            gap:12px;
        }
        .nav-btn {
            background:#222;
            border:1px solid #444;
            color:white;
            padding:8px 14px;
            border-radius:8px;
            font-size:14px;
        }
        .nav-btn:hover { background:#333; }
    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([0.7, 0.3])

    with left:
        st.markdown("<h3 style='color:white;'>ArtGallery</h3>", unsafe_allow_html=True)

    with right:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Home", key="nav_home"):
                goto("home")

        with col2:
            if st.session_state.user:
                if st.button("Profile", key="nav_profile"):
                    goto("profile")
            else:
                if st.button("Log In", key="nav_login"):
                    goto("login")

        with col3:
            if st.button("Cart", key="nav_cart"):
                goto("cart")

        with col4:
            if st.session_state.user:
                if st.button("Logout", key="nav_logout"):
                    st.session_state.user = None
                    goto("home")

# --- HOME ---
def home_page():
    load_css()
    navbar()

    st.markdown("""
    <section class="bw-hero">
        <h1>Discover Exceptional Artworks</h1>
        <p class="sub">Curated minimal gallery — black & white aesthetic.</p>
    </section>
    """, unsafe_allow_html=True)

    artworks = [
        ("Jazz Blue", 3200),
        ("Retro Dreams", 2100),
        ("Modern Abstraction", 4500),
    ]

    st.markdown('<section class="gallery-grid">', unsafe_allow_html=True)

    for name, price in artworks:
        st.markdown(f"""
        <div class="card">
            <div class="thumb"></div>
            <h3>{name}</h3>
            <p class="muted">Painting • ${price}</p>
            <button class="btn-outline">{name}</button>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Add {name}"):
            st.session_state.cart.append({"name": name, "price": price})
            st.success(f"{name} added to cart!")

    st.markdown("</section>", unsafe_allow_html=True)

# --- LOGIN ---
def login_page():
    load_css()
    navbar()

    card = st.container()

    with card:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)

        st.markdown("""
            <div class="icon">👤</div>
            <h2>Welcome Back</h2>
            <p class="sub">Log in to continue</p>
        """, unsafe_allow_html=True)

        email = st.text_input("Email", placeholder="Email")
        password = st.text_input("Password", type="password", placeholder="Password")

        if st.button("Log In", use_container_width=True):
            st.session_state.user = email
            st.session_state.user_role = "buyer"
            goto("home")

        if st.button("Go to Sign Up"):
            goto("signup")

        st.markdown("</div>", unsafe_allow_html=True)

# --- SIGNUP ---
def signup_page():
    load_css()
    navbar()

    card = st.container()

    with card:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)

        st.markdown("""
            <div class="icon">✨</div>
            <h2>Create Account</h2>
            <p class="sub">Join ArtGallery</p>
        """, unsafe_allow_html=True)

        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        role = st.radio("Choose your role:", ["Buyer", "Artist"])

        if st.button("Sign Up", use_container_width=True):
            st.session_state.user = name
            st.session_state.user_role = role.lower()
            goto("home")

        if st.button("Go to Log In"):
            goto("login")

        st.markdown("</div>", unsafe_allow_html=True)

# --- CART ---
def cart_page():
    load_css()
    navbar()

    st.header("Your Cart")

    if len(st.session_state.cart) == 0:
        st.info("Your cart is empty.")
        return

    total = sum(item["price"] for item in st.session_state.cart)

    for item in st.session_state.cart:
        st.write(f"🖼 **{item['name']}** — ${item['price']}")

    st.write("---")
    st.subheader(f"Total: ${total}")

    st.button("Back to Home", on_click=lambda: goto("home"))

# --- PROFILE ---
def profile_page():
    load_css()
    navbar()

    if st.session_state.user is None:
        st.warning("You are not logged in.")
        if st.button("Go to Login"):
            goto("login")
        return

    st.header("My Profile")

    st.text_input("Name", value=st.session_state.user)
    st.text_input("Email", value=f"{st.session_state.user}@example.com")
    st.text_input("Role", value=st.session_state.user_role)
    st.text_input("Member Since", value="2024")

    if st.button("Logout"):
        st.session_state.user = None
        goto("home")

# --- ROUTER ---
page = st.session_state.page

if page == "home":
    home_page()
elif page == "login":
    login_page()
elif page == "signup":
    signup_page()
elif page == "cart":
    cart_page()
elif page == "profile":
    profile_page()