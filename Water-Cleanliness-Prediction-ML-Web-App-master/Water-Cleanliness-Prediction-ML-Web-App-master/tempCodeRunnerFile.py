from flask import Flask, render_template, request
import pickle
import numpy as np
from werkzeug.exceptions import BadRequestKeyError