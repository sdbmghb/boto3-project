
import boto3

if __name__ == '__main__': 
	session = boto3.Session(profile_name='python_boto')
	ec2=session.instances.all()
	ec2 = session.resource('ec2')
	for i in ec2.instances.all():
	    print(i)

