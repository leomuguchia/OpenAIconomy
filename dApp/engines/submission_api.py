class SubmissionAPI:
    def submit_to_validators(self, ipfs_hash, metadata):
        submission = {
            'hash': ipfs_hash,
            'metadata': metadata,
            'timestamp': time.time()
        }
        return f"Submitted to validator nodes: {submission}"

    def handle_response(self, response):
        # Handles delayed responses from the validators
        if response['status'] == 'success':
            print(f"Tokens received: {response['tokens']}")
        else:
            print("Validation failed.")
