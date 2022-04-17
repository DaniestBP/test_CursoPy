from io import BytesIO
from flask import Flask, session, request, render_template, redirect, url_for,flash,send_file
from uuid import uuid4
from functools import wraps
import secrets
from models import *



"https://www.google.com/maps/place/Bernardo+Lima+48/@38.7401615,-9.1575212,15z"

types_list = ["Solicitors", "Restaurants-Bars", "Hotels", "Veterinary", "Hairdressing","Groceries", "Nurseries", "Agencies", "Others"]

@app.route("/")
def home():
    advert_all = Advert.query.all()
    u_current= session.get("id")
    u_table = User.query.get(u_current)

    if u_table:
        user = u_table.id
        return render_template("home.html", text ="Welcome to MyGuide", types_list=types_list, advert_all=advert_all, user=user)
    return render_template("home.html", text ="Welcome to MyGuide", types_list=types_list, advert_all=advert_all)
        


@app.route("/business_filter_by", methods=["GET"])
def filter():
    type_requested = request.args.get("type")
    u_current= session.get("id")
    u_table = User.query.get(u_current)
    advert_by_type= Advert.query.filter_by(business_type=type_requested).all()
    list_byType= [advert for advert in advert_by_type]
    if list_byType:
        if u_table:
            user = u_table.id
            for adv in list_byType:
                imgs = adv.images
            return render_template("listings_by_type.html", ad_by_type=advert_by_type, user=user, imgs=imgs)
        return render_template("listings_by_type.html", ad_by_type=advert_by_type)
    else:
        flash("No listings of the type selected available yet")
        return redirect(url_for("home"))
    
    
@app.route("/advert/<advert_id>")
def show_listing(advert_id):
    ad_show=Advert.query.get(advert_id)
    d_lon= 0.000334
    d_lat= 0.002245
    lon = float(ad_show.longitude)
    lat = float(ad_show.latitude)
    u_current= session.get("id")
    u_table = User.query.get(u_current)

    if u_table:
        user = u_table.id
        if ad_show.images:
            imgs = ad_show.images
            return render_template ("listing.html", ad=ad_show, lat=lat, lon=lon, d_lon=d_lon, d_lat=d_lat, user=user,imgs=imgs)
    if ad_show.images:
        imgs = ad_show.images
        return render_template ("listing.html", ad=ad_show, lat=lat, lon=lon, d_lon=d_lon, d_lat=d_lat, imgs=imgs)
    
    return render_template ("listing.html", ad=ad_show, lat=lat, lon=lon, d_lon=d_lon, d_lat=d_lat)
    


@app.route("/signup", methods = ["GET", "POST"])
def registration():
    verb = request.method
    if verb == "POST":
        email_u = request.form.get("email")
        name_u = request.form.get("name")
        pwd_u = request.form.get("pwd") # Pending encrypt
        
        try:
            if email_u and pwd_u:
                u_id = uuid4().hex
                token_new = secrets.token_hex(16)
                user_new = User(id=u_id, name=name_u, email = email_u, pwd = pwd_u, token = token_new)
                db.session.add(user_new)
                db.session.commit()
                res = redirect(url_for("login"))
                res.status_code = 307
                return res
        except:
            flash(f"This email {email_u} was already stored in our database")
            return render_template("signup.html")
    return render_template("signup.html", text = "Sign up")
 

def authorize(f):
    @wraps(f)
    def i():
        cookie_id = session.get("id")
        cookie_token = session.get("token")
        if cookie_id and cookie_token:
            cookie_conf = User.query.filter_by(token=cookie_token).first()

            if cookie_conf.token == cookie_token:
                return f()
        return redirect(url_for("login"))
    return i 

@app.route("/auth")
@authorize
def auth():
    cookie_token = session.get("token")
    u = User.query.filter_by(token=cookie_token).first()
    user = u.id
    print(user)
    return redirect(url_for("dashboard" ,  user= user))


@app.route("/login", methods=["GET", "POST"])
def login():
    verb = request.method
    if verb == "POST":
        email_u = request.form.get("email")
        pwd_u = request.form.get("pwd")
        result = User.query.filter_by(email=email_u).first()
        try:
            if result.pwd == pwd_u:
                new_token = secrets.token_hex(16)
                session["token"] = new_token
                session["id"] = result.id
                result.token = session["token"]
                db.session.add(result)
                db.session.commit()
                return redirect(url_for("auth"))
            else:
                flash("Password incorrect")
        except AttributeError:
            flash("Email address incorrect")
            return render_template("login.html", text = "Log in")
    return render_template("login.html", text = "Log in")


@app.route("/us_dashb/<user>", methods=["GET", "POST"])
def dashboard(user):
    user = User.query.get(user)
    if user:
        try:
            u_adverts = Advert.query.filter_by(user_id=user.id).all()
            if u_adverts:
                adverts = [ad for ad in u_adverts]
            else:
                adverts = []
        except IndexError:
            return render_template("u_dashboard.html", text= f"{(user.name)} dashboard")
    return render_template("u_dashboard.html", text= f"{(user.name)} dashboard", us_adverts=adverts)
            

