import glob
import os
import sys
# temp = glob.glob("/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_new/*beam")
# temp = glob.glob("/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_new/data2textprefixtune_y*_act*e=10*512_test_beam")
# temp = glob.glob("/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_new/data2textprefixtune_n_20_act_pee*beam")

# temp = glob.glob("/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_infix/data2textprefixtune*beam")
# temp = glob.glob("/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_lowdata/*valid*beam")
# temp = glob.glob("/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_lowdata/*100_valid_beam")


# temp = glob.glob("/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_lowdata/*ev*checkpoint*beam") # checkpoint of size 100. index 0, 1, 2
temp = glob.glob("/juice/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_lowdata_finetune/*ev*checkpoint*beam") # checkpoint of size 100. index 0, 1, 2


for temp_ in temp:
    if 'finetune' in os.path.basename(temp_):
        # print('bad,', temp_)
        continue

    os.system("./measure_scores.py "
              "/u/scr/xlisali/contrast_LM/transformers/examples/text-generation/e2e_results_lowdata/data2textprefixtune_y_20_act_cat_b=10-e=5_d=0.0_u=no_lr=5e-05_w=0.0_s=101_r=n_m=512_lowdata_2_100st=200_ev=20-checkpoint-180_valid_gold "
              "{}  -p  -t -H >> results_lowdata_prefixtune100.txt".format(temp_))