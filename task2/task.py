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

def recommend_medicines(indication):
    recommended_medicines = []
    for med in medicines:
        if med["Indication"].lower() == indication.lower():
            recommended_medicines.append(med)
    return recommended_medicines

def main():
    print("Welcome to the Medicine Recommendation System")
    print("Available indications:")
    indications = set(med["Indication"] for med in medicines)
    for i, indication in enumerate(indications, 1):
        print(f"{i}. {indication}")

    while True:
        user_input = input("\nEnter the number or name of the indication (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        if user_input.isdigit() and 1 <= int(user_input) <= len(indications):
            indication = list(indications)[int(user_input) - 1]
        else:
            indication = user_input

        recommended = recommend_medicines(indication)
        if recommended:
            print(f"\nRecommended medicines for {indication}:")
            for i, med in enumerate(recommended, 1):
                print(f"{i}. {med['Name']}")
                print(f"   Category: {med['Category']}")
                print(f"   Dosage Form: {med['Dosage Form']}")
                print(f"   Strength: {med['Strength']}")
                print(f"   Manufacturer: {med['Manufacturer']}")
                print(f"   Classification: {med['Classification']}")
        else:
            print(f"No medicines found for {indication}")

if __name__ == "__main__":
    main()
