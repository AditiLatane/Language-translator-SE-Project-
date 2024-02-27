from gtts import gTTS
import os

# Text to be converted to speech
text = "आमच्या या वेबसाईट वर विविध विषयावरील मराठी निबंध आणि भाषणे उपलब्ध आहेत"

# Choose the language
language = 'en'

# Create an instance of gTTS
speech = gTTS(text=text, lang=language, slow=False)

# Save the speech as a .mp3 file
speech.save("output.mp3")

# Play the speech
os.system("start output.mp3")



# from langcodes import Language

# def language_name_to_code(language_name):
#     try:
#         # Attempt to parse the language name
#         lang = Language.get(language_name)
#         # Get the language code
#         lang_code = lang.language
#         return lang_code
#     except ValueError:
#         # Handle the case where the language name is not valid
#         print(f"Error: Could not find language code for '{language_name}'")
#         return None

# # Example usage:
# given_language = "hindi"
# language_code = language_name_to_code(given_language)

# if language_code:
#     print(f"The language code for '{given_language}' is '{language_code}'")
