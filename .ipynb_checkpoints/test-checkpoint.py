from pandas.testing import assert_frame_equal

def test_merge_datasets():
    # Define merge function
    def merge_datasets(df1, df2, df3, key):
    
        merged_df = pd.merge(df1, df2, on=key, how='inner')
        merged_df = pd.merge(merged_df, df3, on=key, how='inner')
        return merged_df
    
    # Sample subset of data
    demo_sample = demographic_train.sample(10, random_state=42)
    vitals_sample = vitals_train[vitals_train['patient_id'].isin(demo_sample['patient_id'])]
    labs_sample = labs_train[labs_train['patient_id'].isin(demo_sample['patient_id'])]
    
    # Merge the sample data
    merged_sample = merge_datasets(demo_sample, vitals_sample, labs_sample, 'patient_id')
    
    # Validate the merged result by manually merging and comparing
    expected_merged_sample = pd.merge(demo_sample, vitals_sample, on='patient_id', how='inner')
    expected_merged_sample = pd.merge(expected_merged_sample, labs_sample, on='patient_id', how='inner')
    
    assert_frame_equal(merged_sample, expected_merged_sample)

# Running the test
test_merge_datasets()
