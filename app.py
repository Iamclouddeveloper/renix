from flask import Flask, render_template,send_file,flash,request,jsonify,session,redirect,url_for
from flask_mail import Mail, Message
import os
import random
from dotenv import load_dotenv




app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

load_dotenv()

app.config['MAIL_SERVER'] = 'smtppro.zoho.eu'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about.html')

@app.route('/recruitment-services')
def recruitment_services():
    return render_template('recruitment_services.html')

@app.route('/engineering-services')
def engineering_services():
    return render_template('engineering_services.html')

@app.route('/pay-n-park-parnking-services')
def parking_services():
    return render_template('parking_services.html')

@app.route('/information-technology')
def it_services():
    return render_template('it_services.html')


@app.route('/blogs')
def blogs():
    return render_template('blog.html')


@app.route('/auto-connect')
def blog_auto_connect():
    return render_template('blog_auto_connect.html')

@app.route('/rasp-version')
def blog_raspversion():
    return render_template('blog_raspversion.html')

@app.route('/rail-network-and-operations')
def blog_rail_network():
    return render_template('blog_rail_network.html')

@app.route('/pay-n-park')
def blog_pay_n_park():
    return render_template('blog_pay_n_park.html')

@app.route('/railway-signalling-solution')
def blog_railway_signalling():
    return render_template('blog_railway_signalling.html')

@app.route('/parking-management')
def blog_parking_management():
    return render_template('blog_parking_management.html')

@app.route('/derby-telugu-association')
def blog_derby_telugu_association():
    return render_template('blog_DTA.html')

@app.route('/derby-hindu-temple')
def blog_derby_hindu_temple():
    return render_template('blog_DHT.html')

@app.route('/harihar-rajan')
def blog_harihar():
    return render_template('blog_harihar.html')

@app.route('/blog-flyer-pro')
def blog_flyer_pro():
    return render_template('blog_flyer_pro.html')


@app.route('/blog-ai-business')
def blog_ai_business():
    return render_template('blog_ai_business.html')


@app.route('/blog-cloud-computing')
def blog_cloud_computing():
    return render_template('blog_cloud_computing.html')

@app.route('/blog-cybersecurity')
def blog_cybersecurity():
    return render_template('blog_cybersecurity.html')

@app.route('/blog-data-analytics')
def blog_data_analytics():
    return render_template('blog_data_analytics.html')

@app.route('/blog-blockchain')
def blog_blockchain():
    return render_template('blog_blockchain.html')

@app.route('/blog-devops')
def blog_devops():
    return render_template('blog_devops.html')

@app.route('/blog-5g')
def blog_5g():
    return render_template('blog_5g.html')

@app.route('/blog-iot')
def blog_iot():
    return render_template('blog_iot.html')

@app.route('/blog-soft-skills')
def blog_soft_skills():
    return render_template('blog_soft_skills.html')

@app.route('/blog-ar-vr')
def blog_ar_vr():
    return render_template('blog_ar_vr.html')

@app.route('/blog-quantum')
def blog_quantum():
    return render_template('blog_quantum.html')

@app.route('/blog-edge-computing')
def blog_edge_computing():
    return render_template('blog_edge_computing.html')


@app.route('/terms-of-use')
def terms_of_use():
    return render_template('terms_of_use.html')

@app.route('/cookie-policy')
def cookie_policy():
    return render_template('cookie_policy.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

    

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['subject']
        user_answer = request.form.get('captcha')
        # Validate captcha
        correct_answer = session.get('captcha_answer')
        if not correct_answer or str(user_answer) != str(correct_answer):
            flash("Captcha failed. Please solve the math question correctly.", "danger")
            return redirect(url_for('contact'))

        recipients = [os.getenv('MAIL_USERNAME')]
        cc_addresses = [cc.strip() for cc in os.getenv('MAIL_CC', '').split(',') if cc.strip()]


        # Create the message
        message = Message(
            subject="New Contact Message - RENIX UK",
            recipients=recipients,
            cc=cc_addresses
        )
        message.html = render_template(
            "email_template.html",
            name=username,
            phone=phone,
            email=email,
            message=msg
        )

        try:
            mail.send(message)
            flash("Thank you for your message! We will contact you soon.", "success")
        except Exception as e:
            print("Email sending error:", e)
            flash(f"An error occurred while sending your message: {str(e)}", "danger")
            
     #  generate new math captcha
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    session['captcha_answer'] = num1 + num2
    return render_template('contact.html',num1=num1, num2=num2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)