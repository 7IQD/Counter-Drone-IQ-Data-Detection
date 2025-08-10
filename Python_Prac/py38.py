# How to pair raw IQ data and then Normalise IQ data
raw_iq = [137, 250, 120, 10]

def zip_raw_iq(iqdata_raw):
    i = iqdata_raw[0::2]
    q = iqdata_raw[1::2]
    return i, q

def zip_normalised_iqdata(n_idata, n_qdata):
    z_n_iqdata  = list(zip(n_idata, n_qdata))
    print(z_n_iqdata)
    return z_n_iqdata
    
def normalise(p_iqdata):
    n_p_iqdata = []
    for i_data,q_data in p_iqdata:
        normalised_iqdata = (i_data - 128)/128.0, (q_data - 128)/128.0
        n_p_iqdata.append(normalised_iqdata)
        print("Normalised IQ Data:", n_p_iqdata)
    return n_p_iqdata    

# call zipping function to pair raw_iq data
paired_iqdata = zip_raw_iq(raw_iq)
print("Paired IQ Data", paired_iqdata)

# Now convert paired IQ Data into Normalised Data
print("Now convert paired IQ Data into Normalised Data")
normalised_iqdata = normalise(paired_iqdata) # Function Call to normalise the Paired IQ Data
print("Normalised IQ Data Pairs", normalised_iqdata)
    