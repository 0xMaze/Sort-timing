from unittest import result
from sort_timer import Sorter
from array_generator import ArrayGenerator
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    array_gen = ArrayGenerator()
    sorter = Sorter()
    arr = None

    arr_size = request.form.get("array_size")
    arr_type = request.form.get("array_type")

    print(arr_size, arr_type)

    if arr_size == "small":
        if arr_type == "random":
            arr = array_gen.small_random_array
        elif arr_type == "sorted":
            arr = array_gen.small_sorted_array
        elif arr_type == "reversed":
            arr = array_gen.small_reversed_array
    elif arr_size == "big":
        if arr_type == "random":
            arr = array_gen.big_random_array
        elif arr_type == "sorted":
            arr = array_gen.big_sorted_array
        elif arr_type == "reversed":
            arr = array_gen.big_reversed_array

    if arr is None:
        return render_template("index.html")
    else:
        arr_cp = arr.copy()
        return render_template(
            "index.html", results=sorter.get_timings(arr), array=arr, array_cp=arr_cp
        )
