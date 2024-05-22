import httpx
from typing import List, Tuple
import asyncio
import queue

class batch_request:
    
    def __init__(self, api_key):
        self.api_key = api_key  # Assuming you will use api_key somewhere
        self.base_url = "http://35.239.135.107:30001"
        self.base_url2 = "http://34.68.121.35:30001"
        self.base_url3 = "http://34.170.152.22:30001"
        self.thread_cnt = 130
        self.thread_cnt2 = 130
        self.thread_cnt3 = 135
    async def sync_call(self, prompt_list: List[str], output_length: int):
        output_length = output_length + 1
        result_queue = queue.Queue()
        
        total_thread_cnt = self.thread_cnt + self.thread_cnt2 + self.thread_cnt3
        prompt_per_thread = (len(prompt_list) // total_thread_cnt) + 1
        
        tasks = []
        thread_index = 1
        for i in range(0, len(prompt_list), prompt_per_thread):
            batch = prompt_list[i:i + prompt_per_thread]
            batch_tuples = [(f"{prompt}", output_length) for prompt in batch]
            
            if thread_index <= self.thread_cnt:
                tasks.append(send_batch(self.base_url, batch_tuples, thread_index, result_queue))
            elif self.thread_cnt < thread_index <= self.thread_cnt + self.thread_cnt2:
                tasks.append(send_batch(self.base_url2, batch_tuples, thread_index, result_queue))
            else:
                tasks.append(send_batch(self.base_url3, batch_tuples, thread_index, result_queue))
            thread_index += 1
        
        results = await asyncio.gather(*tasks)
        
        combined_results = []
        for result in results:
            combined_results.extend(result)
                
        return combined_results

    
    def __call__(self, prompt_list: List[str], output_length: int):
        return asyncio.run(self.sync_call(prompt_list, output_length))

def extract_required_part(output: str) -> str:
    return output 

async def send_batch(base_url, requests, thread_id, result_queue):
    results = await run_vllm(base_url, requests)
    return results

async def run_vllm(base_url, requests: List[Tuple[str, int]]) -> List[str]:
    async with httpx.AsyncClient(timeout=300.0, follow_redirects=True, max_redirects=10_000) as client:
        request_items = [{'prompt': prompt, 'output_len': output_len} for prompt, output_len in requests]
        response = await client.post(f"{base_url}/run_batch", json=request_items)
        results = response.json()
        batch_results = [item['result'] for item in results]
        processed_list = [extract_required_part(string) for string in batch_results]
        return processed_list
