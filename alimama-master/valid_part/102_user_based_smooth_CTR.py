# -*- coding: utf-8 -*-

"""
@author: Dylan Chen

"""

import pandas as pd
from function_utils import BayesianSmoothing
from tqdm import tqdm

columns = ['instance_id', 'user_id', 'user_gender_id', 'user_age_level', 'user_occupation_id',
           'user_star_level', 'context_date_day']
train = pd.read_pickle('../processed/train_valid/train_id_processed.p')[columns + ['is_trade']]
test = pd.read_pickle('../processed/train_valid/test_id_processed.p')[columns]

for feat_1 in ['user_gender_id', 'user_age_level', 'user_occupation_id', 'user_star_level', 'user_id']:

    print(feat_1)

    res = pd.DataFrame()
    temp = train[[feat_1, 'context_date_day', 'is_trade']]

    for day in tqdm(range(18, 26)):
        count = temp.groupby([feat_1]).apply(lambda x: x['is_trade'][(x['context_date_day'] < day).values].count()).\
            reset_index(name=feat_1 + '_all')
        count1 = temp.groupby([feat_1]).apply(lambda x: x['is_trade'][(x['context_date_day'] < day).values].sum()).\
            reset_index(name=feat_1 + '_1')
        count[feat_1 + '_1'] = count1[feat_1 + '_1']
        # TODO: should handle first day conversion count and sum ?
        count.fillna(value=0, inplace=True)
        count['context_date_day'] = day
        res = res.append(count, ignore_index=True)

    # only smooth user_id here, cause user_id has a high cardinality
    if feat_1 == 'user_id':
        print('smoothing user_id')
        bs = BayesianSmoothing(1, 1)
        bs.update(res[feat_1 + '_all'].values, res[feat_1 + '_1'].values, 1000, 0.001)
        res[feat_1 + '_smooth'] = (res[feat_1 + '_1'] + bs.alpha) / (res[feat_1 + '_all'] + bs.alpha + bs.beta)

    # all features conversion rate
    res[feat_1 + '_rate'] = res[feat_1 + '_1'] / res[feat_1 + '_all']

    train = train.merge(res, how='left', on=[feat_1, 'context_date_day'])
    test = test.merge(res, how='left', on=[feat_1, 'context_date_day'])

    if feat_1 == 'user_id':
        train['user_id_smooth'] = train['user_id_smooth'].fillna(value=bs.alpha / (bs.alpha + bs.beta))
        test['user_id_smooth'] = test['user_id_smooth'].fillna(value=bs.alpha / (bs.alpha + bs.beta))

    train[feat_1 + '_rate'] = train[feat_1 + '_rate'].fillna(value=0)
    test[feat_1 + '_rate'] = test[feat_1 + '_rate'].fillna(value=0)


# ================================================
#                saving
# ================================================

feature_columns = [col for col in list(train) if
                   col.endswith(('_1', '_all', '_smooth', '_rate'))]

train[['instance_id'] + feature_columns].to_pickle('../features/train_valid/train_feature_102.p')
test[['instance_id'] + feature_columns].to_pickle('../features/train_valid/test_feature_102.p')
