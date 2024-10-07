import ipfshttpclient

class PackagingEngine:
    def __init__(self):
        self.client = ipfshttpclient.connect()

    def bundle_collaboration_data(self, logs, output):
        data_bundle = {
            'logs': logs,
            'output': output,
            'timestamp': time.time()
        }
        return data_bundle

    def upload_to_ipfs(self, data_bundle):
        hash_result = self.client.add_json(data_bundle)
        return hash_result['Hash']
