# Evaluate Qwen2.5-Math-Instruct
PROMPT_TYPE="qwen25-math-cot"

# Qwen2.5-Math-1.5B-Instruct
export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"
MODEL_NAME_OR_PATH="/share/project/herunming/dataset/LlamaFactory/saves/qwen3-4b/full/sft/chemistry-baseline/checkpoint-939"
bash sh/eval.sh $PROMPT_TYPE $MODEL_NAME_OR_PATH

