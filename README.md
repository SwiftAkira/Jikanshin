**Jikanshin - Real-Time Speech Translation**

Jikanshin is a Python-based application designed for real-time speech translation. This project aims to provide subtitles by translating spoken language from any detected language to your preferred language, displaying them at the bottom of the screen.

**Current Status**
⚠️ This project is still under development and does not fully work yet. 

Currently, the application uses your own microphone for input, but the goal is to enhance it to capture audio from your PC and provide real-time translation subtitles.FeaturesLanguage Detection: Automatically detects the language being spoken.

Real-Time Translation: Translates the detected speech into the preferred language using OpenAI's GPT-4o Mini.

Subtitles Display: Displays the translated text as subtitles at the bottom of the screen.

**Installation**
_**To set up the environment and dependencies: **_
Clone the repository: git clone https://github.com/SwiftAkira/jikanshin.git
cd jikanshin

_**Create a virtual environment and activate it:**_
python -m venv jikanshin_env
jikanshin_env\Scripts\activate

_**Install the required packages:**_
pip install -r requirements.txt

**Usage**
**_To run the application: _**
python jikanshin.py
DependenciesVoskLangidOpenAITransformersTkinterRoadmapFix
the current issues and ensure stable operation.
Enhance the application to capture and translate audio from the PC instead of the microphone.
Improve language detection and translation accuracy.Provide better error handling and user feedback.

**Contributing**

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.License
This project is licensed under the MIT License - see the LICENSE file for details.
