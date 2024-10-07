class AIPluginInterface:
    def integrate_ai_model(self, model):
        print(f"Integrated AI model: {model.name}")
        self.ai_model = model

    def ai_generate(self, user_input):
        # Interact with the AI model to generate output
        ai_output = self.ai_model.generate(user_input)
        return ai_output

    def ai_adjust(self, feedback):
        # Adjust the AI's output based on feedback
        adjusted_output = self.ai_model.adjust(feedback)
        return adjusted_output
