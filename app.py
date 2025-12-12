from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User, Translation, UserFeedback
from translation_service import TranslationService
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///translations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)
with app.app_context():
    db.create_all()

# Initialize translation service
translator = TranslationService()

# Mock user system (in a real app, implement proper authentication)
current_user_id = 1  # Default user for demo

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        src_lang = request.form['source_language']
        tgt_lang = request.form['target_language']
        
        try:
            translated = translator.translate(text, src_lang, tgt_lang)
            
            # Save to database
            translation = Translation(
                user_id=current_user_id,
                source_text=text,
                translated_text=translated,
                source_language=src_lang,
                target_language=tgt_lang
            )
            db.session.add(translation)
            db.session.commit()
            
            return render_template('index.html', 
                                 translation=translated,
                                 original=text,
                                 src_lang=src_lang,
                                 tgt_lang=tgt_lang,
                                 translation_id=translation.id)
            
        except Exception as e:
            flash(f"Translation error: {str(e)}", 'error')
    
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    translation_id = request.form['translation_id']
    corrected_text = request.form.get('corrected_text', '')
    rating = request.form.get('rating', 0)
    notes = request.form.get('notes', '')
    
    feedback = UserFeedback(
        translation_id=translation_id,
        corrected_text=corrected_text,
        rating=int(rating),
        feedback_notes=notes
    )
    
    db.session.add(feedback)
    db.session.commit()
    
    flash('Thank you for your feedback!', 'success')
    return redirect(url_for('index'))

@app.route('/history')
def history():
    translations = Translation.query.filter_by(user_id=current_user_id)\
                         .order_by(Translation.timestamp.desc()).all()
    return render_template('history.html', translations=translations)

if __name__ == '__main__':
    app.run(debug=True)

    # This is used for test
    #This is test 2 for branch
    print("EOF")
