class CognitiveCollaborationEngine:
    def __init__(self):
        self.interaction_logs = []
        self.feedback_loops = []

    def log_interaction(self, user_input, ai_output):
        interaction = {
            'timestamp': time.time(),
            'user_input': user_input,
            'ai_output': ai_output
        }
        self.interaction_logs.append(interaction)

    def log_feedback_loop(self, user_feedback, ai_adjusted_output):
        feedback = {
            'timestamp': time.time(),
            'user_feedback': user_feedback,
            'ai_adjusted_output': ai_adjusted_output
        }
        self.feedback_loops.append(feedback)

    def get_collaboration_logs(self):
        return {
            'interactions': self.interaction_logs,
            'feedback_loops': self.feedback_loops
        }
