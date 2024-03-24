from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat-Int4", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat-Int4", device_map="auto", trust_remote_code=True).eval()
model.generation_config = GenerationConfig.from_pretrained("qwen/Qwen-7B-Chat-Int4", trust_remote_code=True)


response, history = model.chat(tokenizer, "你好", history=None)
print(response)

response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)