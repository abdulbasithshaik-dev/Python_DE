import csv
import boto3

required_fields=["name","age"]
new_field="city"
city="Bangalore"

def csv_reader(file_path):

    with open(file_path,"r") as f:
        reader=csv.DictReader(f)
        header=reader.fieldnames
        rows=list(reader)
    return header, rows

def schema_validator(header,required_fields):
    for field in required_fields:
        if field not in header:
            raise ValueError(f"Missing Field:{field}")
    
def transformation(header,rows,city):
    if new_field not in header:
        header.append(new_field)

    for row in rows:
        row[new_field]=city
    return rows       

def write_csv(file_path,header,rows):
    with open(file_path,"w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    return 

def s3_file_upload(file_path,bucket_name,s3_key):
    s3_client=boto3.client("s3",
                           region_name="ap-south-1",
                           aws_access_key_id=,
                           aws_secret_access_key=,
                           )
    s3_client.upload_file(file_path, bucket_name, s3_key)
    print(f"Uploaded successfully to s3://{bucket_name}/{s3_key}")








def process_csv(input_file, output_file):
    header, rows = csv_reader(input_file)

    schema_validator(header, required_fields)

    rows = transformation(header, rows, city)

    write_csv(output_file, header, rows)
    
    s3_file_upload(
        output_file,
        bucket_name="shaikfirstbucket245",
        s3_key="output.csv")


final=process_csv("etl_practice_data.csv","output.csv")
print("successfully done")
