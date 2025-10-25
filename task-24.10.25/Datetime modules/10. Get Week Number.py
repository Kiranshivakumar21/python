from datetime import datetime

sample_date = datetime(2025,10,25)
week_num = sample_date.strftime("%U")
print("Week number:", week_num)
