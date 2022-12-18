from duc_preprocess import duc2001, duc2002



# Writes single document 2001 summarization data to duc2001_output.
duc2001_path="DUC2004/DUC2004_Summarization_Documents [MConverter.eu].tgz"
duc2001_output="DUC2004/DATA"
duc2001.preprocess_sds(duc2001_output, nist_data_path=duc2001_path)