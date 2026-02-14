from django.shortcuts import render
from .forms import TranslationForm
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
import os
from django.http import HttpResponse

def index(request):
    translated_text = ""
    detected_lang = "Detected Language"
    form = TranslationForm()

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            target_language = form.cleaned_data['target_language']
            
            try:
                # Detect language using langdetect
                detected_code = 'auto'
                try:
                    if text.strip():
                        detected_code = detect(text)
                except Exception:
                    detected_code = 'auto'
                
                # Extended Manual Map
                LANG_MAP = {
                    'en': 'English', 'hi': 'Hindi', 'te': 'Telugu', 
                    'ur': 'Urdu', 'ja': 'Japanese', 'zh': 'Chinese', 'zh-cn': 'Chinese',
                    'fr': 'French', 'es': 'Spanish', 'de': 'German',
                    'it': 'Italian', 'ru': 'Russian', 'pt': 'Portuguese',
                    'ar': 'Arabic', 'bn': 'Bengali', 'ta': 'Tamil',
                    'kn': 'Kannada', 'ml': 'Malayalam', 'pa': 'Punjabi'
                }
                
                # Get full name, title case if not in map
                detected_lang = LANG_MAP.get(detected_code, detected_code.upper())
                
                if detected_code == 'auto':
                     detected_lang = "Detected Language"

                translator = GoogleTranslator(source='auto', target=target_language)
                translated_text = translator.translate(text)
            except Exception as e:
                translated_text = f"Error: {str(e)}"

    return render(request, 'translator/index.html', {
        'form': form,
        'translated_text': translated_text,
        'detected_lang': detected_lang
    })

def speak_text(request):
    if request.method == 'GET':
        text = request.GET.get('text')
        lang = request.GET.get('lang')
        
        if text and lang:
            try:
                tts = gTTS(text=text, lang=lang)
                response = HttpResponse(content_type='audio/mpeg')
                tts.write_to_fp(response)
                return response
            except Exception as e:
                return HttpResponse(str(e), status=500)
    return HttpResponse("Invalid request", status=400)
