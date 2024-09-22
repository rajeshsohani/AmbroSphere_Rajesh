from django.urls import path
from .views import demo, admin01, mypdf, deletpage, merge_pdfs, pdf_to_word, word_to_pdf,home

urlpatterns = [
    path('', home),
    path('demo/', demo),
    path('admin01/', admin01, name="ad_min"),
    path('pdftools/', mypdf, name='pdftools'),
    path('deletepage/', deletpage, name='deletpage'),
    path('merge_pdfs/', merge_pdfs, name='merge_pdfs'),
    path('pdf_to_word/', pdf_to_word, name='pdf_to_word'),
    path('word_to_pdf/', word_to_pdf, name='word_to_pdf'),
]
