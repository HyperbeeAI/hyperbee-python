import httpx
from typing import List, Tuple
import time
import threading
import random
import json
import queue
import re

class batch_request():
    
    def __init__(self, api_key):
        self.base_url = "https://api-fastest.hyperbee.ai"
        self.client = httpx.Client(timeout=180.0)
        self.thread_cnt = 22
        
    def __call__(self, prompt_list: List[str], output_length: int):
        self.base_url = "http://34.27.22.31:30001"
        self.client = httpx.Client(timeout=180.0)
        output_length = output_length + 1
        threads = []
        result_queue = queue.Queue()
        prompt_per_thread = (len(prompt_list) // self.thread_cnt) + 1

        try:
            for i in range(0, len(prompt_list), prompt_per_thread):
                batch = prompt_list[i:i + prompt_per_thread]
                batch_tuples = [(prompt, output_length) for prompt in batch]
                t = threading.Thread(target=send_batch, args=(self.client, self.base_url, batch_tuples, i+1, result_queue))
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
        
            # Collect results from the queue
            results = [result_queue.get() for _ in range(len(threads))]
            results.sort(key=lambda x: x[0]) 
            
            combined_results = []
            for result in results:
                combined_results.extend(result[1])
                
            return combined_results
        finally:
            self.client.close()

def extract_required_part(output: str) -> str:
    return output.split("<|end|>")[0][1:]

def send_batch(client, base_url, requests, thread_id, result_queue):
    results = run_vllm(client, base_url, requests)
    result_queue.put((thread_id, results))

def run_vllm(client, base_url, requests: List[Tuple[str, int]]) -> List[Tuple[str, str]]:
    request_items = [{'prompt': prompt, 'output_len': output_len} for prompt, output_len in requests]
    response = client.post(f"{base_url}/run_batch", json=request_items)
    response.raise_for_status()
    results = response.json()
    batch_results = [item['result'] for item in results]
    processed_list = [extract_required_part(string) for string in batch_results]
    return processed_list
    
    
    
