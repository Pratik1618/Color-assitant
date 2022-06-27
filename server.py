from name import red, pink, orange, yellow, purple, green, blue, brown
import combine
import colors_from_image
import palettes_import
from fileinput import filename
from flask import Flask, redirect, render_template, request, url_for
import os
from werkzeug.utils import secure_filename
import convert

UPLOAD_FOLDER = '/home/jayesh/Desktop/new'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# data = [['#534340', '#BB9981', '#C5D8A4', '#F4FCD9'], ['#874356', '#C65D7B', '#F68989', '#F6E7D8'], ['#B7CADB', '#FDF6EC', '#F3E9DD', '#DAB88B'], ['#FDFFA9', '#FFD365', '#00C897', '#019267'], ['#E6D5B8', '#E45826', '#F0A500', '#1B1A17'], ['#E8FFC2', '#00FFDD', '#2FA4FF', '#0E185F'], ['#826F66', '#C69B7B', '#F7CCAC', '#3A3845'], ['#F4BBBB', '#F1E1A6', '#C3E5AE', '#97DBAE'], ['#F5F5F5', '#E2D784', '#05595B', '#062C30'], ['#1A132F', '#5B7DB1', '#61A4BC', '#F7E2E2'], ['#D9CE3F', '#E83A14', '#890F0D', '#630606'], ['#E5EFC1', '#A2D5AB', '#39AEA9', '#557B83'], ['#FFDDEE', '#FFBDE6', '#F473B9', '#0E3EDA'], ['#EEEEEE', '#ECA6A6', '#D18CE0', '#E2DEA9'], ['#F2FA5A', '#5EE6EB', '#56BBF1', '#4D77FF'], ['#F582A7', '#F10086', '#711A75', '#180A0A'], ['#4D96FF', '#6BCB77', '#FFD93D', '#FF6B6B'], ['#6EDCD9', '#E15FED', '#9254C8', '#332FD0'], ['#243D25', '#5F7464', '#E4AEC5', '#FAD9E6'], ['#A63EC5', '#CE49BF', '#F190B7', '#FBD6D2'], ['#EEEEEE', '#EBD671', '#85C88A', '#6FB2D2'], ['#D49B54', '#C74B50', '#712B75', '#46244C'], ['#C0EDA6', '#FFF7BC', '#FF8080', '#FD5D5D'], ['#A97155', '#BE8C63', '#E4D1B9', '#8FBDD3'], ['#F56D91', '#F7F5F2', '#DFDFDE', '#8D8DAA'], ['#FFA8A8', '#FDD7AA', '#F6FFA4', '#B6FFCE'], ['#EAEA7F', '#FDAF75', '#F24A72', '#333C83'], ['#FFF8D5', '#B4ECE3', '#8479E1', '#733C3C'], ['#FAFFAF', '#95D1CC', '#5584AC', '#22577E'], ['#FFD124', '#00AFC1', '#0093AB', '#006778']]


# from convert import conv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def get_home():
    return render_template("colorpallete2.html")


@app.route("/combine", methods=["POST", "GET"])
def get_combine():
    if request.method == "POST":
        number_palettes = request.form.get("number_palettes")
        scheme = request.form.get("scheme")
        number_colors = request.form.get("number_colors")
        # print(f"number_palettes = {number_palettes} - scheme = {scheme}")
        return render_template("combine_page.html", combinations=combine.get_combinations(scheme, number_palettes, number_colors))

    else:
        return render_template("combine_page.html")


@app.route("/convert", methods=["GET", "POST"])
def get_convert():
    if request.method == "POST":
        r = request.form.get("r")
        g = request.form.get("g")
        b = request.form.get("b")
        # hexvalue = rgb_to_hex(int(r),int(b),int(g))
        a = int(r)
        b = int(g)
        c = int(b)
        return render_template("convert_page.html", Hex = convert.rgb_to_hex(a, b, c))
    else:
        return render_template("convert_page.html")



@app.route("/palette/month")
def get_palette_month():
    return render_template("palette_page_month.html", data=palettes_import.month_data_list)


@app.route("/palette/year")
def get_palette_year():
    return render_template("palette_page_year.html", data=palettes_import.year_data_list)


@app.route("/palette/all-time")
def get_palette_all_time():
    return render_template("palette_page_all_time.html", data=palettes_import.all_time_data_list)


@app.route("/colorname")
def get_name():
    # passing the red varible from name.py to name_page.html
    return render_template("name_page.html", colorsRed=red, colorsPink=pink, colorsOrange=orange, colorsYellow=yellow, colorsPurple=purple, colorsGreen=green, colorsBlue=blue, colorsBrown=brown)


@app.route('/uploadLabel', methods=["GET", 'POST'])
def uploadLabel():
    if request.method == "POST":
        isthisFile = request.files.get('file')
        fileName = isthisFile.filename
        # print(isthisFile)
        print(isthisFile.filename)
        global_filename = str(filename)
        isthisFile.save(os.path.join(
            app.config['UPLOAD_FOLDER'], isthisFile.filename))
        # print(global_filename)
        return render_template("colorpallete2.html", data=colors_from_image.getColors(str(fileName)))
    else:
        return render_template("colorpallete2.html")


if __name__ == "__main__":
    app.run(debug=True)
