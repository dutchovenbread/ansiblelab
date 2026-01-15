import boto3

session = boto3.Session(
  profile_name = 'labs',
  region_name = 'us-east-2'
)

ec2_client = session.client('ec2')

regions = [region["RegionName"] for region in ec2_client.describe_regions()["Regions"]]

for r in regions:
  print(f"Region: {r}")