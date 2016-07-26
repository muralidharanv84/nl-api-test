import argparse

import sentiment_analysis

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--transcript_file', help='File containing the transcript to be analyzed')
    parser.add_argument(
        '--multiunit_file', help='Multiple messages to analyze in one file, one line per unit. Results will be averaged')
    
    args = parser.parse_args()
     
    transcript_file = args.transcript_file
    multiunit_file = args.multiunit_file
    
    if transcript_file:
        file = open(transcript_file);
        text = file.read()
        file.close()
        
        result = sentiment_analysis.analyze_sentiment(text)
        print ("About to analyze: ", text)
        polarity = result[0]
        magnitude = result[1]
        
        print ("Polarity: ", polarity, " Magnitude: ", magnitude)
    
    elif multiunit_file:
        multiunit_file = args.multiunit_file
    
        file = open(multiunit_file)
        lines = file.read().splitlines()
        file.close()
        
        sum_polarity = 0
        sum_magnitude= 0
        num_lines = 0
        for line in lines:
            print ("About to analyze: ", line)
            result = sentiment_analysis.analyze_sentiment(line)
            polarity = result[0]
            magnitude = result[1]
            
            sum_polarity += polarity
            sum_magnitude += magnitude
            num_lines += 1
            
        print("Average polarity: ", sum_polarity / num_lines,
              " Average magnitude: ", sum_magnitude / num_lines)
