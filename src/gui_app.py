"""
GUI Application Module
Tkinter-based GUI for AI Healthcare Assistant
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from predictor import DiseasePredictor
from personal_health import PersonalHealthProfile


class AIHealthcareGUI:
    """Main GUI Application for AI Healthcare Assistant"""
    
    def __init__(self, root):
        """
        Initialize the GUI application
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("AI Healthcare Assistant")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Set style
        self.setup_styles()
        
        # Get paths
        project_root = Path(__file__).parent.parent
        models_path = os.path.join(project_root, "models", "trained_models.joblib")
        profiles_dir = os.path.join(project_root, "profiles")
        
        # Initialize modules
        try:
            self.predictor = DiseasePredictor(models_path)
            self.health_manager = PersonalHealthProfile(profiles_dir)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load models: {e}\n\nPlease run train_model.py first.")
            self.root.quit()
            return
        
        # Store references
        self.current_frame = None
        self.selected_symptoms = {}
        self.current_profile = None
        self.symptom_duration = tk.StringVar(value="3-7")
        
        # Show home screen
        self.show_home_screen()
    
    def setup_styles(self):
        """Setup custom styles for the GUI"""
        self.bg_color = "#ecf0f1"
        self.primary_color = "#3498db"
        self.secondary_color = "#2ecc71"
        self.danger_color = "#e74c3c"
        self.text_color = "#2c3e50"
        
        self.root.configure(bg=self.bg_color)
    
    def clear_frame(self):
        """Clear current frame"""
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = None
    
    def show_home_screen(self):
        """Display the home screen with main options"""
        self.clear_frame()
        
        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.current_frame = frame
        
        # Title
        title = tk.Label(
            frame,
            text="AI Healthcare Assistant",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            frame,
            text="Predict diseases based on symptoms",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        subtitle.pack(pady=10)
        
        # Button container
        button_frame = tk.Frame(frame, bg=self.bg_color)
        button_frame.pack(pady=40)
        
        # General Disease Prediction Button
        btn_general = tk.Button(
            button_frame,
            text="General Disease Prediction",
            font=("Arial", 14, "bold"),
            bg=self.primary_color,
            fg="white",
            padx=20,
            pady=15,
            width=30,
            command=self.show_general_prediction_screen,
            cursor="hand2"
        )
        btn_general.pack(pady=15)
        
        # Personal Healthcare Prediction Button
        btn_personal = tk.Button(
            button_frame,
            text="Personal Healthcare Prediction",
            font=("Arial", 14, "bold"),
            bg=self.secondary_color,
            fg="white",
            padx=20,
            pady=15,
            width=30,
            command=self.show_personal_prediction_screen,
            cursor="hand2"
        )
        btn_personal.pack(pady=15)
        
        # Exit Button
        btn_exit = tk.Button(
            button_frame,
            text="Exit",
            font=("Arial", 14, "bold"),
            bg=self.danger_color,
            fg="white",
            padx=20,
            pady=15,
            width=30,
            command=self.root.quit,
            cursor="hand2"
        )
        btn_exit.pack(pady=15)
    
    def show_general_prediction_screen(self):
        """Display the general disease prediction screen"""
        self.clear_frame()
        
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.current_frame = main_frame
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.primary_color)
        header_frame.pack(fill=tk.X)
        
        header = tk.Label(
            header_frame,
            text="General Disease Prediction",
            font=("Arial", 18, "bold"),
            bg=self.primary_color,
            fg="white",
            pady=10
        )
        header.pack()
        
        # Back button
        back_btn = tk.Button(
            header_frame,
            text="← Back to Home",
            font=("Arial", 10),
            bg="white",
            fg=self.primary_color,
            command=self.show_home_screen,
            cursor="hand2"
        )
        back_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Duration selection section
        duration_label = tk.Label(
            content_frame,
            text="How long have you had these symptoms?",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        duration_label.pack(anchor=tk.W, pady=(0, 10))
        
        duration_frame = tk.Frame(content_frame, bg=self.bg_color)
        duration_frame.pack(anchor=tk.W, pady=(0, 15))
        
        durations = [
            ("Less than 3 days (1-2 days)", "1-2"),
            ("3-7 days (1 week)", "3-7"),
            ("1-2 weeks", "1-2w"),
            ("2-4 weeks", "2-4w"),
            ("More than 4 weeks", "4+w")
        ]
        
        for text, value in durations:
            rb = tk.Radiobutton(
                duration_frame,
                text=text,
                variable=self.symptom_duration,
                value=value,
                font=("Arial", 10),
                bg=self.bg_color,
                fg=self.text_color,
                activebackground=self.bg_color,
                activeforeground=self.primary_color
            )
            rb.pack(anchor=tk.W, pady=3)
        
        # Symptom selection label
        label = tk.Label(
            content_frame,
            text="Select your symptoms:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        label.pack(anchor=tk.W, pady=(15, 10))
        
        # Scrollable frame for symptoms
        canvas = tk.Canvas(content_frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_color)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create checkboxes for symptoms
        symptoms = self.predictor.get_all_symptoms()
        self.selected_symptoms = {symptom: tk.BooleanVar() for symptom in symptoms}
        
        for symptom in symptoms:
            cb = tk.Checkbutton(
                scrollable_frame,
                text=symptom.replace('_', ' ').title(),
                variable=self.selected_symptoms[symptom],
                font=("Arial", 10),
                bg=self.bg_color,
                fg=self.text_color,
                activebackground=self.bg_color,
                activeforeground=self.primary_color
            )
            cb.pack(anchor=tk.W, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button frame
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=20)
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="Clear All",
            font=("Arial", 11, "bold"),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=10,
            command=self._clear_symptoms,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Predict button
        predict_btn = tk.Button(
            button_frame,
            text="Predict Disease",
            font=("Arial", 11, "bold"),
            bg=self.secondary_color,
            fg="white",
            padx=15,
            pady=10,
            command=self._predict_general,
            cursor="hand2"
        )
        predict_btn.pack(side=tk.RIGHT, padx=5)
    
    def show_personal_prediction_screen(self):
        """Display the personal healthcare prediction screen"""
        self.clear_frame()
        
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.current_frame = main_frame
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.secondary_color)
        header_frame.pack(fill=tk.X)
        
        header = tk.Label(
            header_frame,
            text="Personal Healthcare Prediction",
            font=("Arial", 18, "bold"),
            bg=self.secondary_color,
            fg="white",
            pady=10
        )
        header.pack()
        
        # Back button
        back_btn = tk.Button(
            header_frame,
            text="← Back to Home",
            font=("Arial", 10),
            bg="white",
            fg=self.secondary_color,
            command=self.show_home_screen,
            cursor="hand2"
        )
        back_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Check for existing profile
        profiles = self.health_manager.get_available_profiles()
        
        if profiles:
            # Option to load existing profile
            self._show_load_profile_screen(content_frame, profiles)
        else:
            # Show create new profile form
            self._show_create_profile_form(content_frame)
    
    def _show_load_profile_screen(self, content_frame, profiles):
        """Show option to load existing profile"""
        label = tk.Label(
            content_frame,
            text="Select a profile or create new:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        label.pack(anchor=tk.W, pady=(0, 10))
        
        # Profile list
        listbox = tk.Listbox(content_frame, height=5, font=("Arial", 10))
        listbox.pack(fill=tk.X, pady=10)
        
        for profile_file in profiles:
            listbox.insert(tk.END, profile_file.replace('_', ' ').replace('.json', ''))
        
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=20)
        
        def load_selected():
            selection = listbox.curselection()
            if selection:
                profile_file = profiles[selection[0]]
                self.health_manager.load_profile(profile_file)
                self._show_prediction_with_profile(content_frame)
        
        load_btn = tk.Button(
            button_frame,
            text="Load Profile",
            font=("Arial", 11, "bold"),
            bg=self.primary_color,
            fg="white",
            padx=15,
            pady=10,
            command=load_selected,
            cursor="hand2"
        )
        load_btn.pack(side=tk.LEFT, padx=5)
        
        new_btn = tk.Button(
            button_frame,
            text="Create New Profile",
            font=("Arial", 11, "bold"),
            bg=self.secondary_color,
            fg="white",
            padx=15,
            pady=10,
            command=lambda: self._show_create_profile_form(content_frame),
            cursor="hand2"
        )
        new_btn.pack(side=tk.LEFT, padx=5)
    
    def _show_create_profile_form(self, content_frame):
        """Show form to create new profile"""
        # Clear previous content
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        label = tk.Label(
            content_frame,
            text="Create New Health Profile",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        label.pack(anchor=tk.W, pady=(0, 20))
        
        # Form frame
        form_frame = tk.Frame(content_frame, bg=self.bg_color)
        form_frame.pack(fill=tk.X, pady=10)
        
        # Name
        tk.Label(form_frame, text="Name:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W)
        name_entry = tk.Entry(form_frame, font=("Arial", 10), width=40)
        name_entry.pack(anchor=tk.W, pady=(0, 15))
        
        # Age
        tk.Label(form_frame, text="Age:", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W)
        age_entry = tk.Entry(form_frame, font=("Arial", 10), width=40)
        age_entry.pack(anchor=tk.W, pady=(0, 15))
        
        # Previous Diseases
        tk.Label(form_frame, text="Previous Diseases (comma-separated):", font=("Arial", 10), bg=self.bg_color).pack(anchor=tk.W)
        diseases_entry = tk.Entry(form_frame, font=("Arial", 10), width=40)
        diseases_entry.pack(anchor=tk.W, pady=(0, 15))
        
        def save_profile():
            name = name_entry.get()
            age = age_entry.get()
            diseases_text = diseases_entry.get()
            previous_diseases = [d.strip() for d in diseases_text.split(',') if d.strip()]
            
            # Validate
            is_valid, error_msg = self.health_manager.validate_profile(name, age)
            if not is_valid:
                messagebox.showerror("Validation Error", error_msg)
                return
            
            # Create and save profile
            profile = self.health_manager.create_profile(name, age, previous_diseases)
            self.health_manager.save_profile()
            
            # Show prediction with new profile
            self._show_prediction_with_profile(content_frame)
        
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=20)
        
        save_btn = tk.Button(
            button_frame,
            text="Save Profile and Continue",
            font=("Arial", 11, "bold"),
            bg=self.secondary_color,
            fg="white",
            padx=15,
            pady=10,
            command=save_profile,
            cursor="hand2"
        )
        save_btn.pack(side=tk.LEFT, padx=5)
    
    def _show_prediction_with_profile(self, content_frame):
        """Show symptom prediction screen with profile"""
        # Clear previous content
        for widget in content_frame.winfo_children():
            widget.destroy()
        
        # Profile info
        profile = self.health_manager.current_profile
        if profile:
            profile_label = tk.Label(
                content_frame,
                text=f"Profile: {profile['name']}, Age: {profile['age']}",
                font=("Arial", 10, "italic"),
                bg=self.bg_color,
                fg=self.primary_color
            )
            profile_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Duration selection section
        duration_label = tk.Label(
            content_frame,
            text="How long have you had these symptoms?",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        duration_label.pack(anchor=tk.W, pady=(10, 10))
        
        duration_frame = tk.Frame(content_frame, bg=self.bg_color)
        duration_frame.pack(anchor=tk.W, pady=(0, 15))
        
        durations = [
            ("Less than 3 days (1-2 days)", "1-2"),
            ("3-7 days (1 week)", "3-7"),
            ("1-2 weeks", "1-2w"),
            ("2-4 weeks", "2-4w"),
            ("More than 4 weeks", "4+w")
        ]
        
        for text, value in durations:
            rb = tk.Radiobutton(
                duration_frame,
                text=text,
                variable=self.symptom_duration,
                value=value,
                font=("Arial", 10),
                bg=self.bg_color,
                fg=self.text_color,
                activebackground=self.bg_color,
                activeforeground=self.primary_color
            )
            rb.pack(anchor=tk.W, pady=3)
        
        # Symptom selection label
        label = tk.Label(
            content_frame,
            text="Select your symptoms:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        label.pack(anchor=tk.W, pady=(15, 10))
        
        # Scrollable frame for symptoms
        canvas = tk.Canvas(content_frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_color)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create checkboxes for symptoms
        symptoms = self.predictor.get_all_symptoms()
        self.selected_symptoms = {symptom: tk.BooleanVar() for symptom in symptoms}
        
        for symptom in symptoms:
            cb = tk.Checkbutton(
                scrollable_frame,
                text=symptom.replace('_', ' ').title(),
                variable=self.selected_symptoms[symptom],
                font=("Arial", 10),
                bg=self.bg_color,
                fg=self.text_color,
                activebackground=self.bg_color,
                activeforeground=self.secondary_color
            )
            cb.pack(anchor=tk.W, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button frame
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=20)
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="Clear All",
            font=("Arial", 11, "bold"),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=10,
            command=self._clear_symptoms,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Predict button
        predict_btn = tk.Button(
            button_frame,
            text="Predict Disease",
            font=("Arial", 11, "bold"),
            bg=self.secondary_color,
            fg="white",
            padx=15,
            pady=10,
            command=self._predict_personal,
            cursor="hand2"
        )
        predict_btn.pack(side=tk.RIGHT, padx=5)
    
    def _clear_symptoms(self):
        """Clear all selected symptoms"""
        for var in self.selected_symptoms.values():
            var.set(False)
    
    def _predict_general(self):
        """Make general disease prediction"""
        # Get selected symptoms
        symptoms_dict = {
            symptom: 1 if self.selected_symptoms[symptom].get() else 0
            for symptom in self.selected_symptoms
        }
        
        # Check if at least one symptom is selected
        if sum(symptoms_dict.values()) == 0:
            messagebox.showwarning("Warning", "Please select at least one symptom")
            return
        
        # Get symptom duration
        duration = self.symptom_duration.get()
        
        # Make prediction with duration
        result = self.predictor.predict_disease(symptoms_dict, duration=duration)
        
        if result:
            self._show_prediction_result(result, is_personal=False)
    
    def _predict_personal(self):
        """Make personal disease prediction"""
        # Get selected symptoms
        symptoms_dict = {
            symptom: 1 if self.selected_symptoms[symptom].get() else 0
            for symptom in self.selected_symptoms
        }
        
        # Check if at least one symptom is selected
        if sum(symptoms_dict.values()) == 0:
            messagebox.showwarning("Warning", "Please select at least one symptom")
            return
        
        # Get symptom duration
        duration = self.symptom_duration.get()
        
        # Make prediction with duration
        result = self.predictor.predict_disease(symptoms_dict, duration=duration)
        
        if result:
            # Calculate risk score
            profile = self.health_manager.current_profile
            risk_score, risk_level = self.health_manager.calculate_risk_score(
                result['predicted_disease'],
                profile['previous_diseases'] if profile else []
            )
            
            # Add to history
            if profile:
                self.health_manager.add_prediction_to_history(
                    result['predicted_disease'],
                    result['confidence'],
                    risk_level,
                    duration=duration
                )
                self.health_manager.save_profile()
            
            self._show_prediction_result(result, is_personal=True, risk_level=risk_level, risk_score=risk_score)
    
    def _show_prediction_result(self, result, is_personal=False, risk_level=None, risk_score=None):
        """Display prediction results"""
        self.clear_frame()
        
        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.current_frame = frame
        
        # Title
        title = tk.Label(
            frame,
            text="Prediction Results",
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title.pack(pady=10)
        
        # Predicted disease
        disease_label = tk.Label(
            frame,
            text=f"Predicted Disease: {result['predicted_disease']}",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.secondary_color
        )
        disease_label.pack(pady=10)
        
        # Confidence
        confidence_label = tk.Label(
            frame,
            text=f"Confidence: {result['confidence']:.2f}%",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        confidence_label.pack(pady=5)
        
        # Symptom duration
        if 'symptom_duration' in result:
            duration_map = {
                '1-2': 'Less than 3 days (1-2 days)',
                '3-7': '3-7 days (1 week)',
                '1-2w': '1-2 weeks',
                '2-4w': '2-4 weeks',
                '4+w': 'More than 4 weeks'
            }
            duration_text = duration_map.get(result['symptom_duration'], result['symptom_duration'])
            duration_label = tk.Label(
                frame,
                text=f"Symptom Duration: {duration_text}",
                font=("Arial", 11, "italic"),
                bg=self.bg_color,
                fg=self.primary_color
            )
            duration_label.pack(pady=5)
        
        # Risk level (if personal)
        if is_personal and risk_level:
            risk_color = self.danger_color if risk_level == "HIGH" else (self.primary_color if risk_level == "MEDIUM" else self.secondary_color)
            risk_label = tk.Label(
                frame,
                text=f"Risk Level: {risk_level} (Score: {risk_score})",
                font=("Arial", 12, "bold"),
                bg=self.bg_color,
                fg=risk_color
            )
            risk_label.pack(pady=5)
        
        # Top 3 predictions
        results_label = tk.Label(
            frame,
            text="Top 3 Possible Diseases:",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        results_label.pack(pady=15)
        
        results_text = tk.StringVar()
        for i, (disease, prob) in enumerate(result['top_3'], 1):
            results_text.set(results_text.get() + f"{i}. {disease} ({prob:.2f}%)\n")
        
        results_display = tk.Label(
            frame,
            text=results_text.get(),
            font=("Arial", 11),
            bg=self.bg_color,
            fg=self.text_color,
            justify=tk.LEFT
        )
        results_display.pack(pady=10)
        
        # Solutions Section
        if 'solutions' in result:
            solutions_label = tk.Label(
                frame,
                text="📋 Recommended Solutions:",
                font=("Arial", 12, "bold"),
                bg=self.bg_color,
                fg=self.primary_color
            )
            solutions_label.pack(pady=(20, 10))
            
            solutions = result['solutions']
            
            # Create scrollable frame for solutions
            canvas = tk.Canvas(frame, bg=self.bg_color, highlightthickness=0, height=200)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg=self.bg_color)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # Add solutions content
            solution_text = f"""
💊 TREATMENTS:
{self._format_list(solutions.get('treatments', []))}

🏡 HOME REMEDIES:
{self._format_list(solutions.get('home_remedies', []))}

⚠️ WHEN TO SEE A DOCTOR:
{self._format_list(solutions.get('when_to_see_doctor', []))}

🛡️ PREVENTION:
{self._format_list(solutions.get('prevention', []))}

⏱️ Duration: {solutions.get('duration', 'N/A')}
🔴 Severity: {solutions.get('severity', 'N/A')}
            """
            
            solution_display = tk.Label(
                scrollable_frame,
                text=solution_text,
                font=("Arial", 9),
                bg=self.bg_color,
                fg=self.text_color,
                justify=tk.LEFT,
                wraplength=500
            )
            solution_display.pack(padx=10, pady=5, anchor=tk.W)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = tk.Frame(frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=20)
        
        # Back button
        back_btn = tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 11, "bold"),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=10,
            command=self.show_home_screen,
            cursor="hand2"
        )
        back_btn.pack(side=tk.LEFT, padx=5)
        
        # Home button
        home_btn = tk.Button(
            button_frame,
            text="Home",
            font=("Arial", 11, "bold"),
            bg=self.primary_color,
            fg="white",
            padx=15,
            pady=10,
            command=self.show_home_screen,
            cursor="hand2"
        )
        home_btn.pack(side=tk.RIGHT, padx=5)
    
    def _format_list(self, items):
        """Format list items with bullet points"""
        if isinstance(items, list):
            return '\n'.join([f'  • {item}' for item in items])
        return f'  • {items}'


def main():
    """Main function to run the GUI"""
    root = tk.Tk()
    app = AIHealthcareGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
