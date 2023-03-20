# Agri-Food-Supply-Chain

# FOOD_SUPPLY
<h1>Processed Food Traceability using Blockchain Technology</h1>


<p>
Blockchain is  ground-breaking technology, after the application in cryptocurrency and bitcoins, is now started refining every industry. The list of industries that are boosted-up by the adaptation of Blockchain Technology involves Health Care, Supply Chain, Insurance, Education and so on. Supply Chain, being a vivacity of each and every industry, plays an important role in maintaining the whole process obvious. It is a process of producing food and other desired products by the process of cultivation. Food Supply Chain is the system that comprises of process of managing the whole process of food from manufacturing till the consumption of the food. It is a wholly long and tedious  process. Therefore, this study designed a multimode storage mechanism that combines blockchain storage and traditional storage, and proposed a new system architecture for the entire processed food supply chain based on blockchain technology.</p>


<h3>Properties of blockchain</h3>

![image](https://user-images.githubusercontent.com/69450294/216298541-6daf98f5-bdfa-44c9-9a12-11185e30564e.png)


<h3>METHODOLOGY -</h3>

<p>In this project, to achieve traceability between farmer and consumer a single chain was used based on the Ethereum Blockchain to store and retrieve details of all entities, simultaneously the same data and additional details like non sensitive data is being store on SQL Lite. This project works to check the traceability on processed food chains. The Entities in our project are farmer, distributor, retailer, consumer and Admin to supervise and validate the information provided by the rest of the entities. For writing the smart contracts, Solidity Language was used which works on Ethereum Blockchain. To complete this project Django was used to build a website, for storing and retrieving the details on blockchain Ganache was used which is local host based service. Additionally to interact between them using web3 module, brownie was used which is a python based framework for allowing the smart contract to store and retrieve details. In the website developed the admin controls the initial details of farmer’s produce which is added to the blockchain.The admin add the distributor and retailer to the system through the admin portal where he is able to main the users having access to the system and to check all the details are correct.  A market place is available for the distributor to check what goods are available in the system, the same also works for the retailer where he is able to check what goods are available to him through the distributor. 
</p>

![image](https://user-images.githubusercontent.com/69450294/216298889-0eb012f2-739d-4f0d-afd8-f32ff0d4523d.png)


<p>Also a Quick Response (QR) code is generated for final product which is available at retail store to check for the product details and provide traceability for consumer. All the details  All the details are available through the QR code for the consumer from location where the crop was produce, the processing involved, to the entities details who purchased the produce at each levels. Additional feature is added where the framer is suggested what crop to grow through the supply and demand of the system. </p>
<h3>Architecture of proposed system</h3>

![image](https://user-images.githubusercontent.com/69450294/216299226-444d2af7-0268-4415-b2cd-3c8d9c0b0e67.png)

<p>Processed Food always plays a critical role in food security in India. Therefore, based on a our finding on processed-food, an information management system was constructed for the processed flood supply chain to test the scenario. The system development languages include Python, JavaScript, Html and Css, and data are handled and sent through Solidity to Ganache and Django framework development. Smart Contracts are handled through Solidity.
</p>

<p> In this system we added two admin panels first in Fig 4. this admin panel is handled in the backend were admin can verify the details of the entity as well as upload their information and images directly in any file formats like csv, xlsx, etc. Along with this it stores all the data of entries performed in this system using Django.  </p>

<h2>Admin Panel</h2>

![image](https://user-images.githubusercontent.com/69450294/216299706-6340e87b-5796-41fb-8c42-09e730742460.png)

<p> The second entity in our system is Distributor Purchase panel. Distributor login onto the system using his/her credentials and move to any particular product page where he/she can buy the product from where it gets the information about product like what processes used and quantity. The same panel is also available for retailer for purchasing products.
</p>

<h2>Distributor Panel</h2>

![image](https://user-images.githubusercontent.com/69450294/216299847-11029570-b446-40d4-bd10-a902f62430c2.png)

<p>At the last phase of our project, when the retailer buys any product from the distributor a QR code is generated which is given to the retailer by which he/she can apply it with the product and while buying this product consumer can get overall information about the product just by scanning this QR code.
</p>


<h3>Conclusion</h3>
<p>This project has a great impact on food Supply chain management. By using the blockchain, data is collected at every stage of the process so that the recalls or frauds are removed. This makes the system more secure and transparent. As the system uses end to end traceability and immutability, it brings efficiency in processed food supply management. At each level data is verified and then data being publicly available through various channels to increase security. This system also helps to reduce the cost and to bring  food safety as food will not be contaminated or spoiled due to end to end monitoring.</p>

<p>In the future, many processed food companies will be able to add their data in our system by creating this system fully marketplace where deals between companies, distributor and retailer and even can be extended till the consumer. This same  can be extend to the food forecasting and perishable food products. This system will help manufacturers to build trust with the consumer and food security.</p>

<h3>UserHome Panel- </h3>

![FSC](https://user-images.githubusercontent.com/69450294/216301682-7d712dcf-e331-4abf-bbcc-d6ef7ada79d1.png)

