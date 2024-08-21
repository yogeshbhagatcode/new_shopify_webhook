shopify_webhook
#############################


Getting started
***************
Method -1  

Add this in "config.yml" file.  
OPENEDX_EXTRA_PIP_REQUIREMENTS:  
- git+https://url/shopify_webhook.git  
build image using ``tutor images build openedx --no-cache``  
  
Method -2  
Clone this repo in ``$(tutor config printroot)/env/build/openedx/requirements``  
Add "-e ./shopify_webhook/" in private.txt file in the same directory.  
Build image using ``tutor images build openedx --no-cache``  
  
Method -3  
While choosing step-1 or step-2 do not build image and just run ``tutor dev launch``  
Doing this will also perform the migration.  


Create oauth application
************************

Go to {lms_url}/admin/oauth2_provider/application/  
Add application  
Client id: webhook_receiver (you can choose to keep the auto generated value too.)  
User: (Create and assign a staff user)  
Client type: Confidential  
Authorization grant type: Client credentials  
Client secret: (it will be generated automatically)  
Name: webhook_receiver  


Set tutor plugin
****************

Copy the content of ``shopify_configs.py`` file from this repo.  
Go to ``$(tutor config printroot)/env/plugins/`` directory and create a file ``shopify_configs.py``  
Now paste the copied content in this file.  
Enable this plugin using ``tutor plugins enable shopify_configs`` command.  
