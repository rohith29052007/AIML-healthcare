"""
Disease Recommendations Module
Provides solutions, treatments, and recommendations for predicted diseases
"""

# Comprehensive disease solutions database
DISEASE_SOLUTIONS = {
    'common cold': {
        'description': 'A viral infection affecting the upper respiratory tract',
        'symptoms': ['Runny nose', 'Sore throat', 'Cough', 'Sneezing', 'Mild fever'],
        'treatments': [
            'Rest and sleep (7-8 hours daily)',
            'Drink plenty of fluids (water, warm tea, soup)',
            'Take vitamin C supplements or citrus fruits',
            'Use saline nasal drops',
            'Gargle with salt water for sore throat'
        ],
        'home_remedies': [
            'Honey and lemon tea',
            'Ginger water with turmeric',
            'Chicken soup',
            'Eucalyptus oil steam inhalation',
            'Warm compress on sinuses'
        ],
        'medications': [
            'Paracetamol 500mg (for fever/pain)',
            'Ibuprofen 200mg (for inflammation)',
            'Antihistamine for nasal congestion'
        ],
        'when_to_see_doctor': [
            'Symptoms persist beyond 10 days',
            'High fever (>101°F)',
            'Difficulty breathing',
            'Severe headache or chest pain'
        ],
        'prevention': [
            'Wash hands frequently',
            'Avoid touching face',
            'Maintain distance from infected people',
            'Avoid smoking and secondhand smoke',
            'Eat balanced diet rich in vitamins'
        ],
        'duration': '7-10 days',
        'severity': 'Low'
    },
    
    'flu': {
        'description': 'Influenza - a viral respiratory infection more severe than common cold',
        'symptoms': ['Fever', 'Body aches', 'Fatigue', 'Cough', 'Sore throat'],
        'treatments': [
            'Complete bed rest (2-3 weeks)',
            'Maintain high fluid intake',
            'Use humidifier to ease respiratory symptoms',
            'Antiviral medication (if within 48 hours)',
            'Fever management with medication'
        ],
        'home_remedies': [
            'Ginger and turmeric tea',
            'Garlic supplements',
            'Honey with warm milk',
            'Steam inhalation',
            'Rest in a warm room'
        ],
        'medications': [
            'Oseltamivir (Tamiflu) - antiviral',
            'Paracetamol 500mg',
            'Ibuprofen 200-400mg',
            'Cough suppressant if needed'
        ],
        'when_to_see_doctor': [
            'High fever (>102°F) lasting >3 days',
            'Difficulty breathing',
            'Chest pain or pressure',
            'Confusion or severe headache',
            'Coughing up blood'
        ],
        'prevention': [
            'Get annual flu vaccine',
            'Wash hands regularly',
            'Avoid crowds during flu season',
            'Maintain good hygiene',
            'Stay healthy with exercise and diet'
        ],
        'duration': '1-2 weeks',
        'severity': 'Medium'
    },
    
    'tuberculosis': {
        'description': 'A serious bacterial infection typically affecting the lungs',
        'symptoms': ['Persistent cough >3 weeks', 'Chest pain', 'Blood in sputum', 'Fever', 'Night sweats'],
        'treatments': [
            'Antibiotic therapy (6+ months required)',
            'Take all prescribed medications consistently',
            'Regular monitoring and follow-ups',
            'Nutritious diet to support immune system',
            'Adequate rest'
        ],
        'home_remedies': [
            'Maintain high-protein diet',
            'Garlic and ginger tea',
            'Sunlight exposure (vitamin D)',
            'Honey to soothe throat',
            'Rest in well-ventilated room'
        ],
        'medications': [
            'Isoniazid + Rifampicin + Pyrazinamide + Ethambutol',
            'Vitamin B6 (to prevent side effects)',
            'Calcium supplements'
        ],
        'when_to_see_doctor': [
            'URGENT: Seek immediate medical care',
            'Long-term monitoring required',
            'Regular X-rays needed',
            'Monthly follow-ups for medication adjustment'
        ],
        'prevention': [
            'BCG vaccination',
            'Avoid close contact with TB patients',
            'Maintain good nutrition',
            'Quit smoking',
            'Treat latent TB infection'
        ],
        'duration': '6-24 months treatment',
        'severity': 'High - REQUIRES MEDICAL CARE'
    },
    
    'pneumonia': {
        'description': 'Infection causing inflammation of lung air sacs',
        'symptoms': ['Cough', 'Fever', 'Shortness of breath', 'Chest pain', 'Fatigue'],
        'treatments': [
            'Antibiotics (for bacterial pneumonia)',
            'Cough medicine and expectorants',
            'Oxygen therapy (if needed)',
            'Chest physiotherapy',
            'Review treatment progress regularly'
        ],
        'home_remedies': [
            'Warm salt water gargles',
            'Honey and lemon drink',
            'Onion and honey syrup',
            'Vapor home rubs',
            'Adequate rest and hydration'
        ],
        'medications': [
            'Amoxicillin or Azithromycin (antibiotic)',
            'Cough syrup with codeine',
            'Expectorants',
            'Paracetamol for fever'
        ],
        'when_to_see_doctor': [
            'URGENT: Severe difficulty breathing',
            'Chestpain getting worse',
            'Blood in sputum',
            'Confusion or severe headache',
            'Regular monitoring required'
        ],
        'prevention': [
            'Pneumonia vaccine',
            'Annual flu shot',
            'Avoid smoking',
            'Maintain good hygiene',
            'Strengthen immunity'
        ],
        'duration': '2-3 weeks for recovery',
        'severity': 'High - REQUIRES MEDICAL CARE'
    },
    
    'asthma': {
        'description': 'Chronic respiratory condition causing airway inflammation',
        'symptoms': ['Shortness of breath', 'Chest tightness', 'Wheezing', 'Cough', 'Difficulty exercising'],
        'treatments': [
            'Inhaler medications (reliever and preventer)',
            'Avoid known triggers',
            'Regular monitoring of peak flow',
            'Emergency action plan preparation',
            'Long-term controller medications'
        ],
        'home_remedies': [
            'Steam inhalation',
            'Ginger and honey drink',
            'Warm milk with turmeric',
            'Mustard oil massage on chest',
            'Breathing exercises (pranayama)'
        ],
        'medications': [
            'Salbutamol inhaler (for acute attacks)',
            'Fluticasone propionate (preventer)',
            'Montelukast (leukotriene inhibitor)',
            'Theophylline'
        ],
        'when_to_see_doctor': [
            'Difficult breathing requiring emergency visit',
            'Peak flow readings in yellow zone',
            'Need for reliever inhaler >2 times/week',
            'Regular check-ups (every 1-3 months)'
        ],
        'prevention': [
            'Identify and avoid triggers',
            'Use air purifier',
            'Regular exercise',
            'Maintain healthy weight',
            'Control allergies'
        ],
        'duration': 'Chronic - lifelong management',
        'severity': 'Medium to High'
    },
    
    'anxiety': {
        'description': 'Mental health condition characterized by excessive worry',
        'symptoms': ['Excessive worry', 'Panic', 'Restlessness', 'Difficulty sleeping', 'Physical tension'],
        'treatments': [
            'Cognitive behavioral therapy (CBT)',
            'Mindfulness and meditation',
            'Regular exercise',
            'Psychotherapy with professional',
            'Anxiety management techniques'
        ],
        'home_remedies': [
            'Deep breathing exercises',
            'Progressive muscle relaxation',
            'Yoga and stretching',
            'Meditation and mindfulness',
            'Limit caffeine intake'
        ],
        'medications': [
            'SSRIs (Sertraline, Paroxetine)',
            'SNRIs (Venlafaxine)',
            'Propranolol (for physical symptoms)',
            'Benzodiazepines (short-term use only)'
        ],
        'when_to_see_doctor': [
            'Anxiety interferes with daily life',
            'Panic attacks occurring',
            'Thoughts of self-harm',
            'Unable to manage stress',
            'Regular therapy sessions recommended'
        ],
        'prevention': [
            'Regular exercise',
            'Healthy sleep schedule',
            'Limit stress and caffeine',
            'Social connections',
            'Time management'
        ],
        'duration': 'Variable - ongoing management',
        'severity': 'Medium'
    },
    
    'diabetes': {
        'description': 'Metabolic disorder affecting blood glucose regulation',
        'symptoms': ['Increased thirst', 'Frequent urination', 'Fatigue', 'Blurred vision', 'Weight loss'],
        'treatments': [
            'Blood sugar monitoring (daily)',
            'Medication (oral or insulin)',
            'Balanced diet low in refined carbs',
            'Regular exercise',
            'Weight management'
        ],
        'home_remedies': [
            'Cinnamon water',
            'Bitter gourd juice',
            'Fenugreek seeds',
            'Aloe vera gel',
            'Regular walking'
        ],
        'medications': [
            'Metformin',
            'Glipizide',
            'Insulin injections',
            'GLP-1 agonists',
            'ACE inhibitors'
        ],
        'when_to_see_doctor': [
            'Monthly blood sugar monitoring',
            'HbA1c testing every 3 months',
            'Annual comprehensive checks',
            'Eye and foot examinations',
            'Kidney function tests'
        ],
        'prevention': [
            'Maintain healthy weight',
            'Regular physical activity',
            'Eat whole grains and vegetables',
            'Limit sugar and processed foods',
            'Regular health checkups'
        ],
        'duration': 'Chronic - lifelong management',
        'severity': 'High - Regular monitoring'
    },
    
    'hypertension': {
        'description': 'High blood pressure condition affecting cardiovascular health',
        'symptoms': ['Headaches', 'Dizziness', 'Nosebleeds', 'Shortness of breath', 'Often asymptomatic'],
        'treatments': [
            'Blood pressure monitoring (daily)',
            'Antihypertensive medications',
            'Low-sodium diet',
            'Regular exercise (30 mins daily)',
            'Stress management'
        ],
        'home_remedies': [
            'Garlic supplements',
            'Hibiscus tea',
            'Potassium-rich foods',
            'Meditation and yoga',
            'Reduce caffeine intake'
        ],
        'medications': [
            'ACE inhibitors (Lisinopril)',
            'Beta-blockers (Metoprolol)',
            'Calcium channel blockers',
            'Diuretics (Hydrochlorothiazide)',
            'Combination therapy if needed'
        ],
        'when_to_see_doctor': [
            'Regular monitoring (monthly initially)',
            'Adjust medication as needed',
            'Check for complications',
            'Annual cardiovascular assessment',
            'Emergency care if BP >180/120'
        ],
        'prevention': [
            'Maintain healthy weight',
            'Reduce salt intake',
            'Regular exercise',
            'Limit alcohol',
            'Manage stress'
        ],
        'duration': 'Chronic - lifelong management',
        'severity': 'High - Requires management'
    },
    
    'migraine': {
        'description': 'Severe headache disorder with potential neurological symptoms',
        'symptoms': ['Severe headache', 'Nausea', 'Sensitivity to light', 'Aura (visual disturbances)', 'Vomiting'],
        'treatments': [
            'Rest in quiet, dark room',
            'Take painkillers early (within 30 mins)',
            'Apply hot/cold compress',
            'Stay hydrated',
            'Preventive medications'
        ],
        'home_remedies': [
            'Peppermint oil massage',
            'Ginger tea',
            'Lavender essential oil',
            'Cool compress on forehead',
            'Lie down in dark room'
        ],
        'medications': [
            'Ibuprofen 200-400mg',
            'Sumatriptan (triptan class)',
            'Propranolol (preventive)',
            'Topiramate (preventive)',
            'Magnesium supplements'
        ],
        'when_to_see_doctor': [
            'Migraines increasing in frequency',
            'Severe pain interfering with life',
            'New symptoms appearing',
            'Need preventive medication',
            'Consultation with neurologist'
        ],
        'prevention': [
            'Identify and avoid triggers',
            'Maintain regular sleep schedule',
            'Stay hydrated',
            'Manage stress',
            'Regular exercise'
        ],
        'duration': '4-72 hours per episode',
        'severity': 'Medium to High'
    }
}


