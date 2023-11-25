# NLP Final Project: Prefix Tuning

Group project by Grace Wang, Nobline Yoo, Richard Zhu

[Paper](https://drive.google.com/file/d/1Dtvst-zzubB1xsiQZEEkJpXdB7LsB4g5/view?usp=sharing)

Based significantly on code from [Li and Liang 2021](https://aclanthology.org/2021.acl-long.353.pdf). The authors also provide a [Codalab](https://worksheets.codalab.org/worksheets/0x16e0c8e7ab1f4b22aaccddc8b586541f)

Download and place additional folders/files into the necessary folders/directories (sources in brackets)

/e2e-metrics/pycocoevalcap/ (/pycocoevalcap/ [here](https://worksheets.codalab.org/bundles/0xaec7a306d076440fbc5f65d6b0ec2c19))
/gpt2-medium-s3/ (will install when install dependencies in transformers folder with command "pip install transformers/" at root /)

To train the baseline, run

```bash
pip install transformers/ && python gpt2/train_e2e.py  --preseqlen 10 --learning_rate 0.00005 --seed 22 --epoch 10 --notes earlystop > stdout_baseline_rgn.txt
```

To run the prefix initialization ablation, run

```bash
pip install transformers/ && python gpt2/train_e2e.py  --preseqlen 10 --learning_rate 0.00005 --init_random table2text --seed 22 --epoch 10 --notes earlystop > stdout_baseline_rgn.txt
```
