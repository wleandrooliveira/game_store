from datetime import datetime
from flask import render_template, session, redirect,url_for, flash
from . import main
from .. import db
from ..models import Category


@main.route('/', methods = ['GET', 'POST'])
def index ():
    return "Essa página é a principal"

