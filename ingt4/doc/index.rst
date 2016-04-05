Installation Steps
==================


First Step
**********
Install the module

 .. image:: http://image.noelshack.com/fichiers/2016/14/1459842293-step1.jpg



Second Step
***********
Activate the Cron Job in the Administration menu :

* Settings
* Technical
* (Automation) Scheduled Actions

 .. image:: http://image.noelshack.com/fichiers/2016/13/1459514717-step2.png



Third Step
**********
Create a configuration, to access to it, you have to go in your Inventory app.

 .. image:: http://image.noelshack.com/fichiers/2016/13/1459515874-step30.png


and click on Configuration, then Ingram  :

 .. image:: http://image.noelshack.com/fichiers/2016/13/1459515396-step31.png


You can now make your configuration :

 .. image:: http://image.noelshack.com/fichiers/2016/14/1459842216-step33.png


**Button explanation :**

* Check FTP Connection : Check if the connection with your credentials is correctly set.
* Download : Download the products files with the names set at the end of this configuration.
* Synchronize : synchronize the products categories and products. Based on the SKU (product reference) to define if the products already exists.
* Clean Date : Set as inactive product that were not synchronized for a week but were already used in Odoo. If products are not used, it will be deleted.
* Delete Data : Set as inactive all the ingram products already used in the Odoo. If products aren't used, it will deleted.
 
 
**Fields explanation :**

* Name : Name associed with the configuration
* Supplier : Link to the Ingram supplier
* Country : Supplier's country
* Location : Stock for the products
* Category : Products category
* Path : Path where the donwloaded files are stored
* Warning Mail : If something wrong during the Cronjob, email adresses will receive the informations

* FTP Server 
    * Server Address : URL for the FTP server 
    * Login : Login
    * Password : Password
* Xml server 
    * Server Xml Address : URL for the XML Server
    * XML Request : Active the XML Request (must be active)
    * Login : Login
    * Password : Password
* Date of last cronjob synchronization : Date of the last cronjob synchronization
* Date of last importation : Date of the last manual download (click on the button)
* Date of last synchronization : Date of the last manual synchronization (click on the button)
* Products Categories File Name : Name of the file used for the products categories
* Products File Name : Name of the file used for the products 


**Warning : The header of the products file must be this one :**

*'Ingram Part Number, Vendor Part Number, EANUPC Code, Plant, Vendor Number, Vendor Name, Weight, Category ID, Customer Price, Retail Price, Availability Flag, BOM Flag, Warranty Flag, Material Long Description, Material Creation Reason code, Material Language Code, Music Copyright Fees, Recycling Fees, Document Copyright Fees, Battery Fees, Availability (Local Stock),Availability (Central Stock),Creation Reason Type, Creation Reason Value, Local Stock Backlog Quantity, Local Stock Backlog ETA, Central Stock Backlog Quantity, Central Stock Backlog ETA'*


Don't forget to define the sales and purchases taxes (VAT) on the Accounting page.

 .. image:: http://image.noelshack.com/fichiers/2016/13/1459515129-step4.png