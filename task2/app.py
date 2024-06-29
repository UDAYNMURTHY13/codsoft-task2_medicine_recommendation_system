from flask import Flask, render_template, request

# Medicine data in a list of dictionaries
medicines = [
    {"Name": "Acetocillin", "Category": "Antidiabetic", "Dosage Form": "Cream", "Strength": "938 mg", "Manufacturer": "Roche Holding AG", "Indication": "Virus", "Classification": "Over-the-Counter"},
    {"Name": "Ibuprocillin", "Category": "Antiviral", "Dosage Form": "Injection", "Strength": "337 mg", "Manufacturer": "CSL Limited", "Indication": "Infection", "Classification": "Over-the-Counter"},
    {"Name": "Dextrophen", "Category": "Antibiotic", "Dosage Form": "Ointment", "Strength": "333 mg", "Manufacturer": "Johnson & Johnson", "Indication": "Wound", "Classification": "Prescription"},
    {"Name": "Clarinazole", "Category": "Antifungal", "Dosage Form": "Syrup", "Strength": "362 mg", "Manufacturer": "AbbVie Inc.", "Indication": "Pain", "Classification": "Prescription"},
    {"Name": "Ibuprovir", "Category": "Antidepressant", "Dosage Form": "Syrup", "Strength": "758 mg", "Manufacturer": "Eli Lilly and Company", "Indication": "Fungus", "Classification": "Over-the-Counter"},
    {"Name": "Dolocillin", "Category": "Antiviral", "Dosage Form": "Ointment", "Strength": "451 mg", "Manufacturer": "Novo Nordisk A/S", "Indication": "Diabetes", "Classification": "Prescription"},
    {"Name": "Cefmet", "Category": "Antifungal", "Dosage Form": "Tablet", "Strength": "440 mg", "Manufacturer": "AstraZeneca plc", "Indication": "Depression", "Classification": "Prescription"},
    {"Name": "Amoxistatin", "Category": "Antiviral", "Dosage Form": "Inhaler", "Strength": "46 mg", "Manufacturer": "Sanofi S.A.", "Indication": "Fever", "Classification": "Over-the-Counter"},
    {"Name": "Lisinopril", "Category": "Antihypertensive", "Dosage Form": "Tablet", "Strength": "10 mg", "Manufacturer": "Merck & Co.", "Indication": "Hypertension", "Classification": "Prescription"},
    {"Name": "Metformin", "Category": "Antidiabetic", "Dosage Form": "Tablet", "Strength": "500 mg", "Manufacturer": "Novartis AG", "Indication": "Diabetes", "Classification": "Prescription"},
    {"Name": "Atorvastatin", "Category": "Lipid-lowering", "Dosage Form": "Tablet", "Strength": "20 mg", "Manufacturer": "Pfizer Inc.", "Indication": "High Cholesterol", "Classification": "Prescription"},
    {"Name": "Levothyroxine", "Category": "Thyroid hormone", "Dosage Form": "Tablet", "Strength": "100 mcg", "Manufacturer": "Abbott Laboratories", "Indication": "Hypothyroidism", "Classification": "Prescription"},
    {"Name": "Amlodipine", "Category": "Antihypertensive", "Dosage Form": "Tablet", "Strength": "5 mg", "Manufacturer": "Bayer AG", "Indication": "Hypertension", "Classification": "Prescription"},
    {"Name": "Omeprazole", "Category": "Proton pump inhibitor", "Dosage Form": "Capsule", "Strength": "20 mg", "Manufacturer": "GlaxoSmithKline plc", "Indication": "Acid Reflux", "Classification": "Over-the-Counter"},
    {"Name": "Sertraline", "Category": "Antidepressant", "Dosage Form": "Tablet", "Strength": "50 mg", "Manufacturer": "Bristol-Myers Squibb", "Indication": "Depression", "Classification": "Prescription"},
    {"Name": "Albuterol", "Category": "Bronchodilator", "Dosage Form": "Inhaler", "Strength": "90 mcg/actuation", "Manufacturer": "Boehringer Ingelheim", "Indication": "Asthma", "Classification": "Prescription"},
    {"Name": "Tamoxifen", "Category": "Antineoplastic", "Dosage Form": "Tablet", "Strength": "20 mg", "Manufacturer": "AstraZeneca plc", "Indication": "Breast Cancer", "Classification": "Prescription"},
    {"Name": "Dextromethorphan", "Category": "Antitussive", "Dosage Form": "Syrup", "Strength": "15 mg/5 mL", "Manufacturer": "Johnson & Johnson", "Indication": "Cough", "Classification": "Over-the-Counter"},
    {"Name": "Pseudoephedrine", "Category": "Decongestant", "Dosage Form": "Tablet", "Strength": "30 mg", "Manufacturer": "Bayer AG", "Indication": "Cold", "Classification": "Over-the-Counter"},
    {"Name": "Acetaminophen", "Category": "Analgesic", "Dosage Form": "Tablet", "Strength": "500 mg", "Manufacturer": "Johnson & Johnson", "Indication": "Headache", "Classification": "Over-the-Counter"},
    {"Name": "Ibuprofen", "Category": "Analgesic", "Dosage Form": "Tablet", "Strength": "200 mg", "Manufacturer": "Pfizer Inc.", "Indication": "Body Pain", "Classification": "Over-the-Counter"},
]

# Initialize Flask app
app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    # Get unique indications from the list of medicines
    indications = set(med["Indication"] for med in medicines)
    # Render the home page template with indications
    return render_template('index.html', indications=indications)

# Route for recommendation results
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get selected indication from form data
    indication = request.form['indication']
    # Filter medicines by indication
    recommended_medicines = [med for med in medicines if med["Indication"].lower() == indication.lower()]
    # Render the recommendation results template with recommended medicines
    return render_template('recommend.html', indication=indication, recommended_medicines=recommended_medicines)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
