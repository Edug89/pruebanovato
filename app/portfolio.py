from flask import (
    Blueprint, render_template,
)
import sendgrid
from sendgrid.helpers.mail import *


bp = Blueprint("portfolio", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return render_template("portfolio/index.html")

@bp.route('/mail', methods=['POST'])
def mail():
    return render_template('portfolio/sent_mail.html')