Allowed_exten=["png", "jpg", "jpeg", "gif"]

def allowed_file(filename):
    return filename.split(".")[1].lower() in Allowed_exten

@app.route("/create_adv", methods= ["GET", "POST"])
def create_ad():
    verb = request.method
    u_token = session.get("token")
    u = User.query.filter_by(token=u_token).first()
    u_id = u.id
    
    if verb == "POST":
        name= request.form.get("adv_name")
        address_ad = request.form.get("address")
        phone_ad = request.form.get("contact_phone")
        email_ad = request.form.get("contact_email")
        lat = request.form.get("latitude")
        lon = request.form.get("longitude")
        type = request.form.get("business_type")
        if type in types_list:
            advert = Advert(id=uuid4().hex, user_id=u_id, adv_name=name,  address= address_ad, latitude=lat, longitude=lon, contact_phone=phone_ad, contact_email=email_ad, business_type=type)
            print(advert)
            db.session.add(advert)
            db.session.commit()
            res = redirect(url_for("dashboard", user=u_id))
            # res.status_code = 307
            return res
    return render_template("ad_creation.html", user=u_id, text=f"{u.name}, build it up!", ad="")
        

@app.route("/edit_spc/<adv_id>", methods= ["GET", "POST"])
def edit_space(adv_id):
    print(adv_id)
    # advert = Advert.query.filter_by(id=adv_id).first()
    ad = Advert.query.get(adv_id)
    ad_name = ad.adv_name
    
    if request.method == "POST":
        descript = request.form["adver_description"]
        if descript:
            ad.description = descript
            db.session.add(ad)        
        file = request.files["image"]
        if file and allowed_file(file.filename):
            image = Upload(id=uuid4().hex, advert_id = adv_id, filename=file.filename, data=file.read())
            db.session.add(image)
        db.session.commit()
        imgs = Advert.query.get(adv_id).images

        # flash(f"Uploaded {file.filename}, {ad.text_des}")
        return render_template("advert_final.html", adv_id=adv_id, imgs=imgs, adv_descr=ad.description, ad=ad)
    
    return render_template("customize.html", text=f"Customize '{ad_name}' space", ad=ad)


@app.route("/advert_view/<img_id>")
def img_advert(img_id):
    advert_img = Upload.query.filter_by(id=img_id).first() #ahora solo tenemos una imagen y por ello pasamos al "send_file" directamente el advert_imgs pero cuando haya mas de una imagen para cada anuncio habra que hacer un loop 
    return send_file(BytesIO(advert_img.data), attachment_filename=advert_img.filename, as_attachment=False, mimetype="image/jpg")

    # return render_template("advert_final.html", img=img, advert_imgs=advert_imgs)



@app.route("/remove")
def remove_from():
    
    adv_id = request.args.get("adv_id")
    ad_to_rem =Advert.query.get(adv_id)
    if ad_to_rem:
        flash("Your space is being removed")
        db.session.delete(ad_to_rem)
        db.session.commit()
        return redirect(url_for("dashboard", user=ad_to_rem.user_id))
    else: 
        flash("An error occurred")
    return redirect(url_for("dashboard", user=ad_to_rem.user_id))


@app.route("/unsubs", methods=["GET", "POST"])
def unsubs():
    if request.method == "POST":
        user_email = request.form.get("email")

        u_to_rem =User.query.filter_by(email =user_email).first()
        if u_to_rem:
            flash("User deleted")
            db.session.delete(u_to_rem)
            db.session.commit()
            return redirect(url_for("home"))
        else: 
            flash("An error occurred")
    return render_template("unsubscribe.html", text="Unsubscribe")



@app.route("/update", methods=["GET", "POST"])
def update_object():
    # ob_up = Advert.query.filter_by(adv_name="Bar Joselito").update(dict(business_type="Restaurants-Bars"))
    adv_id = request.args.get("adv_id")
    ad_to_up =Advert.query.get(adv_id)
    if request.method == "POST":
        new_info = request.form.to_dict()
        if new_info:
            for k,v in new_info.items():
                if v:
                    setattr(ad_to_up, k, v)   #The setattr() function sets the value of the specified attribute of the specified object.
            db.session.commit()
            flash("Space updated with success")
            return redirect(url_for("dashboard", user=ad_to_up.user_id))
        else:
            new_values = [data for data in new_info.values()]
            old_values = [ad_to_up.id, ad_to_up.adv_name, ad_to_up.address,ad_to_up.latitude, ad_to_up.longitude, ad_to_up.contact_phone, ad_to_up.contact_email,ad_to_up.business_type]
            for value in new_values:
                if value in old_values:
                    True
            flash("No updates received")
            return redirect(url_for("dashboard", user=ad_to_up.user_id))
    return render_template("ad_creation.html", ad=ad_to_up)


@app.route("/logout")
def logout():
    session.pop("id", None)
    session.pop("token", None)
    flash("You were logged out. See you soon!")
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)