# Report-Generation
Given a topic as the query our task is to generate a full fledge wikipedia-type report on that topic that is concise yet information heavy.

Dataset is available at cs1160310@hpc.iitd.ac.in/scratch/cse/btech/cs1160310/IR/A2_dataset/

to train this model
`./build.sh
`
`python3 create_train_val_data.py
`
`python3 train.py`

To get complete reranking of the set of queries
`./rerank.sh --query <query_file> --top1000 <top_1000_file> --collection <passage_collection_file>`
