import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

ERROR_MSG = 'Error: Missing text to translate'

def get_translation(translation_object):
    return translation_object.get('translations')[0].get('translation')

def tranlsate_text(text, model_id):
    if isinstance(text, str):
        text = language_translator.translate(
            text=text,
            model_id=model_id
            ).get_result()
        return get_translation(text)
    return ERROR_MSG

def english_to_french(english_text):
    return tranlsate_text(english_text, 'en-fr')

def french_to_english(french_text):
    return tranlsate_text(french_text, 'fr-en')
