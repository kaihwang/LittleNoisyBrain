import pd as pd


qcdf = pd.merge(pd.read_csv('Data/mriqcp202.txt', sep='\t'), pd.read_csv('Data/mriqc02.txt', sep='\t'), on = 'subjectkey')
qcdf = qcdf.drop([0])
sdf = pd.read_csv('Data/abcd_inclusioncriteriasubset.csv')
df = pd.merge(qcdf, sdf, on ='subjectkey')

#rest 380
#mid 411
#sst 445
#nback 370

# subjects with complete fMRI data
idx = ((df['iqc_rsfmri_1_sub_02_nody'].astype('float')>228) & (df['iqc_rsfmri_2_sub_02_nody'].astype('float')>228)) & \
(df['iqc_rsfmri_3_sub_02_nody'].astype('float')>228) & (df['iqc_rsfmri_4_sub_02_nody'].astype('float')>228) & \
(df['iqc_mid_1_sub_02_nody'].astype('float')>300) & (df['iqc_mid_2_sub_02_nody'].astype('float')>300) & \
(df['iqc_sst_1_sub_02_nody'].astype('float')>300) & (df['iqc_sst_2_sub_02_nody'].astype('float')>300) & \
(df['iqc_nback_1_sub_02_nody'].astype('float')>270) & (df['iqc_nback_2_sub_02_nody'].astype('float')>270)




df['iqc_rsfmri_fd_count'] = df['iqc_rsfmri_1_sub_02_nody'].astype('float') + df['iqc_rsfmri_2_sub_02_nody'].astype('float') + df['iqc_rsfmri_3_sub_02_nody'].astype('float') + df['iqc_rsfmri_4_sub_02_nody'].astype('float')
df['iqc_mid_fd_count'] = df['iqc_mid_1_sub_02_nody'].astype('float') + df['iqc_mid_2_sub_02_nody'].astype('float') 
df['iqc_sst_fd_count'] = df['iqc_sst_1_sub_02_nody'].astype('float') + df['iqc_sst_2_sub_02_nody'].astype('float') 
df['iqc_nback_fd_count'] = df['iqc_nback_1_sub_02_nody'].astype('float') + df['iqc_nback_2_sub_02_nody'].astype('float') 

# sort by FD
df.sort_values(by=['iqc_rsfmri_fd_count', 'iqc_nback_fd_count', 'iqc_sst_fd_count', 'iqc_mid_fd_count'], ascending=False)