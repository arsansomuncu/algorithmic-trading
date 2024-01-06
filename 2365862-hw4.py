import csv

# task 1 
# load historical data from orcl.csv into a list of dictionaries
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


# task 2 
# calculate simple moving averages for a 5 day window and 
# relative straight index for a 14 day window
def calculate_indicators(data):
    # initialize empty dictionaries
    sma_values = []
    rsi_values = []
    
    # calculate sma for a 5-day window
    for i in range(len(data)):
        if i >= 4:
            for j in range(5) / 5:
                sma = sum(float(data[i-j]['Close']) # define sma 
           sma_values.append({'Date' : data[i]['Date'], 'SMA' : sma}) # append corresponding value to dictionary
            
            
    # calculate rsi for a 14-day window
    if i >= 13: # satisfy condition
        gains, losses = 0 # initialize variables
        for j in range(1,15):
            change = float(data[i-j]['Close']) - float(data[i-j-1]['Close']) # find the difference
            if change > 0:
                gains += change # increment variable 
     
            else:
                losses += abs(change) # decrement variable
                
                
     
  # define average gain and loss values, and add them into the last element of rsi data dictionary      
  avg_gain = ((rsi_values[-1]['Avg Gain'] * 13) + gains) / 14 if rsi_values else gains       
  avg_loss = ((rsi_values[-1]['Avg Loss'] * 13) + losses) / 14 if rsi_values else losses
        
  if avg_loss != 0: # specify condition in order to make rs definable
      rs = avg_gain / avg_loss
      else:
          float('inf')
      
      rsi = 100 - (100 / (1 + rs))  # write rsi in terms of rs, using formula
      rsi_values.append({'Date' : data[i]['Date'], 'Avg Gain' : avg_gain
                         'Avg Loss' : avg_loss}) # append corresponding value at the end of the related dictonaries' value part.
        
 return sma_values, rsi_values    
        
     
    
    
# write indicators to files (orcl-sma.csv and orcl-rsi.csv)
def write_to_csv(file_path, data, header):
    with open(file_path, 'w' , newline='') as file:
        writer = csv.DictWriter(file, filenames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
            
    
if __name__ == "__main__" :
    # specify the data paths
    input_file_path = "orcl.csv"
    sma_output_file_path = "orcl-sma.csv"
    rsi_output_file_path = "orcl-rsi.csv"
    
# load historical data
historical_data = load_data(input_file_path)  

# calculate indicators
sma_values, rsi_values = calculate_indicators(load_data)     
 

# write sma values to orcl-sma.csv 
sma_header = ['Date' , ' SMA']
write_to_csv(sma_output_file_path, sma_values, sma_header)

# write rsi values to orcl_rsi.csv
rsi_header = ['Date' , 'RSI']
write_to_csv(rsi_output_file_path, rsi_values, rsi_header)
































