def get_disease_solutions(disease_name):
    """
    Get comprehensive solutions for a disease
    
    Args:
        disease_name: Name of the disease
    
    Returns:
        Dictionary with recommendations and solutions
    """
    disease_lower = disease_name.lower().strip()
    
    # Direct match
    if disease_lower in DISEASE_SOLUTIONS:
        return DISEASE_SOLUTIONS[disease_lower]
    
    # Fuzzy match - check for similar names
    for disease_key in DISEASE_SOLUTIONS.keys():
        if disease_lower in disease_key or disease_key in disease_lower:
            return DISEASE_SOLUTIONS[disease_key]
    
    # Default response for unknown disease
    return {
        'description': f'Information about {disease_name} is not available in our database',
        'symptoms': ['Please consult a healthcare professional'],
        'treatments': ['Seek medical advice from a qualified doctor'],
        'home_remedies': ['Rest and maintain proper hygiene'],
        'medications': ['As prescribed by your doctor'],
        'when_to_see_doctor': ['As soon as possible for proper diagnosis'],
        'prevention': ['Maintain good health habits and hygiene'],
        'duration': 'Varies - consult doctor',
        'severity': 'Unknown - REQUIRES MEDICAL ASSESSMENT'
    }


def format_solutions_for_display(disease_name):
    """
    Format disease solutions nicely for display
    
    Args:
        disease_name: Name of the disease
    
    Returns:
        Formatted string with recommendations
    """
    solutions = get_disease_solutions(disease_name)
    
    formatted = f"""
╔════════════════════════════════════════════════════════════════╗
║                        TREATMENT GUIDE                         ║
║                     for {disease_name.upper()}
╚════════════════════════════════════════════════════════════════╝

📋 DESCRIPTION:
{solutions['description']}

🩺 COMMON SYMPTOMS:
{format_list(solutions['symptoms'])}

💊 RECOMMENDED TREATMENTS:
{format_list(solutions['treatments'])}

🏡 HOME REMEDIES:
{format_list(solutions['home_remedies'])}

💉 MEDICATIONS:
{format_list(solutions['medications'])}

⚠️ WHEN TO SEE A DOCTOR:
{format_list(solutions['when_to_see_doctor'])}

🛡️ PREVENTION:
{format_list(solutions['prevention'])}

⏱️ EXPECTED DURATION: {solutions['duration']}
🔴 SEVERITY LEVEL: {solutions['severity']}

════════════════════════════════════════════════════════════════

⚕️ IMPORTANT: This information is for educational purposes.
   Always consult a healthcare professional for proper diagnosis
   and treatment.
"""
    return formatted


def format_list(items):
    """Format list items with bullet points"""
    if isinstance(items, list):
        return '\n'.join([f'  • {item}' for item in items])
    return f'  • {items}'


if __name__ == '__main__':
    # Test the recommendations system
    test_diseases = ['common cold', 'tuberculosis', 'diabetes', 'anxiety']
    
    for disease in test_diseases:
        print(format_solutions_for_display(disease))
        print('\n')
