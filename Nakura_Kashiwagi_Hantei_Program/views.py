from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import FormView
from .forms import DetectorForm
from .detector.detector import Detector
from NKHP.settings import DTCR, RESULT_BASE_TEXT


def main_view(request):
    if request.method == 'POST':
        base_form = DetectorForm(data=request.POST)
        if base_form.is_valid():
            context = request.POST['context']
            value_output_layer = DTCR.detect_author(content=context)
            if value_output_layer[0][0] > value_output_layer[0][1]:
                result = RESULT_BASE_TEXT \
                         + ["\t柏木%.0fパーセント" %
                            float(value_output_layer[0][0] * 100)]
            else:
                result = RESULT_BASE_TEXT \
                         + ["\t奈倉%.0fパーセント" %
                            float(value_output_layer[0][1] * 100)]
    else:
        result = ['']
        base_form = DetectorForm()

    form = base_form.as_p()
    return render(request, 'main.html', locals())
