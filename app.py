import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import joblib

scaler = joblib.load(r'D:\Projects\Projects\IPL_SCORE_PREDICTION\Scalers\Scaler.joblib')

strike_joblib = joblib.load(r'D:\Projects\Projects\IPL_SCORE_PREDICTION\Scalers\striker_encoder.joblib')
bowler_encoder = joblib.load(r'D:\Projects\Projects\IPL_SCORE_PREDICTION\Scalers\bowler_encoder.joblib')
bowling_team_encoder = joblib.load(r'D:\Projects\Projects\IPL_SCORE_PREDICTION\Scalers\bowling_team_encoder.joblib')
batting_team_encoder = joblib.load(r'D:\Projects\Projects\IPL_SCORE_PREDICTION\Scalers\batting_team_encoder.joblib')
venue_encoder = joblib.load(r'D:\Projects\Projects\IPL_SCORE_PREDICTION\Scalers\venue_encoder.joblib')




# Load the saved model
model = load_model(r'D:\Projects\Projects\IPL_SCORE_PREDICTION\Scalers\ipl_score_predicter.h5')


# Create a Streamlit app
st.title("IPL Score Predictor")

venue_list =  ['M Chinnaswamy Stadium', 'Punjab Cricket Association Stadium, Mohali', 'Feroz Shah Kotla', 'Wankhede Stadium', 'Eden Gardens', 'Sawai Mansingh Stadium', 'Rajiv Gandhi International Stadium, Uppal', 'MA Chidambaram Stadium, Chepauk', 'Dr DY Patil Sports Academy', 'Newlands', "St George's Park", 'Kingsmead', 'SuperSport Park', 'Buffalo Park', 'New Wanderers Stadium', 'De Beers Diamond Oval', 'OUTsurance Oval', 'Brabourne Stadium', 'Sardar Patel Stadium, Motera', 'Barabati Stadium', 'Vidarbha Cricket Association Stadium, Jamtha', 'Himachal Pradesh Cricket Association Stadium', 'Nehru Stadium', 'Holkar Cricket Stadium', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Subrata Roy Sahara Stadium', 'Shaheed Veer Narayan Singh International Stadium', 'JSCA International Stadium Complex', 'Sheikh Zayed Stadium', 'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium', 'Maharashtra Cricket Association Stadium', 'Punjab Cricket Association IS Bindra Stadium, Mohali', 'Saurashtra Cricket Association Stadium', 'Green Park'] 
bat_team_list = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals', 'Mumbai Indians', 'Deccan Chargers', 'Kings XI Punjab', 'Royal Challengers Bangalore', 'Delhi Daredevils', 'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad', 'Rising Pune Supergiants', 'Gujarat Lions', 'Rising Pune Supergiant'] 
bowl_team_list = ['Royal Challengers Bangalore', 'Kings XI Punjab', 'Delhi Daredevils', 'Kolkata Knight Riders', 'Rajasthan Royals', 'Mumbai Indians', 'Chennai Super Kings', 'Deccan Chargers', 'Pune Warriors', 'Kochi Tuskers Kerala', 'Sunrisers Hyderabad', 'Rising Pune Supergiants', 'Gujarat Lions', 'Rising Pune Supergiant'] 
striker_n_list =  ['SC Ganguly', 'BB McCullum', 'RT Ponting', 'DJ Hussey', 'Mohammad Hafeez', 'PA Patel', 'ML Hayden', 'MEK Hussey', 'MS Dhoni', 'SK Raina', 'JDP Oram', 'S Badrinath', 'T Kohli', 'YK Pathan', 'SR Watson', 'M Kaif', 'DS Lehmann', 'RA Jadeja', 'M Rawat', 'D Salunkhe', 'SK Warne', 'SK Trivedi', 'L Ronchi', 'ST Jayasuriya', 'DJ Thornely', 'RV Uthappa', 'PR Shah', 'AM Nayar', 'SM Pollock', 'Harbhajan Singh', 'AC Gilchrist', 'Y Venugopal Rao', 'VVS Laxman', 'A Symonds', 'RG Sharma', 'SB Styris', 'AS Yadav', 'SB Bangar', 'WPUJC Vaas', 'RP Singh', 'K Goel', 'JR Hopes', 'KC Sangakkara', 'DPMD Jayawardene', 'Yuvraj Singh', 'IK Pathan', 'S Sohal', 'B Lee', 'PP Chawla', 'WA Mota', 'Shahid Afridi', 'RR Sarwan', 'S Sreesanth', 'VRV Singh', 'S Chanderpaul', 'R Dravid', 'LRPL Taylor', 'JH Kallis', 'V Kohli', 'MV Boucher', 'P Kumar', 'SB Joshi', 'Z Khan', 'R Vinay Kumar', 'WP Saha', 'LR Shukla', 'AB Agarkar', 'M Kartik', 'I Sharma', 'AM Rahane', 'DJ Bravo', 'MA Khote', 'G Gambhir', 'V Sehwag', 'S Dhawan', 'Shoaib Malik', 'MK Tiwary', 'KD Karthik', 'R Bhatia', 'MF Maharoof', 'VY Mahesh', 'DB Das', 'HH Gibbs', 'DNT Zoysa', 'D Kalyankrishna', 'GC Smith', 'SA Asnodkar', 'Sohail Tanvir', 'SP Fleming', 'S Vidyut', 'JA Morkel', 'LPC Silva', 'DB Ravi Teja', 'SE Marsh', 'YV Takawale', 'SS Tiwary', 'RR Raje', 'Joginder Sharma', 'MS Gony', 'M Muralitharan', 'M Ntini', 'W Jaffer', 'CL White', 'Misbah-ul-Haq', 'DT Patil', 'A Kumble', 'DW Steyn', 'S Anirudha', 'MM Patel', 'AB de Villiers', 'A Chopra', 'BJ Hodge', 'T Taibu', 'Umar Gul', 'PP Ojha', 'SP Goswami', 'B Akhil', 'Salman Butt', 'TM Dilshan', 'A Mishra', 'J Arunkumar', 'Iqbal Abdulla', 'CK Kapugedera', 'LA Pomersbach', 'Shoaib Akhtar', 'AB Dinda', 'SR Tendulkar', 'B Chipli', 'DR Smith', 'SD Chitnis', 'Kamran Akmal', 'TM Srivastava', 'MK Pandey', 'RR Powar', 'JP Duminy', 'JD Ryder', 'KP Pietersen', 'CH Gayle', 'MC Henriques', 'A Flintoff', 'FH Edwards', 'PC Valthaty', 'RJ Quiney', 'AD Mascarenhas', 'AS Raut', 'Pankaj Singh', 'RS Bopara', 'DL Vettori', 'M Manhas', 'PJ Sangwan', 'MN van Wyk', 'AA Bilakhia', 'TL Suman', 'Shoaib Ahmed', 'GR Napier', 'R Bishnoi', 'RE van der Merwe', 'KP Appanna', 'M Vijay', 'SB Jakati', 'L Balaji', 'NV Ojha', 'LA Carseldine', 'RJ Harris', 'D du Preez', 'DS Kulkarni', 'SM Harwood', 'Yashpal Singh', 'AN Ghosh', 'AD Mathews', 'SM Katich', 'DA Warner', 'J Botha', 'A Nehra', 'Mashrafe Mortaza', 'GJ Bailey', 'AB McDonald', 'Y Nagar', 'Niraj Patel', 'T Henderson', 'A Singh', 'R Ashwin', 'T Thushara', 'Mohammad Ashraful', 'CA Pujara', 'OA Shah', 'AP Tare', 'AT Rayudu', 'R Sathish', 'R McLaren', 'MS Bisla', 'YA Abdulla', 'EJG Morgan', 'AA Jhunjhunwala', 'P Dogra', 'A Uniyal', 'KA Pollard', 'MJ Lumb', 'DR Martyn', 'S Narwal', 'M Morkel', 'Anirudh Singh', 'Jaskaran Singh', 'FY Fazal', 'AC Voges', 'MD Mishra', 'J Theron', 'R Sharma', 'Mandeep Singh', 'KM Jadhav', 'SW Tait', 'PD Collingwood', 'VS Malik', 'SJ Srivastava', 'AP Dole', 'Bipul Sharma', 'DE Bollinger', 'BAW Mendis', 'B Sumanth', 'C Madan', 'AG Paunikar', 'AJ Finch', 'MR Marsh', 'STR Binny', 'IR Jaggi', 'DT Christian', 'RV Gomez', 'UBT Chand', 'UT Yadav', 'Sunny Singh', 'NJ Rimmington', 'MA Agarwal', 'AUK Pathan', 'AL Menaria', 'DJ Jacobs', 'WD Parnell', 'TD Paine', 'SB Wagh', 'AC Thomas', 'BJ Haddin', 'NLTC Perera', 'MS Wade', 'JE Taylor', 'RN ten Doeschate', 'SL Malinga', 'AG Murtaza', 'TR Birt', 'Harpreet Singh', 'NL McCullum', 'DH Yagnik', 'AC Blizzard', 'M Klinger', 'I Malhotra', 'A Mithun', 'P Parameswaran', 'AA Chavan', 'ND Doshi', 'CJ Ferguson', 'B Kumar', 'S Rana', 'JEC Franklin', 'Shakib Al Hasan', 'F du Plessis', 'SPD Smith', 'MN Samuels', 'KK Cooper', 'HV Patel', 'Ankit Sharma', 'RE Levi', 'RR Bhatkal', 'Harmeet Singh', 'BA Bhatt', 'CJ McKay', 'DJ Harris', 'N Saini', 'DA Miller', 'Azhar Mahmood', 'A Ashish Reddy', 'V Pratap Singh', 'BB Samantray', 'RJ Peterson', 'S Nadeem', 'VR Aaron', 'MJ Clarke', 'AP Majumdar', 'Gurkeerat Singh', 'P Awana', 'SP Narine', 'A Chandila', 'PA Reddy', 'MC Juneja', 'AD Russell', 'KK Nair', 'KB Arun Karthik', 'GH Vihari', 'MDKJ Perera', 'R Shukla', 'JD Unadkat', 'M Vohra', 'JP Faulkner', 'R Rampaul', 'BJ Rohrer', 'Q de Kock', 'KV Sharma', 'SMSM Senanayake', 'LJ Wright', 'X Thalaivan Sargunam', 'DJG Sammy', 'MG Johnson', 'A Mukund', 'SV Samson', 'BMAJ Mendis', 'KL Rahul', 'CM Gautam', 'KW Richardson', 'Parvez Rasool', 'GJ Maxwell', 'R Dhawan', 'SA Yadav', 'CJ Anderson', 'JJ Bumrah', 'CA Lynn', 'MA Starc', 'AR Patel', 'Sandeep Sharma', 'BR Dunk', 'Shivam Sharma', 'LMP Simmons', 'VH Zol', 'BCJ Cutting', 'Mohammed Shami', 'BE Hendricks', 'S Gopal', 'M de Lange', 'RR Rossouw', 'JO Holder', 'JDS Neesham', 'Imran Tahir', 'MM Sharma', 'DJ Hooda', 'CH Morris', 'SS Iyer', 'SA Abbott', 'AN Ahmed', 'YS Chahal', 'J Suchith', 'P Negi', 'RG More', 'Anureet Singh', 'HH Pandya', 'NM Coulter-Nile', 'PV Tambe', 'MJ McClenaghan', 'DJ Muthuswami', 'SN Thakur', 'SN Khan', 'D Wiese', 'S Aravind', 'JC Buttler', 'CR Brathwaite', 'MP Stoinis', 'C Munro', 'P Sahu', 'KH Pandya', 'TG Southee', 'MJ Guptill', 'KJ Abbott', 'TM Head', 'AD Nath', 'NS Naik', 'Ishan Kishan', 'SW Billings', 'RR Pant', 'KS Williamson', 'KC Cariappa', 'PSP Handscomb', 'Sachin Baby', 'J Yadav', 'UT Khawaja', 'HM Amla', 'BB Sran', 'N Rana', 'F Behardien', 'ER Dwivedi', 'JJ Roy', 'BA Stokes', 'Vishnu Vinod', 'TS Mills', 'Basil Thampi', 'CR Woakes', 'V Shankar', 'Rashid Khan', 'RA Tripathi', 'RD Chahar', 'LH Ferguson', 'C de Grandhomme', 'PJ Cummins', 'Mohammad Nabi', 'Kuldeep Yadav', 'Washington Sundar', 'S Badree', 'A Choudhary', 'AR Bawne', 'AJ Tye', 'Ankit Soni', 'K Rabada', 'AF Milne', 'SP Jackson', 'Swapnil Singh', 'R Tewatia', 'AS Rajpoot'] 
bowler_n_list = ['P Kumar', 'Z Khan', 'AA Noffke', 'JH Kallis', 'SB Joshi', 'CL White', 'B Lee', 'S Sreesanth', 'JR Hopes', 'IK Pathan', 'K Goel', 'PP Chawla', 'WA Mota', 'GD McGrath', 'B Geeves', 'MF Maharoof', 'R Bhatia', 'DL Vettori', 'R Vinay Kumar', 'B Akhil', 'AB Dinda', 'I Sharma', 'AB Agarkar', 'M Kartik', 'Mohammad Hafeez', 'DJ Hussey', 'MM Patel', 'SR Watson', 'SK Trivedi', 'SK Warne', 'D Salunkhe', 'Pankaj Singh', 'YK Pathan', 'Mohammad Asif', 'VY Mahesh', 'SM Pollock', 'A Nehra', 'DS Kulkarni', 'Harbhajan Singh', 'DJ Bravo', 'VS Yeligati', 'AM Nayar', 'MA Khote', 'Sohail Tanvir', 'JDP Oram', 'MS Gony', 'P Amarnath', 'M Muralitharan', 'Joginder Sharma', 'RP Singh', 'DNT Zoysa', 'SB Bangar', 'Shahid Afridi', 'PP Ojha', 'D Kalyankrishna', 'VRV Singh', 'Yuvraj Singh', 'DW Steyn', 'CRD Fernando', 'ST Jayasuriya', 'V Kohli', 'Gagandeep Singh', 'Umar Gul', 'SC Ganguly', 'LR Shukla', 'PJ Sangwan', 'Shoaib Malik', 'V Sehwag', 'A Kumble', 'DP Vijaykumar', 'SB Styris', 'RR Raje', 'JA Morkel', 'L Balaji', 'CK Kapugedera', 'DR Smith', 'WPUJC Vaas', 'Y Venugopal Rao', 'AD Mascarenhas', 'A Mishra', 'DJ Thornely', 'PM Sarvesh Kumar', 'Abdur Razzak', 'TM Dilshan', 'SD Chitnis', 'M Ntini', 'RR Powar', 'SK Raina', 'BAW Mendis', 'T Thushara', 'A Flintoff', 'Kamran Khan', 'T Henderson', 'FH Edwards', 'Harmeet Singh', 'KP Pietersen', 'LRPL Taylor', 'JD Ryder', 'Anureet Singh', 'CH Gayle', 'RR Bose', 'YA Abdulla', 'RS Bopara', 'SL Malinga', 'DP Nannes', 'RG Sharma', 'Shoaib Ahmed', 'BJ Hodge', 'RA Jadeja', 'RE van der Merwe', 'KP Appanna', 'JP Duminy', 'SR Tendulkar', 'VS Malik', 'SM Harwood', 'AS Raut', 'D du Preez', 'RJ Harris', 'TL Suman', 'A Singh', 'M Morkel', 'LA Carseldine', 'S Tyagi', 'SB Jakati', 'A Mithun', 'AM Rahane', 'A Symonds', 'C Nanda', 'J Botha', 'CK Langeveldt', 'SS Sarkar', 'AM Salvi', 'Jaskaran Singh', 'SW Tait', 'A Uniyal', 'AA Jhunjhunwala', 'AD Mathews', 'RS Gavaskar', 'R Ashwin', 'JM Kemp', 'S Ladda', 'SE Bond', 'SJ Srivastava', 'Bipul Sharma', 'Y Nagar', 'UT Yadav', 'MC Henriques', 'R McLaren', 'J Theron', 'S Narwal', 'AC Voges', 'KAJ Roach', 'KA Pollard', 'C Ganapathy', 'SB Wagh', 'R Sharma', 'AN Ahmed', 'R Sathish', 'AP Dole', 'FY Fazal', 'PD Collingwood', 'MR Marsh', 'L Ablish', 'S Sriram', 'AB McDonald', 'DE Bollinger', 'JD Unadkat', 'MK Tiwary', 'ND Doshi', 'Iqbal Abdulla', 'AL Menaria', 'STR Binny', 'AUK Pathan', 'AG Murtaza', 'JEC Franklin', 'AC Thomas', 'WD Parnell', 'M Manhas', 'DT Christian', 'DB Ravi Teja', 'BA Bhatt', 'JJ van der Wath', 'S Aravind', 'R Ninan', 'Shakib Al Hasan', 'NLTC Perera', 'RV Gomez', 'PC Valthaty', 'S Nadeem', 'S Randiv', 'J Syed Mohammad', 'NL McCullum', 'JE Taylor', 'KMDN Kulasekara', 'TG Southee', 'P Parameswaran', 'S Dhawan', 'B Kumar', 'AA Kazi', 'VR Aaron', 'P Prasanth', 'Y Gnaneswara Rao', 'AA Chavan', 'RW Price', 'GJ Maxwell', 'JP Faulkner', 'DAJ Bracewell', 'Ankit Sharma', 'DJ Harris', 'TP Sudhindra', 'SP Narine', 'HV Patel', 'KK Cooper', 'GB Hogg', 'P Awana', 'MN Samuels', 'AD Russell', 'Azhar Mahmood', 'A Chandila', 'P Negi', 'RJ Peterson', 'CJ McKay', 'R Shukla', 'MJ Clarke', 'V Pratap Singh', 'A Ashish Reddy', 'BW Hilfenhaus', 'K Upadhyay', 'Sunny Gupta', 'MG Johnson', 'JJ Bumrah', 'AS Rajpoot', 'B Laughlin', 'GH Vihari', 'Mohammed Shami', 'BMAJ Mendis', 'CH Morris', 'Anand Rajan', 'AJ Finch', 'MM Sharma', 'KV Sharma', 'SMSM Senanayake', 'R Rampaul', 'R Dhawan', 'JO Holder', 'IC Pandey', 'LJ Wright', 'S Kaul', 'YS Chahal', 'KW Richardson', 'DJG Sammy', 'Sandeep Sharma', 'PV Tambe', 'Parvez Rasool', 'RN ten Doeschate', 'MG Neser', 'NM Coulter-Nile', 'CJ Anderson', 'MA Starc', 'AR Patel', 'JDS Neesham', 'M Vijay', 'SA Yadav', 'S Badree', 'R Tewatia', 'V Shankar', 'Imran Tahir', 'Shivam Sharma', 'S Rana', 'BE Hendricks', 'PJ Cummins', 'K Santokie', 'S Gopal', 'Karanveer Singh', 'DJ Muthuswami', 'TA Boult', 'SA Abbott', 'DJ Hooda', 'P Suyal', 'J Suchith', 'D Wiese', 'MJ McClenaghan', 'HH Pandya', 'RG More', 'GS Sandhu', 'M de Lange', 'J Yadav', 'Gurkeerat Singh', 'M Ashwin', 'JW Hastings', 'C Munro', 'Mustafizur Rahman', 'CR Brathwaite', 'KJ Abbott', 'P Sahu', 'BB Sran', 'KH Pandya', 'S Kaushik', 'T Shamsi', 'MP Stoinis', 'Swapnil Singh', 'SM Boland', 'CJ Jordan', 'KC Cariappa', 'A Zampa', 'BCJ Cutting', 'DL Chahar', 'KS Williamson', 'Kuldeep Yadav', 'TS Mills', 'A Choudhary', 'TM Head', 'BA Stokes', 'CR Woakes', 'T Natarajan', 'Rashid Khan', 'C de Grandhomme', 'Basil Thampi', 'AJ Tye', 'AF Milne', 'K Rabada', 'Washington Sundar', 'SN Thakur', 'SS Agarwal', 'NB Singh', 'Ankit Soni', 'Mohammad Nabi', 'Mohammed Siraj', 'LH Ferguson'] 


# Create input widgets
venue = st.selectbox("Select Venue:",venue_list)  # list of unique venues
batting_team = st.selectbox("Select Batting Team:", bat_team_list)  # list of unique batting teams
bowling_team = st.selectbox("Select Bowling Team:", bowl_team_list)  # list of unique bowling teams
striker = st.selectbox("Select Striker:", striker_n_list)  # list of unique strikers
bowler = st.selectbox("Select Bowler:", bowler_n_list)  # list of unique bowlers

# Create a button to predict the score
predict_button = st.button("Predict Score")

# Define a function to predict the score
def predict_score():
    # Encode the input values
    encoded_venue = np.array([venue_encoder.transform([venue])[0]])
    encoded_batting_team = np.array([batting_team_encoder.transform([batting_team])[0]])
    encoded_bowling_team = np.array([bowling_team_encoder.transform([bowling_team])[0]])
    encoded_striker = np.array([strike_joblib.transform([striker])[0]])
    encoded_bowler = np.array([bowler_encoder.transform([bowler])[0]])

    # Create a numpy array with the encoded values
    input_array = np.array([encoded_venue, encoded_batting_team, encoded_bowling_team, encoded_striker, encoded_bowler])

    # Reshape the array to match the model input shape
    input_array = input_array.reshape(1, 5)

    # Scale the input array using the loaded scaler
    input_array = scaler.transform(input_array)

    # Make a prediction using the loaded model
    predicted_score = model.predict(input_array)

    # Convert the predicted score to an integer
    predicted_score = int(predicted_score[0, 0])

    # Display the predicted score
    st.write("Predicted Score:", predicted_score)

# Run the predict_score function when the button is clicked
if predict_button:
    predict_score()



