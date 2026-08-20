from flask import Flask, render_template, request
import os
from database import create_table, save_contact, get_contacts


# ==========================================================
# APPLICATION CONFIGURATION
# ==========================================================

app = Flask(__name__)

create_table()


app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "development-secret-key"
)



# ==========================================================
# ROUTES
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")



# ==========================================================
# PROJECT DETAIL ROUTES
# ==========================================================


@app.route("/projects/marbleerp")
def marbleerp():

    return render_template(
        "projects/marbleerp.html"
    )



@app.route("/projects/retail-analytics")
def retail_analytics():

    return render_template(
        "projects/retail.html"
    )



@app.route("/projects/data-platform")
def data_platform():

    return render_template(
        "projects/analytics.html"
    )






# ==========================================================
# ABOUT PAGE ROUTE
# ==========================================================


@app.route("/about")
def about():

    return render_template(
        "about.html"
    )





# ==========================================================
# SERVICES ROUTES
# ==========================================================


@app.route("/services/erp")
def service_erp():

    return render_template(
        "services/erp.html"
    )




@app.route("/services/data-analytics")
def service_data_analytics():

    return render_template(
        "services/data_analytics.html"
    )




@app.route("/services/automation")
def service_automation():

    return render_template(
        "services/automation.html"
    )



# ==========================================================
# CONTACT FORM
# ==========================================================


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")

    email = request.form.get("email")

    message = request.form.get("message")


    print("New Contact Message")
    print("-------------------")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)


    save_contact(
        name,
        email,
        message
    )


    return render_template(
        "contact_success.html"
    )





@app.route("/admin/contacts")
def admin_contacts():


    contacts = get_contacts()


    return render_template(
        "admin_contacts.html",
        contacts=contacts
    )



# ==========================================================
# APPLICATION START
# ==========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )