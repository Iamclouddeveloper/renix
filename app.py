from flask import Flask, render_template,send_file,flash,request,jsonify,session,redirect,url_for,Response
from flask_mail import Mail, Message
from PIL import Image, ImageDraw, ImageFont
import os
import io, random
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv('SECRET_KEY')




app.config['MAIL_SERVER'] = 'smtppro.zoho.eu'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)


@app.route('/',  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('subject')
        user_answer = request.form.get('captcha')
        
        if not username or not email or not msg:
            flash("Please fill in all required fields.", "danger")
            return redirect(url_for('home'))
        
        # Validate captcha
        correct_answer = session.get('captcha_answer')
        if not correct_answer or str(user_answer) != str(correct_answer):
            flash("Captcha failed. Please solve the math question correctly.", "danger")
           
            return redirect(url_for('home'))

        recipients = [os.getenv('MAIL_USERNAME')]
        cc_addresses = [cc.strip() for cc in os.getenv('MAIL_CC', '').split(',') if cc.strip()]

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
        
        # ----------to User ----------
        auto_reply = Message(
            subject="Thank you for contacting RENIX (UK)",
            recipients=[email]
        )

        auto_reply.html = render_template(
            "auto_reply.html",
            name=username
        )

        try:
            mail.send(message)
            mail.send(auto_reply)
            flash("Thank you for your message! We will contact you soon.", "success")
        except Exception as e:
            print("Email sending error:", e)
            flash(f"An error occurred while sending your message: {str(e)}", "danger")

        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about.html')

@app.route('/business-support-services')
def business_support_services():
    return render_template('business_support.html')


@app.route('/iot-embedded-systems')
def iot_embedded_systems():
    return render_template('iot_embedded.html')


@app.route('/pay-n-park-parnking-services')
def parking_services():
    return render_template('parking_services.html')

@app.route('/information-technology')
def it_services():
    return render_template('it_services.html')


@app.route('/blogs')
def blogs():
    return render_template('blog.html')




@app.route('/rail-network-and-operations')
def blog_rail_network():
    return render_template('blog_rail_network.html')

@app.route('/pay-n-park')
def blog_pay_n_park():
    return render_template('blog_pay_n_park.html')

@app.route('/blog-community')
def blog_community():
    return render_template('blog_community.html')

@app.route('/blog-flyer-pro')
def blog_flyer_pro():
    return render_template('blog_flyer_pro.html')

@app.route('/tamannas-restaurant')
def tamannas_restaurant():
    return render_template('tamannas_restaurant.html')



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

    


@app.route('/captcha_image')
def captcha_image():
    # Generate random numbers
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    captcha_text = f"{num1} + {num2} = ?"

    # Store the answer in session
    session['captcha_answer'] = num1 + num2

    # Create image (black background)
    img = Image.new('RGB', (180, 60), color='black')
    draw = ImageDraw.Draw(img)

    # Load font (fall back if missing  (DejaVuSans-Bold.ttf) , arial.ttf)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 32)
    except:
        font = ImageFont.load_default()

    # Draw captcha text (white)
    draw.text((20, 10), captcha_text, fill="white", font=font)

    # Add random noise dots
    for _ in range(200):
        x = random.randint(0, img.width - 1)
        y = random.randint(0, img.height - 1)
        draw.point((x, y), fill="white")

    # Add random noise lines
    for _ in range(6):
        x1 = random.randint(0, img.width)
        y1 = random.randint(0, img.height)
        x2 = random.randint(0, img.width)
        y2 = random.randint(0, img.height)
        draw.line((x1, y1, x2, y2), fill="white", width=1)

    # Save image to memory
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return Response(buf, mimetype='image/png')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)